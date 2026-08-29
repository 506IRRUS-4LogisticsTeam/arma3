# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.5

## ADDED IN 0.4.5

+ Added partial gripod support for AI units when loadout is edited through Virtual Arsenal

+ Initial injection of 1990s M113s

+ AN/PEQ-16

+ Standalone RMR sight attachment, inc. forward-mounting versions

+ Added exhaust smoke generator to USAF vehicles

+ Added new smoke launchers effects to M1 tanks

+ Added Trijicon RX01 reflex sight

+ Camo variants of SR-25 Suppressor

+ RX01 w/o Filter

+ Field manual entry on using the A-10A's TVM

+ Added Xmas gift 1
{CHANGESADDED}

## IMPROVED IN 0.4.5

^ Cargo script is able to attach boats too

^ Forced AH6 & MH6 visibility in virtual garage

^ Improved Leupold MK4+M2010 scope alignment

^ Added displayNameShort to USAF magazines

^ Limited dynamic object drawing to Object Draw Distance

^ Added additional seat to MH-6M to fix issues with LOAD waypoint

^ Tweaked XPS3 Textures

^ Clean-up of M240 sections, UVsets and named properties

^ Added new PhysX to M2 Bradley family vehicles

^ Added interior occluders to M2 Bradley family vehicles

^ Picture in Picture bounding box tech applied to vehicle models. For optimising non-scripted PiP screens

^ Reduced headbanging when driving M113 & M2 Bradley

^ Removing Longbow radar from AH-64D is now handled through Vehicle Customisation menu (classes for the old editor placeable unit can still be spawned, VhC hides radar model and disables active radar sensor)

^ Linked CROWS PiP with current optic mode

^ Added recoil coef to USAF vehicle magazines

^ Improved M113 PhysX configuration

^ Replaced majority of M1911 mags in M1 Abrams inventory, with M9 mags (correct mags for resupplying crew sidearms)

^ Added new sounds for M1 using soundSet technology

^ Readded track driveOnComponent to M1

^ Improved M109 PhysX

^ Added interior occluders to M113

^ Added improved PhysX to M109

^ Added antiwater material to M113 interior

^ Reduced range of vehicles

^ Added new sounds for M1 (kudos to daskal from Steel Beast community)

^ Increased TOW2 time of flight & speed characteristic according to following table - https://fas.org/man/dod-101/sys/land/tow-flight.gif

^ Replaced USMC units' AN/PEQ-15s with AN/PEQ-16s

^ Disabled compatibility of forward-mounting Aimpoint T1s on M14 EBR, M24 and M40A5 where they would float in mid-air

^ Added vanilla FCS to AH64 & AH1Z autocannons

^ Zeus is now able to move vehicles during their engine startup

^ Tweaked M1025 PhysX

^ Adjusted Raven backpack mass

^ Improved FMTV PhysX configuration

^ Improved MZRZ4 PhysX configuration - final fix for suspension anims

^ Improved PhysX configuration of HEMMT, M1117 & Caiman

^ Adjusted fuel range of USAF vehicles

^ Tweaked ai firemodes settings

^ Adjusted Hellfire & Maverick speed

^ Adjusted aiDispersionCoefs for tanks

^ Updated IOTV vests

^ Exhaust smoke generator now consumes some fuel

^ Reduced recoil for M109A6

^ Adjusted Mk82 & Cluster bombs values so AI should use it more frequently

^ SOCOM FMTVs now have proper sound attenuation setting for open-top vehicles

^ Improved smoke dischargers for M1084A1R SOV

^ SR-25 rail covers were not retexturable

^ Adjusted sensor parameters on AGM-65F (Anti-Ship, IR Maverick): Lowered max target speed, raised max locking range

^ Added extra pip view distance options

^ US MERDC textures

^ Added gauges anims to Caiman

^ Added new driver anim to Caiman

^ Improved FMTV driver animation, mirror shape, gagues (animations/visuals) & shadows

^ Rescaled TOW missiles to correct size

^ Animated TOW-2/2A standoff probe extension

^ Added pedal anims to A10A

^ Tweaked A10A Center of Mass

^ Updated MK19 config and fix packing error

^ Tweaked 3rd person camera for tanks

^ Added TOW missile fly sound

^ Added rear-view mirrors to A-10A cockpit
{CHANGESIMPROVED}

## FIXED IN 0.4.5

@ Fixed MBAV Grenadier vest hitpoints inheritance

@ Fixed Duke hint being visible for everyone in MP

@ Fixed Caiman & FMTV 3rd person camera

@ Fixed FMTV missing gunner proxies in fire geometry

@ Fixed NT4 shadows

@ `Heli_light_03_base_F` missing hitpoints error

@ Fixed Doomsday mags ammo count

@ `rhsusf_mrzr4_w_mud` missing textures error

@ SU-230/PVS (CX5395) version of SpecterDR, was not displaying the correct reticle in 2D optics

@ Some vehicles had missing author strings when running USAF standalone

@ Only one mirror was functioning in FMTV gunner's view

@ Some missing geo in 90s M113

@ PiP view on FMTVs' passenger side mirrors, were inverted

@ Editor option to fold MRZR roll cage, was not functioning

@ Fixed Mark V SOC Zeus hint

@ Unarmed M113 view gunner LOD missing selection names: animation to hide IFF panels did not work, and cupola was always showing desert camo

@ Fixed duplicate turret hitpoints .rpt spam for some of the vehicles

@ IFF panels on M2A3 Bradley variants would shrink when using the "Hide IFF Panel" animation

@ Minor M109 alpha sorting bug when viewing antennas through the wire mesh on the turret bustle

@ Fixed MELB camera twitching when switching to ground lock

@ AH-64 & AH-1z were missing gunBeg/End memory points definition

@ Fixed mMaxDroop typo in PhysX configs of many USAF vehicles

@ Fixed MZRZ sound configuration

@ Fixed AI in A10A didn't want to use GAU-8 on ground targets

@ Fixed damage in AFM from rolling on the ground on UH-60 & CH-47

@ M977A4 (Repair) cabin SVC lights displaced

@ ACU uniform insignia alpha sorting

@ AH-1Z/UH-1Y Changed maximum and minimum anti-torque rotor pitch T0003819

@ UH-60M slightly changed SAS gsins.

@ Fixed ALQ-131 z fighting from pilot LOD

@ Fixed GAU-8 devbranch errors

@ Fixed mod logos
{CHANGESFIXED}

## REMOVED IN 0.4.5

- Redundant animation to hide AIM-9s on AH-64D, no longer shows in Vehicle Customisation (was made obsolete by Dynamic Loadouts)

- Removed US tropical verdant variants
{CHANGESREMOVED}

