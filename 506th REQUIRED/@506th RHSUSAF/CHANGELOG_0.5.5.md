# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.5.5

## ADDED IN 0.5.5

+ Vert grip attachment for M4/M16 rifles w/M203 UGL

+ Adds Q-Net Armor to M1240A1 and M1277 M-ATV variants

+ Adds M1165A1 armoured GMV with SAG-2 (M2, Mk19 and M134 with scondary M240) and rear M240 swing-mount turrets

+ Added Q-Nets to M1277 M-ATV CROWS variants

+ Adds the first iteration of the M1A2 SEP V2 MBT, equipped with M153 CROWS

+ NXS sniper scopes (Navy/Marines '5.5-22x56' 2nd Focal-Plane and Army '3.5-15x50 F1' 1st Focal-Plane models. Includes long boi models with sunshade. Mil-dot and H58 reticles for 3.5-15x50)

## IMPROVED IN 0.5.5

^ Tweaked M11xx armor value so AI is engaging it with small arms

^ Added SCAR magazines to ammo crate

^ Adjusted opticType on RHS accessories

^ Reduced recoil of GAU8 - http://feedback.rhsmods.org/view.php?id=5963

^ Tweaked GBU-12 flight params - attempt to fix http://feedback.rhsmods.org/view.php?id=5496

^ Added spalling to vanilla HEAT penetrators

^ Added ability to detach empty FGM-148 tube

^ Reduced FGM-148 penetration to some more realistic values

^ Added ability to tow M119 Howitzer

^ Minor tweak to 105mm M14B1 casing geometry

^ Optimized wheels in last LOD of FMTV models

^ M119 Roadway LOD is hidden when vehicle is towed

^ Added MP7 muzzle accessories to Joint Rails (asdg_MuzzleSlot_46 )

^ Added compatibility entries for BIS accessories

^ Adjusted displaynames for M249s with Lightweight Collapsible Buttstock Assembly

^ Added some roundness to top LOD of UH-60 fuel tanks

^ Made ballistic glasses & goggles inventory icons more consistent with rest of the content

^ Tweaked announcer - pull up message is no longer triggered when gear is down

^ Slight section count reduction in all M11XX HMMWVs

^ Tweaked Bradley HE tracers size - http://feedback.rhsmods.org/view.php?id=6023

^ Reduced height of MRZR ViV bounding box to its height when the rollcage is folded

^ Moved a vertex on ported C-130J model that caused some texture distortion on one side of the fuselage

^ Towing user actions are now only available to players

^ Added TOW ammo hitpoint to M1134, M996 & M1045 - http://feedback.rhsmods.org/view.php?id=6027

^ Tweaked what weapons are visible in Eden ammo crate

^ Tweaked visibility of folded weapons in VA - http://feedback.rhsmods.org/view.php?id=6037

^ Experimental change to C130J hitpoints

^ Reduced CH53E AFM contact points

^ Adjusted alignment of O-GPK turret shadow on M-ATVs

^ Added additional particle effects to C130J - engine refract & extra destruction particle effects

^ Tweaked roadway setup of C130J so it starts correctly even when placed in Zeus

^ Tweaked front M1 gun limits - http://feedback.rhsmods.org/view.php?id=5516

^ Move forward M249 by 5cm to prevent various optics clipping when weapon is deployed in prone stance - http://feedback.rhsmods.org/view.php?id=6033

^ Adjusted turn in animation of M1151 GPK turrets gunners - http://feedback.rhsmods.org/view.php?id=6034

^ Added LODs to AN-PRC-152 editor prop

^ Added version of AN/PRC-152 configured as a basic radio-slot inventory item

^ Adjusted tan colour of WMX flashlight (thanks to Eagle and warden)

^ Improved M1127 Textures with full re-bake

^ Added experimental function which removes engine fire particle effects after vehicle was repaired & engine was turned on

^ Reworked AFG attachment position on SOPMOD Block 2 rifles

^ Reworked AFG attachment position on M16A4 rifles

^ Reworked AFG attachment position on HK416/M27 rifles

^ Corrected `descriptionShort` text on several 6Rnd. magazines for the M32

^ Reduced spalling on HEDP rounds fired from Mk19 due to their high rate of fire and amount of bullets it can create

^ Animated M240 feed cover on M1151/M1165

^ Configured MELB GAU-19/A fire rates selectable between 1000 and 2000 rpm per manufacturer's specs, as opposed to fixed 1300rpm rate per GAU-19/B (may switch back to limited ROF if research reveals the gun should indeed be limited on MELB)

^ Regenerated CfgPatches & ground holders for place able items. Warning! Old editor weapons received scope = 1

^ Added or fixed short description on many accessories & weapons

^ Tweaked MP7 rate of fire - http://feedback.rhsmods.org/view.php?id=6124

^ Tweaked detach action on helicopters & C130J

^ Increased Mk19 grenades life time - http://feedback.rhsmods.org/view.php?id=6056

^ Changed M-ATV, M1151 etc. M240 gunner anim to fix broken neck

^ Adjusted get in points & actions on static weapons + prepared them for 2.04 update

^ Tweaked resolution LODs on vehicle mounted M240B

^ Fixed some door behaviour on uparmoured HMMWVs

^ Added visual smoke shells to Stryker family

^ Tweaked rear rotors hitpoints on CH-47 & 53 - http://feedback.rhsmods.org/view.php?id=6229

^ Unified DAGR & FFAR hit values - http://feedback.rhsmods.org/view.php?id=6125

^ Tweaked sync of BFT map on large maps in MP

^ Slightly increased AI dispersion of man operated M2 machine guns

^ Moved MRZR-4 to the regular "Cars" Eden subcategory

^ Added ability to fold MP7A2

^ M240 OGPK and MCTAGS turrets updated with H24 cradle mount

^ Replaced barrel on Mk19 external view proxy model, with the more detailed barrel from View Gunner LOD

^ Tweaked DUKE destruction function to work better with MATVs

^ Improved M153 CROWS texture

## FIXED IN 0.5.5

@ Fixed Lerca Tan icon error

@ Removed AI FCS laser magazines from Virtual Arsenal

@ Fixed camo1 selection in resolution LODS of rhs_spcs_rifleman.p3d & rhs_spcs_teamleader.p3d - http://feedback.rhsmods.org/view.php?id=5986

@ Fixed folding with safe mode turned on would result with one magazine missing - http://feedback.rhsmods.org/view.php?id=5886

@ Fixed issue when folding weapon could magically spawn new muzzle attachment - http://feedback.rhsmods.org/view.php?id=5991

@ American helicopters were missing correct rotor centre memory points - http://feedback.rhsmods.org/view.php?id=5999

@ Fixed gunner cue  on AH-64 pilot seat was not updating correctly - http://feedback.rhsmods.org/view.php?id=6001

@ Assigned proper materials to engine & fuel tank of Littlebird + added armorComponents to above mentioned hitpoints - http://feedback.rhsmods.org/view.php?id=5998

@ Corrected M1117 crew - http://feedback.rhsmods.org/view.php?id=5987

@ Fixed wrong inheritance of spotting scope

@ M11xx were missing black out lights configs and started with BO lights on

@ Fixed M1151 with LRAS3 was missing gunner get in memory points

@ Fixed M998 4D antenna hiding (this time for real)

@ Removed duplicated LWIRCM from MELB- http://feedback.rhsmods.org/view.php?id=6011

@ M240 was missing a section of it's gas-tube underneath the bipod

@ Fixed duplicated glass selection on M1240a1 with mk19

@ Removed basket options from CH-53E

@ Wheel hitpoints belonging to the second axle on several MRAPs, had steering animations

@ Mk19 M1240A1 had some duplicated glass panes that did not follow turret rotation

@ M1277 M-ATV w/ Mk19 CROWS windows were not tinted the same as the other non-SOCOM M-ATVs

@ M1 tanks were not able to load more than 8 rounds via loadout editor in some cases

@ Fixed scripted turrets not being locked properly in MP - http://feedback.rhsmods.org/view.php?id=5894

@ M1 loader gun had wrong compartment defined

@ Not all M113 scripted turrets were locked properly

@ Turned out vehicle commander of Stryker was invisible for people inside when he was using one of the mounted weapons

@ Fixed small typo in FROG rvmat

@ 6Rnd. M662 Red Flare only contained one round

@ US Army & USMC helicopters were using wrong author string - http://feedback.rhsmods.org/view.php?id=6138

@ Fixed small typo in A10A flight model config - http://feedback.rhsmods.org/view.php?id=6166

@ Fixed door gunner limits on UH-60 -http://feedback.rhsmods.org/view.php?id=6180

@ Fixed UH-1Y copilot legs

@ ACU geometry model components were not conventionally numbered

@ Replaced "&" with "+" on grip & bipods combos since inventory system is using structured text - this resulted & being treated as html code.

@ Fixed bipods reappearing when dismounting gripod - http://feedback.rhsmods.org/view.php?id=6218

@ Fixed spacing between components on M1 tanks which resulted in MG bullets going through rear armor - http://feedback.rhsmods.org/view.php?id=6087

@ Fixed IBAS FCS when M791 rounds are loaded - http://feedback.rhsmods.org/view.php?id=6230

@ MRZR-4 blackout light did not fully hide when turned off

@ Spent cases were not ejecting from the correct position on some vehicles with M240 turrets

@ M1151 Mk19 O-GPK ammo box was part of the Mk64 gun mount retexture selection in View Gunner LOD

@ Ammo boxes did not fully hide on roof of M1245 M-ATV

@ Removed obsolete hit part EH

@ Fixed ammo in editor M49 mine objects - http://feedback.rhsmods.org/view.php?id=6220
