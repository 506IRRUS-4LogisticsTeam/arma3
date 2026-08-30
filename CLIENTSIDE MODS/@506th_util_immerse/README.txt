506th Immerse Rework
=====================

Release PBOs:
- 506th_util_immerse.pbo
- 506th_util_immerse_sys.pbo

Original Mod:
Laxemann Immerse

506th Rework:
Clements, S-4 Mod Team


PURPOSE
-------
Preserve the immersion systems from Immerse while allowing players/unit
administrators to reduce effect strength instead of choosing only ON or OFF.


CBA SETTINGS
------------
Category: 506th Immerse

Nearby Fire Twitch
- Enable Nearby Fire Twitch
- Twitch Strength
- Default: 50%

Explosion Shake
- Enable Explosion Shake
- Explosion Shake Strength
- Default: 60%

Weapon Recoil
- Enable Weapon Recoil Shake
- Recoil Shake Strength
- Default: 60%

Firing Force
- Enable Firing Force Effect
- Force Effect Strength
- Default: 45%


SCALING
-------
100% = original Immerse effect magnitude.

Twitch Strength scales:
- Nearby-fire camera shake amplitude
- Nearby-fire DynamicBlur intensity

Explosion Shake Strength scales:
- Explosion camera-shake amplitude
- Explosion duration/frequency calculations remain original

Recoil Shake Strength scales:
- Weapon firing camera-shake amplitude
- Duration/frequency remain original

Force Effect Strength scales:
- Radial blur intensity
- Screen darkening / color-correction intensity
- Original buildup and fade timing remain intact


COMPATIBILITY
-------------
The original LAxemann/L_Immerse internal PBO prefixes and CfgPatches names are
preserved intentionally. This prevents hard-coded paths and addon dependencies
from breaking.

Do NOT load the original Immerse_main.pbo / Immerse_sys.pbo alongside these
replacement PBOs.

Replace the originals with:
- 506th_util_immerse.pbo
- 506th_util_immerse_sys.pbo


LEGACY CLEANUP
--------------
The fired-player handler referenced _weapon even though the legacy parameter
definition did not explicitly retain it. The rework preserves _weapon correctly
while making no gameplay change beyond the configurable effect scaling.
