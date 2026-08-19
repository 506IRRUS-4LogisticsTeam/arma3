# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.4

## ADDED IN 0.4.4

+ Added Dynamic Object Drawing option to RHS Menu Options. In planes & helicopters it's possible to decide whether near zero pixel object chopping optimization should be applied to ground vehicles. Following options are available: Off, Limited by Object View Distance, Limited by Terrain Draw Distance. By default option is turned off

+ Added new S-24 model and textures - close T1334

+ Italian strings by AtixNeon

+ Added FAB-100

+ Added FAB-500 M54 bombs - close T1332
{CHANGESADDED}

## IMPROVED IN 0.4.4

^ Increased max radar range of ZSU-23-4

^ Added showAsCargo params to Mi-8 & Tu-95

^ Klen-PS is automaticly disengaged after losing track

^ Removed vanilla lock tone sound on vehicles with SPO-15 RWR

^ Improved Tochka-U physx

^ Tweaked planes head leaning during sharp turns

^ Tweaked Su-25 loadouts

^ Tweaked sensors range further

^ Tu-95 sensors defined

^ Update to Shilka sounds (May be further modified)

^ Adjusted Su-25  & MiG-29 dive indicator

^ Increased CM immunity of AFRF radar guided missiles a little bit

^ Calibrated Su-25 CCIP mark

^ Added AP belts for ZSU and ZU-23

^ Update to BMD sounds

^ Adjusted Su-25 hitpoints

^ Ka-52 radar range increased to 11 km

^ ZSU-32 IncomingMissileDetectionSystem set to 0

^ Added firemodes to KMGU-2

^ Adjusted Su-25 hitpoints

^ Tweaked timing of AK(S)-74 reload animation

^ Renamed 5N7 to 7N6 and 7N6 to 7N6M, since 5N7 seems to exist only on wikipedia
{CHANGESIMPROVED}

## FIXED IN 0.4.4

@ Fixed Klen-PS throwing script error when USAF was not loaded

@ Fixed few scripts which were dependant on USAF, now should work without USAF loaded

@ 9M120 missile magazine had the wrong `pylonWeapon` assigned (other 9M120M/F/O, variants weren't affected)

@ Fixed AKS-74 folding into AK-74M

@ Fixed AKS-74N (plum) folding into NPZ version

@ Fixed AKS-74N (Plum - folded) muzzleflash was visible at all times

@ Fixed UAZ & Ural sounds

@ Fixed Vikhr missile guidance

@ Fixed Mi-24 ATGM handling on dedicated server

@ Fixed engine startup script

@ Fixed Pak-Fa inherited some Su-25 scripts

@ Fixed MiG-29 HUD clipping when mastersafe & HMD was engaged

@ Su-25 launch authorization lights were not working properly

@ AK103+GP25 reload anim was out of sync

@ Fixed rifle cartridges shadows

@ Fixed Tochka-U sounds

@ Fixed T-72B3 Tank Commander override

@ Fixed MiG-29 speed & alt baro indicator textures

@ Fixed MiG-29 wreck doing crazy stunts (non convex geometry)

@ Fixed UAZ (DShkM) gunner zoom levels

@ Fixed T-80UK dazzler glass weird texture

@ Fixed BMD-2 gun particle effects - close T2311

@ Inverted T-50 fin animations

@ PAK-FA was missing some radar size properties. Version with external pylons is now easier to detect by radars

@ Corrected bad strings for repair Ural in some languages - close T2320

@ T-50 & MiG-29 were missing pylon proxies in their fire geometry

@ Mi-24 Increased maxTorque and maxMainRotorStress values.
{CHANGESFIXED}

## REMOVED IN 0.4.4
{CHANGESREMOVED}

