506th Suppress Fix
Release folder: @506th_util_supression

REQUIRED CONTENTS
addons\506th_util_supression.pbo
addons\506th_util_supression_sys.pbo
mod.cpp

IMPORTANT
Both PBOs are required. The base PBO supplies the legacy macro/include path used by
the suppression system. The system PBO contains the modernized suppression effects.

FIXES IN THIS BUILD
- Corrects the CfgPatches case mismatch:
  L_Suppress_suppress_main -> L_Suppress_Suppress_main
- Includes BOTH halves of the original split addon.
- Keeps legacy internal PBO prefixes so hardcoded include paths resolve.
- Rebrands the CBA Addon Settings category to "506th Suppress Fix".
- Adds configurable master, blur, desaturation, radial blur, camera shake,
  and near-impact strengths.
- Keeps suppression detection/projectile tracking behavior unchanged.

INSTALL
Remove prior test versions of this suppression fix.
Install/load ONLY the complete @506th_util_supression folder from this package.
CBA_A3 is still required.

USE
- Master Effect Strength — 65%: Overall suppression intensity. This is the first thing I'd adjust. 50–70% is the intended range.
- Dynamic Blur — 45%: Controls the nasty screen blur. Turn this down first if suppression still feels like a flashbang.
- Desaturation — 50%: Controls how much color gets sucked out of the screen. Lower = more natural-looking.
- Radial Blur — 60%: Gives the tunnel/disorientation feeling from incoming fire. I'd keep this moderate.
- Camera Shake — 75%: Physical punch/chaos. This can stay relatively high because it adds immersion without destroying visibility.
- Near-Impact Effect — 50%: Extra visual hit when rounds snap extremely close. Increase this if you want near misses to feel particularly violent.
