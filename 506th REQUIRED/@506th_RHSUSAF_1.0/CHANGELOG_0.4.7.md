# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.7

## ADDED IN 0.4.7
{CHANGESADDED}

## IMPROVED IN 0.4.7

^ Added disableWheelsWhenDestroyed = 1 to USAF helicopters

^ Tweaked penetration of M993 round

^ Increased antirollbar force on Cougars

^ Tweaked Geo Physx & Fire Geometry of Cougars (bottom hull mainly)

^ Added SLAT sim to M1A1 TUSK I

^ Tweaked 3rd person camera of F-22

^ Tweaked M1 ammo hit dependency

^ Removed _generalMacros from RHS configs

^ Tweaked M1 & M2 Fire Geometry & hitpoints

^ Calibrated IHADSS PNVS view & added safezones so position of IHADSS should be same on all screen resolutions

^ Tweaked AI usage of AGM-114K

^ Tweaked all AGM-114 precision

^ Tweaked ATGM oversteer behavior

^ Added AI handler for AGM-114K usage

^ Reduced zeroing range of standalone RMR and MRDS sights, to match the versions mounted on top of MDO/SpecterDR

^ AH-64 PNVS monocular view is now transparent & HDU is visible

^ Increased AH-64 PNVS turn rate to 120 deg per sec

^ AH-64 AI can now switch between laser & radar guided missiles

^ Added text fire mode indicator to A10A

^ Removed old compass from MELB UI

^ Adjusted position of Caiman OGPK turret axis

^ UH-60M Yaw mixing unit now conforms to expectations (pedal neutral at 60 KCAS)
{CHANGESIMPROVED}

## FIXED IN 0.4.7

@ Fixed TOW launching sounds

@ Fixed TOW UI mode indication

@ Fixed accidentally removed AH-64 gunner UI handler which prevent camera jump when direction stabilization in NFOV was activated

@ Floating mag pouch shadows on Rifleman and Team leader SPCS vests

@ Some weapons did not have visible muzzle attachments when running RHS:USAF standalone (missing 'linkProxy' definition)

@ Fixed HIMARS commander could fire when turned in

@ Fixed interior light action

@ Fixed .rpt error for UCP Combat crewman

@ Removed incomingMissileDetectionSystem from ground vehicles

@ Fixed .rtm related .rpt errors

@ SFM wheel brakes UI element is now hidden when RTD is enabled

@ Disabled ability to lock on ground targets with F-22 gun (attempt to fix kamikaze dive attacks on ground targets)

@ Fixed AH-64 missing gunner feed when scrolling to radar MFD page

@ Fixed AH-64 AA/AG radar modes key handlers were not properly initialized

@ AH-64 gunner couldn't use TADS view in some MFD pages combinations

@ Unified AH-64 TADS zoom on pilot & gunner stations
{CHANGESFIXED}

## REMOVED IN 0.4.7
{CHANGESREMOVED}

