# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.9

## ADDED IN 0.4.9

+ Added T-90AM (obyekt 188AM)

+ Added T-90SM (obyekt 188SM)

+ Added T-90SA (obr.2004g.)

+ Added T-90SA (obr.2016g.)

+ added folded as val model

+ Added 3D PSO-1 (ironsight ADS is not working atm) - can be equiped by switching preference to 3D optics in RHS game options

+ Added TNT charges (75, 200 and 400g.)

+ Added OZM-72

+ Gorka-1 uniform

+ Helmet randomization

+ Added new uniforms inventory icons

+ GP-25 is now using magazine proxies

+ Added 2S1

+ Added 810 OBrMP symbology to decals

+ Added Grip system to AS Val & Vintorez

+ Added new SoundSets based sound configuration for vehicles (WIP)

+ Added new sounds for Kamaz-5350

+ Added ability to force scope type in mission with mission namespace variable "rhs_preferedOptic"

+ Added T-14 Armata ※ Offensive systems (armament and fire-control) and defensive systems (armour and active protection) are still very much a Work In Progress

+ Initial commit of Katya and Vidda Warlords missions. Feel free to improve!

+ HIDF vs TLA Warlords

+ Mil Mi-8T (early Hip variant with Klimov TV2-117 powerplant)

+ Added additional ammo types to BM-21

+ Initial push of Livonia Warlords

## IMPROVED IN 0.4.9

^ Tweaked BMP/D-2 ATGM usage by AI when target was close

^ Another attempt to improve MSK-40P behavior in MP

^ Added useWorldEnvMap=true; to vehicle glass rvmat

^ Reduced PhysX track width to decrease chance of wheels with other vehicle wheels collision which usually leads to backflips

^ Reduced Mi-24 glass reflectiveness

^ Tweaked PKP textures (WIP)

^ Tweaked folding script - it's now possible to fold AK74MR & Zenitco variants when optic is mounted on RIS rail

^ added _ti textures for T-72B3 (2016)

^ Added 3D variant of 1P29

^ added new optic for rear cam on T-72B3M

^ added log for T-72B3M

^ added icon for T-72B3M

^ changed names of random components on T-72B3M

^ Improved AFRF VG40MD smoke grenade bounciness

^ Improved RGN/RGO so it uses more engine functionality instead of scripts

^ Tweaked engine startup delay - engine startup delay should be shorter when engine was turned off second ago. Should improve AI behavior which tends to constantly switch on & off gas turbines

^ Changed SVD hand anim to grip one

^ Changed radar shadows to soft one by using visualEx sbSource

^ Added Land_ classes for radars so animations should work on map placed objects

^ Added new virtual garage icons for AFRF static weapons

^ Tweaked 1P87 reticle brightness

^ Added basic setup of cat eyes to 2S1

^ Improved 122mm casing for ejection

^ Improved "Cat Eyes" - now using fade out texture instead of sharp edged one

^ Decal scripts can take arrays of label places

^ Tweaked Ural explosion vulnerability

^ GP-25 is now using soundset tech for firing sounds

^ Tweaked D-30 shell ejection script

^ Tweaked D-30 AI sensor pos so AT variant can now fire behind sandbags

^ Tweaked AI aiming & sensor positions for Kornet & SPG-9

^ Disabled damageHide on Mi8 since it's not used due to Wreck type destruction

^ Cleaned up numberPhysicalWheels - removed it from non helicopter vehicles & added proper value to some of the helicopters

^ Changed tank barrels fire geometry - added new material to them with much higher deflection chance

^ Tweaked spall & HEAT ammo configuration

^ Improved T-72/90 Character Collision Geometries http://feedback.rhsmods.org/view.php?id=4826

^ Adding unique recoil classes to Russian rifles (using values from BI equavilents atm)

^ Tweaked AS Val muzzle smoke

^ RHS Vehicle icons in Virtual Garage should be visible on Steam branch release

^ Added separate name for development branch version

^ Added more apprioriate anim for T90SM gunner

^ Removed heads from characters Shadow LOD

^ Added new accessories icons

^ Tweaked again RPG-7 dispersion

^ Removed some obsolete insurgents from AFRF

^ Added variable to T-72 flag script which allows disable its spawning

^ Made VG-40MD explode on impact (+ removed color variants) - http://feedback.rhsmods.org/view.php?id=2740

^ Added brakes sounds to Kamaz

^ Tweaked VG-40MD ballistic - http://feedback.rhsmods.org/view.php?id=4914

^ Calibrated PSO-1 - http://feedback.rhsmods.org/view.php?id=4910 (WIP)

^ Tweaked scope proxy on PKP - http://feedback.rhsmods.org/view.php?id=4920

^ Changed AK-103 inheritance

^ Readded proxies to characters shadow LOD

^ Some more improvements to characters fire geometry

^ Added offset to FCS animation sources to fight imprecision of animateSource when vehicle is not local

^ Added AFRF loadorder

^ Improved addons loadorder

^ Configured amphibious properties of 2S1

^ Added 2S1 Commander & Loader animations

^ Increased a little bit 2S1 torque on low rpm

^ Added sensorPosition param to some of the static weapons

^ Tweaked RPG-7 proxies size to fit more with vanilla RPG

^ Moved some features of BRM-1K's turret from an external proxy to be part of the model. Vehicle can now be fully retextured with hiddenSelectionsTextures etc.

^ Improved RHS radio protocol compatibility with other mods

^ Tweaked 2S1 water turning radius - http://feedback.rhsmods.org/view.php?id=4960

^ Tweaked BMP1/2 buoyancy lod & reduced turning speed - http://feedback.rhsmods.org/view.php?id=4959

^ Tweaked once again 2s1 water turning

^ Extra customisation anims for Mi-8/17 helicopters

^ Removed countermeasure dispensers from civilian Mi-8

^ Added 6DOF view to Ka-52 - http://feedback.rhsmods.org/view.php?id=4987

^ Tweaked Mi-28 MFD parallax values - http://feedback.rhsmods.org/view.php?id=4985

^ Added facewear proxy to pilot LOD of AFRF uniforms

^ Added forcedInitialOrientationDir[] (Arma 1.92 feature) to 125mm petals

^ Tweaked BTR-60 body normal.

^ Improved ammo event handler inheritance

^ Many AFRF weapons will now accept magazines compatible with CBA JAM

^ VOG-25P & RPG-7 Type-69 are  using triggerAmmo for airburst instead of spawning collider

^ Added optional probability param to turret blow off script

^ Tweaked RWR announcer script

^ Tweaked Ka-52 HUD

^ Improved BTRs amphibious behavior - http://feedback.rhsmods.org/view.php?id=4982 http://feedback.rhsmods.org/view.php?id=4981  http://feedback.rhsmods.org/view.php?id=4984

^ Tweaked Ka-52 main gun indicator http://feedback.rhsmods.org/view.php?id=5002

^ Updated AFRF load order in order to fix compatibility with new, devbranch radio protocols

^ Updated Katya Warlords points

^ Improved lights and cat eyes on T14

^ Enlarged cat eye lights on T-14 so they are slightly more visible

^ Added RWR, LWR & Arabalet radar to Ka-60

^ Re-generated Russian Mi-8 textures after removing some baked-in shadow artefacts from hidden or moving parts

^ Some additional customisation animations for Mi-8/Mi-17 series

^ Unified decals rvmat

^ Reduced flare count on Ka-52 to 128 to make it in line with Mi-28

^ Unified decals rvmat

^ Increased z bias on decals

^ Tweaked Ural & UAZ wheels rvmat

^ Added WIP BM-21 caps

^ Removed hand held compass from mi-28 & Ka-52 cockpit

^ Added basic dynamic loadout configuration for BM-21 using pylons tech

^ Tweaked Ural wheels specular map & rvmat

^ Improved Civilian Mi-8 textures

^ Tweaked Kamaz land contact points

^ Tweaked Ural/Kamaz wheels again

^ Tweaked Ural-4320 sound config

^ Tweaked ZiL-131 suspension

^ Tweaked decals alpha sorting on GAZ-66

^ Added log to BMP-3 shadow

^ Tweaked decals RVMAT on BMP-1

^ added TI textures for Kamaz & UAZ wheels + configured spare wheels TI

^ Tweaked BM-21 animations

^ Tweaked BM-21 particle effects

^ Added wheel damage materials for Ural, UAZ, Kamaz, Zil-131 & GAZ-66

^ Standardized wheel damage on trucks

^ Tweaked again BM-21 firing effects

^ Added launcher hitpoint to BM-21

^ Tweaked tracer burn time on PKM rounds (last mag round)

^ Extracted Sprut SD proxies and made commander periscope rotatable

^ Tweaked ZIL-131 wheel textures

^ Optimized Ka-52 UI & MFD scripts - replace setObjectTexture trickery with setUserMFDText solution

^ Reduced number of BM-21 fire particles

^ Added TI texture to Ka-52

^ Tweaked TI materials settings to various AFRF air weapons

^ Tweaked BMP-3 wheels TI

^ Tweaked interior light toggle function

^ Adjusted T90SM/AM TI textures to be more in line with rest of T72 variants

^ Adjusted static weapons TI textures

^ EMR uniform TI texture

^ Adjusted Kamaz & SPG-9 TI textures

^ Infantry helmet TI maps

^ Added TI textures for Tu-95, MiG-29 & T-50

^ Tweaked missiles TI materials

^ Added TI textures to Pchela-1T

^ Added TI textures to NSVT, ZU-23 & Kornet

^ Added TI textures for PKP & PKM

^ Warlords mission tweaks

^ Tweaked Igla TI texture

^ Zsh-7A aircrew helmet TI texture

^ Added TI textures for AK103/4/5 & AKM

^ Adjusted procedural TI textures on zenitco accessories

^ Tweaked TI materials of various weapon accessories

^ Added TI textures to AK accessories, SVD, T5000, AS Val, VSS, AKS74U, PP2000 & made some tweaks to other ones

^ Turned off A2 Russian radio protocol in favor of A3 one

^ Added some initial T-14 armor configuration (ERA)

^ Rear cargo doors can now be removed from Mi-8AMT and Mi-8T through Vehicle Customisation

^ Added TI textures to radars and pistols

^ Added new T-72 & T-80 sounds in SoundSet tech

## FIXED IN 0.4.9

@ Fixed Mi-24 hand aircraft throttle indicator by accident

@ Fixed BRM-1K gunner optic view

@ Fixed Zu-23-2 gunner death anim

@ Fixed tooltip string for 7.62x39 drum mag

@ Fixed T-72/90 tracks movement when one of the side was destroyed

@ Fixed BTR-70 periscope selection

@ 2S3 was missing buoyancy property in geometry LOD

@ 6b71m + Balaclava helmet variants had two conflicting `camo1` hiddenselections in lower LODs (named camo1 and Camo1)

@ Fixed 2A41 weapon selection

@ Fixed Russian radio protocol missing .wss rpt error

@ T-50 with external pylons was missing in Zeus

@ Moved BM-21 to artillery subcategory

@ Added static weapons bags to cfgPatches so they can be used in Zeus

@ Alpha sorted cargo LOD of T-72 obr 2016

@ Fixed BM9 selection on T tanks when player starts as a gunner

@ Fixed gripod freeze - http://feedback.rhsmods.org/view.php?id=4712

@ Corrected Mi-17/8 auto-hover center.

@ Fixed some of the pistols were missing safemode

@ Fixed radars destruction

@ Fixed Tochka-U starts with engine on when camo is selected

@ Igla launchers did not have penetration materials (produced dirt pfx when shot at)

@ Fixed RGO grenade was using wrong ammo

@ Adjusted PhysX setup for 2S1, temporary fix to make it somewhat useable

@ Fixed Russian radars were not moving when controlled by AI

@ GAZ-66 R142 had land contact memory points in wrong place

@ Fixed AGS-30 sounds in AI fire modes

@ Fixed BMP-3 driver animation

@ Fixed zeroing for 6P9 & 6P53

@ Fixed missing penetration materials for 6P9 & 6P53

@ Fixed missing rvmats on tank barrels

@ Fixed some Russian radio protocol .rpt errors

@ Fixed some error messags if unit has only single magazine and gripod is attached

@ Fixed updating base class errors due to sound config overwrites

@ Fixed missing heads shadows in view pilot

@ Fixed Tigr-M driver interior sounds + ability to switch between seats

@ Fixed PRP-3 radar action - http://feedback.rhsmods.org/view.php?id=4860

@ Fixed GP-25 recoil (was defined in mode, not in muzzle and that caused pop up error) - http://feedback.rhsmods.org/view.php?id=4879

@ Fixed one needle in Kamaz interior had some zfighting issues

@ Added missing 6P9 suppressor icon - http://feedback.rhsmods.org/view.php?id=4873

@ Fixed MiG-29 was missing attenuation  effect - http://feedback.rhsmods.org/view.php?id=4890

@ Added penetration materials, armor & explosion shielding parameter to all RHS explosives - http://feedback.rhsmods.org/view.php?id=4877

@ Fixed D-30 folding in virtual garage - http://feedback.rhsmods.org/view.php?id=4883

@ Readded old Mi-24 interior sounds till new ones are ready - fix for http://feedback.rhsmods.org/view.php?id=4853

@ Fixed characters hands being screwd in last res LOD - added shadowlod param

@ Fixed people tag on Kamaz was assigned to multiple bones - http://feedback.rhsmods.org/view.php?id=4825

@ Small zfighting issues fixes in Kamaz cabin

@ Fixed missing 1P29 2D option - http://feedback.rhsmods.org/view.php?id=4875

@ Fixed some small zfighting issues in Gaz-66 cabin

@ Fixed SVD silenced sounds - http://feedback.rhsmods.org/view.php?id=4888

@ 1P29 was using wrong memory point in 3d mode

@ Fixed open shadow in 2nd shadow LOD of PSO-1M21

@ Fixed some issues with 3D PSO scope model - http://feedback.rhsmods.org/view.php?id=4910  http://feedback.rhsmods.org/view.php?id=4912

@ Removed some old sound definitions - http://feedback.rhsmods.org/view.php?id=4927

@ Fixed some issues with new character fire geometries

@ Fixed zeroing sync for 3D variant of PSO-1M2-1 - http://feedback.rhsmods.org/view.php?id=4935

@ Added missing DTK-1P icon - http://feedback.rhsmods.org/view.php?id=4938

@ BMD-4 FCS animation speed was not updated (it was to slow) - http://feedback.rhsmods.org/view.php?id=4946

@ Fixed some missing uv sets rpt errors in diag exe

@ Repaired non-closed geometry in shadow LOD of Type69 rocket grenade

@ Some parts of BMP-1 and BMP-1K FireGeometry LOD were sharing `Component##` selection names, so did not function correctly. Regenerated components to fix.

@ Fixed tank commander override was working even when gun or turret was destroyed - http://feedback.rhsmods.org/view.php?id=4958

@ Fixed PGO-7 illumination script - http://feedback.rhsmods.org/view.php?id=4973

@ Fixed BMD-1 maljutka removal Virtual Garage action + optimized some of the components by using useSource = 1 property - http://feedback.rhsmods.org/view.php?id=5045

@ Fixed Gorka-R broken geometry

@ Fixed UAZ driver animation due to inheritance to BIS offroad & it's recent fix for seat switching - http://feedback.rhsmods.org/view.php?id=5056

@ Forgot to commit improved BTR-60 geo buoyancy - fix for http://feedback.rhsmods.org/view.php?id=5063

@ Fixed T72/T90 gun mantle weighting - http://feedback.rhsmods.org/view.php?id=5117

@ extra commas

@ Fixed various cars/trucks missing engine on/off sounds

@ Fixed floating part of mesh on BM-21

@ Fixed salvo settings for BM-21

@ Fixed Kamaz glass TI

@ Fixed T80UE-1 searchlight http://feedback.rhsmods.org/view.php?id=5151

@ Fixed cockpit glass alpha sorting on MiG-29 http://feedback.rhsmods.org/view.php?id=5169

@ Fixed Ka-52 snapping in tracking mode

@ Fixed 2S3 turret TI texture

@ Fixed Tigr-STS & M thermal textures

@ Fixed some of the GAZ-66 Kungs parts were missing rvmats

@ Folded AK-103 with Zenitco rail, had magazine proxy in the wrong position

@ Fixed missing ZiL-131 map icon

@ HUD Off user action was appearing in unarmed "Mi-8MT (Cargo)" instead of armed "Mi-8MTV-3 (Cargo)"

@ Opening cargo doors on Mi-8s was not blocking units from sitting in the correct seats on some variants

## REMOVED IN 0.4.9

- Removed vanilla entries from magazine wells since it's already introduced in base game