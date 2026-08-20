import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

CHUNK_SIZE = 8 * 1024 * 1024

EXCLUDE_DIRS = {
    ".git",
    ".github",
    "automation",
    "publisher",
    "updater",
    ".idea",
    ".vscode",
    "__pycache__",
}

EXCLUDE_FILES = {
    ".gitignore",
    ".gitattributes",
    "Thumbs.db",
    "desktop.ini",
    "manifest.json",
    ".506th_updater_state.json",
    ".manifest_hash_cache.json",
}

def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            block = f.read(CHUNK_SIZE)
            if not block:
                break
            h.update(block)
    return h.hexdigest()

def should_skip(path, root):
    rel = path.relative_to(root)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return True
    if path.name in EXCLUDE_FILES:
        return True
    if path.name.endswith(".506thdownload"):
        return True
    return False

def load_cache(path):
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--cache", required=True)
    args = parser.parse_args()

    root = Path(args.source).resolve()
    output = Path(args.output).resolve()
    cache_path = Path(args.cache).resolve()

    cache = load_cache(cache_path)
    new_cache = {}
    files = []

    paths = [p for p in root.rglob("*") if p.is_file() and not should_skip(p, root)]

    for index, path in enumerate(paths, 1):
        rel = path.relative_to(root).as_posix()
        stat = path.stat()
        old = cache.get(rel)

        if (
            old
            and old.get("size") == stat.st_size
            and old.get("mtime_ns") == stat.st_mtime_ns
            and old.get("sha256")
        ):
            digest = old["sha256"]
            print(f"[{index}/{len(paths)}] Cached  {rel}")
        else:
            print(f"[{index}/{len(paths)}] Hashing {rel}")
            digest = sha256_file(path)

        new_cache[rel] = {
            "size": stat.st_size,
            "mtime_ns": stat.st_mtime_ns,
            "sha256": digest,
        }

        files.append({
            "path": rel,
            "size": stat.st_size,
            "sha256": digest,
        })

    files.sort(key=lambda x: x["path"].lower())

    manifest = {
        "schema": 4,
        "name": "506th Arma 3 Mod Repository",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "file_count": len(files),
        "total_bytes": sum(x["size"] for x in files),
        "files": files,
    }

    output.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    cache_path.write_text(json.dumps(new_cache, indent=2), encoding="utf-8")

    print(f"\nCreated {output}")
    print(f"Files: {manifest['file_count']}")
    print(f"Bytes: {manifest['total_bytes']}")

if __name__ == "__main__":
    main()
