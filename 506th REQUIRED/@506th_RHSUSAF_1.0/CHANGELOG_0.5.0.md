# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.5.0

## ADDED IN 0.5.0

+ Added SOCOM AUV and SOCOM ASV Ammmo Boxes to all variants as a configurable option

+ M1240 M-ATV MRAP (M2, Mk. 19, M240, OGPK and CROWS)

+ Extra Hellfire and DAGR magazines positioned for fixed-wing aircraft (A-29 etc)

+ M257 Hydra 70mm ILLUM rocket. Flare ignites after ~10 seconds of flight: approx 3km-4km ahead of launch point. Provides up to 120s of illumination.

+ Added M1245 MATV SOF Version.
{CHANGESADDED}

## IMPROVED IN 0.5.0

^ Added 2 IHADSS helmets to AH64 cargo & removed parachutes from it - http://feedback.rhsmods.org/view.php?id=4530

^ Tweaked Stryker BFT

^ Added mirror folding VG attribute to Stryker

^ Lowered M1 Abrams interior engine sounds - http://feedback.rhsmods.org/view.php?id=5189

^ Added death animations to Stryker crew

^ Tweaked Stryker airman guards position to reduce clipping with other passengers

^ Optimized interior light toggle function

^ Stryker config clean up

^ Improved FCBC2 symbology on Stryker MFD

^ Added new VG icons for M1025

^ Added working periscopes to Stryker Vehicle Commander

^ Improved Stryker BFT MFD

^ Updated folding script with support for custom folding gestures ("rhs_fold_anim" param)

^ Matched woodland FMTV wheel color to current woodland textures

^ Added geometric occluders to Stryker interior

^ Added folding animations to Mk17

^ Added recoils for folded SCARs

^ Adjusted M2 CROWS zeroing settings to be consistent with LRF + tweaked manual steps on Caiman & RG33 - http://feedback.rhsmods.org/view.php?id=4977

^ Tweaks to SCAR folding initialization

^ Added additional resolution LOD to ACU

^ Tweaked MATV physx

^ Made aiming cursor availability on mounted M240s, consistent with other MGs

^ M240H now ejects appropriately sized cartridges (see GREF UH-1H)

^ Changed M3 HMG name

^ Re-equipped A-10A with USAF gray LAU-131 rocket pods (legacy green ones are still available, renamed as LAU-68 but retain the extant 'rhs_mag_FFAR_7_USAF' classname)

^ Replaced all 40mm HE with HEDP

^ Switched regular US Army desert units to OEF-CP ACUs

^ Changed displaynames for helicopter rockets referencing "FFAR" to "Hydra" since FFAR is an older generation of rocket

^ rhs_mag_FFAR_7_USAF (Green LAU-68 rocket pods for fixed-wing aircraft) now fires old-style 70mm FFAR rockets, more suited to the classname

^ Tweaked shotgun reload script

^ Tweaked spalling properties

^ Added additional optics components to interior of Bradley

^ Tweaked twin M3 HMG configuration

^ Added workaround for AI not being able to eject from planes with ejecting seats

^ Tweaked LR AA missiles behavior - http://feedback.rhsmods.org/view.php?id=5284

^ Added AI friendly laser designators to helicopters

^ Added ability to manually reload M2, M240 & Mk19 on vehicle mounted weapons like M113 or MATVs by pressing reload key ("R")

^ Added custom recoil to M590 shotgun

^ Unified CROWS zoom levels - http://feedback.rhsmods.org/view.php?id=5349

^ Converted CROWS screens to MFD tech

^ Updated HUD horizon on A10A & F22A

^ Enabled interior cargo light in Stryker

^ Tweaked AH-64 interior light

^ Tweaked attenuation values on CROWS turrets

^ Added experimental interior shoting sounds to some vehicle mounted weapons

^ Tweaked attenuation settings of static weapons

^ Added LOAL mode to DAGR

^ DAGR was missing cam shake when being fired

^ Tweaked cam shake settings across USAF vehicles

^ Tweaked water resistance settings of UH60M & CH-47 - http://feedback.rhsmods.org/view.php?id=5359
{CHANGESIMPROVED}

## FIXED IN 0.5.0

@ Fixed C-130J not flying in 3den editor - http://feedback.rhsmods.org/view.php?id=5182

@ Fixed CH-47 & CH-53 downwash effect + improved buoyancy

@ Fixed Stryker rear wheels destruction animation

@ Fixed Stryker passenger seats (#1 was not accessible)

@ Fixed some shotgun reload function errors - http://feedback.rhsmods.org/view.php?id=5212

@ Fixed some Stryker hatches related issues

@ Fixed Stryker Air Guards had extra reflectors (searchlights)

@ Fixed some errors with folding script if weapon was without magazine - http://feedback.rhsmods.org/view.php?id=5037

@ Fixes ammo crates on top of M1239 AUV Mk. 19

@ Fixes window glass on M1238A1.p3d

@ Adds mirror glass to LOD 0/1/2/3/4 of the M1239 AUV

@ Fixed missing hands weighting in 3rd resolution LOD of ACU

@ Fixed TOW missiles being unresponsive if AI is being ordered to fire them by player commander - http://feedback.rhsmods.org/view.php?id=5252

@ 20 round M196 tracer mag had incorrect displayname string

@ M240 was missing safe mode switching sound - http://feedback.rhsmods.org/view.php?id=5260

@ Fixed some accessories icons - http://feedback.rhsmods.org/view.php?id=5265

@ Adds 2x more string entries for MATV names

@ Fixed M781 Practice round was missing in magazine well - http://feedback.rhsmods.org/view.php?id=5277

@ Fixed M2A2 components (regenerated then)

@ Fixed MATV OGPK M2 turret loadout - http://feedback.rhsmods.org/view.php?id=5293

@ Removed wrong config overwrites in USAF mod - http://feedback.rhsmods.org/view.php?id=5298

@ Added olive texture for M-ATV

@ Changed a bit MATV armor - http://feedback.rhsmods.org/view.php?id=5301

@ Fixed CH47 RTD ground contact points - http://feedback.rhsmods.org/view.php?id=5278

@ Missing door sound error on MRAPs when running USAF standalone

@ Some UH-60 variants could carry more occupants than they should

@ Fixed SMAW missile trail cfg - http://feedback.rhsmods.org/view.php?id=5348

@ Pass with CheckAll o2script - fixed otocHlaven/OtocHlaven on MATV

@ Fixed AOR2 texture - http://feedback.rhsmods.org/view.php?id=5338

@ Fixed duplicated hitpoints .rpt errors with static weapons

@ Fixed some missing texture error with MATV
{CHANGESFIXED}

## REMOVED IN 0.5.0
{CHANGESREMOVED}
