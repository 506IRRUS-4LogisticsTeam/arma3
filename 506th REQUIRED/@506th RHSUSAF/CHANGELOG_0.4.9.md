# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.9

## ADDED IN 0.4.9

+ M1126 Stryker ICV

+ Tan pilot helmets to reflect change in US Army standard issue helmet color.

+ M16A4s with VLTOR IMOD buttstocks. Thanks to toadie2k for the stock model

+ M249 PIP with solid buttstock and RIS

+ Added M49A1 tripware flare

+ MK17 SCAR (standard FDE, and special 'murican textures)

+ M249 Lightweight Collapsible Buttstock

+ Added simple CWSS FCS for M1A1s with commander's Thermal Sight Module

+ Alternate ACH helmets with tan rhino mounts

+ Helmet randomization

+ Added new uniform inventory icons

+ Added unflip functions to MRZR

+ Additional M81, UCP, and Coyote Brown 100 and 200 round softpack mags for the M249

+ GAU-21 HMG added to CH-53E ramp (model by nextanimationstudio, gifted to RHS by armyinf & co.)

+ M1239 SOCOM Armored Utility Vehicle, designated M1239 AUV in game. Un-armed, M2 and Mk19 CROWS Variants

+ Adds all comms equipment as master file for all vehicles with comms gear, and AN/PRC-152 test object

+ M1238A1 RG-33 SOCOM Armored Security Vehicle 4X4. Un-armed, M2 and Mk19 CROWS variants

+ M1220 Caiman with CROWS-mounted Mk19

+ Editor placeable M2A1 and M19A1 ammo can items

+ ACH (Early)

+ ACH (Early/Rhino)

+ Battle Dress Uniform by DeltaHawk (in Lowland ERDL camo for GREF HIDF)

+ new USGI 20 and 30 rounds mags & magpull acc

+ New GBU-12 model

+ Added M8541 version with MRDS

+ Added M8541A version with MRDS

+ Added Leupold Mk4 M5 with MRDS

+ S&S Plateframe vest (several loudouts)

+ G3 uniform in AOR2 camo

+ Extra USMC SPC vest variant for M40 Scout Snipers

+ Added ability to force scope type in mission with mission namespace variable "rhs_preferedOptic"

+ Added reload system to M590 shotgun together with new animations - requires Arma 1.

+ Mk316 Mod 0 Special Ball (HPBT) ammunition for SR-25 and Mk17. Generally similar to M118 Special Ball, but slightly faster `initspeed` and reduced `visibleFire`

+ Added TI textures to Caiman, FMTV, HIMARS, HEMTT, RG33 & MRZR

+ Added M1025 TI textures

+ Added TI textures to F-22A

+ Added TI maps to AH1Z, UH1Y & CH-53

+ Added TI map to M252 mortar

## IMPROVED IN 0.4.9

^ AI should now engage M113 gunners

^ Modified US aircraft magazine displaynames and added `descriptionShort` tooltips (mouse over mag name in Dynamic Loadouts UI for a more detailed description)

^ Improved MLRS scripted firing effects

^ Tweaked M113 Mk19 gunner animation

^ Improved HIMARS MLRS launch VFX

^ Reduced glass reflection in AH-64 cockpit

^ Reduced PhysX track width to decrease chance of wheels with other vehicle wheels collision which usually leads to backflips

^ [UH-1Y]Gunners now hold onto miniguns

^ Separate "M249 VFG" classes in Arsenal are no longer required to convert the M249 to use a grip instead of a bipod (inc. new bipod slot attachments for M249)

^ Added grip system slot to Para stock M249s

^ Unified AH-64 MFD brightness

^ Tweaked inertia for M320 standalone grenade launcher

^ Improved M4 fire geometry

^ Gave M249 plastic box magazines a more appropriate `mass` value

^ Changed Aimpoint T1's displayname to its US military designation (SU-278/PVS)

^ Tweaked M16 fire geometry

^ Tweaks to AI TOW usage

^ Improved M107 & M2010 fire geometry

^ Extended class-switching script for top-mounting PEQ lasers, to accept value `rhsusf_acc_anpeq15 = 2;` (used in RHS:USAF for SCAR rail height accessories)

^ Anim to randomly fold the barrel handle on M249s

^ Tweaked M134 ammo count & used bullets on USAF helicopters

^ Added Virtual Garage option to close & open commander hatch on M113

^ Improved position/tint of M68 CCO lenses and brought back killflash

^ Unified hand animation scheme for M4's

^ US Army units now use M4's with Matech BUIS

^ Increased COM of MRZR & increased antirollbar - it should allow more natural weight shifting with same

^ Added new icons for M249 magazines

^ Tweaked engine startup delay - engine startup delay should be shorter when engine was turned off second ago. Should improve AI behavior which tends to constantly switch on & off gas turbines

^ Added new virtual garage icons for USAF static weapons

^ Tweaked M2 Bradley gun armor (no longer destroyable with small arms fire)

^ Added separate light hitpoints to bradley, stored in Hitpoints class

^ Animation to hide Rhino on RG33L Plus and Caiman Plus up-armoured MRAPs

^ Adjusted scale of M153 CROWS. Now has a correct height of 0.762 meters

^ Replaced TD Grip with KAC grip on the M27 IAR that has a permanent grip

^ M240 bipod legs position when folded

^ Added retexture selections to M249/Minimi

^ SR-25EC (Enhanced Carbine) now utilises 7.62mm muzzle-mounted suppressor attachments, instead of the Mk.11 type of collar-locking slide-on suppressor. (Joint Muzzles compatible)

^ Tweaked M113 land contact memory points snapping in Eden editor

^ Tweaked spall, HEAT & thermobaric ammo configs

^ Tweaked M240 fire geometry

^ Improved M240 hidden selections since magazines are moved to separate proxies

^ Regenerated 5.56mm STANAG magazine icons

^ Tweaked PiP scopes aspect ratio - it's now adjusted for 16:9 screens - http://feedback.rhsmods.org/view.php?id=4788

^ Added simple geometries to ACOG scopes

^ Added proper buoyancy & firegeometry to M4 Block II & Mk18

^ Resized and added LODs to original

^ Added new inventory icons for weapon accessories

^ RHS Vehicle icons in Virtual Garage should be visible on Steam branch release

^ Added separate name for development branch version

^ Re-equipped some MARSOC units with S&S Plateframe vests

^ Updated MARSOC Mk17 DMR's optic, to include an offset MRDS

^ Switched SWCC crews to AOR2 uniforms

^ Adjusted M2010 muzzle attachment so it can support Join Rails

^ Tweaked characters hands in shadow LOD

^ Removed heads from characters Shadow LOD

^ Halved the size of SU-230/PVS (SpecterDR) red dot in main telescope.

^ Adjusted SIDE proxy position on SMAW and M72

^ Adjusted proxy positioning setup of MAAWS and its optic to be more conventional

^ 40mm smoke grenades have now impact fuze & correct smoke time (~17-30 seconds) - http://feedback.rhsmods.org/view.php?id=4896

^ Added new VG icons to HEMTTs

^ Improved blank ammo with submunition tech so it works correctly in MP - http://feedback.rhsmods.org/view.php?id=4916

^ Added special high deflective material to armored vehicles barrels

^ Readded proxies to characters shadow LOD

^ Some more improvements to characters fire geometry

^ Added offset to FCS animation sources to fight imprecision of animateSource when vehicle is not local

^ Added visual optics destruction to many vehicles

^ M1 Tank: Converted zoom values to macros, Removed hs materials references from config, Tweaked turret & gun hitpoint values

^ Added RHSUSF loadorder

^ Improved addons loadorder

^ Added support for spent casing ejection to bolt action system (WIP)

^ Randomisation of grip folding on rifle-mounted M320 UGLs

^ Added sensorPosition param to some of the static weapons

^ Moved 100rnd 5.56mm C-Mags to BIS CfgMagazineWells class `STANAG_556x45_Large`. Will now load in M4/M16 type rifles but not M249 and BIS weapons where such magazines should not fit. (Arma 3 V1.92)

^ Added engine destruction effect

^ Added MFD based CROWS monitor

^ Added data link sensor to Stryker in order to simulate Blue Force Tracker

^ Added test BFT MFD panel to Stryker

^ Added data link reporting of own position to vehicles with blue force tracker

^ Added new 5.56x45mm cartridge

^ Improved ammo event handler inheritance

^ Cleared out BI magazine classnames from CfgMagazineWells where they are are now defined in vanilla Arma 3

^ Many USAF weapons will now accept magazines compatible with CBA JAM

^ Configured M14 EBR-RI for proxy magazines and `manazineWell[]`

^ Adjusted M14 EBR-RI handAnim and nudged laser/light proxy forward a little

^ Underbarrel proxy slot for M240 (part of proof-of-concept testing, but might find uses in future)

^ Updated USAF load order in order to fix compatibility with new, devbranch radio protocols

^ Converted M590 buckshot to shotSubmunitions to be more in line with new vanilla shotguns. Air friction is now working with pellets so beware that ballistics are quite different to what it used to be

^ Tweaked 12GA models

^ Mk.19 40mm mag displaynameshort

^ Disabled handheld compass in AH-64 & AH-1Z cockpit

^ M203, M320 & M32 are using sound set firing sounds

^ Added Wound textures and rvmats for ABU

^ Added Wound textures and rvmats for BDU

^ Added countermeasure dispensers to CH-47F model (hides when countermeasures are removed via Dynamic Loadouts/Pylons settings)

^ Configured all USAF aircraft to carry realistic amounts of of flares+chaff, which can be managed via Dynamic Loadouts/Pylon Settings (e.g. can load only flares for maximal amount of CM releases, but will be ineffective against radar-based threats)

^ Added TI textures for plenty of US vehicles & fixed some TI textures which were using placeholder abrams hull texture. Note that those vehicles are still missing engine heat textures

^ Tweaked M1117 wheels TI texture

^ Added separate rvmat for USAF vehicles spare wheels

^ Added wheel TI texture to M1238A1

^ Unified M1A1FEP & HC hitpoints + fixed engine smoke - http://feedback.rhsmods.org/view.php?id=5162

^ Improved Stryker TI textures

^ Added new fire geometry to Cougars - http://feedback.rhsmods.org/view.php?id=4991

^ Tweaked Cougars glass

^ Tweaked Cougar suspension animation

^ Added placeholder TI Textures to Cougar

^ Tweaked M113 wheels TI

^ Tweaked interior light toggle function

^ Added working fire geometry for MCTAGS turret

^ Added interior light to Stryker

^ Added basic 2nd res LOD to Stryker

^ Added HEMTT TI textures

^ Removed redundant/different displayname definitions from desert HEMTT classes

^ TI textures for ACU

^ Added decal RVMAT to M1232 & M1237

^ Added decal RVMAT to M1025

^ Adjusted static weapons TI textures

^ TI texture for G3 uniform

^ FROG uniform TI texture

^ Infantry/SOF helmet TI textures

^ Tweaked F22 decals material

^ Added procedural TI textures to Stinger pod

^ TI textures for crew helmets (ACVC, HGU-56)

^ Added damage & destruction materials to M252 mortar

^ Tweaked TI materials of various weapon accessories

^ Added second uvset to M8541 for scope selection

## FIXED IN 0.4.9

@ Fixed M113 gunner was using wrong LOD when in optic mode

@ Fixed M113 gunner view offset in non optic mode

@ Fixed M113 weapons were using wrong memory point for guns

@ [UH-60]Fixed missing "main rotor hide" selection in one res LOD, causing duplicated rotors at some distances.

@ Fixed tooltip text for C-Mag

@ Fixed missing launchers in Zeus crate menu

@ Fixed some AH-64 rpt errors about missing MFD icons

@ Some woodland Abrams were using desert decals

@ [UH-1Y]Fixed locked camera bug for gunners(UsePiP = 1)

@ Fixed M113 tracks explosion shielding

@ Added missing UH-1Y gunner anims /facepalm

@ M240B had an extra cocking handle in the View Pilot LOD

@ Fixed TOW AI engagment ranges

@ Reduced M113 resistance against IEDs

@ MELBs had unrealistic ability to detect passive sensor locks (visual, IR etc.) Now only RWR and MAWS

@ Added static weapons bags to cfgPatches so they can be used in Zeus

@ Updated M109 loadout selection after magazine renaming

@ Fixed M113 hatch stayed open

@ USMC grenadiers had wrong M4 (added carryhandle M4 w/ M203)

@ Fixed gripod freeze - http://feedback.rhsmods.org/view.php?id=4712

@ CH-53E ramp shadow LOD was welded to the fuselage creating some distortion when the ramp moved

@ Fixed small FAST helmet glitches with cover selection

@ Adds LODs to M1239 SOCOM AUVs

@ Fixed AO on M1239 Main CO

@ Adds Comms install to M1239 AUV

@ Adds comms suite to Cougar MRAP

@ USMC side winders were using wrong ammo

@ Fixed camo darkness on Cougar MRAP

@ Adds comm suite install to Caiman MRAP and RG-33L MRAP.

@ Fixes glass position on M1239 SOCOM AUV MRAP interior

@ Adds units to SOCOM AUV config file

@ Fixed UH-1Y was able to detect IR locks

@ Fixed USMC M32 grenadiers were using wrong weapons (with additional scope which they couldn't use, since it's integrated - it caused rpt spam)

@ Fixed open geometry in shadow LOD of TA31RCO-RMR PIP variant

@ Adds more undercarriage geometry to M1232 / M1237 MRAPs for far LODs

@ Adds OGPK Additional customisation options: Overhead protection and turret bustle to M1232 / M1237 MRAP

@ SOCOM AUV Thermal

@ Adds configurable turret accessories for Caiman MRAP with O-GPK turret

@ Adds O-GPK accessories to FMTVs

@ Fixes a bunch of little FMTV issues: CP Box cargo strap clipping, removes extra animations from versions that don't have them

@ Added autocenter & buoyancy named properties to C130J - please pay attention to missions already created since it might break plane position

@ M1 tanks were not engaging other tanks when AFRF was not used

@ Removed radio cables from pilot LOD of some IOTV vest since they were clipping badly in 1st person view

@ Fixed IOTV (repair) vest didn't match 1st res lod & pilot LOD

@ Fixed Mk.19 sounds in AI fire modes

@ Fixed zeroing of Glock 17, M9 Beretta & M1911A1

@ Fixed missing penetration material for Glock 17

@ Removed Abrams TI textures in HIMARS rvmat - temporary fix till proper TI textures are there

@ Fixed camo selections on Black PMAGs and CMAGs - http://feedback.rhsmods.org/view.php?id=4828

@ Flag position on Caiman MRAPs changed position in different LODs

@ Some ACOG sights had a high section count in lower LODs

@ Fixed M1238A1 turn out option for drivers - http://feedback.rhsmods.org/view.php?id=4844

@ Regenerated components on M1239 - http://feedback.rhsmods.org/view.php?id=4823

@ Fixed M1A2SEPv1 CITV firegeometry materials - http://feedback.rhsmods.org/view.php?id=4847

@ Fixed some error messags if unit has only single magazine and gripod is attached

@ Fixed missing uvset error on MBAV & Plateframe vests (tex1 in rvmat)

@ Fixed some unnecessary tex1 reference in rvmat which were causing .rpt spam in Diag.exe

@ Fixed some bad interpolation in FFV RG-33 config

@ Fixed some broken inheritance due to fault sound configs overwrites

@ PMAG was very slightly offset to the right of the magazine proxy axis

@ Fixed missing head shadows in view pilot

@ Fixed driver interior sounds + added ability to switch between seats for various USAF vehicles with turn out/in option

@ SMAW & MAAWS were missing dispersion - http://feedback.rhsmods.org/view.php?id=4865

@ Fixed initial view angle for M1117 driver - http://feedback.rhsmods.org/view.php?id=4861

@ Removed turn out option from M1238A1 Crows - http://feedback.rhsmods.org/view.php?id=4867

@ Fixed FROG uniform ghost LOD

@ Scoped out incomplete Smoke and Illum mag classes for MAAWS that were showing in Arsenal but are not made compatible with the launcher

@ Fixed inverted Stryker crew - http://feedback.rhsmods.org/view.php?id=4832

@ Added penetration materials, armor & explosion shielding parameter to all RHS explosives

@ Fixed missing fire mode indicator in some of the helicopters if AFM & gauges were turned on

@ Fixed Stryker RWS optics hitpoints

@ Fixed Stryker fuel hitpoint

@ Fixed missing uvset asserts

@ Fixed some minor issues with new character firegeometry

@ Removed ambient shadow under mirrors from Stryker

@ Added some missing cfgPatches entries for USAF troops

@ Fixed inverted normals on 12GA bullets

@ Typo in M249 CfgMagazineWells classname

@ Typo in ABU and BDU displayName

@ M136 and SMAW  launchers are no longer accepted under Code Duello (Duel Purpose -> Dual Purpose)

@ Short M590 shotgun was missing magazine proxy

@ A-10A's cockpit shadow become non-closed when assigning different texture/materials the 'camo2' hiddenSelection

@ Fixed ghost LOD on M4 with M320

@ Fixed spare wheels TI on RG33L & SOCOMUAV

@ Fixed RG33 & SOCOMUAV TI textures being super bright in TI when gun was fired

@ Fixed some of the M1232 & M1237 vehicles were missing rvmats on certain selections

@ Fixed HEMTT exhaust particle effects

@ Fixed USAF air weapons TI textures

@ Fixed open shadows in some FMTV models

@ Another fix for HEMTT exhaust particles

@ removed extra space in HEMMT displayname string

@ RPT errors fixes related to M252

@ Fixed vehclass typo in MRZR cfg

## REMOVED IN 0.4.9

- Removed .p3d files: m16a4_ris_pmag.p3d, m16a4_ris_carryhandle_pmag.p3d (separate models are obsolete since mag proxy implementation)

- Removed unneeded M249 models: `m249_pip_S_vfg.p3d`, `m249_pip_L_vfg.p3d` (separate obsolete since converting bipods to attachments)

- removed vanilla entries from magazine wells since it's already introduced in base game

- Removes old RG-33 MRAP series as legacy vehicles

