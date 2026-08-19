# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.3.1

## ADDED IN 0.4.3.1

+ Added warning lights to Su-25 & calibrated some more indicators

+ Added engine startup delay to AFRF jets

+ New AK Animations deployed, Model.cfgs of respective weapons retimed

+ Added Klen-PS targeting system to Su-25 (vehLockTargets (default R) - activate laser, vehLockTurretView (default ctrl+t) - lock target)
{CHANGESADDED}

## IMPROVED IN 0.4.3.1

^ Some more tweaks to Su-25 interior

^ Changed Kh-25/29 missile trail effect

^ Klen-PS can be now turned off by pressing R second time, cooldown time is dependent on usage time (<15s - 15s of cooldown, <30s = 30s cooldown, >30 & <60 = 60s of cooldown)

^ Added new mixed AT loadout preset for Su-25

^ Tweaked Su-25 hitpoints

^ Another tweak to engine startup script to improve it's behaviour in MP

^ Tweaked MCLOS function

^ Tweaked explosionShielding of PFM-1 mine

^ Increased PTM-1 mine hit value

^ Added PTM-1 & PFM-1 to mine module

^ Adjusted 9K32 and 9K38 damage values and parameters

^ Rotated incorrectly oriented submunitions

^ Re-added old AK mag change sound that was synced with RHS_GestureReloadAK2

^ Tweaked BMP-2 tracks rvmat

^ Added short description to ammo types

^ Tweaks to russian SACLOS missiles

^ Small tweak to su25 interior texture

^ Reduced Lipa/Vitebsk mag count due to MP compatibility 
{CHANGESIMPROVED}

## FIXED IN 0.4.3.1

@ Some Kh-25 variants could not be fired (magazines weren't defined as compatible with their intended launcher weapon)

@ Fixed wrong magazine in ammo crate

@ Fixed PKM tracer count

@ Fixed missing missile error while using Su-25 (AT) variant

@ Fixe 2S3 Nuke explosion time

@ Mi-24 Changed Yaw SAS.

@ Mi-24 Changed max tail rotor stress.

@ Mi-8 changed Yaw SAS.

@ Fixed model.cfg errors with pedals

@ Fixed YakB submunition exploding when close to the helicopter

@ Removed some of custom panels from Mi-24, Mi-28 & Ka-52 gunners

@ Fixed UAZ, Ural & Tochka defines

@ Fixed access to Tu-95 control panel

@ Tochka-U wheels script errors and steering anims

@ Removed gunner seat from ejection seats

@ Removed (again) pylons from Mi-24VT

@ Fixed ZSU-23-4 component placement and various other model fixes

@ Fixed Mi-24P GSh cannon memory points

@ Mi-24 corrected force exertion point Z axis.

@ Mi-24 added some yaw stability into the yaw controller channel.

@ Mi-24 Reverted tail rotor Dynamic Pressure Ratio modifier to default.

@ Fixed .rpt errors about missing clear_empty.paa texture

@ Some of the russian missiles were missing missileKeepLockedCone parameter reducing their off bore capabilities

@ Mi-8 atrq pedal anims were inverted

@ Fixed Kh-29L wrong guidance

@ Fixed AK-74 (GP25) aiming memory points

@ Fixed missing Lipa on Mi-24

@ Fixed sound config had incorrect inheritance overriding Kh-29 missile launcher parameters
{CHANGESFIXED}

## REMOVED IN 0.4.3.1
{CHANGESREMOVED}

