import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

import boto3
import requests
from botocore.config import Config

ROOT = Path.cwd()
BUCKET = os.environ["R2_BUCKET"]
ENDPOINT = os.environ["R2_ENDPOINT"]
TOKEN = os.environ["GITHUB_TOKEN"]
REPOSITORY = os.environ["GITHUB_REPOSITORY"]
SHA = os.environ["GITHUB_SHA"]
BEFORE_SHA = os.environ.get("BEFORE_SHA", "")

EXCLUDE_TOP = {".git", ".github", "automation", "publisher", "updater"}
EXCLUDE_FILES = {
    ".gitignore", ".gitattributes", "manifest.json",
    ".506th_updater_state.json", ".manifest_hash_cache.json",
    "Thumbs.db", "desktop.ini",
}

LFS_VERSION = "version https://git-lfs.github.com/spec/v1"

s3 = boto3.client(
    "s3",
    endpoint_url=ENDPOINT,
    region_name="auto",
    config=Config(signature_version="s3v4"),
)

def run(*args):
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()

def excluded(rel):
    p = Path(rel)
    return (
        not p.parts
        or p.parts[0] in EXCLUDE_TOP
        or p.name in EXCLUDE_FILES
        or p.name.endswith(".506thdownload")
    )

def parse_lfs_pointer_bytes(data):
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return None
    if not text.startswith(LFS_VERSION):
        return None
    oid = None
    size = None
    for line in text.splitlines():
        if line.startswith("oid sha256:"):
            oid = line.split(":", 1)[1].strip()
        elif line.startswith("size "):
            size = int(line.split(" ", 1)[1].strip())
    if oid and size is not None:
        return {"sha256": oid, "size": size}
    return None

def git_blob(rel, ref="HEAD"):
    return subprocess.check_output(["git", "show", f"{ref}:{rel}"], cwd=ROOT)

def manifest_for_head():
    entries = []
    names = run("git", "ls-tree", "-r", "--name-only", "HEAD").splitlines()

    for idx, rel in enumerate(names, 1):
        if excluded(rel):
            continue

        data = git_blob(rel)
        lfs = parse_lfs_pointer_bytes(data)

        if lfs:
            size = lfs["size"]
            digest = lfs["sha256"]
        else:
            size = len(data)
            digest = hashlib.sha256(data).hexdigest()

        entries.append({
            "path": rel.replace("\\", "/"),
            "size": size,
            "sha256": digest,
        })
        print(f"[manifest {idx}/{len(names)}] {rel}")

    entries.sort(key=lambda x: x["path"].lower())
    return {
        "schema": 5,
        "name": "506th Arma 3 Mod Repository",
        "git_commit": SHA,
        "file_count": len(entries),
        "total_bytes": sum(x["size"] for x in entries),
        "files": entries,
    }

def changed_paths():
    # workflow_dispatch or unusual first push: compare HEAD~1 when available
    before = BEFORE_SHA
    if not before or set(before) == {"0"}:
        try:
            before = run("git", "rev-parse", "HEAD~1")
        except Exception:
            before = ""

    if not before:
        raise RuntimeError(
            "No previous commit is available. This hosted workflow is incremental and "
            "expects R2 to already be seeded."
        )

    out = run("git", "diff", "--name-status", "-M", before, SHA)
    changes = []
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]

        if status.startswith("R"):
            old, new = parts[1], parts[2]
            changes.append(("D", old))
            changes.append(("A", new))
        else:
            changes.append((status[0], parts[1]))
    return [(s, p) for s, p in changes if not excluded(p)]

def github_media_url(rel):
    owner, repo = REPOSITORY.split("/", 1)
    encoded = "/".join(quote(part, safe="") for part in rel.split("/"))
    # media.githubusercontent.com serves the LFS-backed content for a repository path.
    return f"https://media.githubusercontent.com/media/{owner}/{repo}/{SHA}/{encoded}"

def download_to_temp(rel, expected_sha=None, expected_size=None):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/octet-stream",
        "User-Agent": "506th-R2-Publisher/5.0",
    }
    url = github_media_url(rel)

    fd, temp_name = tempfile.mkstemp(prefix="506th-r2-")
    os.close(fd)
    h = hashlib.sha256()
    count = 0

    try:
        with requests.get(url, headers=headers, stream=True, timeout=120) as r:
            r.raise_for_status()
            with open(temp_name, "wb") as f:
                for chunk in r.iter_content(chunk_size=8 * 1024 * 1024):
                    if not chunk:
                        continue
                    f.write(chunk)
                    h.update(chunk)
                    count += len(chunk)

        digest = h.hexdigest()

        if expected_size is not None and count != expected_size:
            raise RuntimeError(f"{rel}: size mismatch {count} != {expected_size}")
        if expected_sha is not None and digest.lower() != expected_sha.lower():
            raise RuntimeError(f"{rel}: SHA-256 mismatch")

        return temp_name
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise

def upload_file(rel, manifest_entry):
    print(f"UPLOAD {rel} ({manifest_entry['size']} bytes)")
    temp_name = download_to_temp(
        rel,
        expected_sha=manifest_entry["sha256"],
        expected_size=manifest_entry["size"],
    )
    try:
        # boto3 automatically uses multipart upload through upload_file for larger objects.
        s3.upload_file(temp_name, BUCKET, rel.replace("\\", "/"))
    finally:
        os.unlink(temp_name)

def delete_file(rel):
    print(f"DELETE {rel}")
    s3.delete_object(Bucket=BUCKET, Key=rel.replace("\\", "/"))

def upload_manifest(manifest):
    body = json.dumps(manifest, indent=2).encode("utf-8")
    s3.put_object(
        Bucket=BUCKET,
        Key="manifest.json",
        Body=body,
        ContentType="application/json",
        CacheControl="no-cache",
    )

def main():
    manifest = manifest_for_head()
    by_path = {x["path"]: x for x in manifest["files"]}

    changes = changed_paths()
    print(f"{len(changes)} changed path operation(s) detected.")

    # Upload/replace changed objects first.
    for status, rel in changes:
        rel = rel.replace("\\", "/")
        if status == "D":
            continue
        entry = by_path.get(rel)
        if entry is None:
            continue
        upload_file(rel, entry)

    # Delete objects removed from Git after uploads succeed.
    for status, rel in changes:
        if status == "D":
            delete_file(rel)

    # Publish manifest last. Members therefore never see a manifest referring to
    # new files before those files have successfully reached R2.
    upload_manifest(manifest)

    print("Publish complete.")
    print("https://pub-c5632053ba844beca4069371167a6fff.r2.dev/manifest.json")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
