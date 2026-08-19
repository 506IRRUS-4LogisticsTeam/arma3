# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.5.1

## ADDED IN 0.5.1

+ add vehicle in vehicle transport to CH-47 config

+ add vehicle in vehicle transport to CH-47 model

+ Vehicle in Vehicle Transport for C-130 model

+ Vehicle in Vehicle Transport for C-130 config

+ Adds the first iteration of the M1127 Stryker RV for de-bugging purposes (Not functional)

+ Adds DVE for Reyhard to use in various US Forces vehicles

+ Adds first iteration of the M1132 Engineer Squad Vehicle (ESV) with M2, and Surface Mine Plow (SMP).

+ Adds M1126 Stryker with Mk. 19 GMG

+ Adds DVE to RG-33 SOCOM ASV, and RG-33L 6X6 Series of MRAPs

+ Adds DVE to M1239 SOCOM AUV

+ Adds DVE to M142 HIMARS

+ Adds first commit of the M1134 Stryker ATGM Vehicle.

+ Adds detail to gunners controls

+ add vehicle in vehicle transport to CH-53 config and model

+ Adds the M240B MMG to the M1134 Commander's position, except not-working. Only animated.

+ Added M14 by WinteR5
{CHANGESADDED}

## IMPROVED IN 0.5.1

^ Added scripted workaround for planes not willing to engage ground targets if they have WSO

^ Tweaked ACOG back lens triangulation - http://feedback.rhsmods.org/view.php?id=5360

^ Changed M151 description from HEDP to HE - http://feedback.rhsmods.org/view.php?id=5380

^ Removed explosion sound from penetrator base class

^ Tweaked GBU-12 center of mass

^ Improved AGM-114 accuracy in terminal phase

^ Increased MP7 ammo damage output - http://feedback.rhsmods.org/view.php?id=2324

^ Added some workaround for SACLOS not working with AI with vanilla manual control - might be reverted if it contains some nasty side effects - http://feedback.rhsmods.org/view.php?id=5367

^ Tweaked SCAR-H recoil values - http://feedback.rhsmods.org/view.php?id=5387

^ Tweaked optics post processing effects

^m9 hammer animation set to single action

^ Tweaked ERA blocks durability against HEATs

^ Added healing attribute to M1230A1 + added few more first aid kits & medikits - http://feedback.rhsmods.org/view.php?id=5483

^ Tweaked M68CCO & SU-278 visuals when aiming down the sight

^ Tweaked M1240A1 weight - http://feedback.rhsmods.org/view.php?id=5441

^ Tweaked M150 PP effects

^ M19 is now triggered only on contact - placing mines in the middle of road will be no longer effective

^ M19 is now using additional penetrator to simulate blast damage

^ Added simple Rhino system to MATV (work on M1240A1 with M2 variant only at the moment)

^ Added visible waypoints to Stryker BFT

^ Tweaked Stryker Vehicle Commander view

^ Removed Stryker periscope full screen mode since periscopes can be used from vehicle interior

^ Tweaked hitpoints configuration on MATV + more tweaks to fire geometry

^ Added proper firegeometry to MATV  - http://feedback.rhsmods.org/view.php?id=5418

^ Optimized R2T on MATV gunner positions - mirrors are no longer rendered when you are on gunner seat which result in smoother CROWS PIP screen

^ Tweaked interior glass of MATV

^ Applied RHINO functionality to rest of MATVs

^ Tweaked MATV dashboard texture

^ Changed MATV inheritance - add couple more base classes

^ Added bounding box extender to MATV to ensure proper damage detection to RHINO

^ Added RHINO destruction particle effects

^ Added test BFT map to MATV

^ Tweaked wheels hitpoints on MATV & M1117

^ Adjusted map icons for MATV

^ Reduced Rhino durability

^ Tweaked M1025 driver animation - http://feedback.rhsmods.org/view.php?id=5480

^ Tweaked C130J copilot animation - http://feedback.rhsmods.org/view.php?id=5432

^ Increased HEAT & ATGM indirectHit range - http://feedback.rhsmods.org/view.php?id=5431

^ Tweaked MATV interior (unarmed variant for now)

^ Tweaked Javelin locking in top down mode

^ Added DVE & new dashboard textures to M1240 (basic variant only for now)

^ Tweaked DVE picture in picture screen ratio & added emissive material

^ Tweaked MATV wheel rvmats

^ Added separate TI rvmat for spare wheels for rest of MATV variants

^ Added few more details to MATV interior

^ MATV left mirror bounding box is moved away to the left when DVE is deployed so only one render source is used

^ Added DAGR GPS MFD to M1240 (basic variant only)

^ Added scripted solution for M1240 gear indicator

^ Splitted BFT function to separate file

^ Changed Co-Driver configuration on MATV - WARNING! It's now using turret, instead of regular seat meaning that missions with crew inside might need updating!

^ CROWS screens in MATVs are now emitting some actual light

^ New interior applied to all MATV variants

^ All MATV doors are animated with same speed now

^ Increased FFV rotation limits on MATV SOF variants (more freedom traded for visuals)

^ Tweaked M1126 (Mk19) inheritance

^ Added acceleration pedal animation to MATVs

^ Added various small dashboard indicators (lights, parking brake, service lights) to MATV

^ MATV co driver & Stryker Vehicle Commander can now use waypoint manager

^ Tweaked BFT brightness in direct light

^ Added data link to MATVs - they report now their position and get allies location on BFT

^ Tweaked BFT map rotation (reduced animPeriod to 0 - rotation should be smooth and instant)

^ Added handbrake to MATV

^ CH-53E user actions are now also available when using remote controlled unit

^ Tweaked sounds EH macros (simplified them)

^ Tweaked CH-47 floating time - http://feedback.rhsmods.org/view.php?id=5564

^ Zeroed Mk17 ironsights to M80 Ball - http://feedback.rhsmods.org/view.php?id=5564

^ Tweaked M113 Mk19 view gunner ammo box - http://feedback.rhsmods.org/view.php?id=5538

^ Added glass destruction to Cougars

^ Added RHINO functionality to M1230 & M1237 vehicles

^ Tweaked UH60M max landing speed

^ Tweaked M1025/M998 wheel hitpoints

^ Added cargo variants of CH-47F and C130J

^ Added new animation for M1134 gunner

^ Updated RHS loader to Old Man update

^ Added additional Stryker icons and updated CfgPatches

^ add cargo variant to CH-53

^ add CH-53 cargo classes to CfgPatches

^ Added new inventory icons for US backpacks

^ Tweaked load of Eagle backpack - http://feedback.rhsmods.org/view.php?id=5622

^ Added inertia to static M2 (test)

^ Added some basic handling of M1127 weapons

^ Enabled periscopes on M1134

^ Added animations for M1127 gunner

^ Tweaked gunner animations on M1127 (added IK)

^ Added PiP to LRAS3

^ Added KIA animations for new stryker poses

^ Added inertia to MATV OGPK mounted weapons

^ Added smoke launcher mem points for M1134

^ Tweaked locality of LOAL script - http://feedback.rhsmods.org/view.php?id=5635

^ Added animation for folding of marker dispenser to M1132

^ Improved camera movement on static weapons

^ Added new icon for Eagle III (Coyote) backpack

^ Added toolkit and mine detector to EOD Technicians

^ Added animated ironsights to M14

^ Added magazine proxies to M14

^ Added M80 ball magazines for M14

^ Added icons for M14 inventory accessories

^ Tweaked muzzle flashes on new M14 accessories

^ Standardized M14 fire geometry

^ Reconfigured muzzle attachments on M14 & M14 EBR

^ Tweaked PP Effects on G33

^ Reorganized some of the scopes within JR framework - moved i.e. M150 + PNVS variant to long rail variant only

^ Added custom recoil for M14

^ Tweaked dispersion across M14 family

^ Tweaks to inertia of some weapons

^ Added turret lock indicator to M1134

^ Added action to fold mast on M1134

^ Added action to M1132 to unfold Lane Marking System (not working yet)

^ Added some scripted reticle for LRAS3

^ Added turret hitpoints to M1134

^ Updated M14 textures + added Fiberglass variant

^ Added M14 ground holders and Virtual Ammo Box entries

^ Configured M1134 commander pintle weapon

^ Added basic MITAS MFD

^ Added damage textures to new Stryker variants

^ Added new desert Stryker variants to CfgPatches

^ Tweaked PIP acog scopes (removed rvmat from R2T - picture should bit brighter)

^ Updated crew proxies in Stryker fire geometry

^ Added basic MFD for Stryker LRAS3
{CHANGESIMPROVED}

## FIXED IN 0.5.1

@ HIMARS launcher hitpoint & firegeometry fixes - http://feedback.rhsmods.org/view.php?id=5364

@ Fixed missing MATV KIA animation

@ Fixed wrong ammo in Mk14 Mk316 magazine - http://feedback.rhsmods.org/view.php?id=5370

@ FMTV, MATV, Cougar, Caiman, HEMTT & Stryker were missing memory points for wheel trails decals - http://feedback.rhsmods.org/view.php?id=5374

@ Fixed M1A1 driver KIA animation - http://feedback.rhsmods.org/view.php?id=5377

@ Fixed glove clipping on G3 uniform

@ Added missing supply memory point to CH-53 - http://feedback.rhsmods.org/view.php?id=5402

@ Fixed missing supply memory point on few M977A4 variants - http://feedback.rhsmods.org/view.php?id=5481

@ Tweaked M1126 geometric occludders for passengers - http://feedback.rhsmods.org/view.php?id=5498

@ Updated MATV CfgPatches - http://feedback.rhsmods.org/view.php?id=5420

@ Fixed M397 bouncing mine functionality - http://feedback.rhsmods.org/view.php?id=5471

@ Removed 3UGL from M320 GL

@ Fixed some z fighting in Stryker cargo compartment

@ Fixed missing damage UI in Stryker

@ Fixed Stryker Vehicle Commander LOD in optics mode

@ Fixed some potentially inherited MFD values for UH1Y

@ Mk19 static weapon had wrong components in fire geometry

@ Fixed MATV glass hitpoints

@ Fixed M1245 was missing MFD memory points

@ Fixed FFV restrictions on one of the M1079 seats

@ Fixed DUKE system destruction on MATVs

@ Fixed 2nd missing UV set on MATV CROWS lenses + tweaked materials

@ Fixed MATV turret mirrors on M240 & Mk19 variant

@ DIRCM was affecting radar guided missiles - http://feedback.rhsmods.org/view.php?id=5502

@ AIM-9M on AH1Z is now using correct model of AIM9M

@ Fixed M1117 hull hitpoints - http://feedback.rhsmods.org/view.php?id=5511

@ Fixed red dot on G33 with T1 combo - http://feedback.rhsmods.org/view.php?id=5518

@ Fixed missing sections rpt errors for Stryker, HEMTT & FMTV

@ Fixed MATV gunner hatch was closed from passenger seat of M2 variant

@ First config of M1127 Turret

@ M1127 Shadow LOD fix, turret configging, model cfg editing fixes

@ Maybe fixed the DVE file with a PBO Prefix

@ Fixed M1240 spare wheel TI texture

@ MATV DVE monitor was shutting down when reversing due to BBoxes being to close to head

@ Co-driver of armed MATVs was missing BFT scale adjust action

@ Fixes a mem point on M1232 RG-33L 6X6

@ Possibly fixed M142 HIMARS config

@ M142 Mirror selection delete in Pilot LOD

@ Fixed missing icon on SU230A/PVS when 3D mode was used - http://feedback.rhsmods.org/view.php?id=5577

@ Fixed CH-53E fold action didn't synchronize fuel status correctly when folding or unpacking - http://feedback.rhsmods.org/view.php?id=5587

@ Fixed UV offset on some of the scopes - http://feedback.rhsmods.org/view.php?id=5556

@ Fixed rpt spam related to wheel reference

@ Fixed rpt spam related to duplicated DUKE weapons

@ Fixed missing OGPK mirrors points on RG33L & Caiman

@ Fixed bits of Cougars fire geometry

@ Fixed FMTV SOV .rpt errors

@ Fixed FMTV SOV had wrong turret attenuation

@ Fixed few rpt errors on RG33, Stryker & SOCOMAUV

@ Fixed .rpt error about "dimension should be array of 2" for static weapons

@ Fixed M1A1HC Olive texture after removing IFF panel - http://feedback.rhsmods.org/view.php?id=5594

@ Fixed some .rpt errors with FG

@ Fixed M109 assert connected to Commander memory points

@ Fixed duplicated weapons for M2A2 due to VG components

@ Fixed AIM9M error on AH1Z (magazine compatibility)

@ Fixed some wrong components on M1A2

@ Fixed UH60M was spawning above its land contact points

@ Fixed some .rpt errors related to CH53

@ Fixed: The M1134 Gunner now has the top hatch in Pilot LOD

@ M1127 LOD improvements

@ M1127 Adds Gunner Traverse Controller Stick

@ M1127 Interior texture improvements / LOD fixes

@ Added M1134 Fire geo

@ Interior texture fixes

@ Sight housing and assy now rotates with the TOW Missile Carrier

@ Adds M1127 Smoke Grenade Discharger Panel Mask

@ Up-sized the M1134 Mask to 2K

@ Slightly improved M1127 Smoke panel texture

@ Changed NOHQ to account for movement of the Azimuth indicator on the gunner's panel

@ Fixed HMG reload sounds

@ Fixed missing NVG shadow in view pilot

@ Fixed missing uvset on M8541 scopes

@ Added some missing memory points to RHS_M14_RAIL.p3d

@ Fixed one error related to turn out on Strykers

@ Fixed muzzle flashes on M1134 & M1127 weapons

@ Fixed rogue component in Fire Geo of m1a1hc.p3d

@ Fixed flashbang script not working when AFRF was not loaded - http://feedback.rhsmods.org/view.php?id=5651
{CHANGESFIXED}

## REMOVED IN 0.5.1

- Remove M1134 mask file and changes with mask_ca
{CHANGESREMOVED}

