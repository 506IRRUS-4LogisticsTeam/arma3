# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.6

## ADDED IN 0.4.6

+ Hard-edge tri-color woodland/desert for BTR-80

+ Added scripts & FX to MSK-40P (WIP)

+ Added ZiL-131 (WIP)

+ Added T-72B3 (obr.2016)

+ Added 126th Coastal Defense Brigade Platoon decals

+ Added SM-320 Tripwire Flares

+ Added 6P53 Pistol

+ Added long-lost BMD-1 Tricolor camo

+ Added new armor simulation to AFRF equipment

+ Added optics hitpoints to T90A

+ UXO for Russian submunitions. Also placeable in Eden and Zeus (inc. minefield modules)

+ APU-68 launch rail for Kh-25 and S-24 air-to-surface munitions

+ Added magazine proxies to all weapons

+ Added 7N14 mag to SVD

+ Added pylon hitpoints to Su-25

+ Added ability to disable vanilla locking boxes - by default option is off and can be changed by checking "Targeting UI Off" checkbox in RHS Menu Options

+ Added ability to disable part of vehicle UI in RHS Game Options
{CHANGESADDED}

## IMPROVED IN 0.4.6

^ Tweaked Kh-29T & Kh-25MT sensors

^ Added workaround for pylon settings adding magazines to wrong turret (NUKE FIX)

^ Tweaks to autocannons configs

^ Inverted Mi-24 AFM artrq pedal animation

^ Tweaked troops NVG handler

^ Improved lower lods in 6B23 6Sh116

^ Improved unditching log proportions on BMP models

^ Improved BTR-80 textures

^ T-72B3 Turret detail corrections and decal placement is more realistic

^ Subdued cream/yellow tone on 2S3 camo

^ Changed tracer color of some Russian bullets (NSV, KPVT, 30mm HE)

^ Tweaked RPG soundFly

^ Tweaked T-72, T-80, T-90, Spurt-SD & BMP-3 tracks fire geometry

^ Tweaked BMP-1/2 tracks fire geometry

^ Tweaked BMD-1/2 & BMP-3 PhysX

^ More AKM line smdi tweaks

^ Added new icons for weapons

^ Added new icons for headgear & vests

^ Adjusted BMP-1 recoil animation

^ Tweaked BMD 1/2/4 PhysX LOD

^ Tweaks to suspension direction of all AFRF vehicles

^ Tweaks to handling of BMD-1/2/4 & BMP-3

^ Disabled LOAL flight profile on Russian bombs that weren't laser-guided

^ Enabled LOAL fire mode on Russian LGB weapons

^ Improved afterburner script

^ Added new cam shake utilizing vanilla functionality to airplanes

^ Removed fuel leak script since functionality is now in base game

^ Improved UAZ & Ural Fire Geometry & hitpoints

^ Experimental change to delayed door closing handler

^ Tweaked tank cannon dispersion

^ Added geometry occluders to Ka-52 & Su-25 interiors

^ Increased get in/out time from tanks to 2.1 seconds (previously 0.8)

^ Added script for leaving tank hatches open when AI bails out when either engine or hull is destroyed

^ Tweaked T-90 damage textures

^ Tweaked AFRF autocannons AI accuracy

^ Updated Su-25 flight model

^ Added icons for MSK-40P, SM-320, PFM-1 and PTM-1

^ Tweaks in mines config and stingtable.xml

^ Added editorpreview icons for MSK-40P, SM-320, PMN-2, TM-62M, PFM-1 and PTM-1

^ Submunitions spin in flight, with random offset

^ Reduced AI dispersion for 2A70

^ Added view cargo geometry occluder

^ Added UV missile detector to Mi-28

^ Tweaked BM-21 launch effects & added current fire mode indicator

^ Tweaked RPG-7 rvmat

^ Tweaked RPG-7 reload animations

^ Added additional AI firemodes to RPG-7

^ Tweaked BTR-60 SMDI map

^ Added Tank DLC current charge indicator to 2S3 & Podnos

^ Tweaked 2S3 Nuke explosion effects

^ Tweaked explosion effects of heavy bombs & cruise missile - close T2029

^ Tweaked camera shake effect of few missiles & bombs

^ Fixed as related mag shading error

^ Added new inventory icons to magazines

^ Added dispersion to RPG's

^ Drum mag texture tweaks

^ Tweaked width of visual tracks trails for T-72 & T-80

^ Tweaked 7.62 & 5.45 cartridge textures & rvmat

^ Added 9S475 hatches animations to Mi-24

^ Improved Mi-24 9S475 script - kudos to Sa-Matra for selectWeapon idea

^ Added empty ATGM shelf to Mi-24 possible loadouts - close T2312

^ Adjusted driver visibility in fire geometry for few more tanks & ifvs (t-80, bmps)

^ Tweaked MiG-29 & T-50 afterburner effects

^ Added pedal animations to T-50

^ Tweaked T-50 armor

^ Added data link to Ka-52, Mi-28 & T-50

^ Tweaked ejection script & changed simulation of canopies to thingX - should prevent possible crashes

^ Tweaked AI engagement ranges for R27 & R77 missiles

^ Added interior light to Su-25

^ Added geometry occluder to MiG-29 & T-50

^ Added interior light to Ka-52, Mi-24, Mi-28, MiG-29 & T-50

^ Tweaked stall warning threshold values

^ Tweaked PG15V & OG15V bounding boxes

^ Added soundFly parameter to O/PG9/15

^ Tweaked missile fire effects

^ Tweaked muzzle flashes rvmat

^ Tigr, Ural & Kamaz drivers may now freerly switch between seats (Tigr-M driver is still not able to do so due to turret setup)

^ Added T-72B3 (2016)

^ Added physX suspension to Mi-28 and removed rotors from PhysX LOD

^ Added main rotor destruction anim to Mi-28

^ Added suspension PhysX and main rotor destruction anim to Mi-8

^ Improved Luna searchlight intensity & range

^ Unified reflectors on IFVs & Tanks (FG-125 lamp)

^ Tweaked dispersion of 2A72 mounted on BTR-80A

^ Improved taxing behavior of fixed wing vehicles

^ Tweaked MiG-29 HUD minimal & maximal ranges of currently selected weapon reporting

^ Tweaked Mi-28 Fire Geometry & added RTD hitpoints (hydraulics & transmission)

^ Added more resolution LODs to Mi-28

^ Added parameter to hide PhysX suspension upon destruction for fixed wing aircracts

^ Adjusted ATGM launchers AI rate of fire - AI operating SACLOS launchers should wait till impact

^ Added turn out option to ZSU-23-4 driver

^ Improved ZSU-23-4 fire geometry

^ Refined wheel selections in geometry LOD so wheel replacing script can use new syntax with component detection
{CHANGESIMPROVED}

## FIXED IN 0.4.6

@ Fixed Ural tail sign alpha sorting

@ Fixed BMP-2 Ghost LOD

@ Fixed some S-25 rockets config errors

@ Fixed MP-433 safet mode selector

@ S-24/S-25 semi-auto mode would fire automatically (set `autofire = 0;`)

@ Fixed HDR going little crazy when using TPD-K1 on T-72 or T-80

@ Fixed one missing unit in cfgPatches preventing of showing some VDV groups in Zeus

@ Fixed wrong LOD being used when looking through NSVT optics on tanks

@ Fixed Zenitco handlers

@ Fixed laser designators magazines prevented rearming at trucks

@ Fixed BMP-2D wrong selection on turret

@ Removed rear handle from Tigr-M

@ Fixed non closed shadow in Su-25 canopy model

@ Fixed random damage texture changing when some parts of vehicles were damaged

@ fixed AS Val & VSS Vintorez sounds in AI modes

@ Fixed BMP-3 turned out mirrors handling

@ Various fixes to updating base classes rpt errors

@ Fixed BMD muzzle flashes not being animated

@ Fixed BTR driver default view direction

@ Adjusted LODDriverTurnedOut to new syntax after Tank DLC release

@ Fixed Gaz-66 initial view angles

@ Fixed copilot Tu-95 animations

@ Fixed vis@ Fixed visiblity of hatch actions in BTRs when using remote units

@ Fixed Radio Protocol errors

@ Fixed MiG-29 ladder being visible after destruction

@ Fixed barrel launched ATGMs missing targets

@ Fixed lodTurnedOut values after syntax change introduced with Tanks DLC

@ Fixed errors with MSK-40P (white) and SM-320

@ Fixed missing some of BMP-3 groups in Zeus

@ PFM-1 and PTM-1 mines floating in the air when deactivated

@ Some more fixes to missile selection after Tanks DLC

@ Removed Ka-52 pilot camera

@ Fixed gap in Su-25 cockpit glass

@ Fixed Mi-28 ejection script triggered when cargo was jumping out from the cargo compartment

@ Fixed Mi-24 FFV seats view when looking down the sights

@ Fixed small missaligment in Ural/Gaz Zu-23 gunner view

@ Fixed SSh-68 LOD

@ Fixed T-5000 missing reload sound

@ Removed pilot camera from Mi-8 & 24

@ Mi-8 Changed control system to have slightly less artificial stability.

@ Mi-8 Tweaked some mixing values in the control system.

@ Mi-8 Changed suspension length so wheels don't sink as much in the AFM.

@ Mi-8 Changed suspension damping to reduce bobbing in the AFM.

@ AK-103-1 and AK-103-2 could sometimes change to full-auto AK-103s when folding stocks or adding NPZ rails

@ Fixed head initial angle for Su-25 & T-50

@ Fixed ejection over water

@ Test fix for MiG29 spawning without textures

@ Fixed typo in air weapons config (weaponLockType instead of weaponLockSystem - radar locking detections were not working because of that)

@ Fixed aileron animations on Tu95

@ Fixed missing land contact memory point for medic bag

@ Fixed S-25 & Kh-25 Klen-PS guidance - close T2392

@ Fixed Maljutka hidding on BMD/BMP when there is no ammo

@ Gaz-66 has a bit more engine torque now

@ Fixed Tigr-STS braking

@ Fixed some UAZ geometry components allowing clipping with front of the car

@ Added T-90 and T-90A names in stringtable.xml

@ Fixed Mi-24 landcontact points

@ Fixed PTS cargo loading

@ Removed some unnecessary config definitions from root config which could cause issues with other mods loaded

@ Exhaust suppressors did not fully hide on Mi-8MTV3

@ AFRF inventory items (vest/helmets/uniforms) were missing in Zeus

@ Removed autocenter=0 from Mi-28 (might affect positioning of helicopter in already created missions)

@ Some upgraded AK-74s inherited the wrong inventory icon

@ Mi-8AMTSh/Mi-171 gunners could not be shot inside the helicopter
{CHANGESFIXED}

## REMOVED IN 0.4.6
{CHANGESREMOVED}

