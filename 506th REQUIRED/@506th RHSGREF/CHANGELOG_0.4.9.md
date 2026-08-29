# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.9

## ADDED IN 0.4.9

+ [UH-1H]Added Tan, Olive and White textureSets

+ Added new inventory icons for GREF uniforms

+ Added CDF 2S1

+ M1941 Jeep Cap

+ M43 Field Caps

+ M40 Stahlhelms

+ M42 Stahlhelms and covered variants

+ S-Mine 35

+ S-Mine 44

+ Glasmine 43

+ A200 mine

+ Stockmine 43

+ Tellermine 43

+ M2A3 bounding mine

+ M3 mine

+ Mk.II mine

+ M7A2 mine

+ 2.5lb Tetrytol charge

+ Model 1939 hand grenades

+ Nb.Hgr.39 smoke grenades

+ Model 1924 hand grenades

+ Model 1943 hand grenades

+ Throwable Sprengbuechse (3kg)

+ Mk.I illumination grenade

+ Mk.II hand grenade

+ Mk.IIIA1 concussion grenade

+ Early AN/M8 smoke grenade

+ M15 White Phosphorous grenade

+ Throwable 1lb TNT charge

+ Added new RKG-3EM grenade script

+ Flecktarn version of Gorka 1 uniform

+ BTR-60 in TLA livery

+ Texture sets for TLA BTR-60PB

+ Added L1A1 rifle (heavy WIP)

+ Added IZh-18 reload animation (WIP, missing prone stance)

+ Added reload animation for M3A1 Grease Gun (WIP, prone variant missing)

## IMPROVED IN 0.4.9

^ [UH-1H]Increased maxFordingDepth

^Configured Mosin SBR and covered SDN-6 suppressor with Joint Muzzles

^ Added ECM to Mi-24G & added laser warning receiver to it

^ MG42 shell ejection particle effects

^ M93 uniform TI texture

^ Added new icons for WW2 helmets & caps

^ RHS Vehicle icons in Virtual Garage should be visible on Steam branch release ^ Added separate name for development branch version

^ Added Eden attribute to hide CHDKZ flag on T-72 http://feedback.rhsmods.org/view.php?id=4854

^ Readded proxies to characters shadow LOD

^ Some more improvements to characters fire geometry

^ Added RHSGREF loadorder

^ Improved addons loadorder

^ IZh-18 is now using shotgun sounds

^ Added deleteIfEmpty = 0 to IZh-18 magazines

^ Gave VHS-2 and its OEM magazines true-to-life compatibility with G36, using common `magazineWells[]' framework. (class CBA_556x45_G36)

^ Tweaked BRDM-2 buoyancy & increased turning rate in water - http://feedback.rhsmods.org/view.php?id=4963

^ Tweaked again BRDM-2 turn ratio

^ Added facewear proxy in pilot LOD of GREF uniforms

^ Update Textures and set default texture for BTR-60

^ Added CBA magwells to GREF weapons

^ Improved flecktarn texture for PASGT-type helmet cover

^ Added L1A1 reload animations

^ Added wooden furniture to L1A1

^ Finger is out of trigger when reloading

^ Added resolution LODs to M1 Garand

^ `Camo` retexture selection for M1951 cap

^ Added M1 Garand reload animations

^ Added silenced sound to L1A1

^ Added magazine proxies for M79

^ Added new reload animation for M79 (WIP)

^ Added some polygons to hide backfaces seen through the opening in the rear of Multicam SDN6 suppressor

^ Added CDF, UN & CHDKZ skins for ZiL-131 (kudos to Tema!)

^ Anim exporter test on M79 (without rotation)

^ Improved M1 Garand reload animation

^ tweaked M79 reload anim

^ Tweaked L1A1 reload animation with model.cfg exporter

^ Tweaked M1 Garand & M79 reload animations

^ Another iteration on L1A1 reload animations

^ Added short ammo description to IZh-18 12GA mags

^ Added resolution LODs to L1A1

^ Added some placeholder M3A1 reload sounds

^ Tweaked M3A1 hand animation

^ Tweaked M3A1 reload animations

^ Merged M3A1 & M3A1 specops to single folder

^ Added inventory icon for specops variant of M3A1

^ Added resolution LODs to MP44

^ Added new hand animation to MP44

^ Added new reload sounds for M3A1

^ Added test MP-44 reload animations

^ Improved MP44 reload animations

^ Added placeholder reload sound to MP44

^ Added reload sounds for L1A1 & M79

^ Improved L1A1 & M79 reload animations

^ Added spent clip ejection from M1 Garand

^ Added M1 Garand reload sound

^ Added sound sets to GREF UGLs

^ Adjusted M1 garand magazine reload switch phase

^ Incorporating improved CDF and ChDKZ Mi-8 textures

^ Tweaked decals RVMAT on GREF vehicles

^ Tweaked Canoe anims & config

^ Configured appropriate GREF aircraft with Dynamic Loadouts/Pylon-based countermeasures

^ Moved origin point of flare/chaff dispensed from L159, to a more realistic location

^ Tweaked available stores for some L39/L159 Pylons

^ Optimized canoe paddle script

^ Added TI texture for BRDM-2 new wheels

^ CDF paratrooper uniform TI map

^ Helmet TI textures

^ Tweaked Superhind TI textures

## FIXED IN 0.4.9

@ [UH-1H]Fixed RPM indicator position

@ Fixed missing Panzerfaust in Zeus crate menu

@ Fixed CHDKZ sniper was using wrong scope

@ Added missing Cesna entry in units[] cfgPatches array - plane was missing in Zeus

@ Fixed driver sounds of armed BRDM-2UM

@ HIDF UH-1H door guns now have correct ammo

@ Nationalist Militia Ural ZU-23 gunner was using non-existent infantry class

@ Fixed grenades were available for M70B1 when only GREF was loaded. Removed them since muzzle grenade feature is not present

@ Adjusted UH-1H wreck placement

@ Fixed Mi-24G eden attribute for setting custom side number

@ corrected a few vehicles using wrong number decal types

@ Selection for tube extension on RPG-75 used model was wrong

@ Fixed AN-2 set side number Eden attribute

@ Fixed missing heads shadows in View Pilot LOD

@ Added penetration materials, armor & explosion shielding parameter to all RHS explosives - http://feedback.rhsmods.org/view.php?id=4876 http://feedback.rhsmods.org/view.php?id=4878

@ Fixed characters hands being screwd in last res LOD - added shadowlod param

@ Fixed missing default magazine property for some of the satchels - http://feedback.rhsmods.org/view.php?id=4904

@ Fixed some minor issues with new character firegeometry

@ Kar98 handAnim had gone AWOL

@ Fixed BRDM-2UM (Armed) searchlight glitch in 1st LOD

@ BRDM-2UM TPKU-2B is hidden in armed variant in interior LOD - http://feedback.rhsmods.org/view.php?id=5001

@ Fixed ZiL-131 crew - http://feedback.rhsmods.org/view.php?id=5049

@ L1A1 was missing case ejection

@ Fixed icon overlay on L1A1

@ Fixed CDF MiG29 textures in multiplayer - http://feedback.rhsmods.org/view.php?id=5090

@ Fixed missing CDF ZiL-131 texture - http://feedback.rhsmods.org/view.php?id=5103

@ Some Mi-24G variants available to Zeus, were equipped with the wrong type of ATGM

@ Camo fuel pod magazine for L39/L159 had an incorrect model path

## REMOVED IN 0.4.9

