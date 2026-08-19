
[5/9/2021 10:14:25 AM][0.5.6][R4486][reyhard]

^ Added experimental function to fix texture randomization on dedicated server

[5/9/2021 9:01:50 AM][0.5.6][R4485][reyhard]

^ Added some missing editor previews
^ Regenerated editor previews

[5/9/2021 8:29:06 AM][0.5.6][R4484][reyhard]

@ One of the addons was missing in load order list

[5/9/2021 8:28:17 AM][0.5.6][R4483][reyhard]

@ Removed obsolete accessory from weapon crate

[5/6/2021 6:41:19 PM][0.5.6][R4482][da12thMonkey]

SEPv2 M2 was not following CROWS

[5/6/2021 4:29:09 PM][0.5.6][R4481][reyhard]

^ Adjusted HEAT submunition initial speed to take into account air friction - http://feedback.rhsmods.org/view.php?id=6110

[5/5/2021 3:44:26 PM][0.5.6][R4480][reyhard]

@ Fixed SACLOS guidance was affected by gun FCS - http://feedback.rhsmods.org/view.php?id=5985

[5/4/2021 5:24:15 PM][0.5.6][R4479][da12thMonkey]

^ Improved damage/destruction visuals of M1A2SEPv2

[5/4/2021 4:53:18 PM][0.5.6][R4478][reyhard]

@ Fixed spawning of destroyed DUKE antennas when vehicle is completely destroyed - http://feedback.rhsmods.org/view.php?id=6330

[5/3/2021 4:00:11 PM][0.5.6][R4477][reyhard]

@ Fixed ghost LOD on Mk18 with M320

[5/3/2021 1:05:17 PM][0.5.6][R4476][da12thMonkey]

@ 40mm stun grenade ammo class required AFRF
^ Increased illumination capability of 40mm flares

[5/2/2021 11:02:03 AM][0.5.6][R4475][reyhard]

^ Reduced thermobaric wave effects & disabled pp effects

[5/2/2021 9:52:19 AM][0.5.6][R4474][da12thMonkey]

Change 105mm/155mm flare deployment to use artillery `aimAboveTarget[]` rather than `triggerDistance`

[5/1/2021 8:58:32 PM][0.5.6][R4473][da12thMonkey]

Commented out edPrev macro for longer M49A1 tripwire mines, to remove error popup in Eden

[5/1/2021 8:25:37 PM][0.5.6][R4472][da12thMonkey]

^ Improved 105mm and 155mm ILLUM rounds: Converted to use submunitions system, added realistic burn times for flares and increased their illumination capability

[5/1/2021 3:24:25 PM][0.5.6][R4471][da12thMonkey]



[5/1/2021 3:07:31 PM][0.5.6][R4470][da12thMonkey]

Tweaked flare PFX

[4/30/2021 9:57:28 PM][0.5.6][R4469][da12thMonkey]

@ M781 40mm Prac grenade was not sorted next to other RHS 40mm magazines in the Virtual Arsenal for weapons with an M320 UGL

[4/30/2021 8:56:42 PM][0.5.6][R4468][da12thMonkey]

+ 40mm Cluster Star (5x signal flare) magazines for M203/M320/M79 type single-shot, low-velocity grenade launchers. M585 white cluster, M663 green cluster, M664 red cluster

[4/30/2021 3:30:23 PM][0.5.6][R4467][da12thMonkey]

^ Tweaked ignition delay and burn time of 40mm flares to realistic values
^ Replaced `rhs_mag_M585_white` flare with `rhs_mag_M583A1_white` flare (M585 is a star cluster flare IRL). rhs_mag_M585_white class is now hidden but can still be loaded, though its displayname is also changed to M583
^ Adjusted green and red flare particles so that they don't look identical to white flares during daylight (green flares do still look quite white, as they do IRL)
^ Increased size and observable distance of M257 Hydra rocket's flare effect
^ Added `affectedByWind = 1;` property to US signal/illum flares (countermeasure flares unchanged)

- Removed macro-generated `Item_rhs_mag_M585_white` ground holder class (added in RHSUSF 0.5.5) for deprecated M585 magazine (legacy rhs_magazine_rhs_mag_M585_white still exists in hidden scope)

[4/30/2021 9:26:12 AM][0.5.6][R4466][da12thMonkey]

@ Fixed non-convex geometry component in GMV M134-carrier turret and regenerated components names for all GMVs

[4/28/2021 4:39:57 PM][0.5.6][R4465][reyhard]

^ Added supply points to various vehicles - http://feedback.rhsmods.org/view.php?id=6319
^ Tweaked CLU hiding logic - http://feedback.rhsmods.org/view.php?id=6313

[4/28/2021 4:08:18 PM][0.5.6][R4464][da12thMonkey]

@ Script error using Leica rangefinder when running RHSUSAF standalone

[4/28/2021 4:02:32 PM][0.5.6][R4463][reyhard]

@ Fixed error in towing system when memory point is used for determining of attach point

[4/25/2021 8:55:38 AM][0.5.6][R4462][da12thMonkey]

^ Slight adjustment to WMX200 flashlight scale

[4/23/2021 10:34:52 AM][0.5.5][R4461][da12thMonkey]

@ Fixed weapon holder path in macro

[4/20/2021 10:42:26 PM][0.5.5][R4460][jenkins]

[0.5.6] versions updated

[4/20/2021 2:24:15 AM][0.5.5][R4459][gurdy]

^ tweaked standard M153 texture
+ unique M153 texture for M1A2SEPv2

[4/17/2021 4:31:40 PM][0.5.5][R4458][reyhard]

@ Fixed ammo in editor M49 mine objects - http://feedback.rhsmods.org/view.php?id=6220

[4/15/2021 10:31:18 AM][0.5.5][R4457][da12thMonkey]

SEPv2 smdi tweak
Assigned wd texture to SEPv2 parts in .p3d, for easier inspection of materials compared to turret, hull etc

[4/15/2021 1:04:08 AM][0.5.5][R4456][gurdy]

^ quick tweaks to M153 diffuse, more improvements to come

[4/9/2021 3:18:57 PM][0.5.5][R4455][reyhard]

@ Removed obsolete hit part EH
reverted postInit changes

[4/4/2021 11:20:31 AM][0.5.5][R4454][reyhard]

^ Tweaked DUKE destruction function to work better with MATVs

[4/3/2021 9:14:25 PM][0.5.5][R4453][da12thMonkey]

@ Ammo boxes did not fully hide on roof of M1245 M-ATV

[4/2/2021 5:13:07 PM][0.5.5][R4452][da12thMonkey]

Added tow bar into appearance randomisation of M1240A1 and M1277 M-ATVs

[4/2/2021 11:51:30 AM][0.5.5][R4451][reyhard]

added new inventory icons

[4/2/2021 11:35:41 AM][0.5.5][R4450][reyhard]

^ Added VhC customization function to postInit

[3/31/2021 10:02:26 AM][0.5.5][R4449][da12thMonkey]

Removed DUKE countermeasure weapon from GMV

[3/30/2021 9:58:16 PM][0.5.5][R4448][da12thMonkey]

^ Replaced barrel on Mk19 external view proxy model, with the more detailed barrel from View Gunner LOD
@ M1151 Mk19 O-GPK ammo box was part of the Mk64 gun mount retexture selection in View Gunner LOD

Added M1165A1 GMV Mk19 carrier

[3/29/2021 2:06:05 PM][0.5.5][R4447][da12thMonkey]

Added tow bar to A1 series M-ATVs (removes RHINO when unhidden, rotates to accommodate Q-Net)
Made A1 front mirror stalks hide-able via vehicle customisation
Added A1-style front mirror stalks to SOCOM M1245 M-ATVs

[3/28/2021 7:02:22 PM][0.5.5][R4446][RichardsD]

@ Fixed Des M1165 Texture

[3/28/2021 5:40:14 PM][0.5.5][R4445][da12thMonkey]

Fixed usti mem points for swing-arm gun in GMV M134 turret 

[3/28/2021 12:24:09 PM][0.5.5][R4444][da12thMonkey]

Applied holsterScale to folded MP7
M134 shadow was missing a few details on GMV

[3/28/2021 12:16:54 PM][0.5.5][R4443][reyhard]

added missing MP7A2 icons

[3/27/2021 10:46:17 PM][0.5.5][R4442][da12thMonkey]

GMV M134 gunner anim
Changed empty casing particle on GMV's M134

[3/27/2021 4:42:37 PM][0.5.5][R4441][da12thMonkey]

@ Spent cases were not ejecting from the correct position on some vehicles with M240 turrets
Equipped M-ATV M240 carriers with H24 cradle mount

[3/27/2021 11:44:50 AM][0.5.5][R4440][da12thMonkey]

Work on GMV M134 minigun turret setup

[3/27/2021 2:02:29 AM][0.5.5][R4439][RichardsD]

+ M1165A1 GMV with M134D, currently weapon does not rotate, otherwise works fine

[3/27/2021 12:55:01 AM][0.5.5][R4438][da12thMonkey]

^ M240 OGPK and MCTAGS turrets updated with H24 cradle mount

Will hopefully update M-ATV OGPK over the weekend

[3/26/2021 9:37:34 PM][0.5.5][R4437][reyhard]

^ Added ability to fold MP7A2

[3/26/2021 8:42:33 PM][0.5.5][R4436][RichardsD]

@ Fixed small part of the M1165A1 GMV WD Texture

[3/26/2021 6:27:25 PM][0.5.5][R4435][RichardsD]

^ Improved M1165A1 GMV Textures WD and Des

[3/26/2021 8:06:13 AM][0.5.5][R4434][da12thMonkey]

Fixed my mistake with GMV textureSources class
GMV spare wheel texture did not change when retexturing other wheels
^ Moved MRZR-4 to the regular "Cars" Eden subcategory

[3/26/2021 2:34:44 AM][0.5.5][R4433][RichardsD]

^ Adds broken GMV WD textures 

[3/25/2021 8:57:49 AM][0.5.5][R4432][da12thMonkey]

Added proxy to fix CROWS M2 having no barrel and feed cover in view Cargo LOD

[3/24/2021 7:59:20 PM][0.5.5][R4431][da12thMonkey]

@ MRZR-4 blackout light did not fully hide when turned off

[3/24/2021 6:00:20 PM][0.5.5][R4430][reyhard]

^ Slightly increased AI dispersion of man operated M2 machine guns

[3/24/2021 5:46:46 PM][0.5.5][R4429][reyhard]

removed debug stuff

[3/24/2021 5:36:40 PM][0.5.5][R4428][reyhard]

^ Tweaked rear rotors hitpoints on CH-47 & 53 - http://feedback.rhsmods.org/view.php?id=6229
^ Unified DAGR & FFAR hit values - http://feedback.rhsmods.org/view.php?id=6125
^ Tweaked sync of BFT map on large maps in MP
@ Fixed IBAS FCS when M791 rounds are loaded - http://feedback.rhsmods.org/view.php?id=6230

[3/24/2021 11:57:20 AM][0.5.5][R4427][da12thMonkey]

Shadows for swing arm mounts
Re-added control bone for hiding trunk user action

[3/23/2021 11:42:56 PM][0.5.5][R4426][da12thMonkey]

Some parameters I forgot to change

[3/23/2021 9:15:46 PM][0.5.5][R4425][reyhard]

^ Added visual smoke shells to Stryker family 

[3/23/2021 9:05:57 PM][0.5.5][R4424][da12thMonkey]

Cargo slots for GMV right-hand running board
Limited FFV turret behaviour of running board slots
Regenerated Swing-arm+ammo box texture and material
General config tweaks
^ Fixed some door behaviour on uparmoured HMMWVs

[3/23/2021 5:27:39 PM][0.5.5][R4423][reyhard]

^ Tweaked resolution LODs on vehicle mounted M240B

[3/23/2021 2:18:15 PM][0.5.5][R4422][da12thMonkey]

Adjusted M1A2SEPv2 config tree to inherit des/wdl variants from a common base class
Updated edPrev images for all Abrams tanks

[3/23/2021 10:24:07 AM][0.5.5][R4421][da12thMonkey]

Fixed typo in mem point name

[3/23/2021 10:18:11 AM][0.5.5][R4420][da12thMonkey]

M1165 GMV:
Added swingarm mounts and ammoboxes with improved textures to top LOD and view LODs
Propagated swingarm bones through other LODs
Updated proxies in other LODs
Added cargo slots to left-side running boards (WIP) - locked when running boards are hidden

[3/22/2021 6:51:17 PM][0.5.5][R4419][reyhard]

@ Fixed spacing between components on M1 tanks which resulted in MG bullets going through rear armor - http://feedback.rhsmods.org/view.php?id=6087

[3/22/2021 6:31:32 PM][0.5.5][R4418][reyhard]

^ Adjusted get in points & actions on static weapons + prepared them for 2.04 update

[3/22/2021 5:04:17 PM][0.5.5][R4417][RichardsD]

+ New H24-6 Mount Textures

[3/22/2021 2:49:08 PM][0.5.5][R4416][da12thMonkey]

!CLEARTEMP!
Moved M1165 GMV data to rhsusf_m1165.pbo, slimmed down model.cfg etc.

[3/21/2021 9:36:04 PM][0.5.5][R4415][da12thMonkey]

^ Changed M-ATV, M1151 etc. M240 gunner anim to fix broken neck

[3/21/2021 11:14:27 AM][0.5.5][R4414][reyhard]

^ Tweaked detach action on helicopters & C130J
^ Increased Mk19 grenades life time - http://feedback.rhsmods.org/view.php?id=6056

[3/21/2021 10:46:04 AM][0.5.5][R4413][da12thMonkey]

Missing WEAPON_RPM macro

[3/21/2021 10:36:11 AM][0.5.5][R4412][reyhard]

^ Tweaked MP7 rate of fire - http://feedback.rhsmods.org/view.php?id=6124

[3/21/2021 10:29:53 AM][0.5.5][R4411][reyhard]

@ Replaced "&" with "+" on grip & bipods combos since inventory system is using structured text - this resulted & being treated as html code.
@ Fixed bipods reappearing when dismounting gripod - http://feedback.rhsmods.org/view.php?id=6218

[3/21/2021 12:21:31 AM][0.5.5][R4410][RichardsD]

^ Rebaked SAG-2 Turret for M1165A1 GMV

[3/20/2021 7:19:44 PM][0.5.5][R4409][reyhard]

small fixes to m1165 scripts
tweaked m1165 rear gunner legs

[3/20/2021 6:45:43 PM][0.5.5][R4408][reyhard]

added dummy structure for M1165

[3/20/2021 6:06:12 PM][0.5.5][R4407][reyhard]

fixing some pboproject dumb things

[3/20/2021 5:59:51 PM][0.5.5][R4406][reyhard]

^ Configured turrets on M1165A1 with M2

[3/19/2021 12:06:43 PM][0.5.5][R4405][reyhard]

removed mag from ground holder

[3/17/2021 12:09:11 PM][0.5.5][R4404][da12thMonkey]

@ ACU geometry model components were not conventionally numbered

[3/16/2021 10:06:00 PM][0.5.5][R4403][reyhard]

some work in progress stuff on m1165a1

[3/16/2021 9:59:52 PM][0.5.5][R4402][reyhard]

backup file

[3/15/2021 10:35:25 AM][0.5.5][R4401][reyhard]

added prefixes to Javelin skeleton

[3/14/2021 7:26:49 PM][0.5.5][R4400][reyhard]

scoped out muzzle flashes

[3/14/2021 7:21:26 PM][0.5.5][R4399][reyhard]

^ Regenerated CfgPatches & ground holders for place able items. Warning! Old editor weapons received scope = 1
^ Added or fixed short description on many accessories & weapons

[3/13/2021 1:45:02 PM][0.5.5][R4398][reyhard]

added shotgun subcategory

[3/12/2021 7:46:50 AM][0.5.5][R4397][reyhard]

added new experimental get out parameter for Mark V SOC turrets

[3/9/2021 10:26:57 PM][0.5.5][R4396][da12thMonkey]

Fixed some parts of NXS scope textures and smdi that were accidentally solid black

[3/5/2021 7:46:22 PM][0.5.5][R4395][da12thMonkey]

^ Configured MELB GAU-19/A fire rates selectable between 1000 and 2000 rpm per manufacturer's specs, as opposed to fixed 1300rpm rate per GAU-19/B (may switch back to limited ROF if research reveals the gun should indeed be limited on MELB)

[3/1/2021 7:10:10 PM][0.5.5][R4394][da12thMonkey]

Ironing out quirks of HK416 grip slot inheritance

[2/25/2021 6:18:19 PM][0.5.5][R4393][reyhard]

@ Fixed door gunner limits on UH-60 -http://feedback.rhsmods.org/view.php?id=6180
@ Fixed UH-1Y copilot legs

[2/24/2021 10:25:32 PM][0.5.5][R4392][da12thMonkey]

Made necessary transforms to GMV model to centre the bounding-box without making it oversized, and re-generated swing-arm animations
Applied transforms to all M11XX .p3ds for consistency (ingame bounding box/model centre is the same, only .p3d grid position has changed)

[2/24/2021 6:16:59 PM][0.5.5][R4391][da12thMonkey]

reverted some NXS scope test classes that were in the previous commit

[2/24/2021 6:04:33 PM][0.5.5][R4390][da12thMonkey]

^ Animated M240 feed cover on M1151/M1165

Test configuration for M1165A1 GMV rear swing-arm pintle. Heavy WIP:
Vehicle bounding box is currently rather funky - swing-arm keyframe-based animation needs centre of the vehicle to be at [0,0,0] but we cannot use `autoCenter 0`

[2/21/2021 8:05:09 PM][0.5.5][R4389][reyhard]

@ US Army & USMC helicopters were using wrong author string - http://feedback.rhsmods.org/view.php?id=6138

[2/21/2021 7:59:13 PM][0.5.5][R4388][reyhard]

@ Fixed small typo in A10A flight model config - http://feedback.rhsmods.org/view.php?id=6166

[2/17/2021 10:54:26 AM][0.5.5][R4387][da12thMonkey]

+ NXS sniper scopes (Navy/Marines '5.5-22x56' 2nd Focal-Plane and Army '3.5-15x50 F1' 1st Focal-Plane models. Includes long boi models with sunshade. Mil-dot and H58 reticles for 3.5-15x50)

[2/12/2021 9:31:21 PM][0.5.5][R4386][reyhard]

^ Added handling of locality changes to the towing script

[2/11/2021 9:44:29 PM][0.5.5][R4385][reyhard]

^ Reduced spalling on HEDP rounds fired from Mk19 due to their high rate of fire and amount of bullets it can create

[2/6/2021 7:51:21 PM][0.5.5][R4384][da12thMonkey]

@ 6Rnd. M662 Red Flare only contained one round
^ Corrected `descriptionShort` text on several 6Rnd. magazines for the M32

[2/6/2021 10:55:48 AM][0.5.5][R4383][da12thMonkey]

Sorted classes in jointRails.h to make it easier to find stuff
Defined compatibility for folded AK-103 w/ Zenitco handguard rail

[2/3/2021 10:01:56 PM][0.5.5][R4382][reyhard]

!CLEARTEMP!
repack no2

[2/3/2021 9:57:42 PM][0.5.5][R4381][reyhard]

!CLEARTEMP!
test pack

[1/19/2021 9:52:43 PM][0.5.5][R4380][da12thMonkey]

^ Reworked AFG attachment position on HK416/M27 rifles

[1/19/2021 3:00:56 PM][0.5.5][R4379][da12thMonkey]

^ Reworked AFG attachment position on M16A4 rifles

[1/18/2021 9:53:43 PM][0.5.5][R4378][da12thMonkey]

^ Reworked AFG attachment position on SOPMOD Block 2 rifles

[1/13/2021 7:34:00 PM][0.5.5][R4377][reyhard]

^ Added experimental function which removes engine fire particle effects after vehicle was repaired & engine was turned on
@ Fixed small typo in FROG rvmat
Ported towing related scripts to USAF so it remains independent from AFRF

[1/3/2021 3:38:27 AM][0.5.5][R4376][RichardsD]

^ Improved M1127 Textures with full re-bake

[12/31/2020 1:53:48 PM][0.5.5][R4375][da12thMonkey]

Fixed SEPv2 CROWS RSc inheritance
Defined RHS mags compatibility in the special CBA magwell for SCAR rifles fitted with EGLM (sake of third-party addons and future-proofing)

[12/30/2020 2:41:04 PM][0.5.5][R4374][da12thMonkey]

Removed textures that were applied to shadowLOD
added countermeasures to CROWS turret for testing/debugging while CITV is disabled

[12/30/2020 12:32:38 PM][0.5.5][R4373][da12thMonkey]

Fixed traverse indicator for SEPv2 commander's CROWS

[12/29/2020 11:49:58 PM][0.5.5][R4372][da12thMonkey]

M1A2SEPv2 now inherits animationSources from other Abrams (MILES panels hiding, smoke grenades etc. now functional)
Set up CROWS to be mostly functional. Currently replaces CITV as commander's turret for testing (Known issue: Traverse indicator in HUD shows rotation of main turret not the CROWS)

[12/29/2020 12:11:08 AM][0.5.5][R4371][RichardsD]

^ Improved bake errors on M1A2SEPv2

[12/23/2020 11:40:06 PM][0.5.5][R4370][da12thMonkey]

Fixed turret selection names in other SEPv2 LODs
Cleaned up `autocenter 0` properties that transferred over from Abrams proxy parts

[12/23/2020 9:25:07 PM][0.5.5][R4369][RichardsD]

^ Added rear light cover for camera on M1A2SEPv2

[12/23/2020 7:53:55 PM][0.5.5][R4368][RichardsD]

^ Re-aligned the spare road wheel and mount on M1A2SEPv2

[12/23/2020 7:02:06 PM][0.5.5][R4367][RichardsD]

^ Added spare road wheel to M1A2SEPv2, and fire geo for loader's ballistic shield

[12/23/2020 6:34:41 PM][0.5.5][R4366][RichardsD]

^ M1A2SEPv2 LODs 1-5 added, and Shadow LOD

[12/23/2020 2:35:45 AM][0.5.5][R4365][RichardsD]

^ Improved M1A2SEP v2 Cargo strap colour

[12/23/2020 1:05:22 AM][0.5.5][R4364][RichardsD]

^ Improved M1A2SEPv2 textures

[12/22/2020 9:27:06 PM][0.5.5][R4363][RichardsD]

^ Improved CO Textures for M1A2SEP v2
@ Fixed position of spare road wheel holder, road wheel to follow
^ Added CIP

[12/22/2020 8:47:18 PM][0.5.5][R4362][da12thMonkey]

SEPv2: resolved some animation issues due to otocvez/otocVez, otochlaven/otocHlaven selection naming conflict on different parts

[12/22/2020 7:25:28 PM][0.5.5][R4361][da12thMonkey]

Fixed incorrect M1A2SEPv2 hiddenSelectionsTextures path
Bumped up decal position indices for all Abrams variants to accommodate added M1A2SEPv2 camo selection

[12/22/2020 4:58:08 PM][0.5.5][R4360][RichardsD]

+ Adds the first iteration of the M1A2 SEP V2 MBT, armed with M153 CROWS. Current issues: Broken hidden selects, broken everything, CROWS non-functional. 

[12/10/2020 10:16:51 AM][0.5.5][R4359][da12thMonkey]

^ Adjusted tan colour of WMX flashlight (thanks to Eagle and warden)

[12/6/2020 2:44:30 PM][0.5.5][R4358][da12thMonkey]

^ Added LODs to AN-PRC-152 editor prop
^ Added version of AN/PRC-152 configured as a basic radio-slot inventory item

[12/1/2020 8:23:40 PM][0.5.5][R4357][reyhard]

@ Turned out vehicle commander of Stryker was invisible for people inside when he was using one of the mounted weapons 

[12/1/2020 8:14:57 PM][0.5.5][R4356][reyhard]

@ Fixed scripted turrets not being locked properly in MP - http://feedback.rhsmods.org/view.php?id=5894
@ M1 loader gun had wrong compartment defined
@ Not all M113 scripted turrets were locked properly 

[11/30/2020 7:43:02 PM][0.5.5][R4355][reyhard]

@ M1 tanks were not able to load more than 8 rounds via loadout editor in some cases 

[11/27/2020 10:29:18 PM][0.5.5][R4354][da12thMonkey]

@ M1277 M-ATV w/ Mk19 CROWS windows were not tinted the same as the other non-SOCOM M-ATVs

[11/26/2020 7:44:01 PM][0.5.5][R4353][da12thMonkey]

Corrected M249 SAW grip attachment handAnim relative to new M249 position

[11/26/2020 2:14:57 PM][0.5.5][R4352][da12thMonkey]

+ Added Q-Nets to M1277 M-ATV CROWS variants
@ Mk19 M1240A1 had some duplicated glass panes that did not follow turret rotation
Fixed some missing parts of the front mirrors on M1240A1 w/ M240 and Mk19
Updated edPrev images for all M-ATVs and added proper ones for M1240A1s

[11/26/2020 8:52:58 AM][0.5.5][R4351][da12thMonkey]

Added Q-Net to other M1240A1 O-GPK variants (still to add to M1277 CROWS variants)
Separated Glass and Door selections on M1240A1 variants (`isDiscrete = 0;` meant they only shrank to half size instead of disappearing when destroyed)
Randomised windscreen Q-Net hiding anim

[11/25/2020 8:23:23 PM][0.5.5][R4350][reyhard]

^ Adjusted turn in animation of M1151 GPK turrets gunners - http://feedback.rhsmods.org/view.php?id=6034

[11/25/2020 7:16:04 PM][0.5.5][R4349][reyhard]

^ Move forward M249 by 5cm to prevent various optics clipping when weapon is deployed in prone stance - http://feedback.rhsmods.org/view.php?id=6033

[11/25/2020 7:01:54 PM][0.5.5][R4348][da12thMonkey]

Remapped Q-Net with a tileable texture, providing higher texel density
Testing new Q-Net armour simulation type with far more extreme dissipation of HEAT penetrators (basic PG-7 HEAT rockets were still easily penetrating M-ATV behind slats)

[11/24/2020 8:04:01 PM][0.5.5][R4347][reyhard]

^ Tweaked front M1 gun limits - http://feedback.rhsmods.org/view.php?id=5516

[11/24/2020 7:51:45 PM][0.5.5][R4346][reyhard]

^ Tweaked QNET armor

[11/24/2020 7:50:40 PM][0.5.5][R4345][reyhard]

added bit of alpha to qnet texture to fix AO shimmering

[11/24/2020 7:14:01 PM][0.5.5][R4344][reyhard]

^ Added additional particle effects to C130J - engine refract & extra destruction particle effects
^ Tweaked roadway setup of C130J so it starts correctly even when placed in Zeus

[11/24/2020 1:16:24 PM][0.5.5][R4343][da12thMonkey]

@ Wheel hitpoints belonging to the second axle on several MRAPs, had steering animations

[11/24/2020 11:41:40 AM][0.5.5][R4342][da12thMonkey]

Fixed typo in GMV damage rvmat

[11/23/2020 11:00:32 PM][0.5.5][R4341][da12thMonkey]

^ Adjusted alignment of O-GPK turret shadow on M-ATVs

[11/23/2020 7:58:50 PM][0.5.5][R4340][reyhard]

^ Experimental change to C130J hitpoints
^ Reduced CH53E AFM contact points

[11/22/2020 4:57:40 PM][0.5.5][R4339][da12thMonkey]

Configured Q-Net hitpoints and destruction

[11/22/2020 11:38:19 AM][0.5.5][R4338][da12thMonkey]

Improved M-ATV Q-Net model.cfg (damage/destruction configuration still to do)

[11/22/2020 11:22:19 AM][0.5.5][R4337][reyhard]

^ Tweaked what weapons are visible in Eden ammo crate
^ Tweaked visibility of folded weapons in VA - http://feedback.rhsmods.org/view.php?id=6037

[11/21/2020 9:38:08 PM][0.5.5][R4336][reyhard]

^ Added inventory icons for new M203 accessories

[11/21/2020 9:13:43 PM][0.5.5][R4335][reyhard]

small turret hitpoint tweak

[11/21/2020 9:13:05 PM][0.5.5][R4334][reyhard]

^ Added TOW ammo hitpoint to M1134, M996 & M1045 - http://feedback.rhsmods.org/view.php?id=6027

[11/21/2020 10:18:29 AM][0.5.5][R4333][reyhard]

@ Removed basket options from CH-53E

[11/20/2020 5:14:26 PM][0.5.5][R4332][reyhard]

^ Towing user actions are now only available to players

[11/18/2020 9:18:56 PM][0.5.5][R4331][da12thMonkey]

^ Reduced height of MRZR ViV bounding box to its height when the rollcage is folded
^ Moved a vertex on ported C-130J model that caused some texture distortion on one side of the fuselage

[11/17/2020 4:32:53 PM][0.5.5][R4330][da12thMonkey]

Triangulated some quads that appeared in the SVLOD during previous tweaks

[11/17/2020 3:01:17 PM][0.5.5][R4329][da12thMonkey]

GMV fire geo

[11/16/2020 9:53:54 PM][0.5.5][R4328][da12thMonkey]

Small change to GMV Virtual Garage icon

[11/16/2020 9:30:10 PM][0.5.5][R4327][da12thMonkey]

GMV:
Set up mirrors in model
Fixed glass destruction on doors and SAG-II turret (fire geo still needs updating to reflect GMV and SAG-II shape)
Moved GMV to SOCOM faction
Made some changes to texture macro names and GMV classnames for consistency

[11/16/2020 5:43:50 PM][0.5.5][R4326][reyhard]

^ Tweaked Bradley HE tracers size - http://feedback.rhsmods.org/view.php?id=6023

[11/16/2020 3:45:23 PM][0.5.5][R4325][da12thMonkey]

GMV:
Added damage rvmat and zbtek selections for new parts
Added TI textures to .rvmats of new parts
Made the spare tyre hide when its holder is hidden
Removed `camo` selections from SVLOD
A couple of minor shadow LOD optimisations
Generated icon for Virtual Garage

[11/16/2020 3:28:02 AM][0.5.5][R4324][da12thMonkey]

^ Slight section count reduction in all M11XX HMMWVs

[11/16/2020 1:49:21 AM][0.5.5][R4323][da12thMonkey]

GMV:
Adjusted size of M240 proxy triangles to minimise height of bounding box
Moved position of antenna axis mem points to match visual model

[11/16/2020 1:35:13 AM][0.5.5][R4322][RichardsD]

@ Mudflap and axle fix for M1165A1 GMV

[11/16/2020 12:30:36 AM][0.5.5][R4321][RichardsD]

+ Adds first commit of the M1165A1 GMV with SAG-2 turret, armed with M2 and M240. Currently neither M240 works, and rear crew proxies do not work. 

[11/15/2020 9:20:59 AM][0.5.5][R4320][reyhard]

^ Tweaked announcer - pull up message is no longer triggered when gear is down

[11/15/2020 1:56:30 AM][0.5.5][R4319][RichardsD]

+ Adds M1165A1 GMV string table entries

[11/14/2020 12:02:15 PM][0.5.5][R4318][da12thMonkey]

Dispenser for sikrits

[11/14/2020 10:07:43 AM][0.5.5][R4317][reyhard]

sikrit change

[11/14/2020 8:44:21 AM][0.5.5][R4316][reyhard]

@ Fixed duplicated glass selection on M1240a1 with mk19

[11/12/2020 8:59:58 PM][0.5.5][R4315][reyhard]

^ Made ballistic glasses & goggles inventory icons more consistent with rest of the content

[11/10/2020 6:33:00 PM][0.5.5][R4314][da12thMonkey]

@ M240 was missing a section of it's gas-tube underneath the bipod

[11/9/2020 7:28:54 PM][0.5.5][R4313][reyhard]

@ Fixed M998 4D antenna hiding (this time for real)
@ Removed duplicated LWIRCM from MELB- http://feedback.rhsmods.org/view.php?id=6011

[11/8/2020 1:09:09 PM][0.5.5][R4312][da12thMonkey]

M-ATV A1:
Adjusted Q-Net alpha sorting order and reduced section count
Simplified hiding of door-mounted mirrors when Q-net is unhidden
Work on getting the door sections of the Q-net to animate, but still need to figure out the best way to rig the flexible sections before and aft of doors

[11/7/2020 6:41:33 PM][0.5.5][R4311][RichardsD]

+ Adds Q-Net Armor to M120A1 (M2) only as test. Still needs selections to be paired, as they are all individual. The normal M1240A1 mirrors are also hidden by default which will need to change, and likely the named selection can be removed. Also needs to have proper alpha sorting for interior, and be animated to the doors. 

[11/7/2020 2:17:48 PM][0.5.5][R4310][da12thMonkey]

^ Added some roundness to top LOD of UH-60 fuel tanks

[11/7/2020 12:19:34 PM][0.5.5][R4309][reyhard]

@ Fixed M1151 with LRAS3 was missing gunner get in memory points

[11/7/2020 12:02:31 PM][0.5.5][R4308][reyhard]

@ M11xx were missing black out lights configs and started with BO lights on

[11/7/2020 11:24:57 AM][0.5.5][R4307][reyhard]

@ Fixed wrong inheritance of spotting scope

[11/6/2020 9:52:08 PM][0.5.5][R4306][da12thMonkey]

^ Adjusted displaynames for M249s with Lightweight Collapsible Buttstock Assembly

[11/6/2020 2:13:08 PM][0.5.5][R4305][reyhard]

^ Added MP7 muzzle accessories to Joint Rails (asdg_MuzzleSlot_46 )
^ Added compatibility entries for BIS accessories

[11/4/2020 8:24:51 PM][0.5.5][R4304][reyhard]

@ Corrected M1117 crew - http://feedback.rhsmods.org/view.php?id=5987

[11/4/2020 8:14:09 PM][0.5.5][R4303][reyhard]

@ Assigned proper materials to engine & fuel tank of Littlebird + added armorComponents to above mentioned hitpoints - http://feedback.rhsmods.org/view.php?id=5998

[11/4/2020 7:32:08 PM][0.5.5][R4302][reyhard]

^ M119 Roadway LOD is hidden when vehicle is towed
ported code

[11/4/2020 4:46:13 PM][0.5.5][R4301][reyhard]

@ Fixed gunner cue  on AH-64 pilot seat was not updating correctly - http://feedback.rhsmods.org/view.php?id=6001 

[11/3/2020 5:46:44 PM][0.5.5][R4300][reyhard]

small typo fixerito

[11/3/2020 5:45:29 PM][0.5.5][R4299][reyhard]

@ American helicopters were missing correct rotor centre memory points - http://feedback.rhsmods.org/view.php?id=5999

[11/2/2020 10:43:24 PM][0.5.5][R4298][da12thMonkey]

Configured towing for Caimans, M11XX HMMWVs and M1117 ASV

[11/2/2020 8:53:47 PM][0.5.5][R4297][da12thMonkey]

Configured towing on all RG33 variants

[11/2/2020 8:48:18 PM][0.5.5][R4296][reyhard]

@ Fixed issue when folding weapon could magically spawn new muzzle attachment - http://feedback.rhsmods.org/view.php?id=5991




[11/2/2020 8:11:29 PM][0.5.5][R4295][da12thMonkey]

^ Optimized wheels in last LOD of FMTV models

[11/2/2020 6:54:12 PM][0.5.5][R4294][da12thMonkey]

Tweaked towing position for individual (non-M11XX) HMMWV variants
Added towing position to M-ATV and FMTV

[11/1/2020 3:25:28 PM][0.5.5][R4293][da12thMonkey]

Added M203 grips with a splash of woodland and desert paint
Reverted some opticsType values that I managed to cock up with the previous commit, back to the values set by reyhard

[11/1/2020 12:53:39 PM][0.5.5][R4292][da12thMonkey]

Tweaked M203grip specular power
Scaled down tex/mat to a more appropriate texel-density

[11/1/2020 11:22:30 AM][0.5.5][R4291][reyhard]

^ Added ability to tow M119 Howitzer (Warning: since whole system is still WIP, M119 is relaying on AFRF scripts - dependency will be solved later)
^ Added towing ability to M1025/M998
^ Minor tweak to 105mm M14B1 casing geometry

[11/1/2020 9:09:46 AM][0.5.5][R4290][reyhard]

^ Added spalling to vanilla HEAT penetrators
^ Added ability to detach empty FGM-148 tube
^ Reduced FGM-148 penetration to some more realistic values

[11/1/2020 12:28:56 AM][0.5.5][R4289][da12thMonkey]

+ Vert grip attachment for M4/M16 rifles w/M203 UGL

[10/31/2020 11:46:06 AM][0.5.5][R4288][reyhard]

^ Tweaked GBU-12 flight params - attempt to fix http://feedback.rhsmods.org/view.php?id=5496
@ Fixed folding with safe mode turned on would result with one magazine missing - http://feedback.rhsmods.org/view.php?id=5886

[10/31/2020 9:04:52 AM][0.5.5][R4287][reyhard]

^ Reduced recoil of GAU8 - http://feedback.rhsmods.org/view.php?id=5963

[10/31/2020 6:17:55 AM][0.5.5][R4286][reyhard]

@ Fixed camo1 selection in resolution LODS of rhs_spcs_rifleman.p3d & rhs_spcs_teamleader.p3d - http://feedback.rhsmods.org/view.php?id=5986

[10/29/2020 7:37:26 PM][0.5.5][R4285][reyhard]

^ Adjusted opticType on RHS accessories 

[10/28/2020 5:49:42 PM][0.5.5][R4284][reyhard]

^ Added SCAR magazines to ammo crate
@ Removed AI FCS laser magazines from Virtual Arsenal

[10/27/2020 4:53:46 PM][0.5.5][R4283][reyhard]

@ Fixed Lerca Tan icon error
^ Tweaked M11xx armor value so AI is engaging it with small arms

[10/26/2020 9:15:20 PM][0.5.4][R4282][jenkins]

[0.5.5] versions updated

[10/26/2020 8:20:41 PM][0.5.4][R4281][da12thMonkey]

^ Adjusted M995 AP caliber (penetration) value following initSpeed correction

[10/26/2020 7:48:29 PM][0.5.4][R4280][reyhard]

@ Fixed M113 with Mk19 missing turret selection - http://feedback.rhsmods.org/view.php?id=5967

[10/26/2020 7:15:55 PM][0.5.4][R4279][da12thMonkey]

@ Some M855 ball and M995 AP mags inherited M855A1 initSpeed

[10/24/2020 3:23:57 PM][0.5.4][R4278][reyhard]

@ Fixed M18 Yellow Smoke grenade translation - http://feedback.rhsmods.org/view.php?id=3541

[10/21/2020 6:22:48 PM][0.5.4][R4277][reyhard]

@ Unified engine damage configuration between M11xx & M1025

[10/21/2020 5:17:48 PM][0.5.4][R4276][reyhard]

fixed DVE transformation direction

[10/20/2020 6:05:14 PM][0.5.4][R4275][reyhard]

^ Added new DVE screen to rest of Stryker variants

[10/20/2020 5:59:20 AM][0.5.4][R4274][reyhard]

@ Fix missing para folded icons which I forgot to commit - http://feedback.rhsmods.org/view.php?id=5950

[10/19/2020 6:52:26 PM][0.5.4][R4273][da12thMonkey]

@ M1127 Stryker RV missing mirror material in external LOD

[10/19/2020 5:36:58 PM][0.5.4][R4272][reyhard]

^ Adjusted to high max fording depth on non USMC M11xx, M998 & M1025 series vehicles
^ Tweaked max wheels turning angle
^ USMC M11xx vehicles are using proper exhaust points

[10/18/2020 6:10:39 PM][0.5.4][R4271][reyhard]

added m14 with optics ai variant

[10/18/2020 9:51:03 AM][0.5.4][R4270][reyhard]

@ Fixed glass selections in fire geometry of M1151 with MCTAGS turret & added missing weapon proxy in FG - http://feedback.rhsmods.org/view.php?id=5941

[10/18/2020 8:04:20 AM][0.5.4][R4269][reyhard]

@ Updated USAF load order & preload list to prevent some of the addons missing from Zeus on dedicated server + fix  dependencies of 3rd addons which relay on USAF loadorder addon

[10/17/2020 9:22:27 PM][0.5.4][R4268][reyhard]

@ Fixed missing picture error for M24 & Leopold binoculars

[10/17/2020 3:20:28 PM][0.5.4][R4267][reyhard]

@ Fixed afterburner script exit condition

[10/17/2020 2:28:23 PM][0.5.4][R4266][reyhard]

@ Fixed flying of SACLOS missiles over line of sight 
@ Some of the M1 groups were still using old names

[10/16/2020 6:09:51 PM][0.5.4][R4265][reyhard]

^ Made antenna animations on M11xx series bit more smooth
^ Added camo variants of M8541 with high mount

[10/14/2020 9:35:55 PM][0.5.3][R4264][jenkins]

[0.5.4] versions updated

[10/14/2020 6:54:11 PM][0.5.3][R4263][reyhard]

added dumb workaround for some broken VG mechanic (note to myself - replace configClasses with configProperties in fn_initVehicle.sqf)

[10/14/2020 6:39:08 PM][0.5.3][R4262][reyhard]

fixed smoke launcher VG action

[10/14/2020 5:46:53 PM][0.5.3][R4261][reyhard]

added smoke grenades to m1151 LVOSS

[10/13/2020 4:04:25 PM][0.5.3][R4260][reyhard]

added VG texture definitions for LRAS3

[10/13/2020 3:47:41 PM][0.5.3][R4259][reyhard]

@ Fixed rhsusf_M1085A1P2_B_D_Medical_fmtv_usarmy deploy action -  http://feedback.rhsmods.org/view.php?id=5930

[10/13/2020 3:43:18 PM][0.5.3][R4258][reyhard]

^ Added flag proxy to Strykers
attempt to fix some edge case on m113 turn out EH
Stryker:
* saved _ca texture as _co and then renamed it to trigger different compression method
* added all new accessories to zbytek selection
* removed render flags from accessories
* reduced number of points in fire geometry since there is apparently limit of 3500 points
* fixed some debug.log errors about wrong move

[10/13/2020 7:44:51 AM][0.5.3][R4257][reyhard]

fixed M10xx pilot LOD was still missing one selection

[10/13/2020 3:19:45 AM][0.5.3][R4256][RichardsD]

@ Fixed M7 LVOSS with new geo and textures
^ Adds hidden selection to the M1151 LRAS3 that doesn't work..

[10/12/2020 6:17:46 PM][0.5.3][R4255][reyhard]

^ Tweaked VG options configuration on M1097 - http://feedback.rhsmods.org/view.php?id=5923

[10/12/2020 6:01:29 PM][0.5.3][R4254][reyhard]

added some placeholder icon for m11xx

[10/12/2020 5:52:06 PM][0.5.3][R4253][reyhard]

added some placeholder icon for m11xx

[10/12/2020 5:20:56 PM][0.5.3][R4252][reyhard]

M11xx:
* Configured LVOSS on variant with LRAS3
* Made some dirty fixerito to smoke launchers
* Added mud flaps animations

[10/12/2020 3:35:36 PM][0.5.3][R4251][reyhard]

@ Fixed ballistic glasses strings - http://feedback.rhsmods.org/view.php?id=5921

[10/11/2020 8:27:30 AM][0.5.3][R4250][reyhard]

@ Some of the single shot rockets had mass assigned
disabled some of the m113 VG actions (might still to reenable some of them - need to check how models are prepared right now)

[10/11/2020 7:35:22 AM][0.5.3][R4249][reyhard]

removed duplicated property

[10/10/2020 12:09:15 PM][0.5.3][R4248][reyhard]

^ Added action to raise & lower TOW tripod in Eden editor via attribute
@ FFV751 was missing tandem HEAT warhead property - http://feedback.rhsmods.org/view.php?id=5915
updated inventory icons

[10/8/2020 3:52:03 PM][0.5.3][R4247][da12thMonkey]

M-ATV boomerang fire geo and more detailed shadow. Added to view LOD for the rear-deck gunners
Added Stryker accessories to view LODs (have checked alpha sorting through driver's periscope but do check again for me)

[10/8/2020 9:37:37 AM][0.5.3][R4246][da12thMonkey]

Section merge after addition of boomerang mast

[10/8/2020 5:45:09 AM][0.5.3][R4245][ballistic09]

Added basic Air Force Security Force rifleman and moved M1165 ASV to Air Force faction

[10/8/2020 1:26:37 AM][0.5.3][R4244][RichardsD]

^ Fixed textures for boomerang on M1245

[10/8/2020 12:47:37 AM][0.5.3][R4243][RichardsD]

+ adds the shot finder (boomerang) made by Foxone to the M1245 M2 and Mk19

[10/7/2020 11:24:13 PM][0.5.3][R4242][da12thMonkey]

Added accessory kits to other Stryker variants

[10/7/2020 11:19:54 AM][0.5.3][R4241][da12thMonkey]

@ HEMTT ammo carrier with APK+M2 only had single memory point in its damper axis (broken suspension travel and gunner IK)

[10/7/2020 2:02:11 AM][0.5.3][R4240][da12thMonkey]

Fixed gunner stance IK not working on Mk19 RG-33Ls

[10/6/2020 8:47:24 PM][0.5.3][R4239][da12thMonkey]

Added trunk actions that were missing from the M1151 PKM-carrier

[10/6/2020 8:17:42 PM][0.5.3][R4238][da12thMonkey]

Made the trunk openable on M1151s

[10/6/2020 2:38:43 PM][0.5.3][R4237][reyhard]

Tweaked M1151 suspension config

[10/6/2020 11:09:17 AM][0.5.3][R4236][da12thMonkey]

Fixed rear M11XX doors opening much more slowly than front ones

[10/6/2020 11:04:05 AM][0.5.3][R4235][da12thMonkey]

M11XX:
added doplnovani memory points
sharpened some components of turrets in last LODs to improve shading
replaced wheels in last LODs with simplified mesh

[10/5/2020 8:51:39 PM][0.5.3][R4234][da12thMonkey]

M11XX:
Added improved physX LOD to other models
Fixed gunner not following turret on Mk19 weapon carriers
Fixed gunner stance IK on M2 MCTAGS turret (missing 'gunner' selection)

[10/5/2020 8:00:18 PM][0.5.3][R4233][reyhard]

optimized gunner adjust action & added AI event handlers

[10/5/2020 5:54:28 PM][0.5.3][R4232][reyhard]

@ Fixed missing muzzle flashes on M1XX & MATVs
@ Fixed M11xx PKM gunner view & gunner animations

[10/5/2020 4:38:45 PM][0.5.3][R4231][da12thMonkey]

M11XX:
Revamped tyre textures
Cleaned up some shading errors in lower resLODs
Applied reyhard's suspension and geoLOD mass tweaks across all other models
Applied interior decal fixes across all models

[10/5/2020 10:34:21 AM][0.5.3][R4230][reyhard]

^ Added M1 TUSK cannon M2 to Fire Geometry

[10/5/2020 9:41:33 AM][0.5.3][R4229][reyhard]

^ Added weapon proxy to Fire Geometry of FMTV, Caiman, Cougar, M1127 & RG33L
^ Added turret adjustment option to gunner of various pintle mounted weapons - use "Adjust up/down" action (default Ctrl+W/S) to lower or expose your character more (WIP)
^ Added suspension animation to M1151
^ Tweaked geometry PhysX & centre of mass of M1151
@ Fixed AI spawning on new Loader MG turrets 
@ Fixed order of turrets on M1A2 TUSK I

[10/5/2020 9:29:49 AM][0.5.3][R4228][reyhard]

@ Fixed M107 ghost LOD  - http://feedback.rhsmods.org/view.php?id=5906

[10/3/2020 12:36:05 PM][0.5.3][R4227][reyhard]

^ Added inertia to weapons mounted on M1 Tanks
^ Added separate turret for M1 Loader - player may now use FFV & M240 separately. Loader now can also use visor mounted on top of his hatch & this setup prevents bug with TI zoom on M1A2 Loader gun. 
^ Added KIA anims for new M113 commander moveset
^ Renamed M1A1SA to M1A1AIM, since models are actually representing AIM variants


[10/2/2020 5:58:03 PM][0.5.3][R4226][da12thMonkey]

Added flag proxies to unarmed and GPK armoured HMMWVs

[10/2/2020 1:42:35 PM][0.5.3][R4225][da12thMonkey]

Configured the front mirrors on A1/UIK M-ATVs with PiP in view Pilot LOD
Fixed camo9 selection overlapping the mirror surface in all LODs

[10/1/2020 10:58:46 PM][0.5.3][R4224][RichardsD]

@ Rebaked M1240A1 / M1277 textures to fix a a few errors

[9/30/2020 9:48:09 AM][0.5.3][R4223][da12thMonkey]

M1277 section count reduction for A1 parts

[9/30/2020 2:06:18 AM][0.5.3][R4222][RichardsD]

+ Adds M1277 with A1 kit (name change from M1240 CROWS, model and clsss names remain the same)
@ Fixed alpha order for windows on all A1 MATVs

[9/29/2020 11:48:57 PM][0.5.3][R4221][RichardsD]

@ Changes the M1240 CROWS to M1277

[9/28/2020 12:50:03 PM][0.5.3][R4220][da12thMonkey]

A bit of section count and config cleanup following addition of A1 M-ATVs

[9/28/2020 1:11:00 AM][0.5.3][R4219][RichardsD]

+ Adds M1240A1 with Underbody Improvement Kit (UIK), in M2, M240, and Mk 19 variants. Q-Net armor and additional tow bar accessory to follow. 

[9/27/2020 3:49:12 PM][0.5.3][R4218][RichardsD]

+ M1240A1 String Table entries

[9/23/2020 7:57:56 PM][0.5.3][R4217][da12thMonkey]

Propagating new fireGeo setup in other M11XX models

[9/18/2020 5:54:23 PM][0.5.3][R4216][da12thMonkey]

Test Fire Geometry and hitpoints adjustment. (Only on the unarmed M1151/M1165 for now)

[9/11/2020 12:43:14 PM][0.5.3][R4215][da12thMonkey]

Configured editor-placeable Scepter jerry can props (rhsusf_c_props.pbo)
Added geoLod properties to jerry cans (remove properties if copy-pasting the models to a vehicle!)

[9/10/2020 11:20:37 PM][0.5.3][R4214][da12thMonkey]

@ M240G had some overlapping camo selections
Scepter jerry can .p3d with LODs (will configure editor prop objects) later

[9/7/2020 1:06:09 PM][0.5.3][R4213][da12thMonkey]

@ AH-1Z's cannon ammunition incorrectly labeled as SAPHEI-T (tracer ammo) rather than SAPHEI

[9/2/2020 7:47:46 PM][0.5.3][R4212][da12thMonkey]

Updated M-ATV edPrev images

[9/2/2020 7:30:19 PM][0.5.3][R4211][reyhard]

^ Added weapon inertia to mounted M2 on FMTV & HEMTT

[9/2/2020 5:48:44 PM][0.5.3][R4210][reyhard]

^ Vastly improved M113 M2 gunner front windshield fire geometry 
^ Added few more customization options to M113 (WIP)
^ Added separate commander turret to M113 - it's now possible to turn in & use FFV
^ Tweaked M113 shadow LOD around commander hatch
^ Added inertia to M113 weapons
changed textures in muzzle flashes from paa to tga

[8/31/2020 2:00:31 PM][0.5.3][R4209][da12thMonkey]

^ Laser/Light attachments can be fitted to forward scout rail on 'SOCOM 16 (Rail)' (bear in mind lasers/lights will clip some long scopes models that fit on the optic rail, and obstructs ironsights)

[8/31/2020 12:31:46 AM][0.5.3][R4208][RichardsD]

@ Fixed MATV Ext and Interior textures

[8/29/2020 5:48:18 PM][0.5.3][R4207][RichardsD]

^ Added straps to Stryker Jerry cans on M1126 M2 only

[8/29/2020 12:08:52 PM][0.5.3][R4206][reyhard]

another tweak to SACLOS beam ridding

[8/28/2020 5:25:16 AM][0.5.3][R4205][reyhard]

@ Fixed Mk17 LB transformed into wrong variant when folded - http://feedback.rhsmods.org/view.php?id=5855

[8/25/2020 8:29:38 PM][0.5.3][R4204][da12thMonkey]

@ Underwing fuel-tanks were visible in C-130J shadow in spite of being removed from visual LODs
^ Minor improvements to C-130J propeller shadows

[8/25/2020 10:45:30 AM][0.5.3][R4203][da12thMonkey]

@ Fixed inaccurate displayName for some Flare/Chaff magazines

[8/24/2020 10:31:50 AM][0.5.3][R4202][reyhard]

m1025 tow damage fix

[8/24/2020 7:28:19 AM][0.5.3][R4201][reyhard]

^ Tweaked M1025/M998 damage selections once again

[8/23/2020 12:52:22 PM][0.5.3][R4200][reyhard]

^ Tweaked beam ridding behaviour

[8/23/2020 11:21:59 AM][0.5.3][R4199][da12thMonkey]

typo

[8/23/2020 11:07:19 AM][0.5.3][R4198][da12thMonkey]

^ CBA JAM magazineWells for more weapons

[8/23/2020 6:34:58 AM][0.5.3][R4197][reyhard]

^ Added facewear proxy to ACU first person LOD

[8/22/2020 7:36:37 PM][0.5.3][R4196][da12thMonkey]

Fix MRZR bad model.cfg inheritance issue when packing with current tools

[8/22/2020 2:58:24 PM][0.5.3][R4195][RichardsD]

@ Fixed MATV Ext textures

[8/22/2020 2:14:43 PM][0.5.3][R4194][RichardsD]

@ Fixed the MATV SOF rear WD Texture

[8/22/2020 3:49:28 AM][0.5.3][R4193][RichardsD]

@ Fixed rear MATV SOF textures

[8/21/2020 2:01:06 PM][0.5.3][R4192][reyhard]

fixed stryker shadows

[8/20/2020 12:04:38 PM][0.5.3][R4191][da12thMonkey]

@ M-ATV Mk.19 CROWS had the wrong "camo" retexture selection in distant LODs
Mk.19 feed chute was not part of CROWS texture selection on all turrets

[8/20/2020 12:52:37 AM][0.5.3][R4190][gurdy]

^ Added hull adshq as test

[8/20/2020 12:36:37 AM][0.5.3][R4189][RichardsD]



[8/19/2020 1:04:50 PM][0.5.3][R4188][da12thMonkey]

!CLEARTEMP!
Removed .bisurf references from M-ATV .rvmats
Updated damage .rvmats to the same standard
Applied procedural TI texture to parts that don't have a TI map

[8/19/2020 3:24:48 AM][0.5.3][R4187][RichardsD]

^ Improved textures on MATV MRAP

[8/18/2020 4:00:19 PM][0.5.3][R4186][da12thMonkey]

Some shadow LOD tweaks

[8/18/2020 8:20:03 AM][0.5.3][R4185][reyhard]

@ Fixed UH1Y door hiding Virtual Garage action - http://feedback.rhsmods.org/view.php?id=5830
^ Few more UH1Y variants will be now visible in VG

[8/17/2020 5:31:25 PM][0.5.3][R4184][da12thMonkey]

Updated M2 gunner anim for M1151 LRAS turret

[8/17/2020 2:54:26 PM][0.5.3][R4183][da12thMonkey]

New MCTAGS gunner anim
Positioned MCTAGS M1151/Cougar/RG-33L Mk19 gunner proxy to fit new anim

[8/17/2020 1:38:32 PM][0.5.3][R4182][da12thMonkey]

Adjusted alignment of M11XX wheel/steering memory points

[8/16/2020 8:02:02 PM][0.5.3][R4181][gurdy]

^ improved stryker hull ao and improved wheel textures

[8/16/2020 7:55:52 PM][0.5.3][R4180][da12thMonkey]

M1151 proxy positioning

[8/16/2020 3:28:46 PM][0.5.3][R4179][da12thMonkey]

RG33L proxy positioning

[8/16/2020 12:35:15 PM][0.5.3][R4178][da12thMonkey]

Caiman proxy positioning
Moved M-ATV and FMTV M2 gunners forward by half and inch

[8/16/2020 9:24:24 AM][0.5.3][R4177][da12thMonkey]

Put flag in other ACU LODs

[8/15/2020 9:17:26 PM][0.5.3][R4176][RichardsD]

^ Added US Flag to ACU in several versions


[8/15/2020 4:11:23 PM][0.5.3][R4175][da12thMonkey]

MATV proxy positioning

[8/15/2020 2:12:58 PM][0.5.3][R4174][da12thMonkey]

Initial work to unify vehicle M2/Mk19 gunner+weapon proxy positions across LODs:
M1025/M1043 HMMWVs
FMTVs
HEMTTs
Cougars

Rescaled M2 first LOD to correct and consistent size
New HMMWV gunner .rtm to fit around scaled-up M2

Other vehicles using these proxies/anims will inevitably have misalignment until changes are applied

[8/13/2020 11:22:55 PM][0.5.3][R4173][ballistic09]

^ Tweaked some speed, penetration, and/or damage values for a few 7.62x51 and 5.56x45 rounds
Re-enabled A2 parts for A2 HMMWVs that got borked after recent animationSources changes

[8/13/2020 8:58:43 PM][0.5.3][R4172][reyhard]

doh

[8/13/2020 8:39:36 PM][0.5.3][R4171][reyhard]

^ Added weapon inertia to Caiman & Cougar
@ Fixed shadows on Cougar turrets
@ Fixed glass pieces on Cougar Mk19 turret

[8/13/2020 8:29:36 AM][0.5.3][R4170][da12thMonkey]

M11XX section merging

[8/13/2020 7:26:09 AM][0.5.3][R4169][reyhard]

readjusted chassis proxy LODs & reextracted chassis proxy 
added missing semicolon

[8/13/2020 4:23:27 AM][0.5.3][R4168][RichardsD]

@ Changed position of all M11XX front suspension to be aligned center

[8/12/2020 8:46:56 PM][0.5.3][R4167][reyhard]



[8/12/2020 7:58:29 PM][0.5.3][R4166][reyhard]

^ Added US Stencil decal font set

[8/11/2020 9:23:33 PM][0.5.3][R4165][reyhard]

^ Changed default BO lights status on USAF vehicles
tweaked alpha sorting on m1165 (added high z bias) & added variant of decal label

[8/11/2020 8:27:16 PM][0.5.3][R4164][reyhard]

^ Adjusted M1025/998/1045 series destroyed model
^ Adjusted M1025/998/1045 dashboard materials
^ Added animated suspension to M1025/998/1045 
model.cfg cleanup

[8/10/2020 6:06:31 PM][0.5.3][R4163][da12thMonkey]

Updated Stryker stencil font ("US No.72 stencil" font with adjusted / \ -)

[8/10/2020 1:01:37 PM][0.5.3][R4162][da12thMonkey]

Added "AP" designator to M995 M249 softpack displayname (in line with M240's M61 AP mags)

[8/10/2020 1:28:25 AM][0.5.3][R4161][gurdy]

+ stryker accessory LODs

[8/9/2020 9:26:31 PM][0.5.3][R4160][reyhard]

@ Added missing bipod sounds USAF accessories
melb hit hull tweak

[8/9/2020 7:56:51 PM][0.5.3][R4159][gurdy]

+ Stryker decal plane and decal files. Not currently implemented.

[8/9/2020 7:44:40 PM][0.5.3][R4158][da12thMonkey]

Painted M11XX thermal texture

[8/9/2020 3:10:12 PM][0.5.3][R4157][da12thMonkey]

M1151 O-GPK Mk19: 
Fixed extra point in the damper axis selection causing some weirdness
Regenerated edPrev images after fixing damper axis weirdness
Adjusted alpha sorting on O-GPK glass

All M11XX:
Some work towards TI textures for M11XX (still needs proper thermal signature for engine painting on the texture)
Applied special .rvmat to spare wheel so it doesn't heat up in TI
Front wheels levitating in bottom res LOD due to selection name typos

[8/9/2020 10:18:42 AM][0.5.3][R4156][da12thMonkey]

M1165 ASV garage icon

[8/8/2020 10:16:07 PM][0.5.3][R4155][gurdy]

^ added MWC to stryker rear

[8/8/2020 8:03:55 PM][0.5.3][R4154][reyhard]

^ Added nicer DVE to Stryker
few tweaks to name plates

[8/8/2020 7:59:20 PM][0.5.3][R4153][gurdy]

@ removed decals from stryker interior
@ stryker interior AO fixes
@ weird layer on pioneer equipment
@ changed opacity on woodland stryker tire dirt

[8/7/2020 2:51:59 PM][0.5.3][R4152][reyhard]

stryker plate numbers test

[8/6/2020 7:17:17 PM][0.5.3][R4151][reyhard]

helicopter hull hitpoint tweaking
simple point was not enough to trick armorComponent system - added 4 small boxes with Component1-4 index to bypass registering pylons with i.e. Component1 being registered as a hull hitpoint

[8/5/2020 5:14:08 PM][0.5.3][R4150][da12thMonkey]

Forgot to limit Leupold M5 scope on the M14 EBR-RI

[8/5/2020 1:00:04 AM][0.5.3][R4149][gurdy]

^ made wheels muddier
@ missing STORM texture

[8/4/2020 1:12:41 PM][0.5.3][R4148][da12thMonkey]

Army M1151 Mk19 CROWS had wrong edPrev path

[8/4/2020 12:33:46 PM][0.5.3][R4147][da12thMonkey]

M1165 ASV edPrev images
Regenerated edPrev images for M11XX family

[8/4/2020 8:45:25 AM][0.5.3][R4146][da12thMonkey]

Made Storm rangefinder follow turret movement
Removed acc_### parts from sections[] array (Not needed for hide animations. Retexture selections already exist for these)

[8/4/2020 3:29:44 AM][0.5.3][R4145][gurdy]

+ garage hide animations for new stryker accessories

[8/4/2020 12:33:46 AM][0.5.3][R4144][gurdy]

@ fixed stryker interior colors

[8/3/2020 9:37:08 PM][0.5.3][R4143][da12thMonkey]

+ M995 5.56mm AP ammunition pouches for M249 (DODIC AA02: 4-M995 AP/1-M856 Tracer, Linked)

[8/3/2020 7:52:37 PM][0.5.3][R4142][reyhard]

added few fake components to circumvent issues with armorComponent index being same on proxies

[8/3/2020 5:41:34 PM][0.5.3][R4141][da12thMonkey]

^ Some adjustments to Joint Rail optics setup on Sniper/DMR rifles
^ Moved railed M14 TOP optics proxy forward slightly to accommodate Leupold Mk.4 M3


[8/3/2020 12:14:51 AM][0.5.3][R4140][gurdy]

@ forgot m1126 acc damage mat
+ fuel cans to stryker
+ created rhsusf_props

[8/2/2020 11:44:47 PM][0.5.3][R4139][da12thMonkey]

New PKM gunner anim to fit M1151
Adjusted gunner proxy position so they can use the standard turned-in anim

[8/2/2020 10:38:11 PM][0.5.3][R4138][gurdy]

^ improved hull textures for LODs
+ M1126 olive (dirty) textures

[8/2/2020 9:20:40 PM][0.5.3][R4137][gurdy]

+ Added hidden selections to new stryker accessory parts

[8/2/2020 3:43:18 PM][0.5.3][R4136][reyhard]

^ Tweaked UH1Y gun limits & gunner animations
^ Added DCL120 scope to UH1Y & CH47 miniguns
^ Tweaked damage behaviour of helicopters

[8/2/2020 1:20:40 PM][0.5.3][R4135][reyhard]

standardized variable names in FMTV function

[8/1/2020 12:32:51 PM][0.5.3][R4134][reyhard]

doh

[8/1/2020 12:28:04 PM][0.5.3][R4133][reyhard]

coma

[8/1/2020 12:18:08 PM][0.5.3][R4132][reyhard]

^ Added DCL-120 & inversed kinematics to UH60M gunners
@ C130J cargo is now only detached when speed is lower than 10m/s - http://feedback.rhsmods.org/view.php?id=5810
@ Fixed VG radar action for AH64D on dedicated server - http://feedback.rhsmods.org/view.php?id=5809
started working on CH47 setup

[8/1/2020 8:07:34 AM][0.5.3][R4131][reyhard]

added retexturability to Stryker proxy wheel parts
fixed shimmering effect on Stryker transparent elements by adding NoAlphaWrite & AlphaTest32 render flags
made some of the Stryker elements sharp in 2nd & 3rd LOD in order to fix some of the shading issues

[8/1/2020 6:25:06 AM][0.5.3][R4130][reyhard]

@ Fixed some CfgMoves .rpt errors related to M1127

[8/1/2020 12:56:32 AM][0.5.3][R4129][gurdy]

@ fixed stryker hull AO issue

[7/31/2020 7:08:01 AM][0.5.3][R4128][reyhard]

forgot to commit updated macros - repack

[7/28/2020 10:36:06 PM][0.5.3][R4127][da12thMonkey]

Work on M11XX damage+destruction visuals
Separated SICPS rear compartment from cab compartment

[7/28/2020 12:34:55 PM][0.5.3][R4126][da12thMonkey]

!CLEARTEMP!
Repacking vehicles with Rhino

[7/28/2020 12:27:38 PM][0.5.3][R4125][reyhard]

forgot to add rvmat in previous commit 

[7/28/2020 12:19:04 PM][0.5.3][R4124][da12thMonkey]

Mk19 M1230 and M1237 missing animations to hide/unhide rhino heating element

[7/28/2020 10:33:58 AM][0.5.3][R4123][reyhard]

added wheel proxies to rest of the strykers and updated how they are implemented. Also pushed wheel thread a little bit further

[7/27/2020 11:32:53 PM][0.5.3][R4122][gurdy]

^ updated stryker wheel textures.

[7/27/2020 9:44:39 PM][0.5.3][R4121][da12thMonkey]

hot rhino hummer

[7/27/2020 9:39:10 PM][0.5.3][R4120][gurdy]

^ Some fixes to stryker textures

[7/27/2020 8:51:28 PM][0.5.3][R4119][reyhard]

^ RHINO is now how in TI when turned on - http://feedback.rhsmods.org/view.php?id=5757

[7/27/2020 7:48:38 PM][0.5.3][R4118][reyhard]

^ Tweaked CH-53E RTD land contact points & adjusted geo physx
@ Fixed Stryker AI cargo issue - Troop Commander is now commander of whole vehicle - http://feedback.rhsmods.org/view.php?id=5713
^ Small tweak to FMTV deploy event handler

[7/27/2020 7:28:12 PM][0.5.3][R4117][da12thMonkey]

Mk19 belt wasn't animating in M1151 MCTAGS turret

[7/27/2020 5:45:46 PM][0.5.3][R4116][da12thMonkey]

Adjusted M11XX crew proxy positions and made new anims for CROWS gunner, co-driver

[7/26/2020 5:31:26 PM][0.5.3][R4115][da12thMonkey]

@ SU-260/P (MDO) wasn't using correct inventory image

[7/26/2020 12:37:20 PM][0.5.3][R4114][reyhard]

^ Tweaked dispersion of USAF weapons - http://feedback.rhsmods.org/view.php?id=5752
@ Fixed DUKE script behaviour on dedicated server - http://feedback.rhsmods.org/view.php?id=5771
^ Tweaked M240 recoil - http://feedback.rhsmods.org/view.php?id=5797
^ Small optimization to optic PiP handler
^ Tweaked 40mm HEDP damage so AI is now using it against IFVs - http://feedback.rhsmods.org/view.php?id=5792
^ Tweaked recoil of 40mm grenades after  after damage change + changed Mk19 CoM

[7/26/2020 12:06:18 PM][0.5.3][R4113][reyhard]

added 2nd variant of mid poly wheel - all variants are available in edit LODs

[7/26/2020 11:24:50 AM][0.5.3][R4112][reyhard]

implemented mid poly wheels to m1126

[7/24/2020 10:51:08 PM][0.5.3][R4111][da12thMonkey]

Setting up alternativeFire class for G36 attachment in SAF

[7/22/2020 6:55:18 PM][0.5.3][R4110][reyhard]

@ Fixed hiding of spare wheel on hemtts
@ Fixed typo in buoyancy named property on hemtts

[7/21/2020 10:03:49 PM][0.5.3][R4109][da12thMonkey]

Added bench seats to rear of M1152 model (hidden on standard US M1152 Cargo Carrier configuration)
Configured M1152 Troop Carrier base class (rhsusf_m1152_tcv_base) for use within non-US factions

[7/20/2020 7:31:31 PM][0.5.3][R4108][da12thMonkey]

Missing camo8 selection in LRAS view Gunner LOD
BFT scaling action was assigned to the wrong turret index
Removed CREW Duke weapon+mag from vehicles that don't have the option to show Duke antennas

[7/20/2020 4:48:53 PM][0.5.3][R4107][da12thMonkey]

LRAS anim

[7/20/2020 4:31:00 PM][0.5.3][R4106][reyhard]

@ Reduced M14 max zeroing from 2000m to 1200m

[7/20/2020 1:47:38 PM][0.5.3][R4105][gurdy]

^ removed redundant geometry 

[7/20/2020 1:24:15 PM][0.5.3][R4104][da12thMonkey]

Removing redundant blank.rtm
!CLEARTEMP!

[7/20/2020 12:19:57 PM][0.5.3][R4103][da12thMonkey]

Some initial crew anims for LTAS M1151 (M2 gunner position and neutral turned in/out)

[7/20/2020 11:26:05 AM][0.5.3][R4102][da12thMonkey]

Replaced .tga with .paa

[7/20/2020 1:19:32 AM][0.5.3][R4101][gurdy]

^ tweaked stryker textures

[7/19/2020 10:31:48 PM][0.5.3][R4100][da12thMonkey]

^ Covered some visible mesh holes/backfaces on CH-53 

[7/19/2020 9:03:27 PM][0.5.3][R4099][da12thMonkey]

Repositioned gunshield and added missing turret parts to other LODs of LRAS M1151, consistent with 1st LOD

[7/19/2020 7:38:12 PM][0.5.3][R4098][da12thMonkey]

Corrected animationsource name for hiding smoke dispensers on LRAS3 M1151

[7/19/2020 6:04:02 PM][0.5.3][R4097][reyhard]

^ Added basic LRAS3 functionality to M1151 (still needs completely new set of animations)

[7/19/2020 5:09:41 PM][0.5.3][R4096][da12thMonkey]

Adjusted alpha sorting order on Stryker parts

[7/19/2020 3:57:01 PM][0.5.3][R4095][gurdy]

+ WIP Stryker accessories (all geo is in edit lod 6)

[7/19/2020 12:45:14 PM][0.5.3][R4094][da12thMonkey]

^ Added a few more edges to UH-1Y FLIR ball to make it appear more round

[7/19/2020 12:02:13 PM][0.5.3][R4093][da12thMonkey]

+ Added winch and AN/AAQ-24 DIRCM meshes to CH-53E model, and copied over improved FLIR mesh from UH-1Y. Credit to Odyseus for providing the winch
Close T2521

[7/19/2020 10:19:10 AM][0.5.3][R4092][reyhard]

added test hi res Stryker wheel

[7/15/2020 4:05:26 PM][0.5.3][R4091][da12thMonkey]

Antenna and BFT hiding for Mk19 and M240 vehicles

[7/15/2020 2:16:50 PM][0.5.3][R4090][da12thMonkey]

Ability to hide BFT and antennas on M11XX (Yet to finish model changes on Mk19 and M240 turreted vehicles)
Enabled Olive texture set on other vehicles

[7/15/2020 12:09:39 AM][0.5.3][R4089][RichardsD]

@ Fixed M1151 Ext NOHQ

[7/14/2020 11:45:35 PM][0.5.3][R4088][RichardsD]

^ Improved Ext textures for removal of non-us specific equipment

[7/14/2020 9:36:06 PM][0.5.3][R4087][RichardsD]

^ Improved ACC Textures
^ Improved SICPS Textures
@ Fixed placement of some comms kit in SICPS

[7/14/2020 8:08:34 PM][0.5.3][R4086][RichardsD]

^ Improved interior textures

[7/14/2020 7:41:29 PM][0.5.3][R4085][RichardsD]

+ M1165 ASV for USAF Security Forces
^ Olive M1152/M1165 texture

[7/13/2020 10:11:20 PM][0.5.3][R4084][da12thMonkey]

M1151 PKM was missing part of its interior
Removed BFT-related MFD and user actions from PKM version
Some config refinements

[7/13/2020 5:56:43 PM][0.5.3][R4083][da12thMonkey]

Gunner proxy position wasn't updated in fireGeo LOD

[7/13/2020 5:29:37 PM][0.5.3][R4082][da12thMonkey]

Functional base class for PKM-armed M1151

[7/13/2020 12:20:40 PM][0.5.3][R4081][da12thMonkey]

Added garage pics for M1152 variants
Updated edPrev images for M1152 SICPS

[7/13/2020 3:24:21 AM][0.5.3][R4080][RichardsD]

^ M1152 SICPS Radio Kit Install part way done
^ M1152 SICPS Textures

[7/12/2020 11:08:30 PM][0.5.3][R4079][RichardsD]

+ M1151 PKM SAF, completely non-working

[7/12/2020 11:55:05 AM][0.5.3][R4078][da12thMonkey]

Initial set of editorPreview images for M11XX

[7/12/2020 11:02:57 AM][0.5.3][R4077][da12thMonkey]

M240 vehicles were using the wrong skeletons
M240 pintle was part of the camo5 selection (exhaust shroud texture)
O-GPK turrets had an extra pane of glass floating in space when turret turned
Unhid tent cover by default on RSV versions of M1152

[7/12/2020 4:33:54 AM][0.5.3][R4076][RichardsD]

+ M1151 MCTAGS M240. Issues- 2x bullets in View Gunner not rotating with remaining belt

[7/12/2020 2:13:19 AM][0.5.3][R4075][RichardsD]

@ Fixed M1152 RSV

[7/12/2020 12:48:43 AM][0.5.3][R4074][RichardsD]

+ M1152 Resupply Veh. Breaks the current M1152, will not hide supplies in back

[7/11/2020 9:41:49 PM][0.5.3][R4073][RichardsD]

+ M1151 M240 OGPK

[7/11/2020 11:06:14 AM][0.5.3][R4072][da12thMonkey]

M1151 OGPK/Mk19 proxy was misplaced in LOD 2

[7/10/2020 8:41:27 PM][0.5.3][R4071][reyhard]

Tweaked dashboard decals appearance on base M1151 - added label rvmat 

[7/10/2020 8:01:46 PM][0.5.3][R4070][RichardsD]

+ M7 LVOSS to M1151 LRAS3

[7/10/2020 12:59:07 PM][0.5.3][R4069][da12thMonkey]

Added M1151 MCTAGS/Mk19
Removed RG33 light dome that sneaked into MCTAGS/M2 View Gunner LOD

[7/10/2020 11:25:03 AM][0.5.3][R4068][da12thMonkey]

Adjusted geometry LOD mass of M11XX to a more realistic tonnage (will probably need some physX tweaks later for engine power/speed/torque etc.)
Fixed some issues with SICP w/r/t the rear door and cargo seat
M1152s had camo selections in the shadow LODs

[7/10/2020 9:45:22 AM][0.5.3][R4067][reyhard]

!CLEARTEMP!
glass panel was missing proper SMDI & NOHQ map

[7/10/2020 4:41:29 AM][0.5.3][R4066][RichardsD]

+ M1152A2 SICPS. Known Issues = Rear Door doesn't work, passenger proxy in rear sits in front. No WD texture yet. Very limited texture work on this component yet. 

[7/9/2020 11:13:39 PM][0.5.3][R4065][da12thMonkey]

Hopefully a final working model.cfg arrangement for Rhino/Bumper/CIP compatibility
Replaced references to opticssilver.rvmat from Arma 3 data on several CROWS vehicles

[7/9/2020 1:12:11 PM][0.5.3][R4064][da12thMonkey]

M1151:
Converted hiding front CIP to an animationSource-based solution (forceAnimate solution wasn't working ingame unless both bumper and rhino were in the same animation state)
More model.cfg streamlining
OGPK had wrong camoN selections in the last LOD
Aligned sights on OGPK turreted vehicles

[7/9/2020 10:20:39 AM][0.5.3][R4063][da12thMonkey]

Added CROWS/Mk19 version of M1151
Cleaned up M11XX model.cfg a bit
Adjusted class inheritance tree for US Army/USMC M11XX subclasses to be more consistent
Adjusted displayname strings of CROWS vehicles to be consistent with naming convention for other turrets
^ Adjusted displayname strings of Mk19 vehicles to be consistent (Should be no more Mk 19/Mk.19/MK19/etc. variations when searching Eden)

[7/9/2020 3:39:50 AM][0.5.3][R4062][ballistic09]

Added turret types to display names
Corrected M1151 display name to M1151A1

[7/9/2020 2:40:42 AM][0.5.3][R4061][RichardsD]

+ Adds M1152 USMC and M1151 M2 CROWS USMC versions

[7/9/2020 2:33:04 AM][0.5.3][R4060][ballistic09]

Unified grammar of M1151 customization option's display names to match that of other RHS vehicles
Testing part randomization on M1151 Deploy variants

[7/9/2020 2:19:47 AM][0.5.3][R4059][RichardsD]

^ Improved New Front Bumper textures - rebaked
+ M1151 OGPK w/ Mk. 19 GMG


[7/8/2020 9:52:33 PM][0.5.3][R4058][da12thMonkey]

Fixed bumper shadow LOD non-closed geometry
Wrong macro assigned to woodland MCTAGS vehicle

[7/8/2020 8:44:13 PM][0.5.3][R4057][reyhard]

removed unnecessary files

[7/8/2020 8:30:35 PM][0.5.3][R4056][da12thMonkey]

added comma...

[7/8/2020 7:53:58 PM][0.5.3][R4055][da12thMonkey]

fixed trailing comma

[7/8/2020 7:50:35 PM][0.5.3][R4054][da12thMonkey]

Set up rhino to work properly with IbisTek bumper
Added M1151 w/ MCTAGS turret for USMC

[7/8/2020 3:36:10 PM][0.5.3][R4053][RichardsD]

+ Adds new front bumper to M1151 Deploy
@ Camo selection added to M1151 Deploy Mk 64 Mount

[7/8/2020 2:39:49 PM][0.5.3][R4052][da12thMonkey]

oops

[7/8/2020 1:35:08 PM][0.5.3][R4051][da12thMonkey]

Fixed non-convexities in view and fire geometry LODs (except WIP OGPK version)

[7/8/2020 10:59:13 AM][0.5.3][R4050][da12thMonkey]

Set up front CIP hiding on M1151 CROWS when Rhino is attached
Cleaned up duplicate section since Rhino was added

[7/8/2020 10:33:29 AM][0.5.3][R4049][da12thMonkey]

M1151:
Corrected OGPK turret inheritance and hiddenselections (should just require p3d/model.cfg fixes @RichardsD)
Configured Rhino that was added to CROWS vehicle

[7/8/2020 4:14:10 AM][0.5.3][R4048][RichardsD]

+ M1151 M2 - OGPK. Known issues = turret has no gun, the camo net won't show, and the gunner's sights are mis-aligned slightly. Will develop further.

[7/7/2020 10:46:21 PM][0.5.3][R4047][da12thMonkey]

M11XX ECV ViV and sling loading setup

[7/7/2020 4:12:49 PM][0.5.3][R4046][da12thMonkey]

Fixed M11XX door glass bone overlap
Copied updated M1152 codriver proxy position to other models

[7/7/2020 12:38:15 PM][0.5.3][R4045][da12thMonkey]

M1151 CROWS monitor was missing a few switches from the pilot LOD
Centred memory points a little more

[7/7/2020 10:08:54 AM][0.5.3][R4044][da12thMonkey]

CROWS M1151: moved BFT scale action to correct turret.

[7/7/2020 9:25:46 AM][0.5.3][R4043][da12thMonkey]

Section count cleanup for LRAS and CROWS M1151
osaVeze axis was a little off-centre on LRAS M1151

[7/7/2020 1:12:12 AM][0.5.3][R4042][ballistic09]

^ Corrected tracer burn times and colors for various 120mm rounds
Added unused (for now) M829A4 and 105mm ammo classes just for the fun of it

[7/6/2020 9:15:21 PM][0.5.3][R4041][da12thMonkey]

Garage icon for CROWS M1151

[7/6/2020 8:32:16 PM][0.5.3][R4040][da12thMonkey]

M1151 CROWS texturesources fix

[7/6/2020 7:48:19 PM][0.5.3][R4039][RichardsD]

+ 1st committ of the M1151 M2 CROWS. Known issues: no hidden selects working on CROWS, aiming reticle mis-alinged in gunner LOD
@ Fixed cargo proxy on M1152, will do to rest later

[7/6/2020 6:58:20 PM][0.5.3][R4038][da12thMonkey]

Corrected M1151/M1152 cargo position proxy and door allocation

[7/6/2020 11:03:06 AM][0.5.3][R4037][da12thMonkey]

Adjustment to M1152 rear cover anim setup

[7/6/2020 10:29:16 AM][0.5.3][R4036][da12thMonkey]

M1152:
Fixed vehicle had stopped moving (geometry LOD components had disappeared)
Fixed Rear Cover scaling to half size rather than hiding (selection overlap with damageHide parent)
Set up hide anim for side CIP panels

[7/6/2020 1:35:10 AM][0.5.3][R4035][RichardsD]

@ Added the CIP to the selection, but appear to have broken the M1152

[7/5/2020 9:34:31 PM][0.5.3][R4034][da12thMonkey]

Fixing hiddenSelections issues after M1152 changes

[7/5/2020 8:58:50 PM][0.5.3][R4033][reyhard]

run checkAll o2script on all M11xx vehicles
fixed sectionsInherit loop

[7/5/2020 8:18:31 PM][0.5.3][R4032][RichardsD]

^ Improvements to M1152 and the whole thing won't pack anymore :(

[7/5/2020 2:29:51 PM][0.5.3][R4031][da12thMonkey]

Garage icons for uparmoured HMMWVs (inc. different turret types)

[7/5/2020 10:28:24 AM][0.5.3][R4030][da12thMonkey]

M1152 config adjustments

[7/5/2020 4:31:07 AM][0.5.3][R4029][RichardsD]

+ M1152 first version with some model.cfg errors

[7/5/2020 3:45:25 AM][0.5.3][R4028][RichardsD]

^ M1152 String table added

[7/4/2020 5:23:11 PM][0.5.3][R4027][RichardsD]

+ Completely broken M1151 with LRAS3 and M2 as first WIP

[7/4/2020 5:12:35 PM][0.5.3][R4026][da12thMonkey]

@ Muzzle flash proxy was not visible when firing MG on some Stryker variants (possible zasleh/muzzleFlash selections clash)

[7/4/2020 4:40:49 PM][0.5.3][R4025][RichardsD]

+ Added M1151 M2/LRAS3 to stringtable

[7/4/2020 10:48:07 AM][0.5.3][R4024][da12thMonkey]

M1151/M1165: Some parts like DUKE antenna and wheels did not have hiddenSelections in lower LODs
M1151 w/ M240 view Gunner LOD: Only the top cover was shaking when firing the weapon, cocking handle was missing


[7/4/2020 1:57:51 AM][0.5.3][R4023][da12thMonkey]

M1151 Mk19 gunner proxy had the wrong index number in view gunner LOD
Adjusted M1165 ext. .rvmat to match recent changes to M1151 ext .rvmat
Reduced section count

[7/3/2020 10:23:18 PM][0.5.3][R4022][RichardsD]

@ Fixed the Hidden select on the Mk 64 mount (da12thmonkey lives!!)

[7/3/2020 10:03:53 PM][0.5.3][R4021][RichardsD]

+ M1151 (Mk. 19)
@ Fixed gunner proxies on M2 Version
^ Added hidden selection to Mk. 64 mount (non working)

[7/3/2020 6:50:00 AM][0.5.3][R4020][reyhard]

fixed duplicated hitpoint class

[7/3/2020 4:08:09 AM][0.5.3][R4019][RichardsD]

^ Improved RVMAT for Ext
@ Fixed some Mk 19 stuff for later version

[7/2/2020 11:34:14 PM][0.5.3][R4018][RichardsD]

+ Adds M1151 (M240)

[7/2/2020 3:20:49 AM][0.5.3][R4017][RichardsD]

^ Adds Rhino to M1151
@ Fixed air scoop shadow LOD issue

[7/2/2020 2:43:59 AM][0.5.3][R4016][ballistic09]

re-added tall air intake to USMC M1151 and M1165...

[7/1/2020 8:28:39 PM][0.5.3][R4015][RichardsD]

^ Added more M1151/M1165 Names to Stringtable

[7/1/2020 6:30:44 PM][0.5.3][R4014][reyhard]

m1xx:
* fixed skeleton inheritance & added more unique names
* fixed \rhsusf\addons\rhsusf_m11xx\data\rhsusf_m1151_tire.rvmat link ( removed slash from beginning)
* fixed snorkel configuration (duplicated entries)
* fixed camo7 selection on armed m1151
* added decal parameter

[7/1/2020 5:14:20 PM][0.5.3][R4013][RichardsD]

+ Adds M1151 W/ GPK Turret M2 as test for armed version

[6/30/2020 10:54:38 PM][0.5.3][R4012][RichardsD]

^ Improved M1151 Wheels

[6/30/2020 8:49:49 PM][0.5.3][R4011][ballistic09]

corrected initial state/position of air intake
linked raised air intake to deep water fording kit (when extended exhaust is unhidden, tall air intake is too)

[6/30/2020 7:24:01 AM][0.5.3][R4010][reyhard]

fixed snorkel animation

[6/30/2020 4:04:37 AM][0.5.3][R4009][RichardsD]

@ Adds CIP Hidden panels
^ Adds LODs
@ Set the snorkel to translate mode but then I broke it


[6/29/2020 9:45:24 PM][0.5.3][R4008][RichardsD]

@ Fixed USMC Versions
^ Separated the raised exhaust from intake for future versions

[6/29/2020 9:13:44 PM][0.5.3][R4007][RichardsD]

@ Renamed camo7 to i1 to support decal system forthcoming

[6/29/2020 8:39:08 PM][0.5.3][R4006][reyhard]

added DAGR & BFT to M1151
cleaned up MATV config

[6/29/2020 7:30:08 PM][0.5.3][R4005][reyhard]

^ Tweaked interior camo selection of MATVs
removed anim folder from rhsusf_main

[6/29/2020 6:10:14 PM][0.5.3][R4004][RichardsD]

^ New tac markings

[6/28/2020 2:08:44 PM][0.5.3][R4003][RichardsD]

^ Adds non-functional comms kit for M1151/M1165
^ Adds non-functional tactical markings (camo7)
^ Adds proper string table names
^ Adds USMC versions of M1151/M1165
^ Adds IFF Panels

[6/28/2020 9:40:53 AM][0.5.3][R4002][reyhard]

updated base classes

[6/28/2020 9:30:05 AM][0.5.3][R4001][reyhard]

cleaned up config - added base class for m1165

[6/27/2020 11:43:45 PM][0.5.3][R4000][RichardsD]

^ M1165 Texture Improvements
^ M1165 fire supp kit re-added

[6/27/2020 10:40:17 PM][0.5.3][R3999][RichardsD]

@ M1151/M1165 Shadow LOD fixes
@ M1165 WD does not appear in Garage any longer


[6/27/2020 8:41:42 PM][0.5.3][R3998][jastreb]

macro fix, force m1165 in garage

[6/27/2020 8:10:02 PM][0.5.3][R3997][jastreb]

minor config fixes

[6/27/2020 6:44:57 PM][0.5.3][R3996][RichardsD]

@ Gauge fixes for M1151
^ M1165 Test added (non-working, currently invisible)

[6/27/2020 12:05:03 PM][0.5.3][R3995][reyhard]

added blank anim

[6/27/2020 3:26:08 AM][0.5.3][R3994][RichardsD]

@ Gauges added to M1151

[6/26/2020 7:16:56 AM][0.5.3][R3993][reyhard]

cleaning up config, part 3

[6/26/2020 6:02:41 AM][0.5.3][R3992][reyhard]

cleaning up config, part 2

[6/26/2020 5:37:12 AM][0.5.3][R3991][reyhard]

cleaned up m1xx config

[6/25/2020 2:10:32 AM][0.5.3][R3990][RichardsD]

+ Adds the 1st version of the M1151 Enhanced Capacity Armament Carrier. See ticket for additional information on development and additional versions that will be created later.

[6/24/2020 9:11:21 PM][0.5.3][R3989][reyhard]

@ USAF references to AFRF which resulted in broken get out action if AFRF was not loaded - http://feedback.rhsmods.org/view.php?id=5764

[6/23/2020 8:49:30 PM][0.5.3][R3988][reyhard]

cleaned up Stryker config

[6/21/2020 2:39:16 AM][0.5.3][R3987][RichardsD]

^ Adds M1132 with plow hidden by default. M1132 with plow re-named to M1132 (M2) SMP. 

[6/5/2020 7:59:42 AM][0.5.3][R3986][reyhard]

^ Updated side mount JR config in USAF

[6/1/2020 1:50:23 PM][0.5.3][R3985][reyhard]

tweaked z sorting of new radio equipment
removed baked shadow from one part of m1126 hull texture to ensure better visuals when M1127 variant is used

[5/31/2020 11:33:37 PM][0.5.3][R3984][RichardsD]

^ M1126, M1127, M1132, M1134 Now have comms install in interior LODS. Consists of AN/VRC-92, AN/VIC-3 IC Boxes, and associated cabling. 

[5/31/2020 10:53:00 AM][0.5.3][R3983][reyhard]

^ Added subtle refract particle effects to missiles
@ Automatic troops NVG handler no longer replaces NVG on character head if there is already some NVG attached to it
^ Another attempt at fixing occluders after binarization
^ Tweaked M1134 alpha sorting in gunner LOD

[5/30/2020 6:40:08 PM][0.5.3][R3982][reyhard]

@ Fixed wrong passenger position in 2nd LOD on M1127
@ Fixed wrong behavior of cargo occluders after binarizing p3d on Stryker series - http://feedback.rhsmods.org/view.php?id=5735

[5/26/2020 6:01:17 PM][0.5.3][R3981][reyhard]

^ Tweaked materials for GLUA model in UI
^ Reduced delay between shots for AI in tanks could  - http://feedback.rhsmods.org/view.php?id=5719
^ USF config was overriding AFRF FCS ammo configuration
^ ERA is more fragile to heavy AP rounds

[5/25/2020 6:08:48 PM][0.5.3][R3980][reyhard]

^ Added Grenade Launcher Unit Assembly controls to M1127
^ Reduced TOW AI autoseek
^ Increased max AI engagement range for M256 cannon (up to 5km)
@ Fixed Lerca zoom - http://feedback.rhsmods.org/view.php?id=5723

[5/21/2020 7:59:50 AM][0.5.3][R3979][reyhard]

added initial framework for M1127 smoke launchers handling (WIP)

[5/20/2020 3:52:35 PM][0.5.3][R3978][reyhard]

^ Tweaked Stryker LODs
^ Removed baked ambient shadow from Tan Stryker hull texture - http://feedback.rhsmods.org/view.php?id=5712

[5/19/2020 3:50:53 PM][0.5.3][R3977][reyhard]

@ Fixed default value in M1132 Distance Interval variable

[5/18/2020 10:00:05 PM][0.5.2][R3976][jenkins]

Update for 0.5.3 version

[5/18/2020 8:24:20 PM][0.5.2][R3975][reyhard]

changed initPhase of Lane Marker System

[5/18/2020 5:26:56 PM][0.5.2][R3974][reyhard]

^ Added Lane Marker System to M1132
^ Tweaked Stryker durability
renamed hidden selections

[5/18/2020 3:42:50 PM][0.5.2][R3973][reyhard]

@ Fixed C130J vehicle paradroping error

[5/17/2020 9:06:10 AM][0.5.2][R3972][reyhard]

@ Fixed DVE action availability - http://feedback.rhsmods.org/view.php?id=5704
^ M1134 Stryker now spawns with full crew

[5/16/2020 10:54:55 AM][0.5.2][R3971][reyhard]

^ Added magazine Wells to M256 & M242 
^ Added "rhs_mag_70Rnd_25mm_M242_M791" magazine to be used with M242
^ Added emissive material to burning engine sparks
^ Added optic destruction to new Stryker variants
^ Tweaked new Stryker variants TI textures
@ Fixed seat switching with "F" key on M1127

[5/16/2020 8:50:33 AM][0.5.2][R3970][reyhard]

@ Fixed visibility of Raven laser designator - http://feedback.rhsmods.org/view.php?id=2749

[5/15/2020 3:01:43 PM][0.5.2][R3969][reyhard]

another fixerito

[5/15/2020 2:50:17 PM][0.5.2][R3968][reyhard]

macros fixes

[5/15/2020 2:48:14 PM][0.5.2][R3967][reyhard]

@ Fixed UH-1Y gunner view memory points - http://feedback.rhsmods.org/view.php?id=5700
@ Fixed missing Smokegen string when running USAF standalone 

[5/15/2020 2:33:54 PM][0.5.2][R3966][reyhard]

!CLEARTEMP!
@ Fixed missing STR_RHS_AUTHOR_FULL errors when only USAF mod was loaded
@ Cleaned up M136 & fixed its SMDI map

[5/14/2020 10:21:05 PM][0.5.2][R3965][RichardsD]

^ Fixed the M1134 Desert texture to include TOW Missiles details from the woodland ones

[5/14/2020 5:51:57 PM][0.5.2][R3964][reyhard]

readded autoseek to TOWs again

[5/14/2020 5:25:24 PM][0.5.2][R3963][reyhard]

@ Added workaround for broken vanilla missile manual control on AI. TOW should usable be AI even if target has engine off  - http://feedback.rhsmods.org/view.php?id=5685 
^ Updated head injury macros to be up to date with Old Man

[5/14/2020 2:20:08 AM][0.5.2][R3962][RichardsD]

@ Adds M1132 ESV Desert + hidden selections
@ Adds M1134 ATGM Desert + hidden selections

[5/13/2020 10:45:41 PM][0.5.2][R3961][RichardsD]

@ Adds desert LRAS3 texture

[5/13/2020 5:14:09 PM][0.5.2][R3960][reyhard]

^ Cleaned up inheritance on RHS assets (declarations in wrong place) to fix potential clashes with other mods

[5/12/2020 5:28:25 PM][0.5.2][R3959][reyhard]

^ Tweaked M1134 MFD & PiP screen
removed desert texture from M1127

[5/12/2020 2:23:19 PM][0.5.2][R3958][reyhard]

^ Tweaked M1134 gunsight 
added additional bones for M1132 mine blow - to be used later for damage simulation
cleanup of USAF static weapons - removed proxies from shadow LOD, named properties, UVs, etc


[5/12/2020 6:57:02 AM][0.5.2][R3957][reyhard]

converted macro to upper case and made it with more clear to which faction it belongs

[5/12/2020 3:08:11 AM][0.5.2][R3956][RichardsD]

@ Adds Desert texture for M1127

[5/11/2020 1:34:21 PM][0.5.2][R3955][reyhard]

@ Fixed wrong gunner proxy index on M1240 (M2) - http://feedback.rhsmods.org/view.php?id=5674

[5/11/2020 7:09:30 AM][0.5.2][R3954][reyhard]

forgot to include modified mask in previous stryker commit 

[5/10/2020 11:11:17 AM][0.5.2][R3953][reyhard]

^ Added editor previews for new Stryker variants

[5/10/2020 10:14:58 AM][0.5.2][R3952][reyhard]

^ Improved M1134 Gunner Panel materials

[5/10/2020 9:33:55 AM][0.5.2][R3951][reyhard]

@ Fixed position of SOCOM flash hider in first person LOD

[5/10/2020 8:45:01 AM][0.5.2][R3950][reyhard]

@ Fixed missing front sight for M14 (RIS) - http://feedback.rhsmods.org/view.php?id=5660

[5/10/2020 8:34:38 AM][0.5.2][R3949][reyhard]

^ Tweaked LRAS3 MFD
^ Reduced M1134 turret rotation speed

[5/10/2020 5:14:23 AM][0.5.2][R3948][reyhard]

@ Mast unfolding works also in Virtual Garage when damage on vehicle is disabled

[5/10/2020 4:59:48 AM][0.5.2][R3947][reyhard]

@ Fixed typo in virtualAmmoBox.sqf

[5/9/2020 9:14:25 PM][0.5.1][R3946][jenkins]

Update for 0.5.2 version

[5/9/2020 7:48:24 PM][0.5.1][R3945][reyhard]

fixed default turret spawning on strykers

[5/9/2020 7:32:56 PM][0.5.1][R3944][reyhard]

^ Added basic MFD for Stryker LRAS3

[5/9/2020 5:13:22 PM][0.5.1][R3943][reyhard]

@ Fixed flashbang script not working when AFRF was not loaded - http://feedback.rhsmods.org/view.php?id=5651

[5/9/2020 4:59:41 PM][0.5.1][R3942][reyhard]

hotfixed M14 bipod slot

[5/9/2020 3:16:32 PM][0.5.1][R3941][reyhard]

^ Updated crew proxies in Stryker fire geometry

[5/9/2020 2:53:24 PM][0.5.1][R3940][reyhard]

@ Fixed rogue component in Fire Geo of m1a1hc.p3d

[5/9/2020 2:28:57 PM][0.5.1][R3939][reyhard]

^ Configured M1134 commander pintle weapon
^ Added basic MITAS MFD
^ Added damage textures to new Stryker variants
^ Added new desert Stryker variants to CfgPatches
@ Fixed muzzle flashes on M1134 & M1127 weapons
^ Tweaked PIP acog scopes (removed rvmat from R2T - picture should bit brighter)


[5/9/2020 10:07:48 AM][0.5.1][R3938][reyhard]

^ Added M14 ground holders and Virtual Ammo Box entries

[5/9/2020 9:34:38 AM][0.5.1][R3937][reyhard]

^ Updated M14 textures + added Fiberglass variant

[5/9/2020 1:59:07 AM][0.5.1][R3936][ballistic09]

woodland CH-47's were in wrong faction
added desert faction variants for new Strykers
disabled desert camo option for new Strykers for now

[5/8/2020 6:18:14 PM][0.5.1][R3935][reyhard]

^ Added turret lock indicator to M1134
^ Added action to fold mast on M1134
^ Added action to M1132 to unfold Lane Marking System (not working yet)
^ Added some scripted reticle for LRAS3
^ Added turret hitpoints to M1134
@ Fixed one error related to turn out on Strykers

[5/8/2020 4:11:53 AM][0.5.1][R3934][ballistic09]

finalizing ITAS/MITAS UI element positions
added placeholder ITAS/MITAS optics/reticles

[5/7/2020 7:13:02 PM][0.5.1][R3933][reyhard]

added couple more animations to m1134

[5/7/2020 2:55:56 PM][0.5.1][R3932][reyhard]

^ Tweaks to inertia of some weapons
Tweaked M1134 interior

[5/7/2020 2:43:09 AM][0.5.1][R3931][ballistic09]

M1134 gunner now using MITAS FCS with green thermals...

[5/6/2020 4:10:40 PM][0.5.1][R3930][reyhard]

@ Fixed missing uvset on M8541 scopes
@ Added some missing memory points to RHS_M14_RAIL.p3d
^ Tweaked PP Effects on G33
^ Reorganized some of the scopes within JR framework - moved i.e. M150 + PNVS variant to long rail variant only
^ Added custom recoil for M14
^ Tweaked dispersion across M14 family

[5/5/2020 9:43:44 PM][0.5.1][R3929][reyhard]

small fix

[5/5/2020 9:43:10 PM][0.5.1][R3928][reyhard]

Reenabled lockType = 1 for TOW

[5/5/2020 9:42:36 PM][0.5.1][R3927][reyhard]

Some work on M1134: added animations for gunner seat + tweaks for missile handling

[5/5/2020 5:11:47 PM][0.5.1][R3926][reyhard]

^ Reconfigured muzzle attachments on M14 & M14 EBR

[5/5/2020 2:20:51 PM][0.5.1][R3925][reyhard]

^ Added animated ironsights to M14
^ Added magazine proxies to M14
^ Added M80 ball magazines for M14
^ Added icons for M14 inventory accessories
^ Tweaked muzzle flashes on new M14 accessories
^ Standardized M14 fire geometry
tweaked rail setup
removed HK skin variant

[5/4/2020 11:30:52 PM][0.5.1][R3924][ballistic09]

typo

[5/4/2020 11:25:28 PM][0.5.1][R3923][ballistic09]

minor M14 tweaks

[5/4/2020 8:51:34 PM][0.5.1][R3922][reyhard]

+ Added M14 by WinteR5
cleaned up sound configs

[5/4/2020 6:55:02 PM][0.5.1][R3921][reyhard]

tripod go away

[5/3/2020 1:43:58 PM][0.5.1][R3920][reyhard]

removed proxies from shadow LOD
removed some trailing spaces from some accessories
removed camo selections from BDU & ABU shadow LOD

[5/3/2020 1:26:30 PM][0.5.1][R3919][reyhard]

named properties, uvsets and shadows cleanup

[5/3/2020 1:18:04 PM][0.5.1][R3918][reyhard]

^ Added new icon for Eagle III (Coyote) backpack
@ Fixed missing NVG shadow in view pilot
^ Added toolkit and mine detector to EOD Technicians 

[5/1/2020 3:34:44 PM][0.5.1][R3917][reyhard]

^ Tweaked locality of LOAL script - http://feedback.rhsmods.org/view.php?id=5635

[4/30/2020 7:38:23 PM][0.5.1][R3916][reyhard]

^ Added animation for folding of marker dispenser to M1132
initial commit of M14 (no config)

[4/29/2020 6:53:04 AM][0.5.1][R3915][reyhard]

fixed ghost lod

[4/28/2020 10:54:15 AM][0.5.1][R3914][reyhard]

^ Improved camera movement on static weapons

[4/27/2020 3:23:06 PM][0.5.1][R3913][reyhard]

@ Fixed HMG reload sounds

[4/27/2020 11:44:38 AM][0.5.1][R3912][reyhard]

^ Added KIA animations for new stryker poses
^ Added inertia to MATV OGPK mounted weapons 
^ Added smoke launcher mem points for M1134
disabled smoke launcher on M1127 till proper system is created

[4/26/2020 5:44:23 PM][0.5.1][R3911][RichardsD]

@ Changed NOHQ to account for movement of the Azimuth indicator on the gunner's panel

[4/26/2020 5:11:08 PM][0.5.1][R3910][reyhard]

^ Tweaked gunner animations on M1127 (added IK)
^ Added PiP to LRAS3


[4/26/2020 1:39:56 PM][0.5.1][R3909][reyhard]

^ Added some basic handling of M1127 weapons 
^ Enabled periscopes on M1134
^ Added animations for M1127 gunner
tweaked M1127 SMDI map
removed some obsolete scripts

[4/25/2020 7:03:03 PM][0.5.1][R3908][reyhard]

^ Added inertia to static M2 (test)
tweaked indicator pos on m1134
some more experiments with m1127 turrets setup


[4/25/2020 5:38:44 AM][0.5.1][R3907][RichardsD]

+ Adds the M240B MMG to the M1134 Commander's position, except not-working. Only animated. 

[4/24/2020 6:58:20 PM][0.5.1][R3906][reyhard]

Added placeholder anim for LRAS3 operator

[4/24/2020 6:19:31 PM][0.5.1][R3905][reyhard]

^ Added new inventory icons for US backpacks
^ Tweaked load of Eagle backpack - http://feedback.rhsmods.org/view.php?id=5622
converted backpacks loadouts to macros
removed obsolete CH53 AFM XMLs

[4/24/2020 8:05:04 AM][0.5.1][R3904][TeTeT]

^ add CH-53 cargo classes to CfgPatches

[4/23/2020 9:08:02 PM][0.5.1][R3903][ballistic09]

Added missile indicator to ITAS

[4/23/2020 8:20:07 PM][0.5.1][R3902][TeTeT]

^ add cargo variant to CH-53

[4/23/2020 7:03:19 PM][0.5.1][R3901][reyhard]

^ Added additional Stryker icons and updated CfgPatches

[4/23/2020 6:48:57 PM][0.5.1][R3900][ballistic09]

small workaround for weird UI bug affecting ITAS mode box...

[4/23/2020 6:11:51 AM][0.5.1][R3899][reyhard]

added workaround for missing LRAS optic model - to be investigated later

[4/23/2020 3:34:41 AM][0.5.1][R3898][ballistic09]

Very WIP ITAS for M1134...

[4/22/2020 9:31:29 PM][0.5.1][R3897][TeTeT]

Add ViV to CH-53

+ add vehicle in vehicle transport to CH-53 config and model

[4/22/2020 3:54:58 AM][0.5.1][R3896][RichardsD]

@ Slightly improved M1127 Smoke panel texture

[4/21/2020 8:25:22 PM][0.5.1][R3895][reyhard]

added test M1127 M2 gunner anim

[4/21/2020 6:58:16 PM][0.5.1][R3894][RichardsD]

@ Adds M1127 Smoke Grenade Discharger Panel Mask
@ Up-sized the M1134 Mask to 2K

[4/21/2020 3:05:58 PM][0.5.1][R3893][ballistic09]

LRAS3 tweaks

[4/21/2020 5:25:19 AM][0.5.1][R3892][ballistic09]

Quick and dirty LRAS3 FCS

[4/21/2020 3:28:37 AM][0.5.1][R3891][RichardsD]

- Remove M1134 mask file and changes with mask_ca
@ Added M1134 Fire geo
@ Interior texture fixes
@ Sight housing and assy now rotates with the TOW Missile Carrier


[4/20/2020 9:33:29 PM][0.5.1][R3890][reyhard]

added missing anim

[4/20/2020 9:22:32 PM][0.5.1][R3889][reyhard]

^ Added new animation for M1134 gunner
^ Updated RHS loader to Old Man update

[4/20/2020 8:35:07 PM][0.5.1][R3888][ballistic09]

Tweaks to new Stryker variant's optics and transport items...

[4/20/2020 8:08:48 PM][0.5.1][R3887][RichardsD]

@ M1127 LOD improvements
@ M1127 Adds Gunner Traverse Controller Stick
@ M1127 Interior texture improvements / LOD fixes

[4/20/2020 3:30:41 AM][0.5.1][R3886][RichardsD]

@ Fixed: The M1134 Gunner now has the top hatch in Pilot LOD
+ Adds detail to gunners controls


[4/19/2020 5:39:39 PM][0.5.1][R3885][reyhard]

made M1134 somehow working
work on m1127 - initial attempt to lay out turrets

[4/19/2020 2:12:03 PM][0.5.1][R3884][reyhard]

missed 2 files

[4/19/2020 1:37:44 PM][0.5.1][R3883][reyhard]

^ Added cargo variants of CH-47F and C130J
@ Fixed some .rpt errors related to CH53
cleaned up inheritance of CH47 and C130
added autocenter = 0 to some of the proxies

[4/18/2020 9:43:00 PM][0.5.1][R3882][RichardsD]

+ Adds first commit of the M1134 Stryker ATGM Vehicle. 

[4/18/2020 4:13:54 PM][0.5.1][R3881][reyhard]

@ Fixed M109 assert connected to Commander memory points
@ Fixed duplicated weapons for M2A2 due to VG components
@ Fixed AIM9M error on AH1Z (magazine compatibility)
@ Fixed some wrong components on M1A2
@ Fixed UH60M was spawning above its land contact points
^ Tweaked UH60M max landing speed
sanitized M1A2 model.cfg for new pboproject
added autocenter=0 to some of the proxies

[4/18/2020 12:47:30 PM][0.5.1][R3880][reyhard]

^ Tweaked M1025/M998 wheel hitpoints

[4/15/2020 6:56:15 AM][0.5.1][R3879][reyhard]

@ Fixed M1A1HC Olive texture after removing IFF panel - http://feedback.rhsmods.org/view.php?id=5594
@ Fixed some .rpt errors with FG
sanitized model.cfg for new pboproject 

[4/12/2020 9:08:26 PM][0.5.1][R3878][reyhard]

fixerito

[4/12/2020 8:51:25 PM][0.5.1][R3877][reyhard]

tweaked M1127 & M1132 configuration

[4/12/2020 3:13:24 PM][0.5.1][R3876][reyhard]

^ Added RHINO functionality to M1230 & M1237 vehicles
@ Fixed .rpt error about "dimension should be array of 2" for static weapons

[4/12/2020 1:08:07 PM][0.5.1][R3875][reyhard]

@ Fixed FMTV SOV .rpt errors
@ Fixed FMTV SOV had wrong turret attenuation
@ Fixed few rpt errors on RG33, Stryker & SOCOMAUV

[4/11/2020 9:28:16 PM][0.5.1][R3874][reyhard]

^ Tweaked CH-47 floating time - http://feedback.rhsmods.org/view.php?id=5564
^ Zeroed Mk17 ironsights to M80 Ball - http://feedback.rhsmods.org/view.php?id=5564
@ Fixed UV offset on some of the scopes - http://feedback.rhsmods.org/view.php?id=5556
^ Tweaked M113 Mk19 view gunner ammo box - http://feedback.rhsmods.org/view.php?id=5538
@ Fixed rpt spam related to wheel reference
@ Fixed rpt spam related to duplicated DUKE weapons
@ Fixed missing OGPK mirrors points on RG33L & Caiman
^ Added glass destruction to Cougars
@ Fixed bits of Cougars fire geometry
removed view cargo LOD from cougars
small clean up of M1025 vehicles
tweaking of M1025 fuel & wheels hitpoints (WIP)
sanitized M113 model.cfg for new pborpoject

[4/11/2020 4:37:05 PM][0.5.1][R3873][reyhard]

^ Tweaked sounds EH macros (simplified them)

[4/10/2020 2:34:34 PM][0.5.1][R3872][reyhard]

^ CH-53E user actions are now also available when using remote controlled unit
@ Fixed CH-53E fold action didn't synchronize fuel status correctly when folding or unpacking - http://feedback.rhsmods.org/view.php?id=5587

[4/6/2020 8:49:43 PM][0.5.1][R3871][reyhard]

@ Fixed missing icon on SU230A/PVS when 3D mode was used - http://feedback.rhsmods.org/view.php?id=5577

[4/3/2020 3:07:56 PM][0.5.1][R3870][RichardsD]

@ M142 Mirror selection delete in Pilot LOD

[4/3/2020 9:25:07 AM][0.5.1][R3869][reyhard]

mikero lint checking fix

[4/2/2020 11:09:15 PM][0.5.1][R3868][RichardsD]

@ Possibly fixed M142 HIMARS config

[4/2/2020 10:44:31 PM][0.5.1][R3867][RichardsD]

+ Adds DVE to M142 HIMARS

[4/2/2020 4:50:15 PM][0.5.1][R3866][RichardsD]

+ Adds DVE to M1239 SOCOM AUV
@ Fixes a mem point on M1232 RG-33L 6X6

[4/1/2020 8:05:21 PM][0.5.1][R3865][RichardsD]

+ Adds DVE to RG-33 SOCOM ASV, and RG-33L 6X6 Series of MRAPs

[3/31/2020 5:20:05 PM][0.5.1][R3864][reyhard]

@ Co-driver of armed MATVs was missing BFT scale adjust action

[3/30/2020 7:23:48 PM][0.5.1][R3863][reyhard]

Added DVE template
minor config cleanup

[3/30/2020 7:06:02 PM][0.5.1][R3862][reyhard]

^ Added handbrake to MATV

[3/29/2020 12:13:15 PM][0.5.1][R3861][reyhard]

^ Added acceleration pedal animation to MATVs
^ Added various small dashboard indicators (lights, parking brake, service lights) to MATV
^ MATV co driver & Stryker Vehicle Commander can now use waypoint manager
^ Tweaked BFT brightness in direct light
^ Added data link to MATVs - they report now their position and get allies location on BFT
^ Tweaked BFT map rotation (reduced animPeriod to 0 - rotation should be smooth and instant)

[3/28/2020 3:23:38 PM][0.5.1][R3860][reyhard]

^ Changed Co-Driver configuration on MATV - WARNING! It's now using turret, instead of regular seat meaning that missions with crew inside might need updating!
^ CROWS screens in MATVs are now emitting some actual light
^ New interior applied to all MATV variants
^ All MATV doors are animated with same speed now
^ Increased FFV rotation limits on MATV SOF variants (more freedom traded for visuals)
^ Tweaked M1126 (Mk19) inheritance
removed cargo LOD from MATVs - pilot LOD is used instead
forgot to commit DARG background


[3/25/2020 9:30:04 PM][0.5.1][R3859][reyhard]

@ MATV DVE monitor was shutting down when reversing due to BBoxes being to close to head

[3/25/2020 7:13:19 PM][0.5.1][R3858][RichardsD]

+ Adds M1126 Stryker with Mk. 19 GMG


[3/25/2020 4:16:06 AM][0.5.1][R3857][RichardsD]

+ Adds first iteration of the M1132 Engineer Squad Vehicle (ESV) with M2, and Surface Mine Plow (SMP). 

[3/23/2020 9:24:51 PM][0.5.1][R3856][reyhard]

^ Added DAGR GPS MFD to M1240 (basic variant only)
^ Added scripted solution for M1240 gear indicator
^ Splitted BFT function to separate file
fixed glass damage inside of MATV


[3/22/2020 8:47:12 PM][0.5.1][R3855][reyhard]

^ Tweaked DVE picture in picture screen ratio & added emissive material 
^ Tweaked MATV wheel rvmats
^ Added separate TI rvmat for spare wheels for rest of MATV variants
^ Added few more details to MATV interior
^ MATV left mirror bounding box is moved away to the left when DVE is deployed so only one render source is used

[3/21/2020 2:33:00 PM][0.5.1][R3854][reyhard]

^ Added DVE & new dashboard textures to M1240 (basic variant only for now)
@ Fixed M1240 spare wheel TI texture
minor cfg cleanup

[3/13/2020 12:24:38 AM][0.5.1][R3853][RichardsD]

@ Maybe fixed the DVE file with a PBO Prefix

[3/12/2020 11:41:48 PM][0.5.1][R3852][RichardsD]

+ Adds DVE for Reyhard to use in various US Forces vehicles

[3/5/2020 2:31:18 PM][0.5.1][R3851][reyhard]

^ Tweaked MATV interior (unarmed variant for now)
^ Tweaked Javelin locking in top down mode

[3/1/2020 2:07:38 AM][0.5.1][R3850][RichardsD]

@ M1127 Shadow LOD fix, turret configging, model cfg editing fixes

[2/27/2020 10:14:36 PM][0.5.1][R3849][RichardsD]

@ First config of M1127 Turret

[2/27/2020 8:41:31 PM][0.5.1][R3848][reyhard]

added damage simulation for helicopters

[2/27/2020 3:13:13 PM][0.5.1][R3847][reyhard]

@ Fixed MATV gunner hatch was closed from passenger seat of M2 variant
removed obsolete bones from .rtms

[2/26/2020 9:57:06 PM][0.5.1][R3846][reyhard]

^ Increased HEAT & ATGM indirectHit range - http://feedback.rhsmods.org/view.php?id=5431

[2/26/2020 8:25:29 PM][0.5.1][R3845][reyhard]

^ Tweaked M1025 driver animation - http://feedback.rhsmods.org/view.php?id=5480
^ Tweaked C130J copilot animation - http://feedback.rhsmods.org/view.php?id=5432

[2/26/2020 6:27:51 PM][0.5.1][R3844][reyhard]

@ Fixed missing sections rpt errors for Stryker, HEMTT & FMTV

[2/26/2020 3:12:36 PM][0.5.1][R3843][reyhard]

^ Reduced Rhino durability

[2/25/2020 2:17:10 PM][0.5.1][R3842][reyhard]

cleaned up model cfg

[2/25/2020 1:44:58 PM][0.5.1][R3841][RichardsD]

+ Adds the first iteration of the M1127 Stryker RV for de-bugging purposes (Not functional)

[2/25/2020 9:23:48 AM][0.5.1][R3840][reyhard]

@ AIM-9M on AH1Z is now using correct model of AIM9M
@ Fixed M1117 hull hitpoints - http://feedback.rhsmods.org/view.php?id=5511
@ Fixed red dot on G33 with T1 combo - http://feedback.rhsmods.org/view.php?id=5518
^ Tweaked wheels hitpoints on MATV & M1117
^ Adjusted map icons for MATV
added placeholder config for M1127

[2/24/2020 8:39:34 PM][0.5.1][R3839][reyhard]

^ Added RHINO destruction particle effects
^ Added test BFT map to MATV

[2/24/2020 6:24:15 PM][0.5.1][R3838][reyhard]

@ DIRCM was affecting radar guided missiles - http://feedback.rhsmods.org/view.php?id=5502

[2/24/2020 4:00:37 PM][0.5.1][R3837][reyhard]

@ Fixed MATV turret mirrors on M240 & Mk19 variant
fire geo tweaks

[2/24/2020 2:39:10 PM][0.5.1][R3836][reyhard]

typo fix

[2/24/2020 2:00:57 PM][0.5.1][R3835][reyhard]

@ Fixed FFV restrictions on one of the M1079 seats

[2/24/2020 2:00:52 PM][0.5.1][R3834][reyhard]

@ Fixed DUKE system destruction on MATVs
^ Tweaked MATV dashboard texture
^ Changed MATV inheritance - add couple more base classes
^ Added bounding box extender to MATV to ensure proper damage detection to RHINO
@ Fixed 2nd missing UV set on MATV CROWS lenses + tweaked materials

[2/23/2020 7:32:44 PM][0.5.1][R3833][reyhard]

@ Mk19 static weapon had wrong components in fire geometry
@ Fixed MATV glass hitpoints
^ Tweaked hitpoints configuration on MATV + more tweaks to fire geometry

[2/23/2020 12:20:39 PM][0.5.1][R3832][reyhard]

^ Added proper firegeometry to MATV  - http://feedback.rhsmods.org/view.php?id=5418
^ Optimized R2T on MATV gunner positions - mirrors are no longer rendered when you are on gunner seat which result in smoother CROWS PIP screen
@ Fixed M1245 was missing MFD memory points
^ Tweaked interior glass of MATV

[2/22/2020 7:40:50 PM][0.5.1][R3831][reyhard]

^ Applied RHINO functionality to rest of MATVs

[2/22/2020 7:35:18 PM][0.5.1][R3830][reyhard]

!CLEARTEMP!
removed some obsolete files
fixed excessive uvsets in mp7 magazine model

[2/22/2020 7:04:57 PM][0.5.1][R3829][reyhard]

!CLEARTEMP!
removed unused SR25 animations which were preventing binarization with new pboproject
fixed non triangulated shadows on SR25 suppressors which were slowing down binarization

[2/14/2020 7:57:06 PM][0.5.1][R3828][reyhard]

forgot to update macros

[2/14/2020 5:01:49 PM][0.5.1][R3827][reyhard]

^ Added visible waypoints to Stryker BFT
^ Tweaked Stryker Vehicle Commander view
@ Fixed Stryker Vehicle Commander LOD in optics mode
^ Removed Stryker periscope full screen mode since periscopes can be used from vehicle interior
@ Fixed some potentially inherited MFD values for UH1Y 

[2/12/2020 2:32:39 PM][0.5.1][R3826][reyhard]

some minor fixes

[2/12/2020 8:25:41 AM][0.5.1][R3825][reyhard]

@ Fixed some z fighting in Stryker cargo compartment
@ Fixed missing damage UI in Stryker

[2/10/2020 8:55:46 PM][0.5.1][R3824][reyhard]

^ M19 is now triggered only on contact - placing mines in the middle of road will be no longer effective
^ M19 is now using additional penetrator to simulate blast damage
@ Fixed M397 bouncing mine functionality - http://feedback.rhsmods.org/view.php?id=5471
@ Removed 3UGL from M320 GL
^ Added simple Rhino system to MATV (work on M1240A1 with M2 variant only at the moment)

[2/6/2020 8:40:17 PM][0.5.1][R3823][reyhard]

@ Updated MATV CfgPatches - http://feedback.rhsmods.org/view.php?id=5420

[2/6/2020 7:04:12 PM][0.5.1][R3822][reyhard]

packing fixes

[2/6/2020 6:56:32 PM][0.5.1][R3821][reyhard]

typo for packing fix

[2/6/2020 10:00:33 AM][0.5.1][R3820][reyhard]

@ Tweaked M1126 geometric occludders for passengers - http://feedback.rhsmods.org/view.php?id=5498
^ Tweaked M150 PP effects

[1/30/2020 8:43:53 AM][0.5.1][R3819][reyhard]

fixed typo in model.cfg

[1/30/2020 8:21:15 AM][0.5.1][R3818][reyhard]

^ Tweaked M68CCO & SU-278 visuals when aiming down the sight
^ Tweaked M1240A1 weight - http://feedback.rhsmods.org/view.php?id=5441

[1/30/2020 7:27:38 AM][0.5.1][R3817][reyhard]

@ Fixed missing supply memory point on few M977A4 variants - http://feedback.rhsmods.org/view.php?id=5481

[1/30/2020 6:10:11 AM][0.5.1][R3816][reyhard]

^ Added healing attribute to M1230A1 + added few more first aid kits & medikits - http://feedback.rhsmods.org/view.php?id=5483

[1/27/2020 8:03:38 PM][0.5.1][R3815][reyhard]

fixed weapon functions

[1/27/2020 7:52:12 PM][0.5.1][R3814][reyhard]

sanitized sound configs for new pboproject version

[1/27/2020 7:47:42 AM][0.5.1][R3813][reyhard]

added OFP2Man skeleton to base model.cfg

[1/25/2020 9:07:54 PM][0.5.1][R3812][TeTeT]

Add ViV to CH-47

+ add vehicle in vehicle transport to CH-47 config

[1/25/2020 9:06:18 PM][0.5.1][R3811][TeTeT]

Add ViV to CH-47

+ add vehicle in vehicle transport to CH-47 model

[1/25/2020 7:58:07 PM][0.5.1][R3810][TeTeT]

Add ViV support for C-130

+ Vehicle in Vehicle Transport for C-130 model

[1/25/2020 7:57:38 PM][0.5.1][R3809][TeTeT]

Add ViV to C-130

+ Vehicle in Vehicle Transport for C-130 config

[1/23/2020 4:19:01 PM][0.5.1][R3808][reyhard]

^ Tweaked ERA blocks durability against HEATs

[1/23/2020 8:33:02 AM][0.5.1][R3807][reyhard]

fixed some model.cfg issues which were preventing packing with new zombified pboproject version

[1/20/2020 9:43:56 AM][0.5.1][R3806][reyhard]

removed emissive map

[1/19/2020 12:10:42 PM][0.5.1][R3805][reyhard]

!CLEARTEMP!
repacking addons with new binarize

[1/17/2020 7:00:38 AM][0.5.1][R3804][reyhard]

addon display name change

[1/14/2020 9:59:29 PM][0.5.1][R3803][PuFu]

^m9 hammer animation set to single action

[12/10/2019 10:40:37 PM][0.5.1][R3802][reyhard]

@ Added missing supply memory point to CH-53 - http://feedback.rhsmods.org/view.php?id=5402

[12/9/2019 9:47:44 PM][0.5.1][R3801][reyhard]

^ Tweaked optics post processing effects

[12/9/2019 4:05:27 PM][0.5.1][R3800][reyhard]

tweaked soldiers fire geometries

[12/3/2019 9:27:20 PM][0.5.1][R3799][wld427]

added HiddenSelectionSources support with Hatchet's permission

[12/3/2019 7:20:53 AM][0.5.1][R3798][reyhard]

Another iteration on scar recoil

[12/2/2019 8:14:58 PM][0.5.1][R3797][reyhard]

^ Tweaked SCAR-H recoil values - http://feedback.rhsmods.org/view.php?id=5387

[11/28/2019 8:52:12 PM][0.5.1][R3796][reyhard]

^ Added some workaround for SACLOS not working with AI with vanilla manual control - might be reverted if it contains some nasty side effects - http://feedback.rhsmods.org/view.php?id=5367

[11/27/2019 8:51:52 PM][0.5.1][R3795][reyhard]

another tweak

[11/27/2019 8:39:16 PM][0.5.1][R3794][reyhard]

^ Increased MP7 ammo damage output - http://feedback.rhsmods.org/view.php?id=2324
@ Fixed glove clipping on G3 uniform 

[11/25/2019 8:52:16 PM][0.5.1][R3793][reyhard]

^ Improved AGM-114 accuracy in terminal phase

[11/25/2019 4:43:16 PM][0.5.1][R3792][reyhard]

^ Tweaked GBU-12 center of mass

[11/24/2019 10:06:23 PM][0.5.1][R3791][reyhard]

^ Removed explosion sound from penetrator base class 

[11/24/2019 9:11:14 PM][0.5.1][R3790][reyhard]

@ FMTV, MATV, Cougar, Caiman, HEMTT & Stryker were missing memory points for wheel trails decals - http://feedback.rhsmods.org/view.php?id=5374
@ Fixed M1A1 driver KIA animation - http://feedback.rhsmods.org/view.php?id=5377
^ Changed M151 description from HEDP to HE - http://feedback.rhsmods.org/view.php?id=5380 

[11/23/2019 10:50:37 AM][0.5.1][R3789][reyhard]

^ Tweaked ACOG back lens triangulation - http://feedback.rhsmods.org/view.php?id=5360

[11/23/2019 8:02:37 AM][0.5.1][R3788][reyhard]

minor sound cfg tweak

[11/23/2019 7:46:04 AM][0.5.1][R3787][reyhard]

@ Fixed missing MATV KIA animation
@ Fixed wrong ammo in Mk14 Mk316 magazine - http://feedback.rhsmods.org/view.php?id=5370

[11/22/2019 5:59:04 PM][0.5.1][R3786][reyhard]

tweak to previous Himars commit

[11/22/2019 8:37:16 AM][0.5.1][R3785][reyhard]

@ HIMARS launcher hitpoint & firegeometry fixes - http://feedback.rhsmods.org/view.php?id=5364

[11/21/2019 3:54:50 PM][0.5.1][R3784][reyhard]

^ Added scripted workaround for planes not willing to engage ground targets if they have WSO

[11/20/2019 10:46:59 PM][0.5.0][R3783][Soul_Assassin]

[0.5.1] Version bump

[11/20/2019 6:53:36 PM][0.5.0][R3782][reyhard]

added new variant of M2 ammo with increased camshake for planes

[11/20/2019 6:40:37 PM][0.5.0][R3781][reyhard]

oops, revert

[11/20/2019 6:29:49 PM][0.5.0][R3780][reyhard]

^ Tweaked water resistance settings of UH60M & CH-47 - http://feedback.rhsmods.org/view.php?id=5359

[11/20/2019 12:37:44 PM][0.5.0][R3779][reyhard]

!CLEARTEMP!
@ Fixed some missing texture error with MATV

[11/19/2019 10:44:21 PM][0.5.0][R3778][reyhard]

^ Added LOAL mode to DAGR
^ DAGR was missing cam shake when being fired
^ Tweaked cam shake settings across USAF vehicles

[11/19/2019 4:11:25 PM][0.5.0][R3777][reyhard]

@ Fixed duplicated hitpoints .rpt errors with static weapons
^ Tweaked attenuation settings of static weapons

[11/16/2019 1:22:50 PM][0.5.0][R3776][reyhard]

minor fixes to sound config

[11/16/2019 10:30:42 AM][0.5.0][R3775][reyhard]

^ Tweaked AH-64 interior light
^ Tweaked attenuation values on CROWS turrets
^ Added experimental interior shoting sounds to some vehicle mounted weapons

[11/10/2019 10:09:01 PM][0.5.0][R3774][reyhard]

@ Fixed AOR2 texture - http://feedback.rhsmods.org/view.php?id=5338

[11/10/2019 7:01:11 PM][0.5.0][R3773][reyhard]

^ Unified CROWS zoom levels - http://feedback.rhsmods.org/view.php?id=5349
^ Converted CROWS screens to MFD tech
@ Fixed SMAW missile trail cfg - http://feedback.rhsmods.org/view.php?id=5348
^ Updated HUD horizon on A10A & F22A
@ Pass with CheckAll o2script - fixed otocHlaven/OtocHlaven on MATV
^ Enabled interior cargo light in Stryker

[11/6/2019 9:01:17 PM][0.5.0][R3772][da12thMonkey]

@ Some UH-60 variants could carry more occupants than they should

[11/5/2019 1:51:43 PM][0.5.0][R3771][reyhard]

^ Added custom recoil to M590 shotgun

[10/23/2019 4:07:42 PM][0.5.0][R3770][da12thMonkey]

MATV
Adjustments to speedometer display
Damage .rvmat for SOF rear end

[10/22/2019 2:17:30 AM][0.5.0][R3769][ballistic09]

Removed Arma 3 vanilla gear from M-ATV transport inventory

[10/21/2019 9:43:59 PM][0.5.0][R3768][da12thMonkey]

@ Missing door sound error on MRAPs when running USAF standalone
Some MATV crew anim adjustments 

[10/18/2019 6:28:29 PM][0.5.0][R3767][reyhard]

^ Added ability to manually reload M2, M240 & Mk19 on vehicle mounted weapons like M113 or MATVs by pressing reload key ("R")

[10/17/2019 8:47:36 AM][0.5.0][R3766][reyhard]

tweaked laser designator cfg

[10/17/2019 8:10:59 AM][0.5.0][R3765][reyhard]

tweaked laser designator cfg

[10/17/2019 7:46:02 AM][0.5.0][R3764][reyhard]

tweaked laser designator cfg

[10/17/2019 7:28:40 AM][0.5.0][R3763][reyhard]

^ Added AI friendly laser designators to helicopters

[10/16/2019 2:18:17 PM][0.5.0][R3762][da12thMonkey]

Adjust IR sensor on US helicopters

[10/10/2019 5:52:11 PM][0.5.0][R3761][da12thMonkey]

axis of M1245's CROWS direction indicator wasn't aligned properly

[10/4/2019 7:45:21 AM][0.5.0][R3760][reyhard]

removed more debug code

[10/3/2019 12:42:09 PM][0.5.0][R3759][reyhard]

@ Fixed CH47 RTD ground contact points - http://feedback.rhsmods.org/view.php?id=5278
added rtd ground contact points to edit LOD 10 - they can be exported via o2 script

[10/2/2019 8:47:19 PM][0.5.0][R3758][reyhard]

^ Tweaked LR AA missiles behavior - http://feedback.rhsmods.org/view.php?id=5284

[10/1/2019 8:26:07 PM][0.5.0][R3757][reyhard]

@ Changed a bit MATV armor - http://feedback.rhsmods.org/view.php?id=5301

[9/28/2019 6:59:22 PM][0.5.0][R3756][RichardsD]

@ Added olive texture for M-ATV

[9/28/2019 12:39:44 PM][0.5.0][R3755][reyhard]

added some more mfd icons for A29

[9/27/2019 10:44:02 AM][0.5.0][R3754][reyhard]

added laser designator working with ai

[9/27/2019 6:49:33 AM][0.5.0][R3753][reyhard]

@ Removed wrong config overwrites in USAF mod - http://feedback.rhsmods.org/view.php?id=5298

[9/25/2019 8:02:02 PM][0.5.0][R3752][reyhard]

^ Added workaround for AI not being able to eject from planes with ejecting seats

[9/24/2019 5:40:18 PM][0.5.0][R3751][reyhard]

@ Fixed MATV OGPK M2 turret loadout - http://feedback.rhsmods.org/view.php?id=5293

[9/24/2019 6:23:02 AM][0.5.0][R3750][reyhard]

inheritance check

[9/23/2019 1:56:15 PM][0.5.0][R3749][reyhard]

^ Tweaked twin M3 HMG configuration

[9/22/2019 8:38:11 PM][0.5.0][R3748][reyhard]

!CLEARTEMP!
work on A-29 weapon MFD page
committed missing MZRZ rvmat

[9/21/2019 9:32:33 AM][0.5.0][R3747][reyhard]

^ Tweaked shotgun reload script
^ Tweaked spalling properties
^ Added additional optics components to interior of Bradley
@ Fixed M2A2 components (regenerated then)

[9/20/2019 8:32:30 PM][0.5.0][R3746][reyhard]

@ Fixed M781 Practice round was missing in magazine well - http://feedback.rhsmods.org/view.php?id=5277

[9/19/2019 5:06:56 PM][0.5.0][R3745][reyhard]

firedFCS sync with AFRF

[9/18/2019 7:17:36 PM][0.5.0][R3744][da12thMonkey]

MATV:
Restructured class tree
Mk19 CROWS vehicle had M2 HMG visible in its bottom LOD
Added SOCOM Mk19 CROWS vehicle
Set up Right FFV position on SOCOM vehicles
edPrev images for SOCOM vehicles
Reverted randomisation of ammo hamper on regular SOCOM vehicles (blocks CROWS gunner view to the rear of the vehicle, so figure it shouldn't appear at random)

[9/18/2019 6:54:49 PM][0.5.0][R3743][reyhard]

!CLEARTEMP!
muzzle flash repack

[9/17/2019 10:42:20 PM][0.5.0][R3742][da12thMonkey]

SOF MATV:
Work on Left FFV seat positioning, animation and turn in/out functionality, ability to use AT launchers etc.
CROWS ammo hamper is now randomised on the desert-painted vehicle (still always appears by default on Deployed camo vehicle)
Fixed there was a duplicated spare tyre in one of the View LODs
Fixed: Rear door animation now works when getting in/out of FFV turret
Fixed: getting in the rear passenger doors would put you in the seat on the opposite side of the vehicle

Hopefully sort out the Right FFV seat tomorrow!

[9/16/2019 10:22:21 PM][0.5.0][R3741][da12thMonkey]

MATV's 4th antenna was using the wrong axis set

[9/16/2019 6:21:13 PM][0.5.0][R3740][da12thMonkey]

SOCOM MATV
Section reduction and shadow LOD improvement
Fixed non-convenxities in viewGeo and fireGeo
Fixed inability to apply different textures in garage when selected (missing .paa suffix in file path)


[9/15/2019 7:48:14 PM][0.5.0][R3739][RichardsD]

+ Adds M1245 MATV SOF Version. 

[9/15/2019 2:55:46 AM][0.5.0][R3738][RichardsD]

@ Adds 2x more string entries for MATV names

[9/14/2019 7:42:14 PM][0.5.0][R3737][da12thMonkey]

^ rhs_mag_FFAR_7_USAF (Green LAU-68 rocket pods for fixed-wing aircraft) now fires old-style 70mm FFAR rockets, more suited to the classname 

(Note FFAR is functionally identical to the Hydra rockets carried in the new LAU-131 pods - differences are cosmetic)

Some additional LAU-61 FFAR pods for fixed wing aircraft (only accessible with setPylonLoadout for now, A-10 doesn't seem to carry 19-shot launchers)
Changed pylon name for new LAU-131 Hydra launchers to allow separation of legacy and modern 70mm rocket types

[9/14/2019 1:19:51 PM][0.5.0][R3736][da12thMonkey]

^ Changed displaynames for helicopter rockets referencing "FFAR" to "Hydra" since FFAR is an older generation of rocket

Adjusted classname of newly added grey LAU-131 pods, to remove FFAR reference

[9/14/2019 11:49:55 AM][0.5.0][R3735][da12thMonkey]

M257 tweaks:
Removed additional burst firemodes (no point firing multiple flares so close together, and keeps weapon switching UI cleaner)
Attempt at Tweaking AI firemode
Adjusted airfriction so that rocket reaches correct 3km range when the 9 second delay fuse ignites the flare.

[9/14/2019 12:41:17 AM][0.5.0][R3734][da12thMonkey]

+ M257 Hydra 70mm ILLUM rocket. Flare ignites after ~10 seconds of flight: approx 3km-4km ahead of launch point. Provides up to 120s of illumination.

[9/13/2019 1:13:57 PM][0.5.0][R3733][da12thMonkey]

Trimmed MATV `karoserie` hitpoints that were outside the fireGeo

[9/13/2019 9:58:26 AM][0.5.0][R3732][da12thMonkey]

Converted Hellfire and DAGR launcher rails to be proxy-based
+ Extra Hellfire and DAGR magazines positioned for fixed-wing aircraft (A-29 etc)

[9/13/2019 2:13:25 AM][0.5.0][R3731][ballistic09]

^ Replaced all 40mm HE with HEDP
^ Switched regular US Army desert units to OEF-CP ACUs

[9/12/2019 11:46:10 PM][0.5.0][R3730][da12thMonkey]

Converted US dynamic loadouts rocket pods to be proxy-based
Triple-LAU rocket rack for A-10

[9/12/2019 7:59:43 PM][0.5.0][R3729][da12thMonkey]

^ Re-equipped A-10A with USAF gray LAU-131 rocket pods (legacy green ones are still available, renamed as LAU-68 but retain the extant 'rhs_mag_FFAR_7_USAF' classname)

Added a model for the extended LAU-131A/A LAU-68F/A type FFAR pod, should we want to add APKWS-II in future
The currently unused M264 smoke rocket had incorrect texture paths

[9/12/2019 3:01:40 PM][0.5.0][R3728][reyhard]

^ Changed M3 HMG name

[9/11/2019 11:32:43 PM][0.5.0][R3727][ballistic09]

some cleanup of mags for Mk.19 equipped vehicles

[9/11/2019 10:02:55 PM][0.5.0][R3726][da12thMonkey]

^ Made aiming cursor availability on mounted M240s, consistent with other MGs
^ M240H now ejects appropriately sized cartridges (see GREF UH-1H)
Removed UI aiming cursor from Super Tucano's .50 cal MGs

[9/11/2019 9:34:41 PM][0.5.0][R3725][reyhard]

@ Fixed some accessories icons - http://feedback.rhsmods.org/view.php?id=5265

[9/11/2019 7:42:54 PM][0.5.0][R3724][da12thMonkey]

Applied decal .rvmat to MATV door markings

[9/11/2019 2:56:39 PM][0.5.0][R3723][reyhard]

minor code cleanup

[9/11/2019 2:22:04 PM][0.5.0][R3722][da12thMonkey]

MATV fix view and fire geo non-convexities

[9/11/2019 12:00:11 PM][0.5.0][R3721][da12thMonkey]

MATV
Fixed some M240 bullets not following turret in gunner view LOD
Fixed brake lights were always on (had overlapping section "camo")

[9/11/2019 12:06:26 AM][0.5.0][R3720][da12thMonkey]

MATV:
Fixed spare wheel had wrong selection in LODs 3 and 4
Fixed M240 feed cover rotated around wrong axis
Fixed antenna bases
Fixed flag proxy position
Stopped Mk.64 mount's ammo hamper moving with the gun on M240 version
Improved shadow LODs

[9/10/2019 7:12:24 PM][0.5.0][R3719][reyhard]

@ M240 was missing safe mode switching sound - http://feedback.rhsmods.org/view.php?id=5260

[9/9/2019 7:48:48 PM][0.5.0][R3718][da12thMonkey]

@ 20 round M196 tracer mag had incorrect displayname string

[9/9/2019 6:00:30 PM][0.5.0][R3717][da12thMonkey]

Eventhandler for turret accessory randomisation

[9/9/2019 5:05:13 PM][0.5.0][R3716][da12thMonkey]

Quick MATV driver anim with hands on the wheel

[9/9/2019 3:22:42 PM][0.5.0][R3715][da12thMonkey]

Removed duped gunner proxies from M240 MATV
Removed duped flag proxies from OGPK MATVs
M240 gunner anim to fit MATV
Fixed turn-out state at vehicle init

[9/9/2019 2:39:04 PM][0.5.0][R3714][reyhard]

added magic rtm

[9/9/2019 2:02:45 PM][0.5.0][R3713][reyhard]

@ Fixed TOW missiles being unresponsive if AI is being ordered to fire them by player commander - http://feedback.rhsmods.org/view.php?id=5252
^ Tweaked MATV physx 

[9/9/2019 7:26:09 AM][0.5.0][R3712][reyhard]

updated uniform icons

[9/8/2019 6:17:58 PM][0.5.0][R3711][da12thMonkey]

MATV edprev and garage images
Ongoing shadow LOD improvement

[9/8/2019 12:17:39 PM][0.5.0][R3710][da12thMonkey]

M-ATV section count reduction
Hopefully fixed M240 turret inheritance
Simplified inheritance tree of ingame classes

[9/8/2019 12:03:54 AM][0.5.0][R3709][RichardsD]

+ Adds the initial commit of the M-ATV MRAP, M1240 with M2, Mk. 19, CROWS, and M240. 
^ Notes: M240 needs fixing, needs Phys-x profile, needs unit icons and editor preview photos

[9/6/2019 4:38:32 PM][0.5.0][R3708][da12thMonkey]

Applied _as map and .rvmat changes to ABU boots
Adjusted sage colour of boot

[9/5/2019 10:24:50 PM][0.5.0][R3707][da12thMonkey]

Tweak ACU boot colour and spec/gloss

[9/5/2019 3:34:33 PM][0.5.0][R3706][RichardsD]

@ Adds additional M-ATV Commms equipment to commskit file

[9/4/2019 4:40:01 PM][0.5.0][R3705][da12thMonkey]

Add extra dirt to ACU textures around knees, forearms, arse etc.

[9/4/2019 1:54:19 PM][0.5.0][R3704][da12thMonkey]

More ACU texture adjustments:
Added pattern breaks on reinforcement panels
Toned down diffuse highlights on cloth wrinkles that were making the fabric seem a bit satin

[9/3/2019 5:29:13 PM][0.5.0][R3703][da12thMonkey]

derp

[9/3/2019 10:11:06 AM][0.5.0][R3702][da12thMonkey]

Corrected ACU under shirt colour (UCP sand, OCP/OEFCP Tan 499)
Adjusted saturation of OCP-D brown
Basic _as map for Belleville boots. Generated from LP geometry, with normal map detail, applied to _co and adjusted .rvmat
Added path to _as map in wound .rvmats

[9/3/2019 6:33:38 AM][0.5.0][R3701][reyhard]

@ Fixed missing hands weighting in 3rd resolution LOD of ACU
^ Added additional resolution LOD to ACU

[9/3/2019 1:17:53 AM][0.5.0][R3700][da12thMonkey]

Interim ACU variant textures

[9/2/2019 6:09:00 PM][0.5.0][R3699][da12thMonkey]

Force rebuild of ACU after rvmat update

[9/2/2019 2:57:10 PM][0.5.0][R3698][RichardsD]

@ Changed M-ATV string entries

[9/2/2019 1:43:29 PM][0.5.0][R3697][da12thMonkey]

Basic ACU _as map. Generated from LP geometry, with normal map detail

[9/2/2019 12:32:13 PM][0.5.0][R3696][reyhard]

folded mag sync confg

[9/1/2019 11:07:17 PM][0.5.0][R3695][RichardsD]

^ M-ATV String table entries

[9/1/2019 9:12:43 PM][0.5.0][R3694][RichardsD]

@ Fixes ammo crates on top of M1239 AUV Mk. 19
@ Fixes window glass on M1238A1.p3d
@ Adds mirror glass to LOD 0/1/2/3/4 of the M1239 AUV

[9/1/2019 12:21:14 PM][0.5.0][R3693][reyhard]

^ Tweaks to SCAR folding initialization 

[8/31/2019 2:56:30 PM][0.5.0][R3692][reyhard]

^ Adjusted M2 CROWS zeroing settings to be consistent with LRF + tweaked manual steps on Caiman & RG33 - http://feedback.rhsmods.org/view.php?id=4977

[8/31/2019 2:20:35 PM][0.5.0][R3691][reyhard]

@ Fixed some errors with folding script if weapon was without magazine - http://feedback.rhsmods.org/view.php?id=5037

[8/31/2019 12:03:23 PM][0.5.0][R3690][reyhard]

^ Added recoils for folded SCARs

[8/29/2019 8:46:54 PM][0.5.0][R3689][reyhard]

removed six12 for now - needs some fixes first

[8/29/2019 8:42:45 PM][0.5.0][R3688][reyhard]

,

[8/29/2019 8:34:34 PM][0.5.0][R3687][reyhard]

^ Added folding animations to Mk17

[8/29/2019 2:25:12 PM][0.5.0][R3686][reyhard]

added missing macro

[8/29/2019 1:17:42 PM][0.5.0][R3685][reyhard]

added new folding parameters to SCAR
added test SIX-12 variant of M4A1

[8/28/2019 3:01:02 PM][0.5.0][R3684][reyhard]

updated folding script

[8/26/2019 2:51:47 PM][0.5.0][R3683][reyhard]

updated folding script

[8/26/2019 12:41:11 PM][0.5.0][R3682][reyhard]

^ Added geometric occluders to Stryker interior
@ Fixed Stryker Air Guards had extra reflectors (searchlights)

[8/26/2019 1:22:16 AM][0.5.0][R3681][gurdy]

^ matched woodland FMTV wheel color to current woodland textures

[8/25/2019 9:12:43 PM][0.5.0][R3680][reyhard]

^ Updated folding script with support for custom folding gestures ("rhs_fold_anim" param)

[8/24/2019 6:39:58 PM][0.5.0][R3679][reyhard]

^ Added working periscopes to Stryker Vehicle Commander
^ Improved Stryker BFT MFD
@ Fixed some Stryker hatches related issues

[8/23/2019 8:59:15 PM][0.5.0][R3678][reyhard]

^ Improved FCBC2 symbology on Stryker MFD
^ Added new VG icons for M1025s

[8/23/2019 5:47:40 PM][0.5.0][R3677][reyhard]

^ Optimized interior light toggle function
@ Fixed some shotgun reload function errors - http://feedback.rhsmods.org/view.php?id=5212
^ Stryker config clean up

[8/23/2019 2:33:54 PM][0.5.0][R3676][reyhard]

added inventory icons for new uniform variants

[8/23/2019 11:40:45 AM][0.5.0][R3675][reyhard]

^ Lowered M1 Abrams interior engine sounds - http://feedback.rhsmods.org/view.php?id=5189
^ Added death animations to Stryker crew
^ Tweaked Stryker airman guards position to reduce clipping with other passengers
@ Fixed Stryker rear wheels destruction animation
@ Fixed Stryker passenger seats (#1 was not accessible)

[8/22/2019 9:58:18 PM][0.5.0][R3674][reyhard]

^ Added mirror folding VG attribute to Stryker
attempt at fixing Stryker death anims

[8/22/2019 12:26:52 PM][0.5.0][R3673][reyhard]

^ Tweaked Stryker BFT

[8/21/2019 8:56:27 AM][0.5.0][R3672][reyhard]

^ Added 2 IHADSS helmets to AH64 cargo & removed parachutes from it - http://feedback.rhsmods.org/view.php?id=4530

[8/18/2019 10:31:21 PM][0.5.0][R3671][ballistic09]

Also gfelton's UCP-D textures for ACU

[8/18/2019 8:55:53 PM][0.5.0][R3670][ballistic09]

Initial WIP commit of gfelton's ACU textures (UCP, OEF-CP, & OCP) and sage boot textures for ABU

[8/17/2019 10:44:37 PM][0.5.0][R3669][RichardsD]

+ Adds SOCOM AUV and SOCOM ASV Ammmo Boxes to all variants as a configurable option

[8/15/2019 2:29:33 PM][0.5.0][R3668][da12thMonkey]

Adding M3W to heavyweapons, for use with GREF Tucano

[8/12/2019 10:15:51 AM][0.5.0][R3667][reyhard]

@ Fixed C-130J not flying in 3den editor - http://feedback.rhsmods.org/view.php?id=5182
@ Fixed CH-47 & CH-53 downwash effect + improved buoyancy

[8/11/2019 11:31:52 PM][0.4.9][R3666][Soul_Assassin]

[0.5.0] Version bump

[8/11/2019 7:58:04 PM][0.4.9][R3665][reyhard]



[8/11/2019 7:53:26 PM][0.4.9][R3664][reyhard]



[8/11/2019 6:07:22 PM][0.4.9][R3663][reyhard]

fixed some rpt errors related to stryker anims (death anims are still missing)

[8/8/2019 6:58:38 PM][0.4.9][R3662][da12thMonkey]

NVG section, UV and properties cleanup
PVS-14 had Glock's TI map applied
Removed TI map from M40 mags that was making them glow on SPC vest

[8/8/2019 11:53:47 AM][0.4.9][R3661][reyhard]

@ Fixed vehclass typo in MRZR cfg

[8/7/2019 8:50:45 PM][0.4.9][R3660][da12thMonkey]

TI textures for US vests

[8/7/2019 8:50:07 AM][0.4.9][R3659][reyhard]

!CLEARTEMP!
ALQ 131 ti tex tweak

[8/6/2019 12:20:44 PM][0.4.9][R3658][da12thMonkey]

Shemagh and Oakley SI goggles TI

[8/6/2019 8:10:25 AM][0.4.9][R3657][reyhard]

!CLEARTEMP!
^ Tweaked TI materials of various weapon accessories
^ Added second uvset to M8541 for scope selection

[8/5/2019 7:54:43 PM][0.4.9][R3656][reyhard]

added damage selection to more LODs

[8/5/2019 7:44:27 PM][0.4.9][R3655][reyhard]

!CLEARTEMP!
^ Added damage & destruction materials to M252 mortar
@ RPT errors fixes related to M252
added some TI material to surefire muzzle brakes
added missing ti texture

[8/5/2019 6:18:11 PM][0.4.9][R3654][da12thMonkey]

Fixed removal of camonet animation for SOCOM FMTVs (misspelled animation classname)

[8/5/2019 5:13:31 PM][0.4.9][R3653][da12thMonkey]

Some M1025 decal paths were wrong

[8/5/2019 5:02:50 PM][0.4.9][R3652][da12thMonkey]

Hat TI maps

[8/5/2019 12:20:08 PM][0.4.9][R3651][da12thMonkey]

^ TI textures for crew helmets (ACVC, HGU-56)

[8/5/2019 10:54:48 AM][0.4.9][R3650][reyhard]

^ Added procedural TI textures to Stinger pod

[8/4/2019 9:22:11 PM][0.4.9][R3649][ballistic09]

!CLEARTEMP!
thermal textures for ABU boots

[8/4/2019 9:03:23 PM][0.4.9][R3648][ballistic09]

@ removed extra space in HEMMT displayname string

[8/4/2019 8:35:09 PM][0.4.9][R3647][ballistic09]

fixed some bolts missing from Stryker tire selections

[8/3/2019 2:46:57 PM][0.4.9][R3646][reyhard]

added rvmat to last lod of M252

[8/3/2019 2:43:19 PM][0.4.9][R3645][reyhard]

+ Added TI map to M252 mortar

[8/3/2019 2:23:24 PM][0.4.9][R3644][reyhard]

!CLEARTEMP!
+ Added TI maps to AH1Z, UH1Y & CH-53
small tweaks to usaf air weapons - thermals were heated up by i.e. autocannon fire

[8/3/2019 12:46:24 PM][0.4.9][R3643][reyhard]

+ Added TI textures to F-22A
^ Tweaked F22 decals material 

[8/3/2019 11:55:51 AM][0.4.9][R3642][da12thMonkey]

Regenerated TI map for LWH accessories (goggles)

[8/3/2019 11:53:13 AM][0.4.9][R3641][reyhard]

!CLEARTEMP!
+ Added M1025 TI textures

[8/3/2019 10:12:32 AM][0.4.9][R3640][da12thMonkey]

^ Infantry/SOF helmet TI textures

[8/2/2019 10:10:11 PM][0.4.9][R3639][reyhard]

!CLEARTEMP!
addong repacking

[8/2/2019 9:21:11 PM][0.4.9][R3638][reyhard]

@ Another fix for HEMTT exhaust particles

[8/2/2019 9:17:06 PM][0.4.9][R3637][reyhard]

+ Added TI textures to Caiman, FMTV, HIMARS, HEMTT, RG33 & MRZR
@ Fixed open shadows in some FMTV models

[8/2/2019 6:09:44 PM][0.4.9][R3636][da12thMonkey]

^ FROG uniform TI texture

[8/2/2019 5:47:30 PM][0.4.9][R3635][da12thMonkey]

^ TI texture for G3 uniform

[8/2/2019 1:27:01 PM][0.4.9][R3634][reyhard]

^ Adjusted static weapons TI textures
added placeholder TI textures to F-22

[8/2/2019 11:55:58 AM][0.4.9][R3633][reyhard]

@ Fixed HEMTT exhaust particle effects
^ Added decal RVMAT to M1025s
@ Fixed USAF air weapons TI textures
some minor TI tweaks

[8/2/2019 10:38:53 AM][0.4.9][R3632][reyhard]

@ Fixed some of the M1232 & M1237 vehicles were missing rvmats on certain selections
^ Added decal RVMAT to M1232 & M1237

[8/2/2019 9:25:45 AM][0.4.9][R3631][da12thMonkey]

^ TI textures for ACU

[8/2/2019 9:12:42 AM][0.4.9][R3630][reyhard]

!CLEARTEMP!
repacking addons

[8/2/2019 3:48:24 AM][0.4.9][R3629][ballistic09]

^ Removed redundant/different displayname definitions from desert HEMTT classes
Wound mats and thermal textures for ABU & BDU, courtesy of DeltaHawk

!CLEARTEMP!

[8/1/2019 8:37:05 PM][0.4.9][R3628][reyhard]

^ Added HEMTT TI textures

[8/1/2019 2:51:08 PM][0.4.9][R3627][reyhard]

added placeholder TI textures to M1025

[8/1/2019 2:40:02 PM][0.4.9][R3626][reyhard]

^ Tweaked interior light toggle function
^ Added working fire geometry for MCTAGS turret
^ Added interior light to Stryker
^ Added basic 2nd res LOD to Stryker
@ Fixed spare wheels TI on RG33L & SOCOMUAV
@ Fixed RG33 & SOCOMUAV TI textures being super bright in TI when gun was fired
added placeholder TI textures for RG-33L & MRZR


[7/31/2019 9:00:08 PM][0.4.9][R3625][da12thMonkey]

Basic Stryker ICV editor groups (9 dismount Squad and 5 dismount Wpn Squad)

[7/31/2019 8:04:07 PM][0.4.9][R3624][da12thMonkey]

edPrev images for Stryker
Switched two of the Javelins in Stryker's stowed equipment, for M136s

[7/31/2019 3:30:22 PM][0.4.9][R3623][reyhard]

added placeholder TI textures for HEMTT & FMTV

[7/31/2019 3:21:43 PM][0.4.9][R3622][da12thMonkey]

Fixed missing edPrev image for M49A1 tripwire

[7/31/2019 3:21:36 PM][0.4.9][R3621][reyhard]

^ Added new fire geometry to Cougars - http://feedback.rhsmods.org/view.php?id=4991
^ Tweaked Cougars glass
^ Tweaked Cougar suspension animation
^ Added placeholder TI Textures to Cougar
^ Tweaked M113 wheels TI

[7/30/2019 5:39:30 PM][0.4.9][R3620][reyhard]

^ Improved Stryker TI textures

[7/30/2019 7:48:22 AM][0.4.9][R3619][reyhard]

^ Unified M1A1FEP & HC hitpoints + fixed engine smoke - http://feedback.rhsmods.org/view.php?id=5162

[7/29/2019 9:17:30 PM][0.4.9][R3618][reyhard]

work on Stryker thermal textures

[7/29/2019 3:03:34 PM][0.4.9][R3617][reyhard]

^ Tweaked M1117 wheels TI texture
^ Added separate rvmat for USAF vehicles spare wheels
^ Added wheel TI texture to M1238A1

[7/29/2019 1:44:57 PM][0.4.9][R3616][da12thMonkey]

Macro'd magazine lists where classes will be shared between equivalent BI and CBA magazineWells, for easier updating

[7/28/2019 8:20:42 AM][0.4.9][R3615][reyhard]

^ Added TI textures for plenty of US vehicles & fixed some TI textures which were using placeholder abrams hull texture. Note that those vehicles are still missing engine heat textures

[7/27/2019 11:41:31 AM][0.4.9][R3614][da12thMonkey]

^ Configured all USAF aircraft to carry realistic amounts of of flares+chaff, which can be managed via Dynamic Loadouts/Pylon Settings (e.g. can load only flares for maximal amount of CM releases, but will be ineffective against radar-based threats)

F-22 countermeasures

[7/26/2019 6:18:27 PM][0.4.9][R3613][da12thMonkey]

C-130 countermeasures config

[7/26/2019 1:22:47 PM][0.4.9][R3612][da12thMonkey]

Configured countermeasures pylon on CH-47

^ Added countermeasure dispensers to CH-47F model (hides when countermeasures are removed via Dynamic Loadouts/Pylons settings)

[7/26/2019 10:18:19 AM][0.4.9][R3611][da12thMonkey]

Dynamic countermeasures work for additional US aircraft (UH-1Y, UH-60, CH-53, A-10A)

[7/26/2019 5:31:51 AM][0.4.9][R3610][da12thMonkey]

Reverting ability to retexture BDU

[7/26/2019 12:51:23 AM][0.4.9][R3609][Stagler]

^ Added Wound textures and rvmats for ABU
^ Added Wound textures and rvmats for BDU
^ Added BDU M81 texture matching existing RHS M81 textures 
^ Added provision for hiddenselections in model.cfg.

[7/22/2019 8:41:24 PM][0.4.9][R3608][da12thMonkey]

Removed unnecessary pfx class

[7/22/2019 8:27:32 PM][0.4.9][R3607][reyhard]

removed debug

[7/22/2019 8:15:23 PM][0.4.9][R3606][da12thMonkey]

US Dynamic Loadouts flare/chaff test platforms: AH-64D, AH-1Z

[7/21/2019 7:40:01 AM][0.4.9][R3605][reyhard]

^ M203, M320 & M32 are using sound set firing sounds

[7/21/2019 7:38:35 AM][0.4.9][R3604][reyhard]

@ Fixed ghost LOD on M4 with M320

[7/21/2019 6:20:33 AM][0.4.9][R3603][reyhard]

^ Disabled handheld compass in AH-64 & AH-1Z cockpit

[7/18/2019 8:21:47 PM][0.4.9][R3602][ballistic09]

Randomized OGPK turret configurations
Fixed missing RG-33L USMC decal
^ Mk.19 40mm mag displaynameshort
configed some M430A1 ammo and mags for potential future use...

[7/7/2019 5:27:10 PM][0.4.9][R3601][jastreb]

^ increased permanent muzzle climb for MK17

[7/6/2019 1:21:46 PM][0.4.9][R3600][da12thMonkey]

@ A-10A's cockpit shadow become non-closed when assigning different texture/materials the 'camo2' hiddenSelection

A-10-associated p3ds, UV set and named selections cleanup by O2script

[7/3/2019 3:46:18 AM][0.4.9][R3599][ballistic09]

Fixed M240G inheriting wrong hiddenSelectionsTextures from M240B
Fixed/removed wrong/needless copy-pasted initSpeed definitions from Mk.17 classes
Oriented M829 sabot petal model to correct direction

[6/22/2019 6:08:41 PM][0.4.9][R3598][reyhard]

removed doomslug behavior from standard buckshot after change to submunition

[6/22/2019 5:31:43 PM][0.4.9][R3597][reyhard]

^ Tweaked 12GA models

[6/22/2019 4:20:25 PM][0.4.9][R3596][reyhard]

@ Short M590 shotgun was missing magazine proxy

[6/21/2019 9:48:38 AM][0.4.9][R3595][reyhard]

tweaked buckshot

[6/20/2019 9:24:36 PM][0.4.9][R3594][reyhard]

^ Converted M590 buckshot to shotSubmunitions to be more in line with new vanilla shotguns. Air friction is now working with pellets so beware that ballistics are quite different to what it used to be

[6/20/2019 5:17:43 PM][0.4.9][R3593][reyhard]

^ Updated USAF load order in order to fix compatibility with new, devbranch radio protocols

[6/5/2019 12:38:10 PM][0.4.9][R3592][da12thMonkey]

@ M136 and SMAW  launchers are no longer accepted under Code Duello (Duel Purpose -> Dual Purpose)

[6/1/2019 12:12:31 PM][0.4.9][R3591][da12thMonkey]

^ Underbarrel proxy slot for M240 (part of proof-of-concept testing, but might find uses in future)

[5/30/2019 5:50:37 PM][0.4.9][R3590][ballistic09]

@ Typo in ABU and BDU displayName

[5/30/2019 2:27:39 AM][0.4.9][R3589][ballistic09]

gurdy's improved HIDF lowland-ERDL textures for BDU

[5/22/2019 8:50:07 PM][0.4.9][R3588][da12thMonkey]

Fixed some non-triangulated faces in 40mm grenade secondary shadow LODs

[5/16/2019 8:31:12 PM][0.4.9][R3587][reyhard]

added placeholder mag proxy for m441 grenade

[5/16/2019 10:02:14 AM][0.4.9][R3586][da12thMonkey]

Wrong inventory pic path for Standard-length US SCAR when folded

[5/13/2019 6:31:56 PM][0.4.9][R3585][ballistic09]

Corrected scale and texture paths of M829 sabot petals

[5/12/2019 1:00:34 PM][0.4.9][R3584][da12thMonkey]

Some laser/lights didn't have their correct inventory icons

[5/11/2019 8:26:18 PM][0.4.9][R3583][kllrt]

Fixed path to TI texture

[5/11/2019 8:22:28 PM][0.4.9][R3582][kllrt]

Added M829A3 petal model+textures

[5/10/2019 10:47:31 PM][0.4.9][R3581][da12thMonkey]

Adding Mk316 mags to Arsenal box and Editor items

[5/10/2019 10:37:18 PM][0.4.9][R3580][da12thMonkey]

+ Mk316 Mod 0 Special Ball (HPBT) ammunition for SR-25 and Mk17. Generally similar to M118 Special Ball, but slightly faster `initspeed` and reduced `visibleFire`

Adjusted muzzle velocity (`initspeed`) of SCAR magazines to more realistic values

[5/9/2019 9:33:01 PM][0.4.9][R3579][da12thMonkey]

M14 mag proxy `camo` selection

[5/4/2019 8:11:09 PM][0.4.9][R3578][da12thMonkey]

CBA mag wells for MAAWS and SMAW

[5/3/2019 6:32:41 PM][0.4.9][R3577][da12thMonkey]

@ Typo in M249 CfgMagazineWells classname
^ Cleared out BI magazine classnames from CfgMagazineWells where they are are now defined in vanilla Arma 3
^ Many USAF weapons will now accept magazines compatible with CBA JAM
^ Configured M14 EBR-RI for proxy magazines and `manazineWell[]`
^ Adjusted M14 EBR-RI handAnim and nudged laser/light proxy forward a little

[5/2/2019 7:37:24 PM][0.4.9][R3576][reyhard]

hm

[5/2/2019 7:20:55 PM][0.4.9][R3575][reyhard]

^ Improved ammo event handler inheritance

[4/29/2019 12:18:46 PM][0.4.9][R3574][reyhard]

^ Added new 5.56x45mm cartridge

[4/28/2019 9:42:58 AM][0.4.9][R3573][reyhard]

added placeholder for 120mm petal

[4/19/2019 5:11:39 PM][0.4.9][R3572][reyhard]

added test UI for setting BFT map scale in Stryker

[4/19/2019 4:52:27 PM][0.4.9][R3571][reyhard]

^ Added data link reporting of own position to vehicles with blue force tracker
^ Improved Stryker BFT map 

[4/17/2019 10:15:55 AM][0.4.9][R3570][da12thMonkey]

^ Optics destruction visuals for M1 Abrams

[4/16/2019 9:28:44 PM][0.4.9][R3569][reyhard]

^ Added data link sensor to Stryker in order to simulate Blue Force Tracker
^ Added test BFT MFD panel to Stryker

[4/16/2019 12:40:08 PM][0.4.9][R3568][reyhard]

added instant position update to stryker BFT moving map

[4/16/2019 8:55:44 AM][0.4.9][R3567][reyhard]

fixed uvanimation transformations

[4/16/2019 8:31:55 AM][0.4.9][R3566][Soul_Assassin]

retrigger Stryker build

!CLEARTEMP!

[4/15/2019 10:21:05 PM][0.4.9][R3565][Soul_Assassin]


Fix stryker model cfg to restate build

!CLEARTEMP!

[4/15/2019 10:10:13 PM][0.4.9][R3564][Soul_Assassin]

trigger stryker rebuild

!CLEARTEMP!

[4/15/2019 9:41:54 PM][0.4.9][R3563][reyhard]

added stryker moving map experiment

[4/14/2019 8:42:21 PM][0.4.9][R3562][reyhard]

^ Added crew animations for Stryker (note: death animations are missing)
^ Added some interior equipment to Stryker
^ Added engine destruction effect
^ Added MFD based CROWS monitor

[4/14/2019 6:30:13 PM][0.4.9][R3561][da12thMonkey]

^ Moved 100rnd 5.56mm C-Mags to BIS CfgMagazineWells class `STANAG_556x45_Large`. Will now load in M4/M16 type rifles but not M249 and BIS weapons where such magazines should not fit. (Arma 3 V1.92)

[4/10/2019 9:27:53 AM][0.4.9][R3560][Soul_Assassin]

^ Improved Predator Tactical normals

[4/10/2019 6:54:43 AM][0.4.9][R3559][reyhard]

^ Added sensorPosition param to some of the static weapons

[4/9/2019 9:41:05 PM][0.4.9][R3558][da12thMonkey]

Configured proxies for M443, M576 and M781 40mm grenades

[4/8/2019 10:23:33 PM][0.4.9][R3557][da12thMonkey]

Forgot to rotate grenade models for proxy use

[4/8/2019 8:38:54 PM][0.4.9][R3556][da12thMonkey]

^ Randomisation of grip folding on rifle-mounted M320 UGLs
Work on preparing M320 and M203s for magazine proxies

[4/8/2019 11:09:30 AM][0.4.9][R3555][reyhard]

fixed copy pasta flop in m590 reload loop

[4/7/2019 2:33:00 PM][0.4.9][R3554][da12thMonkey]

Adjusted Abrams Gunner's Primary Sights damage configuration to include the sight-head mirror

[4/7/2019 12:21:21 PM][0.4.9][R3553][reyhard]

+ Added reload system to M590 shotgun together with new animations - requires Arma 1.
@ Fixed inverted normals on 12GA bullets
^ Added support for spent casing ejection to bolt action system (WIP)

[4/6/2019 8:08:03 PM][0.4.9][R3552][da12thMonkey]

Configured M1A2 optics hitpoints

[4/6/2019 11:47:52 AM][0.4.9][R3551][reyhard]

^ Improved addons loadorder

[4/5/2019 7:49:28 PM][0.4.9][R3550][da12thMonkey]

M1A1 gunner optics damage

[4/2/2019 9:26:48 PM][0.4.9][R3549][reyhard]

Added turn in animation for Stryker TC - experimenting with small script

[4/1/2019 8:58:49 PM][0.4.9][R3548][reyhard]




[4/1/2019 8:56:54 PM][0.4.9][R3547][reyhard]

^ Added RHSUSF loadorder

[4/1/2019 8:51:38 PM][0.4.9][R3546][reyhard]

more turnout anim experimentation (config based)

[3/31/2019 9:01:44 PM][0.4.9][R3545][reyhard]

some more experiments with turn out

[3/31/2019 10:09:43 AM][0.4.9][R3544][reyhard]

@ Added some missing cfgPatches entries for USAF troops

[3/30/2019 1:13:56 PM][0.4.9][R3543][reyhard]

^ Added test Stryker Troop Commander turn out animation + copy pasted turn in anims variants from AFRF

[3/29/2019 7:52:59 AM][0.4.9][R3542][reyhard]

^ M1 Tank: 
* Converted zoom values to macros
* Removed hs materials references from config
* Tweaked turret & gun hitpoint values

[3/28/2019 3:15:32 PM][0.4.9][R3541][da12thMonkey]

Re-pathed optics model paths on some vehicles that were using BIS driver periscope, to our own version that has LODs for damaged states

[3/27/2019 10:02:31 PM][0.4.9][R3540][da12thMonkey]

Some work on optics damage for M1A1 versions of Abrams (driver and commander optics so far)

[3/27/2019 10:01:49 PM][0.4.9][R3539][reyhard]

^ Added visual optics destruction to Stryker
^ Tweaked Stryker hitpoints
@ Removed ambient shadow under mirrors from Stryker


[3/27/2019 10:49:51 AM][0.4.9][R3538][reyhard]

^ Added offset to FCS animation sources to fight imprecision of animateSource when vehicle is not local

[3/27/2019 8:16:30 AM][0.4.9][R3537][reyhard]

^ Readded proxies to characters shadow LOD
^ Some more improvements to characters fire geometry

[3/26/2019 9:06:05 PM][0.4.9][R3536][reyhard]

@ Fixed some minor issues with new character firegeometry

[3/25/2019 7:51:22 PM][0.4.9][R3535][reyhard]



[3/25/2019 7:50:51 PM][0.4.9][R3534][reyhard]

^ Added special high deflective material to armored vehicles barrels
work on Stryker optics destruction

[3/21/2019 11:23:19 AM][0.4.9][R3533][reyhard]

^ Improved blank ammo with submunition tech so it works correctly in MP - http://feedback.rhsmods.org/view.php?id=4916

[3/20/2019 7:38:41 PM][0.4.9][R3532][da12thMonkey]

Configured M2A3 optics destruction

[3/20/2019 3:12:31 PM][0.4.9][R3531][da12thMonkey]

Added alternate modelOptics for CROWS and DVE monitors, to allow some slight difference between damage visuals on different optics using the same style of monitor

WIP optics damage for Bradleys (M2A2 is functional but the M2A3 hitpoints config for IBAS, DVE etc. is still pending)

[3/19/2019 9:14:58 PM][0.4.9][R3530][reyhard]

wip work on optics visible damage 

[3/19/2019 12:11:55 PM][0.4.9][R3529][reyhard]

@ Fixed missing uvset asserts
^ Added new VG icons to HEMTTs

[3/19/2019 12:00:42 PM][0.4.9][R3528][da12thMonkey]

Fixed optic destruction not functioning right on RG33 ASV, thanks to reyhard

[3/18/2019 10:57:34 PM][0.4.9][R3527][da12thMonkey]

Work on optics hitpoints for M153 CROWS vehicles

[3/18/2019 8:09:03 PM][0.4.9][R3526][reyhard]

small characters tweaks

[3/18/2019 8:08:47 PM][0.4.9][R3525][reyhard]

fixed optics on stryker

[3/18/2019 7:37:12 PM][0.4.9][R3524][reyhard]

derp

[3/18/2019 7:35:53 PM][0.4.9][R3523][reyhard]

^ Tweaked Stryker RWS UI
@ Fixed Stryker RWS optics hitpoints
@ Fixed Stryker fuel hitpoint

[3/18/2019 5:53:42 PM][0.4.9][R3522][reyhard]

small clean up

[3/17/2019 8:25:11 PM][0.4.9][R3521][da12thMonkey]

Top-mounting PEQ-15s had incorrect PEQ-15A inventory picture

[3/17/2019 6:32:17 PM][0.4.9][R3520][da12thMonkey]

Damage+Destruct LODs for most USAF vehicle OpticsModels.

[3/17/2019 10:59:32 AM][0.4.9][R3519][reyhard]

+ Added ability to force scope type in mission with mission namespace variable "rhs_preferedOptic"
@ Fixed missing fire mode indicator in some of the helicopters if AFM & gauges were turned on

[3/17/2019 8:34:23 AM][0.4.9][R3518][reyhard]

attempt no 2
!CLEARTEMP!

[3/17/2019 8:34:00 AM][0.4.9][R3517][reyhard]

attempt no 2
!CLEARTEMP!

[3/17/2019 8:25:40 AM][0.4.9][R3516][reyhard]

renamed to lower case vehiclesounds - fixing linux build 
!CLEARTEMP!

[3/17/2019 7:14:32 AM][0.4.9][R3515][reyhard]

^ 40mm smoke grenades have now impact fuze & correct smoke time (~17-30 seconds) - http://feedback.rhsmods.org/view.php?id=4896

[3/16/2019 9:40:46 AM][0.4.9][R3514][reyhard]

@ Fixed inverted Stryker crew - http://feedback.rhsmods.org/view.php?id=4832
@ Added penetration materials, armor & explosion shielding parameter to all RHS explosives

[3/15/2019 7:18:43 PM][0.4.9][R3513][da12thMonkey]

^ Adjusted proxy positioning setup of MAAWS and its optic to be more conventional
Added Mk17-wielding MARSOC units that were missing from Zeus/cfgPatches
Added SMAW and MAAWS launcher optics to debugSlot

[3/15/2019 2:50:53 PM][0.4.9][R3512][da12thMonkey]

^ Adjusted SIDE proxy position on SMAW and M72

[3/14/2019 3:52:18 PM][0.4.9][R3511][da12thMonkey]

@Scoped out incomplete Smoke and Illum mag classes for MAAWS that were showing in Arsenal but are not made compatible with the launcher

[3/14/2019 8:50:45 AM][0.4.9][R3510][reyhard]

@ Fixed FROG uniform ghost LOD

[3/12/2019 11:54:03 PM][0.4.9][R3509][da12thMonkey]

Fixed non-convex component in M1238A1 ASV geo LOD
More fire-geo details for M1238A1 ASV and M1239 AUV

[3/12/2019 7:21:04 PM][0.4.9][R3508][da12thMonkey]

Fire geometry and hitpoints for M153 CROWS II on Caiman and SOCOM RG-33s

[3/12/2019 2:18:37 PM][0.4.9][R3507][da12thMonkey]

Stringtabled displaynames for new STANAG magazines and adjusted their sorting order for RHS weapons in Arsenal

[3/11/2019 8:58:28 PM][0.4.9][R3506][reyhard]

added icon for new SPC vest

[3/11/2019 8:28:00 PM][0.4.9][R3505][da12thMonkey]

Slight saturation adjustment to plateframe webbing textures

[3/11/2019 3:26:20 PM][0.4.9][R3504][reyhard]

SMAW had defined new dispersion in wrong place

[3/11/2019 11:41:41 AM][0.4.9][R3503][da12thMonkey]

Fixed: Team Leader version of Plateframe was missing "Camo" hiddenSelection for the main part of the vest

[3/10/2019 10:07:19 PM][0.4.9][R3502][reyhard]

@ Removed turn out option from M1238A1 Crows - http://feedback.rhsmods.org/view.php?id=4867

[3/10/2019 9:43:13 PM][0.4.9][R3501][reyhard]

@ SMAW & MAAWS were missing dispersion - http://feedback.rhsmods.org/view.php?id=4865
@ Fixed initial view angle for M1117 driver - http://feedback.rhsmods.org/view.php?id=4861

[3/10/2019 5:33:21 PM][0.4.9][R3500][da12thMonkey]

+ Extra USMC SPC vest variant for M40 Scout Snipers

[3/10/2019 3:16:59 PM][0.4.9][R3499][reyhard]

@ Fixed driver interior sounds + added ability to switch between seats for various USAF vehicles with turn out/in option

[3/10/2019 2:24:03 PM][0.4.9][R3498][da12thMonkey]

^ Halved the size of SU-230/PVS (SpecterDR) red dot in main telescope.
May be be more difficult to see at 1x magnification, but improves usability at 4x magnification

[3/10/2019 1:41:46 PM][0.4.9][R3497][reyhard]

@ Fixed missing head shadows in view pilot

[3/10/2019 12:40:36 PM][0.4.9][R3496][da12thMonkey]

@ PMAG was very slightly offset to the right of the magazine proxy axis

[3/10/2019 9:02:42 AM][0.4.9][R3495][reyhard]

@ Fixed some broken inheritance due to fault sound configs overwrites 

[3/9/2019 9:58:25 PM][0.4.9][R3494][reyhard]

Stryker:
* Configured lights (materials + rear & brake lights)
* Configured mirrors (R2T)

[3/9/2019 4:21:54 PM][0.4.9][R3493][reyhard]

^ Tweaked characters hands in shadow LOD

[3/9/2019 3:57:21 PM][0.4.9][R3492][reyhard]

^ Removed heads from characters Shadow LOD
general model clean up

[3/9/2019 1:21:23 PM][0.4.9][R3491][reyhard]

@ Fixed some bad interpolation in FFV RG-33 config

[3/9/2019 1:18:07 PM][0.4.9][R3490][reyhard]

@ Fixed some unnecessary tex1 reference in rvmat which were causing .rpt spam in Diag.exe
!CLEARTEMP!

[3/9/2019 12:58:31 PM][0.4.9][R3489][reyhard]

^ Adjusted M2010 muzzle attachment so it can support Join Rails
@ Fixed some error messags if unit has only single magazine and gripod is attached
@ Fixed missing uvset error on MBAV & Plateframe vests (tex1 in rvmat)
added more icons

[3/9/2019 12:06:02 PM][0.4.9][R3488][reyhard]

@ Fixed M1A2SEPv1 CITV firegeometry materials - http://feedback.rhsmods.org/view.php?id=4847

[3/8/2019 11:07:06 PM][0.4.9][R3487][da12thMonkey]

^ Switched SWCC crews to AOR2 uniforms
+ G3 uniform in AOR2 camo

[3/8/2019 10:53:49 PM][0.4.9][R3486][reyhard]

@ Regenerated components on M1239 - http://feedback.rhsmods.org/view.php?id=4823

[3/8/2019 6:26:16 PM][0.4.9][R3485][reyhard]

@ Fixed M1238A1 turn out option for drivers - http://feedback.rhsmods.org/view.php?id=4844

[3/8/2019 2:06:27 PM][0.4.9][R3484][da12thMonkey]

devBranch logo ver.1.0

[3/8/2019 11:14:44 AM][0.4.9][R3483][da12thMonkey]

^ Re-equipped some MARSOC units with S&S Plateframe vests
^ Updated MARSOC Mk17 DMR's optic, to include an offset MRDS
Added a couple of the extra plateframe textures to the data folder (the ones that match the normal map), should we ever wish to use them

[3/8/2019 11:06:30 AM][0.4.9][R3482][reyhard]

^ RHS Vehicle icons in Virtual Garage should be visible on Steam branch release
^ Added separate name for development branch version



[3/8/2019 12:58:39 AM][0.4.9][R3481][da12thMonkey]

Initial config for plateframe (vest weights and inventory capacity might need adjusting)
Reorganised hiddenselections names in plateframe models, for easier retexturing
Section and UVSet cleanup

[3/7/2019 10:23:52 PM][0.4.9][R3480][reyhard]

^ Added new inventory icons for weapon accessories 

[3/7/2019 9:43:50 PM][0.4.9][R3479][WA Lancer]

Fixed missing magpul plate in LOD1 and ViewPilot LOD on rhs_plateframe_sapi_light

[3/7/2019 9:18:06 PM][0.4.9][R3478][WA Lancer]

PlateFrame:
^ Resized and added LODs to original
+ Added Grenadier Variant
+ Added Light Variant
+ Added Machine Gunner Variant
+ Added Marksmen Variant
+ Added Medic Variant
+ Added Rifleman Variant
+ Added Team Leader Variant

[3/7/2019 6:20:20 PM][0.4.9][R3477][da12thMonkey]

+ Added M8541A version with MRDS
+ Added Leupold Mk4 M5 with MRDS
Moved MRDS forward slightly on S&B M8541
Slight increase to inventory "mass" of these sniper scopes with added MRDS



[3/7/2019 1:40:20 PM][0.4.9][R3476][da12thMonkey]

Geometries for last batch of US weapon attachments
@ Some ACOG sights had a high section count in lower LODs

[3/7/2019 9:12:20 AM][0.4.9][R3475][reyhard]

^ Tweaked PiP scopes aspect ratio - it's now adjusted for 16:9 screens - http://feedback.rhsmods.org/view.php?id=4788
^ Added simple geometries to ACOG scopes
^ Added proper buoyancy & firegeometry to M4 Block II & Mk18

[3/7/2019 7:19:03 AM][0.4.9][R3474][Soul_Assassin]

+ Added M8541 version with MRDS

[3/6/2019 10:11:01 PM][0.4.9][R3473][reyhard]

Stryker:
* Attempt to animate Stryker mirrors
* Added VG icon
* Added optic modes to Troop Commander

[3/6/2019 9:46:04 PM][0.4.9][R3472][da12thMonkey]

fixed typo

[3/6/2019 9:14:21 PM][0.4.9][R3471][da12thMonkey]

@ Flag position on Caiman MRAPs changed position in different LODs

[3/6/2019 8:14:21 PM][0.4.9][R3470][reyhard]

^ Regenerated 5.56mm STANAG magazine icons
^ Added icons for new DCU helmets
^ Added icons for SCAR USA
@ Fixed camo selections on Black PMAGs and CMAGs - http://feedback.rhsmods.org/view.php?id=4828
added missing semicolon

[3/5/2019 9:42:02 PM][0.4.9][R3469][reyhard]

Stryker:
* Added damage & destruction rvmats
* Changed FFV turrets name
* Added Fire Geometry p3d for additional testing

[3/5/2019 9:10:42 PM][0.4.9][R3468][reyhard]

@ Removed Abrams TI textures in HIMARS rvmat - temporary fix till proper TI textures are there
!CLEARTEMP!

[3/5/2019 5:34:23 PM][0.4.9][R3467][ballistic09]

Tweaked displayName and displayNameShort of new STANAGS to use same naming convention as other magazines

[3/5/2019 9:59:33 AM][0.4.9][R3466][reyhard]

@ Fixed missing penetration material for Glock 17

[3/5/2019 9:56:29 AM][0.4.9][R3465][reyhard]

@ Fixed zeroing of Glock 17, M9 Beretta & M1911A1

[3/5/2019 2:41:07 AM][0.4.9][R3464][ballistic09]

early ACH (DCU) configs

[3/4/2019 9:52:32 PM][0.4.9][R3463][reyhard]

Stryker:
* Tweaked antenna motion (still wip)
* Added some basic hitpoints
* Added ability to hide each antenna via Virtual Garage
* Muzzle flash adding attempt

[3/4/2019 7:13:46 PM][0.4.9][R3462][da12thMonkey]

Geometry LODs and named selection+UVSet cleanup of many weapon attachments

[3/4/2019 11:46:58 AM][0.4.9][R3461][reyhard]

^ Tweaked M240 fire geometry
^ Improved M240 hidden selections since magazines are moved to separate proxies
removed some unused variants
!CLEARTEMP!

[3/4/2019 11:45:37 AM][0.4.9][R3460][reyhard]

checkAll various fixes - open shadows, named properties fixes, removing redundant UV sets, non convex components

[3/4/2019 4:58:41 AM][0.4.9][R3459][ballistic09]

config for DCU ACH helmet

[3/3/2019 10:48:22 PM][0.4.9][R3458][reyhard]

Stryker
* Added driveOnComponent
* Removed textures from shadow LOD

[3/3/2019 10:17:17 PM][0.4.9][R3457][reyhard]

Stryker:
* added wip antenna anims
* added turret & gun hitpoints (wip)
* removed unused material from wheel


[3/3/2019 9:40:39 PM][0.4.9][R3456][reyhard]

small tweak to geometry physx

[3/3/2019 9:38:34 PM][0.4.9][R3455][reyhard]

Stryker:
* renamed stryker to accomodate mk19 in future
* added user actions for ramp
* configured hidden selections
* configured lights
* some config clean up
* switched back to sound sets
* tweaked suspension strength
* configured smoke grenades
* added new firegeometry (hitpoints are still missing)
* added some config entries for new hitpoints

[3/3/2019 8:09:15 PM][0.4.9][R3454][da12thMonkey]

LODs for new GBU-12 model

[3/3/2019 6:07:05 PM][0.4.9][R3453][sykoCrazy]



[3/3/2019 12:30:58 AM][0.4.9][R3452][da12thMonkey]

Magic mem point box for GBU-12 fly model's geo LOD

[3/3/2019 12:22:57 AM][0.4.9][R3451][da12thMonkey]

Initial config for the All-American SCAR-H

[3/3/2019 12:07:16 AM][0.4.9][R3450][ballistic09]

+ New GBU-12 model

[3/2/2019 9:04:35 PM][0.4.9][R3449][PuFu]

^ SCARH - murican texture

[3/2/2019 6:47:32 PM][0.4.9][R3448][reyhard]

^ Tweaked spall, HEAT & thermobaric ammo configs

[2/28/2019 8:30:04 PM][0.4.9][R3447][reyhard]

@ Fixed Mk.19 sounds in AI fire modes

[2/28/2019 2:15:35 PM][0.4.9][R3446][reyhard]

checkAll various fixes - open shadows, named properties fixes, removing redundant UV sets, non convex components

[2/26/2019 7:38:12 PM][0.4.9][R3445][da12thMonkey]

!CLEARTEMP!
Updated magazine model in the M4 prop used on OGPK turrets as a proxy
Removed prop proxy from lower LODs of vehicles with OGPK (the proxy model only has one high detailed LOD, so figure it was not designed to be included in vehicle's lower LODs)
Used this opportunity updating many vehicle .p3ds, to introduce `useWorldEnvMap="true";` to the .rvmat used on most armoured glass (HEMTT and FMTV A-Kit are using a BIS .rvmat though)

[2/25/2019 7:18:53 PM][0.4.9][R3444][da12thMonkey]

Ground models for stanag mags

[2/24/2019 8:38:05 PM][0.4.9][R3443][reyhard]

added placeholder config for Stryker

[2/24/2019 3:25:32 PM][0.4.9][R3442][reyhard]

author macro replacement continuation
cleaned up numberPhysicalWheels parameter - it should be only used on helicopters

[2/24/2019 11:53:59 AM][0.4.9][R3441][reyhard]

regex missied *.h files

[2/24/2019 11:17:26 AM][0.4.9][R3440][reyhard]

converted Author_Macro to upper case

[2/20/2019 11:47:20 PM][0.4.9][R3439][da12thMonkey]

Assigned per-mag bullet textures to STANAG mags
Test adding high z-bias to tape in Jungle mag model's view Pilot LOD

[2/20/2019 10:36:22 PM][0.4.9][R3438][PuFu]

updated specularity for for mags, bullets etc 

[2/19/2019 11:27:00 AM][0.4.9][R3437][reyhard]

batch fixed some small issues with 2nd uvsets, removed proxies in shadow LOD, cleaned up named properties and fixes some geometries

[2/19/2019 11:18:29 AM][0.4.9][R3436][da12thMonkey]

Tracer version of jungle mag
Fixed typo/double entry of `displaynameShort` param

[2/18/2019 11:09:57 PM][0.4.9][R3435][da12thMonkey]

Some config for M193 ammo

[2/18/2019 9:23:43 PM][0.4.9][R3434][da12thMonkey]

Minor vertical adjustment to the position of new STANAG mags

[2/18/2019 8:25:14 PM][0.4.9][R3433][da12thMonkey]

Initial config for new STANAG mags

[2/18/2019 3:14:59 PM][0.4.9][R3432][da12thMonkey]

Model.cfg stuff for new proxy mags

[2/18/2019 10:02:33 AM][0.4.9][R3431][PuFu]

+ new USGI 20 and 30 rounds mags & magpull acc

[2/6/2019 9:23:11 AM][0.4.9][R3430][reyhard]

@ Removed radio cables from pilot LOD of some IOTV vest since they were clipping badly in 1st person view
@ Fixed IOTV (repair) vest didn't match 1st res lod & pilot LOD
removed some unnecessary named properties

[2/6/2019 8:51:32 AM][0.4.9][R3429][reyhard]

^ Tweaked M113 land contact memory points snapping in Eden editor

[2/5/2019 3:41:09 AM][0.4.9][R3428][gurdy]

Quick creation of early covered ACH with and without Rhino mount (Naming convention may change)
+ ACH (Early)
+ ACH (Early/Rhino)
@Ballistic09#2617 
@sabre#0576 
@Tim aka Delta Hawk#5638 

[2/1/2019 8:46:45 AM][0.4.9][R3427][reyhard]

@ M1 tanks were not engaging other tanks when AFRF was not used

[1/30/2019 2:57:43 PM][0.4.9][R3426][da12thMonkey]

^ SR-25EC (Enhanced Carbine) now utilises 7.62mm muzzle-mounted suppressor attachments, instead of the Mk.11 type of collar-locking slide-on suppressor. (Joint Muzzles compatible)

[1/27/2019 11:03:48 PM][0.4.9][R3425][LAxemann]

Fixed: IFA3 filters and panners were used

[1/26/2019 6:54:39 PM][0.4.9][R3424][LAxemann]

Changed: M249 first person/clost distance sound sound
Added: Many, many, many sounds for later use (staging-phase :D)

[1/26/2019 6:47:51 PM][0.4.9][R3423][LAxemann]

Tweaked and changed: Many sound config parameters

[1/23/2019 2:49:34 PM][0.4.9][R3422][da12thMonkey]

Forgot that weapon base class would have blank hiddenSelectionsTextures array

[1/23/2019 12:44:45 PM][0.4.9][R3421][da12thMonkey]

^ Added retexture selections to M249/Minimi

[1/22/2019 3:20:03 PM][0.4.9][R3420][da12thMonkey]

SOCOM JTAC and EOD units' M4s were missing their vert grip

[1/21/2019 3:09:51 PM][0.4.9][R3419][da12thMonkey]

Re-assigning camo net textures to ones from our own .pbo

[1/21/2019 2:24:37 PM][0.4.9][R3418][da12thMonkey]

Test remapping camo net texture

[1/21/2019 1:05:18 PM][0.4.9][R3417][reyhard]

@ Added autocenter & buoyancy named properties to C130J - please pay attention to missions already created since it might break plane position

[1/20/2019 5:28:57 PM][0.4.9][R3416][da12thMonkey]

RG33L camo nets

[1/20/2019 2:45:01 PM][0.4.9][R3415][da12thMonkey]

FMTV camo net stuff

[1/20/2019 1:35:59 PM][0.4.9][R3414][da12thMonkey]

Generated some camo net textures in colours more appropriate to USAF vehicles

[1/20/2019 1:58:45 AM][0.4.9][R3413][da12thMonkey]

OGPK nets on HEMTT

[1/19/2019 11:32:01 PM][0.4.9][R3412][da12thMonkey]

Camo net for OGPK turret (Caiman first)

[1/16/2019 11:09:29 PM][0.4.9][R3411][da12thMonkey]

FMTV UV set cleanup and glass destruction
Removed some 'camo' selections that had snuck in to the shadow LODs

[1/16/2019 4:01:34 PM][0.4.9][R3410][da12thMonkey]

Forgot to update HEMTT M2s to new muzzle flash proxies

[1/16/2019 1:28:23 PM][0.4.9][R3409][da12thMonkey]

HEMTT OGPK accessories
Cleaned up UV sets and some rogue named properties
Re-added some old RG-33 materials that the HEMTT gunner LOD required

[1/16/2019 1:50:19 AM][0.4.9][R3408][RichardsD]

@ Adds O-GPK accessories to FMTVs
@ Fixes a bunch of little FMTV issues: CP Box cargo strap clipping, removes extra animations from versions that don't have them

[1/16/2019 1:33:16 AM][0.4.9][R3407][da12thMonkey]

Caiman window destruction
Prevented CROWS versions showing extra animations for OGPK equipment

[1/15/2019 8:52:08 PM][0.4.9][R3406][RichardsD]

@ Adds configurable turret accessories for Caiman MRAP with O-GPK turret

[1/15/2019 3:41:01 PM][0.4.9][R3405][da12thMonkey]

AUV rear wheel hitpoints were not aligned properly
Configured destructible rear window

[1/15/2019 4:30:36 AM][0.4.9][R3404][ballistic09]



[1/15/2019 4:18:08 AM][0.4.9][R3403][ballistic09]

+ Editor placeable M2A1 and M19A1 ammo can items
(needs shadow lods)
^ M240 bipod legs position when folded

[1/15/2019 2:06:24 AM][0.4.9][R3402][RichardsD]

@ SOCOM AUV Thermal

[1/14/2019 10:59:10 PM][0.4.9][R3401][da12thMonkey]

Regenerated RG33L geometry components (not all of the fire geo was working)
Adjusted window hitpoints and selections so that they match positions and follow animations correctly
^ Replaced TD Grip with KAC grip on the M27 IAR that has a permanent grip

[1/14/2019 4:54:28 PM][0.4.9][R3400][da12thMonkey]

RG33L section cleanup since turrets were updated
Hid extra animation options that were showing for MCTAGS turrets

[1/14/2019 3:34:32 AM][0.4.9][R3399][RichardsD]

@ Adds OGPK Additional customisation options: Overhead protection and turret bustle to M1232 / M1237 MRAP

[1/13/2019 11:56:47 PM][0.4.9][R3398][da12thMonkey]

+ M1220 Caiman with CROWS-mounted Mk19

[1/13/2019 10:30:40 PM][0.4.9][R3397][da12thMonkey]

AUV MK19 weapon carriers
AUV damage/destruction adjustments
Fixed 'camo' selection that snuck in to ASV shadow LOD

[1/13/2019 4:36:15 PM][0.4.9][R3396][RichardsD]

@ Adds more undercarriage geometry to M1232 / M1237 MRAPs for far LODs

[1/13/2019 3:26:25 PM][0.4.9][R3395][da12thMonkey]

Set up damage and destruction for SOCOM ASV
Added animations to hide the perspex searchlight dome
Attribute for lowering Rhino
Antennas and some other large external parts hidden when loading the vehicle in to a transport plane
Added Mk19 versions to cfgPatches
Edprev images for Mk19 versions
Woodland vehicles moved to hidden scope (selectable by vehicle customisation or as Zeus)

[1/13/2019 3:03:34 AM][0.4.9][R3394][RichardsD]

+ Adds initial version of the M153 CROWS II with MK.19 GMG


[1/12/2019 9:10:47 PM][0.4.9][R3393][da12thMonkey]

Eden object for Omega 9mm suppressor

[1/12/2019 5:20:06 PM][0.4.9][R3392][da12thMonkey]

SOCOM RG33s DUKE configuration
Added flag proxies

[1/12/2019 1:42:18 PM][0.4.9][R3391][reyhard]

RG-33 is now using hideProxyInCombat = 1 by default so it's possible to between seats

[1/12/2019 1:38:26 PM][0.4.9][R3390][da12thMonkey]

ASV vehicle transport bounding box mem points

[1/11/2019 6:07:55 PM][0.4.9][R3389][da12thMonkey]

^Adjusted scale of M153 CROWS. Now has a correct height of 0.762 meters

[1/9/2019 9:13:18 PM][0.4.9][R3388][da12thMonkey]

^Animation to hide Rhino on RG33L Plus and Caiman Plus up-armoured MRAPs
Updated M2 muzzle flash proxy on some vehicles

[1/9/2019 5:22:35 PM][0.4.9][R3387][da12thMonkey]

Restored old 4*4 RG33 classes in hidden scope (configured for 7 passengers)
Made a common parent class for armed versions of the vehicle
Adjusted fording depth

[1/8/2019 8:00:50 AM][0.4.9][R3386][reyhard]

done

[1/7/2019 10:13:20 PM][0.4.9][R3385][da12thMonkey]

Reduced ASV mass (was the same as the 6*6 versions)

[1/7/2019 8:30:24 PM][0.4.9][R3384][da12thMonkey]

RG33 ASV FFV and cargo anim work

[1/6/2019 5:31:55 PM][0.4.9][R3383][da12thMonkey]

Anim for hiding Rhino on ASV

[1/6/2019 3:32:19 AM][0.4.9][R3382][da12thMonkey]

Fixing some parts of headlight selections on SOCOM RG33s
Configured ASV cabin lights

[1/5/2019 11:27:59 PM][0.4.9][R3381][da12thMonkey]

Some SOCOM ASV work

[1/5/2019 7:07:04 PM][0.4.9][R3380][reyhard]

@ Fixed open geometry in shadow LOD of TA31RCO-RMR PIP variant

[1/5/2019 6:28:01 PM][0.4.9][R3379][da12thMonkey]

Adjust AUV fording depth

[1/5/2019 3:47:28 PM][0.4.9][R3378][da12thMonkey]

RG33 ASV section clean up
CROWS was missing its shadow

[1/5/2019 2:33:26 PM][0.4.9][R3377][reyhard]

@ Fixed UH-1Y was able to detect IR locks
@ Fixed USMC M32 grenadiers were using wrong weapons (with additional scope which they couldn't use, since it's integrated - it caused rpt spam)

[1/5/2019 12:39:12 AM][0.4.9][R3376][RichardsD]

!CLEARTEMP!
- Removes old RG-33 MRAP series as legacy vehicles
+ Adds the new M1238A1 RG-33 SOCOM Armored Security Vehicle 4X4 in un-armed and M2 CROWS Variants

[1/4/2019 12:09:55 AM][0.4.9][R3375][RichardsD]

@ Adds units to SOCOM AUV config file

[12/31/2018 9:39:49 PM][0.4.9][R3374][da12thMonkey]

Last few AUV crew anims

[12/30/2018 8:34:28 PM][0.4.9][R3373][da12thMonkey]

Updated edPrev images for Cougar and AUV following recent texture changes

[12/22/2018 12:00:01 PM][0.4.9][R3372][da12thMonkey]

oops

[12/21/2018 11:42:38 PM][0.4.9][R3371][da12thMonkey]

AUV CROWs gunner anims
Mem points for exhaust smoke

[12/20/2018 10:03:27 PM][0.4.9][R3370][da12thMonkey]

AUV work:
Driver anims
Mem points for cabin lights and ViV cargo handling
Replaced "deployed" version's cargo textures with a non-alpha texture and made the camo net a separate section using BIS Tanks DLC camo net textures, to avoid shading issues

[12/20/2018 1:53:12 PM][0.4.9][R3369][da12thMonkey]

Adjusted Caiman CROWS operator view angle and moved memory points to new monitor position

[12/19/2018 11:32:37 PM][0.4.9][R3368][RichardsD]

@ Adds comm suite install to Caiman MRAP and RG-33L MRAP.
@ Fixes glass position on M1239 SOCOM AUV MRAP interior

[12/19/2018 4:49:39 PM][0.4.9][R3367][RichardsD]

@ Fixed camo darkness on Cougar MRAP

[12/19/2018 11:30:49 AM][0.4.9][R3366][reyhard]

@ USMC side winders were using wrong ammo

[12/19/2018 11:29:29 AM][0.4.9][R3365][reyhard]

^ Tweaked M2 Bradley gun armor (no longer destroyable with small arms fire)
^ Added separate light hitpoints stored in Hitpoints class
added missing semicolon

[12/19/2018 4:07:44 AM][0.4.9][R3364][RichardsD]

@ Adds comms suite to Cougar MRAP

[12/19/2018 2:11:32 AM][0.4.9][R3363][RichardsD]

@ Adds Comms install to M1239 AUV
+ Adds all comms equipment as master file for all vehicles with comms gear, and AN/PRC-152 test object

[12/18/2018 11:02:05 PM][0.4.9][R3362][da12thMonkey]

Updated edPrev images for US units following loadout changes
CH-53 ramp guns now crewed by crew with face shields rather than pilots
Put Army SF driver in to public scope so that SOCOM FMTVs and RG33 AUVs can be Zeus'd properly

[12/18/2018 8:30:29 AM][0.4.9][R3361][Soul_Assassin]

trigger auv rebuild

!CLEARTEMP!

[12/18/2018 1:24:54 AM][0.4.9][R3360][ballistic09]

test

[12/17/2018 10:48:49 PM][0.4.9][R3359][da12thMonkey]

AUV section count reduction
Made spare wheel shadow able to hide with the rest of the model

[12/17/2018 9:46:37 PM][0.4.9][R3358][RichardsD]

@ Fixed AO on M1239 Main CO

[12/17/2018 7:39:19 PM][0.4.9][R3357][da12thMonkey]

M1239 AUV garage icons
Fixed destruction .rvmat config paths
Fixed white border edges on door decal alpha texture

[12/16/2018 9:47:07 PM][0.4.9][R3356][da12thMonkey]

GAU-21 LODs

[12/16/2018 8:43:03 PM][0.4.9][R3355][RichardsD]

@ Adds LODs to M1239 SOCOM AUVs

[12/16/2018 12:47:28 PM][0.4.9][R3354][reyhard]

^ Added new virtual garage icons for USAF static weapons

[12/16/2018 12:19:29 PM][0.4.9][R3353][da12thMonkey]

Renamed M1239 AUV folders
pbo names must be lower case, else Linux servers will shit the bed

[12/16/2018 4:44:22 AM][0.4.9][R3352][RichardsD]

+ Adds M1239 LODs for un-armed version only

[12/16/2018 1:10:48 AM][0.4.9][R3351][RichardsD]

+ Adds first version of the M1239 SOCOM Armored Utility Vehicle, designated M1239 AUV in game. 

[12/12/2018 8:46:16 PM][0.4.9][R3350][reyhard]

@ Fixed small FAST helmet glitches with cover selection

[12/12/2018 2:06:52 PM][0.4.9][R3349][da12thMonkey]

GAU-21 softmount recoil/vibration anims

[12/11/2018 6:45:20 PM][0.4.9][R3348][da12thMonkey]

GAU-21 ammobelt UV animation, Shadow LOD improvements

[12/11/2018 1:01:44 PM][0.4.9][R3347][da12thMonkey]

@ CH-53E ramp shadow LOD was welded to the fuselage creating some distortion when the ramp moved
+ GAU-21 HMG added to CH-53E ramp (model by nextanimationstudio, gifted to RHS by armyinf & co.)

GAU-21 still needs some LODs, but modification to he base CH-53E is done otherwise

[12/8/2018 9:55:35 AM][0.4.9][R3346][reyhard]

^ Tweaked engine startup delay - engine startup delay should be shorter when engine was turned off second ago. Should improve AI behavior which tends to constantly switch on & off gas turbines

[12/7/2018 7:00:24 PM][0.4.9][R3345][ballistic09]

Tweaks to the M249 magazine order for the arsenal

[12/7/2018 6:45:59 PM][0.4.9][R3344][da12thMonkey]

Some M249 pouches were using icons with the old textures

[12/7/2018 11:48:22 AM][0.4.9][R3343][reyhard]

^ Added new icons for M249 magazines

[12/7/2018 8:56:02 AM][0.4.9][R3342][Soul_Assassin]

Packtest

[12/7/2018 8:53:39 AM][0.4.9][R3341][Soul_Assassin]

Force rebuild faulty repos, tree conflicts should be fixed

!CLEARTEMP!

[12/7/2018 8:36:39 AM][0.4.9][R3340][Soul_Assassin]

Packtest

[12/7/2018 7:32:48 AM][0.4.9][R3339][reyhard]

- removed vanilla entries from magazine wells since it's already introduced in base game

[12/6/2018 10:16:10 PM][0.4.9][R3338][ballistic09]

+ Additional M81, UCP, and Coyote Brown 100 and 200 round softpack mags for the M249
(Thanks Sabre!)

[12/6/2018 7:18:47 PM][0.4.9][R3337][reyhard]

+ Added unflip functions to MRZR
^ Increased COM of MRZR & increased antirollbar - it should allow more natural weight shifting with same 
fixed m49 references to AFRF (still need to generate ed previews)


[11/30/2018 6:22:33 PM][0.4.9][R3336][wld427]

Set ACH helmet with cammo net to use camo2 selection. 

[11/23/2018 9:24:04 PM][0.4.9][R3335][reyhard]

+ Added new uniform inventory icons

[11/23/2018 9:09:56 PM][0.4.9][R3334][reyhard]

@ Fixed gripod freeze - http://feedback.rhsmods.org/view.php?id=4712

[11/20/2018 4:35:29 AM][0.4.9][R3333][ballistic09]

^ Unified hand animation scheme for M4's
@ USMC grenadiers had wrong M4 (added carryhandle M4 w/ M203)
^ US Army units now use M4's with Matech BUIS
+ Alternate ACH helmets with tan rhino mounts
+ Helmet randomization
(For US Army only currently)

Initial tweaks to US Army regular unit configs (ACU's, KAC forgrips, M24 binoculars, Vector 21B added to units)

[11/16/2018 2:05:02 AM][0.4.9][R3332][ballistic09]

^ Improved position/tint of M68 CCO lenses and brought back killflash

[11/9/2018 8:45:15 AM][0.4.9][R3331][reyhard]

@ Fixed M113 hatch stayed open
^ Added Virtual Garage option to close & open commander hatch on M113

[11/8/2018 8:27:49 AM][0.4.9][R3330][reyhard]

@ Updated M109 loadout selection after magazine renaming

[11/5/2018 8:08:14 AM][0.4.9][R3329][reyhard]

@ Added static weapons bags to cfgPatches so they can be used in Zeus

[11/2/2018 8:34:57 PM][0.4.9][R3328][ballistic09]

Some changes to M1A1 CWS/CWSS optics

[11/1/2018 12:57:51 AM][0.4.9][R3327][ballistic09]

+ Added simple CWSS FCS for M1A1s with commander's Thermal Sight Module

[10/28/2018 8:02:29 AM][0.4.9][R3326][reyhard]

duplicated entry fix

[10/28/2018 5:04:18 AM][0.4.9][R3325][ballistic09]

Added Battle Dress Uniform (initial injection for HIDF in ERDL camo)
Small tweaks to vehicle M240 display names

[10/27/2018 9:08:56 AM][0.4.9][R3324][reyhard]

added SCAR magazine inventory icon

[10/24/2018 3:26:22 PM][0.4.9][R3323][reyhard]

^ Tweaked M134 ammo count & used bullets on USAF helicopters

[10/22/2018 5:46:58 PM][0.4.9][R3322][da12thMonkey]

pboprefix file

[10/22/2018 4:58:47 PM][0.4.9][R3321][da12thMonkey]

remove texheaders.bin

[10/22/2018 2:26:16 PM][0.4.9][R3320][LAxemann]

Added: New weapon sounds for various weapons
Added: prototype of new abrams sounds, heavily WIP; more about the framework for now
Added: folder rhsusf_c_vehiclesounds
Added: folder rhsusf_s_vehiclesounds
Added: folder rhsusf_c_weaponsounds
Added: folder rhsusf_s_weaponsounds

[10/21/2018 5:26:47 PM][0.4.9][R3319][da12thMonkey]

@ MELBs had unrealistic ability to detect passive sensor locks (visual, IR etc.) Now only RWR and MAWS

[10/13/2018 9:51:11 PM][0.4.9][R3318][da12thMonkey]

Ability to collapse M249 Para stocks
Scar folding while grips are attached

[10/9/2018 1:41:09 PM][0.4.9][R3317][da12thMonkey]

weaponInfoType with different idd values for newly added grips

[10/8/2018 11:35:42 PM][0.4.9][R3316][da12thMonkey]

^ Anim to randomly fold the barrel handle on M249s

[10/8/2018 9:23:50 PM][0.4.9][R3315][ballistic09]

Added KAC grip/standard SAW bipod foregrip combo for RIS M249s

[10/8/2018 8:52:08 PM][0.4.9][R3314][PuFu]

!CLEARTEMP!

[10/8/2018 8:18:59 PM][0.4.9][R3313][da12thMonkey]

Generated a sound set for the SCAR-H

[10/8/2018 6:40:20 PM][0.4.9][R3312][PuFu]

scarh recoil

[10/8/2018 4:52:38 PM][0.4.9][R3311][da12thMonkey]

MARSOC Mk17 had 5.56mm SpecterDR instead of 7.62mm

[10/7/2018 6:50:40 PM][0.4.9][R3310][da12thMonkey]

Editor integration of Mk17 rifles and accessories

[10/7/2018 5:07:30 PM][0.4.9][R3309][PuFu]

more ti tetxure dicking about

[10/7/2018 2:00:44 PM][0.4.9][R3308][da12thMonkey]

light M249 inventory pic path

[10/7/2018 1:29:25 PM][0.4.9][R3307][da12thMonkey]

Name of SCAR model.cfg camo hidden selection, did not match .p3d Camo1>>Camo01 

[10/7/2018 1:22:23 PM][0.4.9][R3306][reyhard]

added new inventory icons
ported folding script to USAF

[10/7/2018 8:56:42 AM][0.4.9][R3305][PuFu]

ti_ca

[10/7/2018 12:41:32 AM][0.4.9][R3304][PuFu]

ffs

[10/7/2018 12:38:59 AM][0.4.9][R3303][PuFu]

added ti maps

[10/6/2018 9:50:09 PM][0.4.9][R3302][da12thMonkey]

^ Extended class-switching script for top-mounting PEQ lasers, to accept value `rhsusf_acc_anpeq15 = 2;` (used in RHS:USAF for SCAR rail height accessories)

Added attachment models to fit SCAR top rails

[10/6/2018 8:01:18 PM][0.4.9][R3301][da12thMonkey]

Ammobox config had an incomplete macro

[10/6/2018 1:51:06 PM][0.4.9][R3300][da12thMonkey]

SCAR adjustments:
Moved weapon 4cm down, for a more natural shouldering position - made matching handanims set
Adjusted alignment of some attachment proxies 
Switched muzzle flash proxy for the three-prong type
Added deployment mem point to stop unit sinking in ground when not grip/bipod is fitted

[10/6/2018 11:49:33 AM][0.4.9][R3299][PuFu]

aac spec tweak / folded version in model.cfg

[10/5/2018 10:51:12 PM][0.4.9][R3298][PuFu]

updated SCARs sights anims, added folded versions

[10/5/2018 6:38:07 PM][0.4.9][R3297][reyhard]

^ Improved M107 & M2010 fire geometry

[10/5/2018 5:34:51 PM][0.4.9][R3296][da12thMonkey]

+ M249 Lightweight Collapsible Buttstock

[10/4/2018 9:52:56 PM][0.4.9][R3295][PuFu]

^ more scarH work + accesories 

[10/4/2018 12:18:36 PM][0.4.9][R3294][reyhard]

^ Tweaks to AI TOW usage

[10/4/2018 1:31:19 AM][0.4.9][R3293][da12thMonkey]

Broken SCAR mag model path

[10/4/2018 12:39:38 AM][0.4.9][R3292][PuFu]

^ more work on scars

[10/3/2018 5:04:40 PM][0.4.9][R3291][reyhard]

^ Tweaked M16 fire geometry

[10/3/2018 3:07:49 PM][0.4.9][R3290][da12thMonkey]

Fixed non-closed parts in SCAR SVLODs

[10/3/2018 12:41:00 PM][0.4.9][R3289][da12thMonkey]

^ Gave M249 plastic box magazines a more appropriate `mass` value
^ Changed Aimpoint T1's displayname to its US military designation (SU-278/PVS)

Set up SCAR config (M4 sounds for now - will mess with sound sets later)

[10/2/2018 8:10:41 PM][0.4.9][R3288][PuFu]

^ further geo lod updates on SCAR, SVLod vert number reduced

[10/2/2018 7:50:20 PM][0.4.9][R3287][reyhard]

^ Improved M4 fire geometry
fixed components numbers in M4 geometry

[10/2/2018 7:49:24 PM][0.4.9][R3286][reyhard]

@ Reduced M113 resistance against IEDs

[10/2/2018 9:34:09 AM][0.4.9][R3285][PuFu]

^ removed AO around fireselector and geolods

[10/1/2018 11:42:41 PM][0.4.9][R3284][da12thMonkey]

Fixing trailing commas in model.cfg arrays

[10/1/2018 11:03:28 PM][0.4.9][R3283][PuFu]

+ initial MK17 commit

[9/30/2018 10:58:21 AM][0.4.9][R3282][reyhard]

+ Added M49A1 tripware flare
@ Fixed TOW AI engagment ranges

[9/28/2018 5:53:57 PM][0.4.9][R3281][reyhard]

added icons for new HGU helmets
added missing cfgPatches & virtualAmmoBox.sqf entries for new helmets

[9/28/2018 10:59:55 AM][0.4.9][R3280][reyhard]

^ Tweaked inertia for M320 standalone grenade launcher

[9/26/2018 8:08:13 PM][0.4.9][R3279][da12thMonkey]

@ M240B had an extra cocking handle in the View Pilot LOD

[9/26/2018 12:00:47 PM][0.4.9][R3278][da12thMonkey]

oops

[9/26/2018 7:44:44 AM][0.4.9][R3277][reyhard]

^ Unified AH-64 MFD brightness 

[9/26/2018 12:26:16 AM][0.4.9][R3276][da12thMonkey]

+ M249 PIP with solid buttstock and RIS
^ Separate "M249 VFG" classes in Arsenal are no longer required to convert the M249 to use a grip instead of a bipod (inc. new bipod slot attachments for M249)
^ Added grip system slot to Para stock M249s
- Removed unneeded M249 models: `m249_pip_S_vfg.p3d`, `m249_pip_L_vfg.p3d` (separate obsolete since converting bipods to attachments)

[9/24/2018 5:32:52 PM][0.4.9][R3275][sykoCrazy]

@ Added missing UH-1Y gunner anims /facepalm

[9/24/2018 12:58:35 PM][0.4.9][R3274][da12thMonkey]

Missing Author macro

[9/24/2018 9:53:25 AM][0.4.9][R3273][da12thMonkey]

!CLEARTEMP!
+ M16A4s with VLTOR IMOD buttstocks. Thanks to toadie2k for the stock model
- Removed .p3d files: m16a4_ris_pmag.p3d, m16a4_ris_carryhandle_pmag.p3d (separate models are obsolete since mag proxy implementation)

[9/23/2018 11:24:55 AM][0.4.9][R3272][reyhard]

@ Fixed M113 tracks explosion shielding

[9/22/2018 7:05:10 PM][0.4.9][R3271][sykoCrazy]

@ [UH-1Y]Fixed locked camera bug for gunners(UsePiP = 1)
^ [UH-1Y]Gunners now hold onto miniguns

[9/21/2018 11:04:13 PM][0.4.9][R3270][ballistic09]

@ Some woodland Abrams were using desert decals

[9/21/2018 3:21:36 PM][0.4.9][R3269][reyhard]



[9/21/2018 3:10:17 PM][0.4.9][R3268][reyhard]

@ Fixed some AH-64 rpt errors about missing MFD icons
small cleanup in AH-64 model (uvsets, named properties)

[9/20/2018 3:15:50 PM][0.4.9][R3267][reyhard]

^ Reduced PhysX track width to decrease chance of wheels with other vehicle wheels collision which usually leads to backflips

[9/19/2018 8:49:58 PM][0.4.9][R3266][reyhard]

adjusted dust alpha

[9/19/2018 3:04:22 PM][0.4.9][R3265][reyhard]

^ Tweaked M113 Mk19 gunner animation
@ Fixed missing launchers in Zeus crate menu
^ Improved HIMARS MLRS launch VFX
^ Reduced glass reflection in AH-64 cockpit

[9/18/2018 9:28:43 PM][0.4.9][R3264][reyhard]

More tweaks to MLRS fire effects - tweaked amount of dust & attempt at adding missile trail

[9/18/2018 8:31:54 PM][0.4.9][R3263][reyhard]

@ Fixed tooltip text for C-Mag

[9/18/2018 8:28:35 PM][0.4.9][R3262][da12thMonkey]

more oops

[9/18/2018 12:55:57 PM][0.4.9][R3261][sykoCrazy]

@ [UH-60]Fixed missing "main rotor hide" selection in one res LOD, causing duplicated rotors at some distances.

[9/18/2018 12:36:31 PM][0.4.9][R3260][da12thMonkey]

Oops

[9/17/2018 9:47:35 PM][0.4.9][R3259][reyhard]

^ Improved MLRS scripted firing effects
UV sets cleanup for HIMARS
some experimental tweaks for AI autolanding

[9/17/2018 9:01:17 PM][0.4.9][R3258][da12thMonkey]

^ Modified US aircraft magazine displaynames and added `descriptionShort` tooltips (mouse over mag name in Dynamic Loadouts UI for a more detailed description)

[9/17/2018 3:14:13 PM][0.4.8][R3257][Soul_Assassin]

[0.4.9] Version bump

[9/17/2018 1:16:03 PM][0.4.8][R3256][sykoCrazy]

+ Tan pilot helmets to reflect change in US Army standard issue helmet color.

[9/17/2018 9:20:26 AM][0.4.8][R3255][reyhard]

@ Fixed M113 gunner was using wrong LOD when in optic mode
@ Fixed M113 gunner view offset in non optic mode
@ Fixed M113 weapons were using wrong memory point for guns
^ AI should now engage M113 gunners

[9/16/2018 7:19:09 PM][0.4.8][R3254][Soul_Assassin]

added missing classes

[9/16/2018 4:38:04 PM][0.4.8][R3253][reyhard]

^ Added scripted particle effects to HIMARS (workaround for fire particles not working with pylon weapons - still WIP, missing dust circle and position has sometimes inncorrect offset)

[9/16/2018 3:45:51 PM][0.4.8][R3252][reyhard]

^ Adjusted tracks armor for USAF vehicles

[9/14/2018 3:19:11 PM][0.4.8][R3251][reyhard]

^ Corrected SLAP bullets muzzle velocity
work on MLRS fire effects

[9/14/2018 12:19:38 PM][0.4.8][R3250][da12thMonkey]

@ SPC marksman vest shadow would break when the vest was retextured (rogue 'camo' selection in SVLOD)

[9/13/2018 3:19:03 PM][0.4.8][R3249][da12thMonkey]

HIMARS dynamic loadouts UI pic

[9/10/2018 2:14:19 PM][0.4.8][R3248][reyhard]

^ Added experimental IHADSS workaround for user with triple monitor setup (PiP ratio)
^ Increased minimal hit for ERA blocks so they are no longer triggered by 12.7mm rounds
some WIP work on HIMARS weapons

[9/8/2018 4:09:41 PM][0.4.8][R3247][wld427]



[9/7/2018 2:44:22 PM][0.4.8][R3246][da12thMonkey]

Quick retexture of ATacMS, removing Russian markings etc.

[9/6/2018 10:51:00 PM][0.4.8][R3245][da12thMonkey]

- Cleared out some unused magazine classnames for 12x MLRS rockets. No longer needed for their intended purpose
^ `descriptionShort` property for MLRS/HIMARS magazines

WIP ATacMS (Blocks I and IV), using modified Tochka missile model as a stand-in. Mostly just needs configuration of min/max ranges. Block II/BAT not ingame yet
Separated `hardpoints[]` for guided and unguided MLRS rockets (in case of possible pre-2006 and export configurations of MLRS)

[9/5/2018 9:21:29 PM][0.4.8][R3244][reyhard]

added test himars pylons

[9/4/2018 8:20:55 PM][0.4.8][R3243][reyhard]

small optimization

[9/2/2018 10:58:40 AM][0.4.8][R3242][reyhard]

fixes to grip system

[9/1/2018 8:18:05 AM][0.4.8][R3241][reyhard]

Fixed ammo count of magazine which was readded to inventory during weapon transformation

[8/31/2018 2:21:32 PM][0.4.8][R3240][reyhard]

^ Tweaked HP of ERA blocks on USAF vehicles

[8/31/2018 2:16:50 PM][0.4.8][R3239][reyhard]

^ Added geometry occluder to HIMARS cargo LOD

[8/31/2018 1:49:25 PM][0.4.8][R3238][reyhard]

fixed missing magazines after npz/fold/grip code tweak

[8/31/2018 6:35:29 AM][0.4.8][R3237][reyhard]

@ Fixed gripod system so it keeps currently loaded magazine when transforming

[8/30/2018 5:01:32 PM][0.4.8][R3236][reyhard]

optimized cargo shadow lod

[8/29/2018 7:42:04 AM][0.4.8][R3235][reyhard]

@ Fixed A10A landing gear light

[8/28/2018 7:44:10 PM][0.4.8][R3234][reyhard]

^ Adjusted default radar range in info panels

[8/27/2018 7:02:11 PM][0.4.8][R3233][reyhard]

^ Improved HIMARS cargo shadow LOD
^ Added dedicated driver anim to HIMARS

[8/27/2018 2:39:27 PM][0.4.8][R3232][reyhard]

tweaked LOAL for AGM-114K

[8/27/2018 1:02:24 PM][0.4.8][R3231][reyhard]

some more bomb tweaking

[8/27/2018 12:41:49 PM][0.4.8][R3230][reyhard]

^ Increased Mk82 bomb damage to be in line with GBU-12

[8/26/2018 6:49:15 PM][0.4.8][R3229][reyhard]

@ Removed M142 HIMARS driver turn out action

[8/26/2018 2:56:00 PM][0.4.8][R3228][reyhard]

^ Tweaked M230 AI dispersion coef - AI should be more accurate
some more tweaks to hellfire physic - reduced lead param & increased manev.

[8/26/2018 1:47:11 PM][0.4.8][R3227][reyhard]

increased descend range for agm114L missiles

[8/26/2018 1:38:56 PM][0.4.8][R3226][reyhard]

^ Added maddog autoseek to AIM-120 missiles

[8/26/2018 1:32:20 PM][0.4.8][R3225][da12thMonkey]

PMAG had a superfluous named selection in the pilot LOD

[8/26/2018 8:24:54 AM][0.4.8][R3224][reyhard]

^ Another tweak to Hellfire accuracy

[8/26/2018 7:18:40 AM][0.4.8][R3223][reyhard]

^ Tweaked Bunker Busters TOWs with submunition parameters - they should be able to penetrate light structures and spread thermobaric blast wave inside

[8/26/2018 6:40:12 AM][0.4.8][R3222][reyhard]

M1 tanks & M2 IFVs should be now vulnerable to bombs & heavy satchels

[8/25/2018 7:04:03 PM][0.4.8][R3221][reyhard]

@ Fixed AH-64 & AH-1Z helicopter HMD target icon

[8/25/2018 5:56:32 PM][0.4.8][R3220][da12thMonkey]

Standalone M320 GL wasn't using the same magazine reload sound as the rifle-mounted version (had sound from BIS "M320" bolt-action sniper rifle)

[8/25/2018 5:18:41 PM][0.4.8][R3219][reyhard]

@ M2 Bradley cargo had fault cargoProxyIndexes

[8/25/2018 8:34:13 AM][0.4.8][R3218][reyhard]

@ Fixed some rare script error when TADS view was shown on MFD
^ IHADSS PNVS view is no longer working when PNVS or cockpit electronic systems are damaged

[8/24/2018 9:33:37 AM][0.4.8][R3217][reyhard]

another tweak

[8/24/2018 9:29:56 AM][0.4.8][R3216][reyhard]

added helper hitpoint to bradley

[8/24/2018 8:51:23 AM][0.4.8][R3215][reyhard]

@ Fixed M109 destruction materials

[8/23/2018 3:25:18 PM][0.4.8][R3214][reyhard]

^ Added proper nameSound parameter to smoke shells

[8/23/2018 1:06:53 PM][0.4.8][R3213][da12thMonkey]

@ Vehicle-in-Vehicle `dimensions[]` memory points were not properly set up in several FMTV and HEMTT variants

[8/22/2018 6:49:25 PM][0.4.8][R3212][reyhard]

^ Increased SLAT armor minimal hit - no longer destroyable with small firearms
^ Moved back AH-64 pilot cockpit light to reduce flare effect during night

[8/22/2018 4:14:26 PM][0.4.8][R3211][da12thMonkey]

@ Some cfgweapons classes (mainly headgear) missing `dlc = "RHS_USAF";` attribute

Added Author_Macro_DLC shorthand for adding these in future

[8/22/2018 12:28:46 PM][0.4.8][R3210][reyhard]

@ PNVS movement limits were inverted (forgot that min & max values in pilotCamera class are inverted...)
@ Fixed potential script error in MFD switching script
^ Improved PNVS deinitialization 
^ Added flashing cross in flight mode when PNSV is out of its limits

[8/22/2018 8:08:40 AM][0.4.8][R3209][da12thMonkey]

@ Glass on HIMARS right-hand door did not follow door opening animation
@ Disabled 'top' versions of laser attachments on MP7A1. They don't fit
^ SU-230A SpecterDR scopes `descriptionShort` now denotes them as being for 7.62mm weapons

[8/22/2018 7:31:08 AM][0.4.8][R3208][reyhard]

@ Fixed Mk-14 ironsight
@ Fixed M2 Bradleys hull hitpoints being immortal
@ Fixed M2A2 (basic without BUSK) was missing tracks hitpoints 
@ Fixed CH-53 joystick was moving in wrong direction
@ Fixed woodland AH-64 crew was missing IHADSS helmet during night
@ Fixed PNVS turning off after going into optic mode
@ Fixed AI units with gripods were selecting pistols after spawning
@ Fixed script error after being killed when using IHADSS
@ Fixed AH-64 MFD had big 0 when using AFM & extra gauges were enabled in options
^ Reduced cost of 45ACP ammo - AI should no longer prefer using Colt over rifle
^ Reduced AH-64 FCR range to 8km from 11
^ Increased emissive value of AH-64 MFDs
^ Improved PNVS accuracy (missing AGL to ASL conversion)

[8/21/2018 10:45:47 PM][0.4.7][R3207][Soul_Assassin]

[0.4.8] Version bump

[8/20/2018 6:47:24 PM][0.4.7][R3206][keplager]

^ UH-60M Yaw mixing unit now conforms to expectations (pedal neutral at 60 KCAS)

[8/19/2018 5:56:52 PM][0.4.7][R3205][da12thMonkey]

^ Adjusted position of Caiman OGPK turret axis

[8/19/2018 5:02:14 PM][0.4.7][R3204][reyhard]

^ Added text fire mode indicator to A10A
^ Removed old compass from MELB UI

[8/19/2018 10:24:18 AM][0.4.7][R3203][reyhard]

^ Increased AH-64 PNVS turn rate to 120 deg per sec
^ AH-64 AI can now switch between laser & radar guided missiles

[8/18/2018 8:27:35 PM][0.4.7][R3202][reyhard]

@ AH-64 gunner couldn't use TADS view in some MFD pages combinations
@ Unified AH-64 TADS zoom on pilot & gunner stations

[8/18/2018 7:42:17 PM][0.4.7][R3201][reyhard]

!CLEARTEMP!
changed IHADSS PNVS view to more green version

[8/18/2018 6:00:31 PM][0.4.7][R3200][reyhard]

^ AH-64 PNVS monocular view is now transparent & HDU is visible

[8/18/2018 4:26:18 PM][0.4.7][R3199][reyhard]

@ Fixed AH-64 missing gunner feed when scrolling to radar MFD page
@ Fixed AH-64 AA/AG radar modes key handlers were not properly initialized

[8/18/2018 11:29:31 AM][0.4.7][R3198][da12thMonkey]

^ Reduced zeroing range of standalone RMR and MRDS sights, to match the versions mounted on top of MDO/SpecterDR

[8/17/2018 7:14:57 PM][0.4.7][R3197][reyhard]

^ Added AI handler for AGM-114K usage
@ Disabled ability to lock on ground targets with F-22 gun (attempt to fix kamikaze dive attacks on ground targets)

[8/17/2018 1:45:24 PM][0.4.7][R3196][reyhard]

@ SFM wheel brakes UI element is now hidden when RTD is enabled

[8/17/2018 1:27:32 PM][0.4.7][R3195][reyhard]

^ Tweaked AI usage of AGM-114K
^ Tweaked all AGM-114 precision
^ Tweaked ATGM oversteer behavior

[8/16/2018 6:09:46 PM][0.4.7][R3194][reyhard]

@ Fixed .rtm related .rpt errors

[8/16/2018 2:34:19 PM][0.4.7][R3193][reyhard]

@ Removed incomingMissileDetectionSystem from ground vehicles
^ Calibrated IHADSS PNVS view & added safezones so position of IHADSS should be same on all screen resolutions

[8/15/2018 2:12:45 PM][0.4.7][R3192][reyhard]

@ Fixed .rpt error for UCP Combat crewman 

[8/15/2018 10:04:50 AM][0.4.7][R3191][reyhard]

^ Tweaked M1 & M2 Fire Geometry & hitpoints

[8/15/2018 7:44:30 AM][0.4.7][R3190][reyhard]

ultimate fixirito for SLAT

[8/15/2018 7:11:42 AM][0.4.7][R3189][reyhard]

^ Removed _generalMacros from RHS configs

[8/14/2018 9:07:30 PM][0.4.7][R3188][reyhard]

slat fixing attempt 2

[8/14/2018 8:29:48 PM][0.4.7][R3187][reyhard]

^ Tweaked M1 ammo hit dependency 

[8/14/2018 6:03:02 PM][0.4.7][R3186][reyhard]

M1A2SEPv2 was missing SLAT bone

[8/14/2018 2:26:45 PM][0.4.7][R3185][reyhard]

@ Fixed HIMARS commander could fire when turned in
@ Fixed interior light action

[8/14/2018 1:18:27 PM][0.4.7][R3184][da12thMonkey]

@ Some weapons did not have visible muzzle attachments when running RHS:USAF standalone (missing 'linkProxy' definition)

[8/14/2018 12:53:05 PM][0.4.7][R3183][da12thMonkey]

@ Floating mag pouch shadows on Rifleman and Team leader SPCS vests

[8/13/2018 8:06:22 PM][0.4.7][R3182][reyhard]

renamed binoculars

[8/13/2018 8:03:28 PM][0.4.7][R3181][reyhard]

tweaked M1 Fire Geo micro holes

[8/13/2018 4:47:30 PM][0.4.7][R3180][reyhard]

^ Added SLAT sim to M1A1 TUSK I
^ Tweaked 3rd person camera of F-22


[8/13/2018 3:12:02 PM][0.4.7][R3179][reyhard]

^ Increased antirollbar force on Cougars
^ Tweaked Geo Physx & Fire Geometry of Cougars (bottom hull mainly)

[8/13/2018 2:24:11 PM][0.4.7][R3178][reyhard]

@ Fixed accidentally removed AH-64 gunner UI handler which prevent camera jump when direction stabilization in NFOV was activated

[8/13/2018 12:30:51 PM][0.4.7][R3177][reyhard]

@ Fixed TOW launching sounds
@ Fixed TOW UI mode indication
^ Added disableWheelsWhenDestroyed = 1 to USAF helicopters
^ Tweaked penetration of M993 round

[8/13/2018 12:12:13 PM][0.4.6][R3176][Soul_Assassin]

[0.4.7] Version bump

[8/12/2018 9:04:01 PM][0.4.6][R3175][reyhard]

duh

[8/12/2018 8:51:33 PM][0.4.6][R3174][reyhard]

AI dispersion coef tweaks
^ Tweaked M1A2 fire geometry (WIP)
^ Added SLAT destruction to M1 TUSK tanks


[8/12/2018 11:19:02 AM][0.4.6][R3173][reyhard]

added sfm brakes to ah64
!CLEARTEMP!

[8/12/2018 10:51:42 AM][0.4.6][R3172][reyhard]



[8/12/2018 10:20:51 AM][0.4.6][R3171][reyhard]

^ Tweaked MRZR-4 fire geometry

[8/12/2018 1:05:21 AM][0.4.6][R3170][gurdy]

^ Tweaked M1043 textures

[8/11/2018 2:27:14 PM][0.4.6][R3169][da12thMonkey]

Various M24 rifle accessories were not accessible through Zeus/Eden/Ammobox
Randomised buttstock pouch on M24

[8/10/2018 7:55:59 PM][0.4.6][R3168][da12thMonkey]

Added IHADSS stand-in helmet to Zeus, Eden and Arsenal crate

[8/10/2018 7:16:56 PM][0.4.6][R3167][da12thMonkey]

Fixed bone overlap in MRZR shadow LOD

[8/10/2018 6:07:47 PM][0.4.6][R3166][reyhard]

another fix for pnsv elev 

[8/10/2018 4:26:32 PM][0.4.6][R3165][da12thMonkey]

Cluster bomb Mines and UXO should now sink in water

[8/10/2018 6:58:16 AM][0.4.6][R3164][reyhard]

fixed PNSV movement in Y axis

[8/8/2018 8:41:59 PM][0.4.6][R3163][da12thMonkey]

Apache pilot edPrev images
Updated edPrev images for Airborne units, following SPCS vest changes

[8/8/2018 3:07:14 PM][0.4.6][R3162][reyhard]

changed COM of 114K & move its geometry to center of model to improve AI firing
increased trackoversteer

[8/8/2018 1:52:54 PM][0.4.6][R3161][da12thMonkey]

@ Error popups when opening inventory UI, with M107 or M590 equipped

[8/6/2018 3:29:40 PM][0.4.6][R3160][reyhard]

^ Added AH-64 MFD to AH-1Z as a temporary solution until proper MFD is ready for it
^ Added text fire mode indicator to UH-1/60 & MELBs
fixed gun indicator in MFD

[8/5/2018 8:26:39 PM][0.4.6][R3159][j0zh94]

^ Darkened green smoke grenade for vests

[8/5/2018 2:01:24 PM][0.4.6][R3158][da12thMonkey]

Fixed Cougar fire geometry LOD

[8/5/2018 8:17:18 AM][0.4.6][R3157][reyhard]

fixed script error when geting out from AH-64

[8/5/2018 7:57:32 AM][0.4.6][R3156][reyhard]

disabled PiP MFD restart till it's ironed out

[8/4/2018 2:29:10 PM][0.4.6][R3155][reyhard]

^ Added AI missile assistant for 114K
@ Fixed M2 missing cross in 3rd person when cross is enabled in difficulty settings

[8/2/2018 10:14:45 AM][0.4.6][R3154][reyhard]

^ Added parameter to hide PhysX suspension upon destruction for fixed wing aircracts 

[7/31/2018 2:30:04 PM][0.4.6][R3153][reyhard]

^ Removed _generalMacro from USAF configs

[7/30/2018 11:04:37 PM][0.4.6][R3152][j0zh94]

^ Updated Airborne vests with new SPCS

[7/30/2018 7:05:27 PM][0.4.6][R3151][reyhard]

added some more missing items

[7/30/2018 6:58:42 PM][0.4.6][R3150][reyhard]

@ USAF inventory items (vest/helmets/uniforms) were missing in Zeus

[7/30/2018 6:43:55 PM][0.4.6][R3149][reyhard]

added new vest as editor placable items
added new icons

[7/30/2018 11:04:03 AM][0.4.6][R3148][da12thMonkey]

^ Increased `magazineReloadTime` of CROWS-mounted M2 machine gun (positioned away from operator, more intricate feed system etc.)

CROWS Caiman switched back to 400rnd magazines (1600rnds in 4x 400rnd magazines)

[7/30/2018 10:23:00 AM][0.4.6][R3147][reyhard]

fixed missing colon

[7/30/2018 10:17:10 AM][0.4.6][R3146][reyhard]



[7/30/2018 10:12:27 AM][0.4.6][R3145][reyhard]

^ Added small hint to A-10 TVM script about necessity to press nightvision key in order to activate screen
^ Improved taxing behavior of fixed wing vehicles
changed MRAP ammo count to 15 mags
minor tweaks to F-22 HUD

[7/30/2018 6:01:55 AM][0.4.6][R3144][Redphoenix]

Alpha of M1025 Snorkels is not working ingame - potential fix by fully rebuilding the pbo
!CLEARTEMP!


[7/29/2018 11:24:07 PM][0.4.6][R3143][j0zh94]

^ Added SPCS vest config

[7/29/2018 11:22:12 PM][0.4.6][R3142][j0zh94]

+ Added more variants of SPCS vest

[7/29/2018 9:05:11 PM][0.4.6][R3141][RichardsD]

@ Makes ammo more easily readable in MRAP configs (Caiman, Cougar, RG33l)

[7/29/2018 9:00:45 PM][0.4.6][R3140][RichardsD]

@ Adds more ammmo to Caiman RCWS

[7/29/2018 8:59:55 PM][0.4.6][R3139][RichardsD]

@ Adds more ammmo to Mk 19 and 50 Cal MRAPS (Cougar, Caiman, RG33L)

[7/29/2018 4:14:35 PM][0.4.6][R3138][reyhard]

added missing files

[7/29/2018 4:08:04 PM][0.4.6][R3137][reyhard]

+ Added ability to disable part of vehicle UI in RHS Game Options
added wheel brakes UI element
added SFM wheel brakes to CH-47

[7/27/2018 6:00:54 AM][0.4.6][R3136][reyhard]

forgot to update macros

[7/26/2018 3:49:45 PM][0.4.6][R3135][da12thMonkey]

^ Added rail cover randomization to M16A4 (~30% chance of being hidden)

[7/26/2018 3:44:27 PM][0.4.6][R3134][reyhard]

IHADSS tweaks

[7/26/2018 1:41:09 PM][0.4.6][R3133][reyhard]

^ Added rail cover randomization to M4

[7/26/2018 9:41:23 AM][0.4.6][R3132][reyhard]

testing ammo event handlers
disabled M2 hatch actions

[7/24/2018 3:11:33 PM][0.4.6][R3131][reyhard]

added hybrid solution to ch53 suspension

[7/24/2018 2:50:29 PM][0.4.6][R3130][da12thMonkey]

Fixed bone overlap on ESSS Blackhawk wheels

[7/24/2018 2:25:43 PM][0.4.6][R3129][reyhard]

forgot to commit wheel brakes being on by default in sfm

[7/22/2018 8:23:59 PM][0.4.6][R3128][reyhard]

^ Disabled hiddenSelectionMaterials on M1 tanks
^ Tweaked TUSK I reflector power

[7/22/2018 4:20:41 PM][0.4.6][R3127][sykoCrazy]

^ UH-1Y glass no longer blinds pilots
+ MELB RWR for copilot
^ MELB flight model
@ MELB copilot camera position(was clipping through FLIR model)
@ MELB pilots were not able to move the FLIR MFD
@ AH-6 aimdot has been adjusted
@ AH-6 default loadout changed to "light" variant


[7/22/2018 2:11:08 PM][0.4.6][R3126][reyhard]

+ Added ability to disable vanilla locking boxes - by default option is off and can be changed by checking "Targeting UI Off" checkbox in RHS Menu Options

[7/15/2018 10:06:11 AM][0.4.6][R3125][reyhard]

Tweaked AA sensor in MFD

[7/15/2018 7:57:28 AM][0.4.6][R3124][reyhard]

Added PNVS in IHADSS (toggle via night vision key)

[7/15/2018 6:37:43 AM][0.4.6][R3123][reyhard]

token removal

[7/14/2018 10:48:03 PM][0.4.6][R3122][reyhard]

added IHADSS overlay

[7/14/2018 9:18:49 PM][0.4.6][R3121][reyhard]

AH64D:
added AA & AG mode switch to FCR
added ability to control FCR direction
added FCR wiper animation in MFD
added turn rate & proper slip indicator
added better fire mode detection
added time to waypoint indicator

[7/13/2018 9:22:32 AM][0.4.6][R3120][reyhard]

fixed missing bracket

[7/10/2018 7:40:32 PM][0.4.6][R3119][reyhard]

added fire mode checker for MFD
added air radar to AH-64 (disabled by default + there is no way to turn it on)

[7/10/2018 1:49:12 PM][0.4.6][R3118][reyhard]

^ Added winch hitpoints to UH-60M

[7/9/2018 8:36:36 PM][0.4.6][R3117][reyhard]



[7/9/2018 6:40:23 PM][0.4.6][R3116][da12thMonkey]

^ Added damper and wheel animations to CH-53E.
Test PhysX suspension for CH-53E

N.B. the simulated PhysX wheels do not seem to retract in SFM currently (assuming I didn't just cock it up).
May comment out the physX stuff later and use older `altRadar` and AFM/RTD animation sources for the new dampers and wheels instead

[7/9/2018 4:04:48 PM][0.4.6][R3115][j0zh94]

^ Unified ESAPI plates for USAF vests

[7/8/2018 9:36:53 PM][0.4.6][R3114][reyhard]

some AH64 MFD handler scripts work

[7/8/2018 12:05:25 PM][0.4.6][R3113][reyhard]

another small tweak to m134 gunner anim

[7/8/2018 11:59:10 AM][0.4.6][R3112][reyhard]

^ Added zeroing to Mark V weapons
^ Added radar to Mark V
@ Fixed ironsight memory points for Mark V
@ Merged roadway LOD to main model, removed script & fixed Mark V falling from 5 meters when spawned via createVehicle (i.e. in Virtual Garage)
^ Changed Mark V muzzle flashes
simplified roadway LOD 
close T1573
close T1621

[7/8/2018 8:55:23 AM][0.4.6][R3111][reyhard]

@ Fixed Stinger pod ghost LOD

[7/6/2018 2:10:34 PM][0.4.6][R3110][reyhard]

added test wheel brakes to UH-60M in SFM - there is no UI indication if it's turned on or off atm

[7/5/2018 3:54:50 PM][0.4.6][R3109][da12thMonkey]

Added new .rtm for Cougar driver
Fixed visible mesh holes at the back of the toolboxes, and smoothed out some sharp edges on ladder rungs and door handles

[7/5/2018 2:15:24 PM][0.4.6][R3108][reyhard]

reduced EPE damage for AH64 & UH60

[7/5/2018 1:52:15 PM][0.4.6][R3107][reyhard]

updated preloaded addons list

[7/5/2018 1:45:34 PM][0.4.6][R3106][reyhard]

^ Added TILS spider to A10A HUD
fixed HIMARS destruction type

[7/4/2018 10:42:28 PM][0.4.6][R3105][da12thMonkey]

Cougar gauge animations
Fixed: M2 Cougar cargo proxy positions had not been updated in revision 3074

[7/4/2018 9:00:50 PM][0.4.6][R3104][RichardsD]

@ Fixed Cougar MK19 name to correct "MK19" instead of M2

[7/4/2018 2:42:34 PM][0.4.6][R3103][reyhard]

purge part 2

[7/4/2018 2:33:16 PM][0.4.6][R3102][reyhard]

@ Removed some unnecessary config definitions from root config which could cause issues with other mods loaded

Also removed 
class WeaponFireGun;
class WeaponCloudsGun;
class WeaponFireMGun;
class WeaponCloudsMGun;
since it doesn't serve any purpose in Arma 3

[7/3/2018 8:59:22 PM][0.4.6][R3101][reyhard]

^ Tweaked AH-64 pilot animation
added laser page
tweaked ah64 UI

[7/3/2018 2:59:34 PM][0.4.6][R3100][reyhard]

^ Added interior light to AH-64 cockpit
tweaked engine & weapons pages

[7/2/2018 11:50:52 PM][0.4.6][R3099][RichardsD]

@ Adds hard edge to Cougar Hood

[7/2/2018 9:26:46 PM][0.4.6][R3098][reyhard]

reverted startup time

[7/2/2018 9:26:20 PM][0.4.6][R3097][reyhard]

AH64 cleanup
added wip missile page


[7/2/2018 5:37:07 PM][0.4.6][R3096][da12thMonkey]

Cougar FFV tweaks

[7/1/2018 10:10:00 PM][0.4.6][R3095][reyhard]



[7/1/2018 9:59:14 PM][0.4.6][R3094][reyhard]

more work on AH-64 MFDs & HMD:
* added GUN & RKT pages
* fixed some rpt errors
* added LOAL HMD reticles
* added new gunner animation
* some experiments with AH-64 hitpoints
* tweaked MFD SMDI

[7/1/2018 11:09:01 AM][0.4.6][R3093][reyhard]

forgot to include some more helis in physx rotors purge

[7/1/2018 11:04:50 AM][0.4.6][R3092][reyhard]

^ Added PhysX suspension to UH-60M
^ Added RTD hitpoints to UH-60M
^ Removed rotors from PhysX LOD of helicopters
enabled MFD screens from AH-64 gunner

[6/30/2018 4:04:41 PM][0.4.6][R3091][da12thMonkey]

^ Added PhysX suspension and RTD wheel animations to CH-47 Chinook

[6/30/2018 10:45:31 AM][0.4.6][R3090][reyhard]

^ Added PhysX suspension to AH-64

[6/29/2018 2:30:13 PM][0.4.6][R3089][reyhard]

^ Added RTD wheel animation to AH-64
^ Added additional RTD Hitpoints (Hydraulics,Transmission,Stabilizators) 
tweaked mfd engine when using RTD

[6/29/2018 10:22:54 AM][0.4.6][R3088][reyhard]

fixed duplicated mine detector in ammo crate cfg

[6/28/2018 11:03:43 PM][0.4.6][R3087][ballistic09]

Added new magazines to ammoboxes

[6/26/2018 7:53:19 PM][0.4.6][R3086][reyhard]

some more tweaks to weapon mfd

[6/26/2018 3:15:32 PM][0.4.6][R3085][reyhard]

some tweaks weapon mfd

[6/25/2018 2:30:56 PM][0.4.6][R3084][reyhard]

!CLEARTEMP!
^ Tweaked TI texture of rocket & Hellfire pods
^ Reduced chaff/flare count on AH-64D to 60 rounds
ah64 cleanup


[6/25/2018 8:05:02 AM][0.4.6][R3083][reyhard]

fixed small typos

[6/24/2018 8:43:38 PM][0.4.6][R3082][reyhard]

oops, forgot to add new hpp

[6/24/2018 8:40:54 PM][0.4.6][R3081][reyhard]

+ Added IHADSS placeholder (using HGU model atm)
added weapon page basic shape
tweaked max fuel capacity
tweaked engine power indicators

[6/24/2018 8:09:47 PM][0.4.6][R3080][reyhard]

added 2 mfd helpers

[6/24/2018 12:05:04 AM][0.4.6][R3079][sykoCrazy]

+ Added 2 back seats and tailgate animationSource. Need feedback on this. Good idea/bad idea?

[6/23/2018 11:56:32 PM][0.4.6][R3078][sykoCrazy]

@ Fixed sound issue.. was using MRAP sounds instead of quadbike's

[6/23/2018 3:14:49 PM][0.4.6][R3077][da12thMonkey]

Added second DUKE/Chamelion hitpoint class to Cougar, required by ECM script

[6/23/2018 11:34:37 AM][0.4.6][R3076][reyhard]

fuel page tweaking - few bits are missing

[6/22/2018 8:20:35 PM][0.4.6][R3075][reyhard]

added test fuel page

[6/22/2018 6:20:14 PM][0.4.6][R3074][da12thMonkey]

Cougar FFV anim set with legs extended
Changed cargo anims and proxy positions for a better fit (couple of spots may need custom anims)
Section and UV set cleanup

[6/21/2018 8:16:39 PM][0.4.6][R3073][keplager]

@ AH-64 Changed engine rotationresistance factor to allow for single engine operations.

[6/21/2018 7:22:09 PM][0.4.6][R3072][keplager]

@ UH-60M Single engine flight is possible now (lowered engine rotation resistance).

[6/21/2018 2:30:19 PM][0.4.6][R3071][reyhard]

small tweak to engine mfd page

[6/21/2018 2:14:58 AM][0.4.6][R3070][keplager]

@ AH-64 changed engine and transmission max torque values.

[6/21/2018 12:01:36 AM][0.4.6][R3069][keplager]

@ AH-64 Updated maxTorque to coincide with 16000 lbs OGE hover.

[6/20/2018 2:33:07 PM][0.4.6][R3068][da12thMonkey]

Added some colour-space padding to the alpha texture for Cougar's guages

[6/20/2018 2:27:49 PM][0.4.6][R3067][reyhard]

some tweaks to engine page

[6/20/2018 11:34:17 AM][0.4.6][R3066][da12thMonkey]

Some adjustments to AA missile allocations

[6/19/2018 8:44:44 PM][0.4.6][R3065][reyhard]

!CLEARTEMP!

[6/19/2018 8:40:29 PM][0.4.6][R3064][reyhard]



[6/19/2018 8:37:01 PM][0.4.6][R3063][reyhard]



[6/19/2018 8:33:40 PM][0.4.6][R3062][reyhard]

!CLEARTEMP!

[6/19/2018 8:21:30 PM][0.4.6][R3061][reyhard]

batch no2

[6/19/2018 8:17:14 PM][0.4.6][R3060][reyhard]

packing fix

[6/19/2018 4:46:03 PM][0.4.6][R3059][Kllrt]

Added heavy WIP AH64 (Pls no kill)

[6/19/2018 3:01:59 PM][0.4.6][R3058][reyhard]

^ Added geometry occludder to AH-64 cockpit

[6/18/2018 8:54:55 PM][0.4.6][R3057][reyhard]

it's now possible to switch TADS MFD camera feed without going to camera:
* ctrl+n (check actionKeysNames "TransportNightVision" if it's not working) - switch camera mode
* pg up/down - switch camera zoom (keybinds need change - suggestions are welcome)

[6/18/2018 5:13:32 PM][0.4.6][R3056][da12thMonkey]

Cougar Garage icons

[6/18/2018 2:38:34 PM][0.4.6][R3055][reyhard]

added mfd switch script to ah64 - TADS view from MFD should be working now

[6/17/2018 9:20:45 PM][0.4.6][R3054][RichardsD]

@ Fixes the WD texture to have black wheels, and black exhaust

[6/17/2018 8:39:17 PM][0.4.6][R3053][da12thMonkey]

Fixed Cougar antena anims
Added flag proxy

[6/17/2018 7:09:44 PM][0.4.6][R3052][da12thMonkey]

Hid 4x4 RG-33 (initial step in replacement by Cougar CAT I MRAP)
EdPrev images for Cougars
Fixed Woodland Cougar classname inconsistency
Increased colour padding on alpha texture for external markings

[6/17/2018 4:41:43 PM][0.4.6][R3051][RichardsD]

@ Fixes texture map error on the Cougar interior

[6/17/2018 4:33:21 PM][0.4.6][R3050][RichardsD]

@ Adds Fixed Cougar names

[6/17/2018 4:21:33 PM][0.4.6][R3049][RichardsD]

+ First commit of the Cougar 4x4 MRAP
@ See the ticket https://dev.rhsmods.org/T769 to see what work must be done still

[6/17/2018 11:44:01 AM][0.4.6][R3048][reyhard]

less randomized pages selection

[6/17/2018 11:41:19 AM][0.4.6][R3047][reyhard]

added non working TADS page

[6/17/2018 10:50:14 AM][0.4.6][R3046][reyhard]

work on AH64 Flight Page
added ability to toggle between MFD pages (not exactly - it's using random selection now on user1 or 2 press)
F22 MFD scaling

[6/16/2018 10:04:41 PM][0.4.6][R3045][reyhard]

ah64 mfd work - added flight page

[6/15/2018 7:04:56 PM][0.4.6][R3044][da12thMonkey]

Added ATAS to the stubby-winged UH-60s too

[6/15/2018 5:48:23 PM][0.4.6][R3043][reyhard]

ah64 mfd update

[6/15/2018 3:03:50 PM][0.4.6][R3042][reyhard]

updated AH-64 MFD (WIP)

[6/15/2018 8:34:35 AM][0.4.6][R3041][reyhard]

some test tweaks

[6/14/2018 9:56:25 PM][0.4.6][R3040][gurdy]

- scoped out RAH66 until retexture is complete

[6/14/2018 2:16:23 PM][0.4.6][R3039][reyhard]

^ Added buoyancy = 1 param to some USAF helicopters
improved LOAL - now it should more or less work (AI support in progress)

[6/13/2018 7:19:06 PM][0.4.6][R3038][da12thMonkey]

^ Firing From Vehicles capabilities for front passenger seat on FMTV Special Operations Vehicles
Close T2393

[6/12/2018 4:10:46 PM][0.4.6][R3037][da12thMonkey]

ATAS launcher weapon missing compat with the AH-64 mag

[6/12/2018 2:58:35 PM][0.4.6][R3036][reyhard]

scratches on cockpit glass test

[6/12/2018 2:24:53 PM][0.4.6][R3035][reyhard]

configured ATAS pods

[6/11/2018 10:43:36 PM][0.4.6][R3034][RichardsD]

@ Adds Caiman better detailed windows

[6/11/2018 9:54:34 PM][0.4.6][R3033][RichardsD]

@ Adds less transparent and more textured glass to RG33L

[6/11/2018 9:11:06 PM][0.4.6][R3032][reyhard]

forgot to save
ps: model from Franz & nodunit mod


[6/11/2018 9:09:03 PM][0.4.6][R3031][reyhard]

+ Added modified (retextured, reuved + bashed existing stinger tube models) ATAS pod 

[6/11/2018 3:14:53 PM][0.4.6][R3030][reyhard]

fixed F-22 pilot shadow lod (was using shadow vol view pilot while only shadow vol view cargo is used by game)
some more ah-64 HMD tweaks

[6/11/2018 9:52:43 AM][0.4.6][R3029][reyhard]

fixed alpha sorting on FFAR rockets

[6/11/2018 3:43:28 AM][0.4.6][R3028][RichardsD]

@ Makes a much nicer step texture for the Caiman rear, instead of the terrible non-transparent version

[6/10/2018 7:47:06 PM][0.4.6][R3027][RichardsD]

@ Fixes glitchy suspension component with bad textures on the RG33L

[6/10/2018 6:51:19 PM][0.4.6][R3026][reyhard]

@ Fixed UH-1Y observer camera
reduced amount of spal from M230 autocannon
some shitty experimentations with LOAL
work on ah-64 HMD:
* tweaked waypoints
* added new radar icons
* added pitch ladder in cruise mode
* added head tracker icon

[6/9/2018 11:13:43 PM][0.4.6][R3025][RichardsD]

@ changed face order for clan decal and went to one compartment

[6/9/2018 1:13:37 PM][0.4.6][R3024][reyhard]

^ Added PNVS & TADS view from pilot seat
^ Added new font from Franz & NodUnit AH-64 mod
^ Limited AH-64 cannon movement
^ Improved AH-64 HMD (WIP)

[6/8/2018 4:21:27 PM][0.4.6][R3023][reyhard]

temporarily disabled some wip ui

[6/8/2018 2:08:37 PM][0.4.6][R3022][reyhard]

@ Fixed M9 & Glock bullet speed
^ Added burst limiter to AH-64 (WIP)
^ Tweaked short names for USAF air weapons

[6/8/2018 11:37:59 AM][0.4.6][R3021][reyhard]

^ Tweaked muzzle flashes rvmat
!CLEARTEMP!

[6/7/2018 9:12:49 PM][0.4.6][R3020][sykoCrazy]

@ Fixed CH-47 ramp animation

[6/7/2018 2:31:03 PM][0.4.6][R3019][reyhard]

^ Tweaked Hellfire DIR, LOAL LO/HI params
^ Tweaked missile fire effects
removed obsolete parameters

[6/7/2018 7:31:29 AM][0.4.6][R3018][reyhard]

more tweaks to Javelin
removed obsolete parameters

[6/6/2018 3:01:50 PM][0.4.6][R3017][reyhard]

@ Fixed Javelin motor fire hiding
@ Fixed Javelin top down mode - close T2391

[6/5/2018 8:43:03 PM][0.4.6][R3016][reyhard]

aligned ah64 gunBeg/End memory point - T2390 need testing

[6/5/2018 7:07:19 PM][0.4.6][R3015][reyhard]

fixed popup error with melbs

[6/5/2018 6:40:18 AM][0.4.6][R3014][reyhard]

another tweak to f-22 pilot anim

[6/2/2018 9:58:06 PM][0.4.6][R3013][Redphoenix]

@ Fixed excessive glare of XPS3

[6/2/2018 1:26:38 PM][0.4.6][R3012][da12thMonkey]

Adding the new rocket fly models to model.cfg for flame effects

[6/2/2018 3:06:50 AM][0.4.6][R3011][sykoCrazy]

@ Fixed filepath errors on the littlebird
^ upgraded rocketpods/hydra/hellfire textures
+ added some more common hydra warheads for future use maybe

[6/2/2018 2:22:42 AM][0.4.6][R3010][ballistic09]



[6/1/2018 10:37:30 PM][0.4.6][R3009][ballistic09]

Some RAH-66 tweaks

[6/1/2018 9:34:13 PM][0.4.6][R3008][sykoCrazy]

- Removed old wreck model

[6/1/2018 8:54:14 PM][0.4.6][R3007][sykoCrazy]

^ updated ammobox on gau-19 model

[6/1/2018 8:48:08 PM][0.4.6][R3006][sykoCrazy]

^ updated littlebird models/textures

[6/1/2018 1:01:26 PM][0.4.6][R3005][reyhard]

^ Tweaked gunner LOD of Stinger pod
^ Tweaked F-22 pilot anim

[6/1/2018 2:24:33 AM][0.4.6][R3004][gurdy]

+ M301 cannon for RAH-66

[5/31/2018 2:07:25 PM][0.4.6][R3003][reyhard]

^ Tweaked stall warning threshold values
more tweaks to AI ejection
fixed some artifacts in F22 MFD

[5/31/2018 3:47:00 AM][0.4.6][R3002][gurdy]

+ test vehicle

[5/30/2018 6:21:28 PM][0.4.6][R3001][da12thMonkey]

Added descriptions to Abrams barrel art index, until the system is replaced

[5/29/2018 9:13:18 PM][0.4.6][R3000][reyhard]

^ Added geometry occluder to F-22 cockpit
tweaked f22 details

[5/29/2018 8:53:14 PM][0.4.6][R2999][RichardsD]

@ Updated ammo allotment for RG33L MRAPs

[5/29/2018 3:07:53 PM][0.4.6][R2998][reyhard]

^ Added interior light to F-22 & A-10A
@ Fixed typo in air weapons config (weaponLockType instead of weaponLockSystem - radar locking detections were not working because of that)
tweaked HUD glass light


[5/28/2018 7:38:43 PM][0.4.6][R2997][sykoCrazy]

+ White HGU-56 helmet variant

[5/28/2018 2:56:12 PM][0.4.6][R2996][reyhard]

^ Added collision lights to F-22
@ Fixed ejection over water
^ Tweaked AI engagement ranges for AIM missiles
fixed target box misalignment in HUD
added target recognition to F22 MFD radar

[5/28/2018 12:21:26 PM][0.4.6][R2995][da12thMonkey]

Adjusted GBU-32 scale to match Mk83 bomb diameter
Adjusted Hardpoint configuration for GBU-32 to put it in 1000lb category and stop it loading on A-10A (JDAM was integrated on A-10C)

[5/28/2018 11:15:09 AM][0.4.6][R2994][reyhard]

repack

[5/27/2018 9:06:46 PM][0.4.6][R2993][reyhard]

rvmat tweak

[5/27/2018 8:54:09 PM][0.4.6][R2992][reyhard]

^ Improved F-22 textures
^ Added data link to F-22
^ Tweaked ejection script & changed simulation of canopies to thingX - should prevent possible crashes
+ Added static parachute for USAF ejection seats
more work on F-22 HUD & MFD

[5/27/2018 2:03:55 PM][0.4.6][R2991][da12thMonkey]

Added M240H turret weapons (for use with GREF UH-1, and maybe other helis in future)

[5/26/2018 8:18:27 PM][0.4.6][R2990][reyhard]

+ Added GBU-32 (WIP - no GPS guided functionality yet)
restructured airweapon folder a little bit
more work on F-22 MFD

[5/26/2018 3:45:02 PM][0.4.6][R2989][da12thMonkey]

USMC RG-33L config corrections

[5/26/2018 2:35:41 PM][0.4.6][R2988][reyhard]

fixed f22 compass inverted rotation

[5/26/2018 1:58:44 PM][0.4.6][R2987][reyhard]

^ Tweaked F-22 armor values
^ Added pedal anims to F-22
more work on F-22 mfds
tweaked afterburner max speed handling

[5/26/2018 9:40:47 AM][0.4.6][R2986][reyhard]

fixed duplicated class

[5/26/2018 12:54:25 AM][0.4.6][R2985][RichardsD]

+ Adds M1232 MRAP MCTAGS with MK 19 GMG

[5/25/2018 9:27:17 PM][0.4.6][R2984][da12thMonkey]

+ Tac-Sac, RVG and Stubby TD grips, courtesy of Hamsen, Bill Red and co. (MGM Grips team)

[5/25/2018 3:20:11 PM][0.4.6][R2983][da12thMonkey]

Gunner anims to better fit MCTAGS turret
Increased colour padding on RG-33L stencil/decal texture to reduce alpha/mip bleed

[5/25/2018 3:00:40 PM][0.4.6][R2982][reyhard]

work on mfds

[5/25/2018 1:06:56 PM][0.4.6][R2981][da12thMonkey]

@ Some vehicles had the wrong LOD when aiming down sights of mounted weapons after Tanks DLC
Some adjustment to MCTAGs turret memory points

[5/24/2018 9:53:44 PM][0.4.6][R2980][RichardsD]



[5/24/2018 9:47:11 PM][0.4.6][R2979][RichardsD]

+ Adds the USMC M1221 RG33L 6X6 MRAP
+ Adds separate tactical markings textures for entire RG33L range to reduce file size between USMC / US ARMY versions
+ Adds the Marine Corps Transparent Armored Gun-Shield

[5/24/2018 2:13:56 PM][0.4.6][R2978][reyhard]

more work on f-22 MFDs

[5/24/2018 2:31:26 AM][0.4.6][R2977][sykoCrazy]

- Removed bumps from the window glass(UH-60)

[5/23/2018 8:26:56 PM][0.4.6][R2976][reyhard]

increased mfd tex size from 1k to 2k

[5/23/2018 3:32:29 PM][0.4.6][R2975][reyhard]



[5/23/2018 3:31:32 PM][0.4.6][R2974][reyhard]

more hud work

[5/22/2018 9:30:50 PM][0.4.6][R2973][reyhard]

f22 tweaking continiues - started adding MFDs

[5/22/2018 3:29:10 PM][0.4.6][R2972][reyhard]

^ Improved F22 HUD

[5/21/2018 9:34:26 PM][0.4.6][R2971][reyhard]

small tweak to texture

[5/21/2018 9:22:40 PM][0.4.6][R2970][reyhard]

some more tweaks to F-22 MFD sensors & afterburner

[5/21/2018 9:09:09 PM][0.4.6][R2969][reyhard]



[5/21/2018 9:02:38 PM][0.4.6][R2968][reyhard]

^ Added engine startup delay to F-22
^ Tweaked F-22 flight model (WIP)
improved F-22 interior (WIP)

[5/21/2018 1:34:41 PM][0.4.6][R2967][da12thMonkey]

AH-6 pylon hitpoints

[5/20/2018 6:36:36 PM][0.4.6][R2966][reyhard]

^ Improved F-22 damage textures

[5/20/2018 6:31:43 PM][0.4.6][R2965][reyhard]

^ Added new afterbuner script to F-22

[5/20/2018 5:49:28 PM][0.4.6][R2964][da12thMonkey]

AH-1Z and UH-1Y pylon hitpoints
Adjusted radius and durability of pylons in line with AFRF

[5/20/2018 3:57:10 PM][0.4.6][R2963][reyhard]

^ Increased SMAW & Javelin reload time

[5/20/2018 3:46:09 PM][0.4.6][R2962][da12thMonkey]

Transferred pfx from AFRF
Gave pylon hitpoints some bigger balls

[5/20/2018 3:29:43 PM][0.4.6][R2961][reyhard]

@ Removed VG option for Stinger adding from M2A2 BUSK I

[5/20/2018 3:14:41 PM][0.4.6][R2960][da12thMonkey]

WIP pylon hitpoints stuff for A-10, AH-64 and UH-60
Contains errors in USAF standalone - pfx need to be transferred from AFRF

[5/20/2018 2:36:24 PM][0.4.6][R2959][da12thMonkey]

Macro was moved to cfgArmorMacros

[5/19/2018 9:15:33 PM][0.4.6][R2958][da12thMonkey]

USAF pylon hitpoints prep (macros, bbox in pylon fire geos)

[5/19/2018 9:00:53 PM][0.4.6][R2957][reyhard]

^ Tweaked AH-64 getin anims

[5/18/2018 2:29:57 PM][0.4.6][R2956][da12thMonkey]

ABU hiddenselections removal
UV set cleanup in ABU and the usm_bdu_test template model

[5/18/2018 1:08:15 AM][0.4.6][R2955][ballistic09]

+ Airman Battle Uniform
(Huge thanks to Deltahawk for the uniform, and clima_x for the Belleville boots!)
Still needs wound textures set up at some point...

[5/17/2018 7:07:04 PM][0.4.6][R2954][da12thMonkey]

Added 1.333 ratio optics model for DVE display (640*480, 800*600 etc. single sensor)
Removed NFOV mode (DVEs are fixed magnification/fov)

[5/17/2018 2:13:08 PM][0.4.6][R2953][da12thMonkey]

^ Caiman MRAPs added some extra detail to the Fire Geometry LOD around the chassis area

[5/17/2018 12:46:01 PM][0.4.6][R2952][reyhard]

+ Added Driver Vision Enhancement (including reverse cam) to M2A3 & M1 Tanks - accessible when using optics with +/- on numpad

[5/16/2018 3:04:29 PM][0.4.6][R2951][reyhard]

fixed penetrators on HE rounds

[5/15/2018 9:08:05 PM][0.4.6][R2950][ballistic09]

Fixed units with SR-25's not having ammo due to changes to magazines...

[5/14/2018 12:35:40 PM][0.4.6][R2949][da12thMonkey]

Restoring M249 belt reloadMagazine animations now that they apparently work on dev

[5/14/2018 11:44:27 AM][0.4.6][R2948][reyhard]

...

[5/14/2018 11:36:15 AM][0.4.6][R2947][reyhard]

tweaked cmags reload animations (reloadMagazine is fixed on devbranch)
tweaked duration of cmag reload

[5/11/2018 1:09:02 PM][0.4.6][R2946][da12thMonkey]

Single round shotgun ground models for GREF Izh-18 mags

[5/11/2018 9:16:07 AM][0.4.6][R2945][da12thMonkey]

!CLEARTEMP!
Forcing rebuild of HEMTT .p3ds to incorporate Ballistic09's .rvmat changes

[5/11/2018 6:09:51 AM][0.4.6][R2944][ballistic09]

^ HEMTT wheel rvmats

[5/11/2018 2:09:03 AM][0.4.6][R2943][ballistic09]

minZeroing parameter set for M2 Bradley FCS (200m)
Corrected wrong inventory icon for M249 box mags

[5/9/2018 7:19:14 PM][0.4.6][R2942][da12thMonkey]

@ Textures on dropped 12Ga buckshot and slug magazine models, had mismatched textures

Additional ground models for remaining USAF magazines

[5/9/2018 3:58:35 PM][0.4.6][R2941][reyhard]

^ Added new inventory icons for magazines

[5/9/2018 1:45:08 PM][0.4.6][R2940][da12thMonkey]

Extended placeable magazines for Eden
Some adjustments to display names

[5/9/2018 8:54:05 AM][0.4.6][R2939][reyhard]

^ Changed get in side for AH-64 gunner (anim is still played from wrong side though)
preparation for magazine inventroy icons 

[5/9/2018 1:59:51 AM][0.4.6][R2938][da12thMonkey]

USAF magazine ground models
Fixed some mags lacking author tags

[5/8/2018 10:52:29 PM][0.4.6][R2937][ballistic09]

Removed color definitions from tracer displayNames
Corrected a few typos

[5/8/2018 10:19:59 AM][0.4.6][R2936][da12thMonkey]

+ New M24 SWS model plus muzzle accessories. Black, woodland and desert versions
+ New AN/PEQ-15 model

(these weren't marked down for the change log when they were finalised)

[5/8/2018 7:45:02 AM][0.4.6][R2935][reyhard]

added scope = 1 to some of tracer mags

[5/7/2018 11:17:56 PM][0.4.6][R2934][ballistic09]

More magazine madness (PMAGs done, more C-Mag ammo variants added)

[5/7/2018 9:42:32 PM][0.4.6][R2933][da12thMonkey]

Moved M249 pouches so they mount slightly further to the right
Improved belt animation on M249 mags (added rotations to some bullets so that belt links don't separate during firing)

[5/7/2018 6:34:10 PM][0.4.6][R2932][ballistic09]

Updated displayNameShort for many magazines
Many changes to configs for M249 magazines (200rnd softpacks added, etc...)
Some usability tweaks to M24 binoculars

[5/7/2018 11:03:08 AM][0.4.6][R2931][da12thMonkey]

200Rnd M249 soft pouch (unconfigured: Ballistic09 wants to do it)

[5/7/2018 7:47:11 AM][0.4.6][R2930][reyhard]

^ Tweaked RG-33L mirrors

[5/6/2018 4:23:21 PM][0.4.6][R2929][reyhard]

^ Added safety mode to Mk14 & SR-25
^ Tweaked Mk14 reload animation

[5/6/2018 3:09:07 PM][0.4.6][R2928][reyhard]

^ Reduced armor of M1025 M1025s to better reflect their real life performance

[5/6/2018 12:53:26 PM][0.4.6][R2927][da12thMonkey]

Added Sabre's tan PMAG textures (unconfigured thus far)
Remapped PMAGs from large `acc_###.paa` map, to an individual 512*512 texture for easier retexturing
Updated credits sheet with info from Sabre

[5/6/2018 4:45:19 AM][0.4.6][R2926][MistyRonin]

^ Standarized US magazine strings 

[5/5/2018 5:16:03 PM][0.4.6][R2925][da12thMonkey]

Removed unnecessary non ai vehicles entries
Added .45ACP orange tracer round for use in GREF's WW2 SMGs

[5/5/2018 9:44:04 AM][0.4.6][R2924][reyhard]

added new icons to camo variants of M24SWS

[5/4/2018 3:40:17 PM][0.4.6][R2923][da12thMonkey]

Adjust M240 `magazineReloadSwitchPhase`

[5/4/2018 3:21:10 PM][0.4.6][R2922][reyhard]

sections tweaks

[5/3/2018 10:11:13 PM][0.4.6][R2921][da12thMonkey]

Proxy mag stuff for M240

Hid defunct PMAG M16A4 and M4, and CAP M240 weapons in Arsenal, Eden/Zeus and ammo boxes
Removed reference to "PMAG" in M4+Magpul stock displaynames

[5/3/2018 1:13:40 PM][0.4.6][R2920][reyhard]

testing reloadAction in magazines

[5/2/2018 9:24:56 PM][0.4.6][R2919][da12thMonkey]

Added some animations to M249 magazines
Transferred C-Mag model from SAF (configured test M855 version)
Enabled proxy mags for M40A5

[5/2/2018 3:05:08 PM][0.4.6][R2918][da12thMonkey]

Ported 100rnd M249 soft pouch model from A2/OA - not yet animated

[5/2/2018 2:55:26 PM][0.4.6][R2917][reyhard]

enabled pmag bullet animations 

[5/2/2018 12:34:13 PM][0.4.6][R2916][reyhard]

some more magazines tweaks

[5/2/2018 12:10:02 PM][0.4.6][R2915][reyhard]

tweaked mag proxy switch time

[5/2/2018 11:57:07 AM][0.4.6][R2914][da12thMonkey]

Second batch of mag proxy stuff

Replaced magazine with proxy on:
M249s, HK416+M27

Added memory LOD points to M249 box magazine proxy, if it can be animated

[5/2/2018 11:46:44 AM][0.4.6][R2913][reyhard]

added some random mag proxies test

[5/2/2018 10:46:43 AM][0.4.6][R2912][da12thMonkey]

First batch of mag proxy stuff

Replaced magazine with proxy on:
M4s, M16A4s, M40A5

Added proxy mag models:
`rhsusf_magazineProxy.p3d` proxy slot model
5.56mm STANAG well magazines (30rnd USGI mag and Gen 1 PMAG)
5.56mm 200rnd M249 box (is already rotated relative to M249 STANAG mag well proxy position)
7.62mm AICS well (5 and 10 rnd M40A5 mags)

Configured cfgNonAIVehicles

[5/1/2018 2:31:50 PM][0.4.6][R2911][keplager]

@ Changed weight of M789 laser magazine to match normal magazine.

[5/1/2018 1:52:23 PM][0.4.6][R2910][keplager]

+ Added correct weight for M789 1200 rd. magazine per documentation

[5/1/2018 1:50:56 PM][0.4.6][R2909][keplager]

^ UH-60M Slightly improved FPS stability.

@ UH-60M Corrected fuel amount for base model.

@ UH-60M Changed flight model weights/moments to coincide with correct fuel and ammo weights in config.

+ AH-64 Added correct fuel amount.

@ AH-64 Changed rotor coefficient table.

^ AH-64 Tuned control system per SME.

[5/1/2018 1:01:57 PM][0.4.6][R2908][reyhard]

added missing autocenter = 0 in lod - fixes rpt error

[5/1/2018 11:37:18 AM][0.4.6][R2907][reyhard]

@ Fixed some MELB .rpt errors

[4/29/2018 8:15:45 PM][0.4.6][R2906][reyhard]

Reduced amount of spall from submunition
Added experimental interior impact sound for AP rounds

[4/29/2018 1:55:37 AM][0.4.6][R2905][da12thMonkey]

+ Woodland and desert camo textured Leupold Mk. 4 ER/T 3.5-10x M3 scopes
^ Re-equipped US Army M24 sniper units with appropriate woodland and desert camouflaged versions of the rifle and accessories

Added Sabre's camo textures for the M24 SWS and its muzzle devices

[4/28/2018 6:38:48 PM][0.4.6][R2904][reyhard]

^ Tweaked recoil force of 120mm cannon after friction values changes to base surfaces

[4/25/2018 6:31:21 AM][0.4.6][R2903][ballistic09]

^ Added TOW-2B AERO missiles to A3 series M2 Bradleys
Minor tweaks/fixes to Bradley and TOW configs
Configured magazines for M903 SLAP ammo
^ Added M903 SLAP ammo to TUSK Abrams' CSAMM M2
Updated display names for various vehicle weapons and magazines


[4/24/2018 1:19:17 PM][0.4.6][R2902][reyhard]

@ Removed AH-64 pilot camera

[4/23/2018 6:50:57 PM][0.4.6][R2901][da12thMonkey]

Fixing classname prefix typos

[4/22/2018 9:37:21 PM][0.4.6][R2900][da12thMonkey]

@ HEMTT gun turret traverse axis was off-center close T2378
^ US mines and explosives are now available to Zeus (inc. minefield modules)

Stringtable for BLU-97 UXO

[4/22/2018 8:25:39 PM][0.4.6][R2899][reyhard]

^ Tweaked penetration of M107 ammo

[4/22/2018 7:32:45 PM][0.4.6][R2898][da12thMonkey]

Applied icon to BLU-97 UXO

[4/22/2018 2:43:25 PM][0.4.6][R2897][da12thMonkey]

Increased number of mines dispensed by GBU-89 to real value (after inspecting KGMU-2 config in AFRF more closely)
'armor' and 'explosionShielding' properties added to submunition mines/UXO
Added placeable submunition mines/UXO to eden editor and Sites module (inc. edprev images)

[4/21/2018 4:52:45 PM][0.4.6][R2896][da12thMonkey]

M9: wrong INVENTORY_PICTURE macro

[4/21/2018 3:56:41 PM][0.4.6][R2895][j0zh94]

Further tweaks to dispersion for testing

[4/20/2018 3:33:58 PM][0.4.6][R2894][Festival]

^ Added editorpreview icons for M14, M19 and M112
^ Added icons for M112
^ Tweaks in mines config and stingtable.xml
@ Fixed error with deactivation M112

[4/17/2018 6:13:14 PM][0.4.6][R2893][j0zh94]

^ Improved m249 & M240 recoil pattern. Introduced dispersion to M72 & AT4. Introduced recoil names for M4 (no change to pattern) 

[4/17/2018 6:44:31 AM][0.4.6][R2892][reyhard]

@ Fixed lodTurnedOut values after syntax change introduced with Tanks DLC

[4/15/2018 7:57:18 PM][0.4.6][R2891][ballistic09]

Changed ISU gun reticle to air defence version

[4/15/2018 4:20:22 PM][0.4.6][R2890][reyhard]

^ Increased get in/out time from tanks to 2.1 seconds (previously 0.8)
^ Tweaked A10A physx wheels & fixed it's issue with getout action availability 

[4/14/2018 6:28:50 PM][0.4.6][R2889][da12thMonkey]

restoring M113 driverOpticsModel

[4/13/2018 10:08:09 PM][0.4.6][R2888][da12thMonkey]

@ Part of TOW launcher mount could not change texture, on M2A3 versions of Bradley IFV

[4/13/2018 7:21:35 PM][0.4.6][R2887][da12thMonkey]

^ Charge/Distance firemode info added to Artillery gunner HUDs
Fixing M109 turned-in views inheriting properties from Tanks DLC

[4/13/2018 5:56:37 PM][0.4.6][R2886][da12thMonkey]

HUD info for HIMARS gunner

[4/13/2018 7:56:09 AM][0.4.6][R2885][reyhard]

small tweak to cannon disp

[4/13/2018 6:56:43 AM][0.4.6][R2884][reyhard]

@ Adjusted LODDriverTurnedOut to new syntax after Tank DLC release
^ Tweaked tank cannon dispersion

[4/12/2018 2:12:58 PM][0.4.6][R2883][reyhard]

@ Fixed M113 turrets

[4/10/2018 9:11:53 PM][0.4.6][R2882][da12thMonkey]

Updated M1025 EdPrev images

[4/10/2018 3:43:13 AM][0.4.6][R2881][ballistic09]

More M1043 variants

[4/8/2018 5:29:36 PM][0.4.6][R2880][da12thMonkey]

@ Caiman MRAPs were missing countermeasure weapon to initiate the DUKE system

[4/6/2018 8:45:35 PM][0.4.6][R2879][da12thMonkey]

Corrected unwanted `flightprofiles[]` inheritance on US AT missiles

[4/5/2018 9:35:03 PM][0.4.6][R2878][da12thMonkey]

Adjusted CBU-97 shade of yellow

[4/5/2018 8:18:49 PM][0.4.6][R2877][da12thMonkey]

+ BLU-97 submunition model (5% chance of UXO)

Removed `defaultMagazine` classes for BLU-91/92 mines and BLU-97 UXO - prevents picking up mines after defusing, as submunitions can't be used with the "put" weapon anyway.

[4/4/2018 2:31:18 PM][0.4.6][R2876][da12thMonkey]

@ UV mapping error on rear of AN/PEQ-16
Section and UV set cleanup of PEQ-15s
Disabled reactivation option appearing for GATOR mines, after defusing them

[4/4/2018 1:12:37 AM][0.4.6][R2875][RichardsD]

@ Fixes shadow LOD error on up-armored Caiman MRAPs

[4/3/2018 10:46:12 PM][0.4.6][R2874][da12thMonkey]

+GATOR/GEMSS submunition mines (BLU-91/BLU-92, M74/M75)

[4/3/2018 10:12:36 PM][0.4.6][R2873][reyhard]

^ Tweaked machineguns AI fire modes

[4/3/2018 2:30:22 PM][0.4.6][R2872][reyhard]

@ Some USAF ammo crates were missing in Zeus

[4/2/2018 9:07:39 PM][0.4.6][R2871][reyhard]

fixed old light flag on M1 triplex

[4/2/2018 8:27:39 PM][0.4.6][R2870][reyhard]

@ Various fixes to updating base classes rpt errors

[4/2/2018 3:05:29 PM][0.4.6][R2869][reyhard]



[4/2/2018 2:13:03 PM][0.4.6][R2868][reyhard]

2nd attempt at fixing M109A6 barrel misalignment 

[4/2/2018 2:08:49 PM][0.4.6][R2867][reyhard]

@ Fixed MZRZ was inheriting PiP mirrors

[4/2/2018 2:01:31 PM][0.4.6][R2866][reyhard]

rpt clean up

[4/2/2018 9:37:53 AM][0.4.6][R2865][reyhard]

REPACK EVERYTHING AGAIN
!CLEARTEMP!

[4/2/2018 9:23:11 AM][0.4.6][R2864][reyhard]

fixed m109a6 gun memory points weren't aligned properly

[4/2/2018 8:33:11 AM][0.4.6][R2863][reyhard]

converted convexComponents to armorComponents
fixed typo in armor simulation macro

[4/2/2018 8:20:01 AM][0.4.6][R2862][reyhard]

fixed small typo in cbu89 config

[4/2/2018 7:32:13 AM][0.4.6][R2861][reyhard]

added missing model.cfg to mzrz rtm

[4/2/2018 5:17:50 AM][0.4.6][R2860][da12thMonkey]

Cluster bomb LODs
Fixed: Part of CBU-87 was rotating the wrong direction during inittime anim

[4/1/2018 10:13:17 PM][0.4.6][R2859][reyhard]

changed engine component rvmat from metal_plate to metal

[4/1/2018 9:26:12 PM][0.4.6][R2858][reyhard]

some tweaks to spall system

[4/1/2018 8:51:22 PM][0.4.6][R2857][reyhard]

^ Improved UH60 Wreck RVMAT
^ Improved performance of Abrams loader script
^ Added M1 reload sounds (again kudos to daskal from SB community)
M1A1SA, M1A1SA (TUSK) & all bradley family were converted to new armor simulation 
added a little bit penetration to HEAT shells so they can go through bushes
testing submunition for AP shells
disabled scripted spall handling in favor of submunition solution
changed some text to macros


[4/1/2018 3:53:34 PM][0.4.6][R2856][da12thMonkey]

+ CBU-87 and CBU-89 cluster bomb models
^ CBU-87 pylon configuration reclassified as a 1000lb bomb (A-10 can carry fewer of them now)

Bomb res LODs are still to do. Placeholder meshes for submunition models will be replaced with accurate ones in future

[3/31/2018 11:04:37 PM][0.4.6][R2855][reyhard]

hellfire was missing tandem property

[3/31/2018 11:02:18 PM][0.4.6][R2854][reyhard]

fixed tandem warheads

[3/31/2018 5:03:56 PM][0.4.6][R2853][reyhard]

^ Added delay to TOW usage on Bradleys

[3/31/2018 4:16:10 PM][0.4.6][R2852][reyhard]

experimental door handler test

[3/31/2018 4:02:24 PM][0.4.6][R2851][reyhard]

^ Optimized MELB scripts
@ Duplicated turrets .rpt errors clean up
@ Fixed F-22 rpt errors
^ Removed fuel leak script since it's present in base game already
^ Added camshake to Gau-8 

[3/31/2018 1:49:51 AM][0.4.6][R2850][p1nga]

Update AN-PEQ15

[3/30/2018 11:13:16 AM][0.4.6][R2849][reyhard]

some eventhandlers fixes

[3/30/2018 7:02:36 AM][0.4.6][R2848][reyhard]

purge continues 
!CLEARTEMP! 

[3/30/2018 1:18:27 AM][0.4.6][R2847][ballistic09]

Added basic GPSE functionality for M2A2 commander's optics (No TC override though) :(

[3/29/2018 8:47:03 PM][0.4.6][R2846][reyhard]

started removing Baker stuff from svn

[3/27/2018 11:22:56 PM][0.4.6][R2845][ballistic09]



[3/27/2018 9:13:35 PM][0.4.6][R2844][ballistic09]

Adding the old manually ranged 2-Digit ISU FCS for something in the future... ;)

[3/26/2018 8:39:09 PM][0.4.6][R2843][ballistic09]

@ Fixed lasing with IBAS/CIV didn't trigger Shtora
^ Minor realism tweaks to IBAS/CIV digital zoom modes (24X & 48X)

[3/26/2018 7:24:59 PM][0.4.6][R2842][da12thMonkey]

+ M2A2ODS gunner's Integrated Sight Unit
Ballistic09's work

[3/23/2018 9:36:29 PM][0.4.6][R2841][RichardsD]

@ Adds currently non-functioning Bradley turn out passenger option. Currently allows turn out, but hatch doesn't animate on roof. - Animations also need to be tweaked.Only on M2A2 for now. 

[3/20/2018 6:14:12 PM][0.4.6][R2840][ballistic09]

^ Improved TOW-2B overfly top-attack targeting

[3/20/2018 5:49:41 PM][0.4.6][R2839][reyhard]

tweaked tow gunner anim (wip)

[3/20/2018 2:23:40 PM][0.4.6][R2838][da12thMonkey]

TOW M1025 antennas had no axis mem points for animation
PiP classname produced "Scope is not a value" error in config browser

[3/20/2018 8:32:08 AM][0.4.6][R2837][reyhard]

fixed M1025 tow pip

[3/19/2018 6:46:06 PM][0.4.6][R2836][reyhard]

added new M1025 tow gunner anims
fixed gunner proxy movement
fixed caps hiding on reload

[3/19/2018 5:27:11 PM][0.4.6][R2835][da12thMonkey]

Fixed: Could not steer TOW missiles fired from M1025 (`body=` and `gun=` params were empty)

[3/19/2018 5:29:55 AM][0.4.6][R2834][ballistic09]

Minor changes to how M1025 bumper switching works
Re-added M1025 (M2) textureSources that got removed in last commit
Corrected the designation of the TOW M1025
Added 2 TOW-2B's to TOW M1025

[3/18/2018 11:24:11 PM][0.4.6][R2833][RichardsD]

@ Fixed Normal for TOW HMMVW

[3/18/2018 9:55:24 PM][0.4.6][R2832][RichardsD]

@ Adds M1025 TOW Config and TOW HMMVW

[3/18/2018 6:44:28 PM][0.4.6][R2831][RichardsD]



[3/18/2018 12:39:07 AM][0.4.6][R2830][reyhard]



[3/18/2018 12:19:49 AM][0.4.6][R2829][reyhard]

added new plate to Himras

[3/17/2018 11:18:22 PM][0.4.6][R2828][RichardsD]

@ Adds Missile Pod plates for Reyhard for HIMARS

[3/17/2018 9:55:52 PM][0.4.6][R2827][reyhard]

^ Added engine smoke FX to FMTV & HIMARS
tweaked suspension for USAF vehicles
added cap hidding anim & missile move anim (proper fx & rocket start pos)
configured new rockets


[3/17/2018 4:09:06 PM][0.4.6][R2826][reyhard]

^ ERA now use new armorComponent hit detection
^ Tweaks to M2 Bradley steering values

[3/17/2018 2:44:05 PM][0.4.6][R2825][da12thMonkey]

Removed front fins from M26 227mm MLRS rocket model and copied previous model with front fins as a separate M30/M31 227mm GMLRS rocket model

[3/17/2018 1:13:31 PM][0.4.6][R2824][da12thMonkey]

Padded some parts of HIMARS interior alpha texture to reduce edge bleed

[3/17/2018 12:28:13 PM][0.4.6][R2823][da12thMonkey]

More adjustments to MLRS 227mm rocket texture and materials

[3/17/2018 12:52:28 AM][0.4.6][R2822][da12thMonkey]

HIMARS
Added:
faction variants to editor
editor preview images
Fixed:
unwanted passenger seat (cargo proxy is used for FFV turret)
swapped US Army drivers to Crewmen (CVC helmets)

[3/16/2018 11:57:13 PM][0.4.6][R2821][da12thMonkey]

MLRS 227mm rocket:
added forceNotAlpa property to fly model (whole rocket had transparency due to relative size of the flame alpha)
fixed texture/material paths
added specular map

[3/16/2018 11:01:24 PM][0.4.6][R2820][reyhard]

changed back max elev to 65

[3/16/2018 10:53:13 PM][0.4.6][R2819][reyhard]

work on HIMARS:
added cap selections (not configured)
added usti & konec hlavne mem points
added cluster ammo (heavy WIP) & new weapons
config clean up
added turn in/out anim for commander (WIP)

[3/16/2018 7:30:58 PM][0.4.6][R2818][reyhard]

@ Fixed M1A1 commander & loader turned in mode

[3/16/2018 7:07:12 PM][0.4.6][R2817][RichardsD]

@ Adds M26 Missile for HIMARS

[3/16/2018 11:18:30 AM][0.4.6][R2816][reyhard]

@ Fixed vehicle mounted M240 was using wrong ammo

[3/15/2018 10:24:01 PM][0.4.6][R2815][j0zh94]

First batch of dispersion tests, adjusted CCO zero to realistic value, added texture to AT4 rocket

[3/14/2018 7:18:01 PM][0.4.6][R2814][RichardsD]

+ Adds HIMARS Damage textures
@ Adds commander's seat, but needs tweaking - not showing properly.

[3/14/2018 1:34:30 PM][0.4.6][R2813][reyhard]

damage selections clean up continuation

[3/13/2018 8:52:21 PM][0.4.6][R2812][RichardsD]

@ Fixed desert textures on rear

[3/13/2018 1:44:41 PM][0.4.6][R2811][da12thMonkey]

HIMARS work: hiddenSelectionsTextures weren't assigned, could not be found under RHS factions, reduced section count

[3/13/2018 4:55:17 AM][0.4.6][R2810][RichardsD]

+ Adds the M142 HIMARS initial version

[3/12/2018 8:59:56 AM][0.4.6][R2809][reyhard]

^ Tweaked M2 Bradley PhysX geometry

[3/10/2018 12:10:07 PM][0.4.6][R2808][reyhard]

@ Fixed random damage texture changing when some parts of vehicles were damaged

[3/9/2018 7:08:36 PM][0.4.6][R2807][reyhard]

@ Changed M1025 decal names to more dedicated server friendly ones

[3/9/2018 10:18:25 AM][0.4.6][R2806][reyhard]

^ Added occluder to A10 cockpit

[3/8/2018 9:05:21 PM][0.4.6][R2805][reyhard]

added pistol icons

[3/6/2018 8:06:23 PM][0.4.6][R2804][reyhard]

^ Added new inventory icons for vests

[3/6/2018 2:53:03 PM][0.4.6][R2803][PuFu]

^ T1 UV set 1 error fix 

[3/5/2018 10:11:19 PM][0.4.6][R2802][reyhard]

^ Added new icons for USAF headgear
!CLEARTEMP!

[3/4/2018 4:39:50 PM][0.4.6][R2801][reyhard]

ultimate solution for hidden selections material lod bug + fixed icons for few weapons

[3/3/2018 6:20:56 PM][0.4.6][R2800][reyhard]

^ Added new icons for USAF weapons

[2/22/2018 11:41:24 PM][0.4.6][R2799][gurdy]

@ broken M1043 normals

[2/22/2018 10:44:47 PM][0.4.6][R2798][gurdy]

+ initial test M1043A2

[2/16/2018 8:57:15 PM][0.4.6][R2797][da12thMonkey]

^ Mirrored UVs on SF3P muzzle flash's front-facing planes (muzzle flash pattern appeared upside-down when viewed from the front)

[2/16/2018 7:36:18 AM][0.4.6][R2796][Redphoenix]

some resizing, thansk to Ballistic pointing that out

[2/15/2018 9:02:33 AM][0.4.6][R2795][Redphoenix]

Made Muzzle attachments on M24 Working
Aligned top and muzzle proxies better

[2/15/2018 7:54:11 AM][0.4.6][R2794][Redphoenix]

M24 Muzzle Break and Silencer Models

[2/15/2018 7:21:29 AM][0.4.6][R2793][Redphoenix]

M24 config edits, setting ghillie to scope=1 for now

[2/15/2018 7:18:34 AM][0.4.6][R2792][Redphoenix]

some final m24 model edits

[2/15/2018 7:06:29 AM][0.4.6][R2791][Redphoenix]

Removed some old textures and added _as maps for M24
!CLEARTEMP!

[2/15/2018 6:06:13 AM][0.4.6][R2790][Soul_Assassin]

Fixed M24 texture and rvmat paths

[2/15/2018 5:40:45 AM][0.4.6][R2789][sabre]



[2/15/2018 5:37:57 AM][0.4.6][R2788][sabre]



[2/14/2018 5:34:25 PM][0.4.6][R2787][Redphoenix]

some selection fixes and color selections for easier texture assigning

[2/13/2018 8:52:53 PM][0.4.6][R2786][Redphoenix]

testcommit of M24 changes from motherfile

[2/13/2018 5:49:59 PM][0.4.6][R2785][da12thMonkey]

Animated M24 bolt carrier group
Corrected M24 scale (~0.875) and scope proxy position

[2/13/2018 3:09:10 PM][0.4.6][R2784][Redphoenix]

LODs for M24 base

[2/13/2018 10:15:44 AM][0.4.6][R2783][reyhard]

@ Fixed forced zoom for M113 hatch turn out seats

[2/12/2018 9:53:20 PM][0.4.6][R2782][j0zh94]

Adjusted TracerEndTime to more realistic burn times

[2/12/2018 1:45:20 PM][0.4.6][R2781][reyhard]

@ Fixed laser designators magazines prevented rearming at trucks

[2/11/2018 10:14:36 PM][0.4.6][R2780][Redphoenix]

Interim M24 Commit for Sabre

[2/8/2018 3:12:37 PM][0.4.6][R2779][reyhard]

ffs

[2/8/2018 3:10:10 PM][0.4.6][R2778][reyhard]

@ Fixed M1911A1 inheritance in sound cfg breaking AI fire modes

[2/8/2018 3:01:19 PM][0.4.6][R2777][da12thMonkey]

^ Lofting flight profile for Hellfire
For default "LOBL" type mode so far. No LOAL mode yet

[2/8/2018 2:56:45 PM][0.4.6][R2776][reyhard]

interior view disabled for Bradleys gunners & commanders

[2/8/2018 2:36:12 PM][0.4.6][R2775][reyhard]

changed laser designator on AH-64 to more AI friendly 

[2/6/2018 9:44:56 AM][0.4.6][R2774][reyhard]

+ Added top down attack to Javelin

[2/1/2018 11:03:22 AM][0.4.6][R2773][da12thMonkey]

Renamed class `rhsusf_acc_mrds_fwd_ak_c` -> `rhsusf_acc_mrds_fwd_c_ak` due to script requirements

[2/1/2018 9:03:27 AM][0.4.6][R2772][reyhard]

^ Tweaked ACU rvmats

[2/1/2018 6:56:13 AM][0.4.6][R2771][Soul_Assassin]

Finalizing MRDS

[1/31/2018 11:52:38 PM][0.4.6][R2770][Soul_Assassin]

Coyote MRDS added

[1/31/2018 8:57:35 PM][0.4.6][R2769][da12thMonkey]

^ Disabled woodland AFG attachment on M249 VFG

[1/31/2018 8:32:29 PM][0.4.6][R2768][Soul_Assassin]

+ Added MRDS

[1/31/2018 12:45:55 AM][0.4.6][R2767][ballistic09]

^ Added option to hide A1 brushguard on M1025 bumper

[1/29/2018 4:30:22 PM][0.4.6][R2766][reyhard]

@ Fixed fault M2 Bradley AI sensor

[1/28/2018 10:41:31 AM][0.4.6][R2765][reyhard]

^ Tweaked troops NVG handler

[1/27/2018 7:04:22 PM][0.4.6][R2764][Soul_Assassin]

Su-230/PVS: Added to units and crates, scoped out old ones completely. Added icons.

[1/27/2018 5:18:51 PM][0.4.6][R2763][Soul_Assassin]

Added all specter variants. Configged handlers.
!CLEARTEMP!

[1/26/2018 7:25:34 AM][0.4.6][R2762][Soul_Assassin]

Shadowlod, resl lods and restructure of Specter

!CLEARTEMP!

[1/25/2018 7:21:53 AM][0.4.6][R2761][Soul_Assassin]

Added shadow lod to specter

[1/25/2018 12:14:19 AM][0.4.6][R2760][gurdy]

+ initial injection of M24 Binoculars

[1/24/2018 2:26:31 PM][0.4.6][R2759][reyhard]

@ Fixed rogue triangle in 2nd resolution LOD of M1A2 TUSK I & II

[1/23/2018 3:07:16 PM][0.4.6][R2758][da12thMonkey]

Some adjustments in SpecterDR pilot LOD, to widen the FOV a little
Cleaned up duplicate sections
Switched MRDS dot from amber to correct red


[1/23/2018 1:14:11 PM][0.4.6][R2757][da12thMonkey]

Adjusted SpecterDR scale to 153mm length

[1/23/2018 7:13:30 AM][0.4.6][R2756][Soul_Assassin]

+ Added new SU-230/PVS 

[1/21/2018 7:53:14 PM][0.4.6][R2755][reyhard]

^ Tweaked M1 recoil
^ Tweaked HEMTT PhysX

[1/20/2018 10:37:32 PM][0.4.6][R2754][da12thMonkey]

@ Handle on M2A3's CIV turret did not follow traverse

[1/20/2018 1:36:07 PM][0.4.6][R2753][da12thMonkey]

^ Increased AGM-114 Hellfire `timeToLive`

[1/19/2018 5:37:32 PM][0.4.6][R2752][Redphoenix]

!CLEARTEMP!
+ Added Tan version of RX01 Reflex Sight
^ Improved UI Icons of RX01 Reflex Sights

[1/19/2018 3:30:28 PM][0.4.6][R2751][reyhard]



[1/19/2018 2:29:18 PM][0.4.5][R2750][Soul_Assassin]

[0.4.6] Version bump

[1/19/2018 1:41:19 PM][0.4.5][R2749][Soul_Assassin]

Some more fixes on m1a1 config

[1/19/2018 1:11:36 PM][0.4.5][R2748][Soul_Assassin]

Minor cleanup in m1a1 config

[1/19/2018 10:41:06 AM][0.4.5][R2747][Soul_Assassin]

Config fixes for class docs

[1/16/2018 6:07:58 PM][0.4.5][R2746][da12thMonkey]

A-10 central PiP mirror was a little misaligned from its holder/frame

[1/16/2018 7:10:29 AM][0.4.5][R2745][bek]

abrams barrel art for cosmere nerds

[1/15/2018 10:10:17 PM][0.4.5][R2744][da12thMonkey]

^ Added rear-view mirrors to A-10A cockpit

[1/15/2018 8:54:11 PM][0.4.5][R2743][j0zh94]

^Added TOW missile fly sound

[1/14/2018 7:26:06 PM][0.4.5][R2742][reyhard]

^ Tweaked 3rd person camera for tanks

[1/11/2018 8:34:33 AM][0.4.5][R2741][jastreb]

@ fixed mod logos

[1/9/2018 5:08:56 PM][0.4.5][R2740][j0zh94]

^Updated MK19 config and fix packing error

[1/8/2018 4:59:51 PM][0.4.5][R2739][reyhard]

^ Added pedal anims to A10A
^ Tweaked A10A Center of Mass
@ Fixed ALQ-131 z fighting from pilot LOD
@ Fixed GAU-8 devbranch errors
some more fixes & tweaks to FMTV

[1/8/2018 4:04:09 AM][0.4.5][R2738][ballistic09]

^ Rescaled TOW missiles to correct size
^ Animated TOW-2/2A standoff probe extension

[1/7/2018 10:27:25 PM][0.4.5][R2737][reyhard]

^ Improved FMTV driver animation, mirror shape, gagues (animations/visuals) & shadows

[1/6/2018 11:09:02 PM][0.4.5][R2736][keplager]

@ AH-1Z/UH-1Y Changed maximum and minimum anti-torque rotor pitch T0003819

@ UH-60M slightly changed SAS gsins.

[1/6/2018 9:42:57 PM][0.4.5][R2735][reyhard]

^ Added gauges anims to Caiman
^ Added new driver anim to Caiman

[1/3/2018 4:23:56 AM][0.4.5][R2734][gurdy]

^ xmas antlers test texture

[1/3/2018 12:05:11 AM][0.4.5][R2733][da12thMonkey]

@ ACU uniform insignia alpha sorting

[12/31/2017 6:21:35 PM][0.4.5][R2732][j0zh94]

Added m18 smoke grenade to SL vest

[12/31/2017 4:30:46 PM][0.4.5][R2731][da12thMonkey]

@ M977A4 (Repair) cabin SVC lights displaced

[12/29/2017 5:47:41 PM][0.4.5][R2730][Soul_Assassin]

tga to ignore list on xmas folder

[12/29/2017 5:47:03 PM][0.4.5][R2729][Soul_Assassin]

+ Added Xmas gift 1

[12/24/2017 8:29:47 PM][0.4.5][R2728][gurdy]

^ US MERDC textures
- removed US tropical verdant variants

[12/24/2017 4:28:36 PM][0.4.5][R2727][reyhard]

^ Added extra pip view distance options


[12/24/2017 1:25:25 PM][0.4.5][R2726][reyhard]

@ Fixed damage in AFM from rolling on the ground on UH-60 & CH-47
adjusted size of wheel in geo physx for uh60 (should still look in standard FM)
assigned land contact memory points & geo physx wheels to dampers bones
tweaked rotor lib suspension points

[12/23/2017 8:15:31 PM][0.4.5][R2725][da12thMonkey]

^ Adjusted sensor parameters on AGM-65F (Anti-Ship, IR Maverick): Lowered max target speed, raised max locking range

[12/23/2017 12:33:17 AM][0.4.5][R2724][ballistic09]

typo (╯°□°)╯︵ ┻━┻

[12/23/2017 12:23:05 AM][0.4.5][R2723][ballistic09]

+ Field manual entry on using the A-10A's TVM

[12/21/2017 10:11:32 PM][0.4.5][R2722][da12thMonkey]

!CLEARTEMP!
Adjusted tint colours of RX01 ocular lens

[12/21/2017 4:11:34 PM][0.4.5][R2721][da12thMonkey]

RX01 lens rvmat had a duplicated line

[12/21/2017 10:35:18 AM][0.4.5][R2720][reyhard]

tweaked M1025 & M113 physx

[12/21/2017 6:05:34 AM][0.4.5][R2719][Redphoenix]

+ RX01 w/o Filter

[12/21/2017 12:32:25 AM][0.4.5][R2718][ballistic09]

+ Camo variants of SR-25 Suppressor
^ SR-25 rail covers were not retexturable

[12/20/2017 9:07:35 PM][0.4.5][R2717][Redphoenix]

Added better geometry, more or less finalized textures for glass 

[12/20/2017 3:54:45 PM][0.4.5][R2716][Redphoenix]

Fixed normals again

[12/20/2017 3:22:38 PM][0.4.5][R2715][Redphoenix]

Fixed LODs of Reflex Sight

[12/19/2017 9:27:59 PM][0.4.5][R2714][da12thMonkey]

Forgot to add magic cube tech to standalone RMR view pilot LOD

[12/19/2017 8:49:31 PM][0.4.5][R2713][Redphoenix]

Added LODs for Reflex Sight

[12/19/2017 6:59:55 PM][0.4.5][R2712][da12thMonkey]

^ SOCOM FMTVs now have proper sound attenuation setting for open-top vehicles
^ Improved smoke dischargers for M1084A1R SOV

Added RHSUSAF strings for Smoke Generator

[12/19/2017 5:12:29 PM][0.4.5][R2711][Redphoenix]

More texture tweask for the Reflex Sight

[12/19/2017 3:48:58 PM][0.4.5][R2710][reyhard]

adjusted land contact points for tracked vehicles
fixed M1A2 smoke launchers textures

[12/18/2017 9:42:16 PM][0.4.5][R2709][Redphoenix]

Tweaks on reflex sight

[12/18/2017 8:18:45 PM][0.4.5][R2708][Kllrt]

Renamed RX01 sight, just in case

[12/18/2017 7:35:15 PM][0.4.5][R2707][Kllrt]

+ Added Trijicon RX01 reflex sight

[12/18/2017 3:25:26 PM][0.4.5][R2706][reyhard]

@ Fixed AI in A10A didn't want to use GAU-8 on ground targets
^ Adjusted Mk82 & Cluster bombs values so AI should use it more frequently

[12/18/2017 8:20:12 AM][0.4.5][R2705][reyhard]

fixed smoke launcher not moving on some of m2 models - unified otocvez, otocVez, OtocVez selections

[12/17/2017 8:08:59 PM][0.4.5][R2704][reyhard]

^ Exhaust smoke generator now consumes some fuel 
^ Reduced recoil for M109A6
added smoke launcher to m1117
fixed some duplicated mesh on M1A1FEP (smoke launchers)



[12/17/2017 2:05:14 PM][0.4.5][R2703][reyhard]

added smoke launchers to M2 Bradley
tweaked M1A1 HC & FEP smoke launchers lods

[12/16/2017 8:10:45 PM][0.4.5][R2702][reyhard]

+ Added exhaust smoke generator to USAF vehicles
+ Added new smoke launchers effects to M1 tanks
switched back M1025 gearbox from omegaRPM to effective

[12/16/2017 8:03:58 PM][0.4.5][R2701][da12thMonkey]

IOTV section and UVset cleanup

[12/16/2017 6:47:23 PM][0.4.5][R2700][j0zh94]

Fixed P Drive errors

[12/15/2017 5:15:29 PM][0.4.5][R2699][j0zh94]

^ Updated IOTV vests

[12/15/2017 11:17:02 AM][0.4.5][R2698][reyhard]

testing headAimDown on Caiman 
^ Adjusted aiDispersionCoefs for tanks

[12/14/2017 9:31:46 PM][0.4.5][R2697][reyhard]

^ Adjusted Hellfire & Maverick speed
removed so debug text from ah64 ui script
tweak to M2 track speed

[12/14/2017 8:22:03 PM][0.4.5][R2696][da12thMonkey]

Fixed: Track alpha sorting issue on 90s M113 w/ Mk.19

[12/14/2017 4:25:25 PM][0.4.5][R2695][da12thMonkey]

+ Standalone RMR sight attachment, inc. forward-mounting versions

[12/14/2017 1:10:37 PM][0.4.5][R2694][da12thMonkey]

Fixed: ACOG MDO had a texture assigned to part of the shadow LOD

[12/12/2017 9:47:43 PM][0.4.5][R2693][reyhard]

^ Adjusted fuel range of USAF vehicles
^ Tweaked ai firemodes settings
experimental tweak for ramming damage - need testing in MP

[12/12/2017 4:17:59 PM][0.4.5][R2692][reyhard]

some minor tweaks to MZRZ PhysX (gear switching, peakTorque)

[12/12/2017 9:44:53 AM][0.4.5][R2691][reyhard]

quick test of engineMOI for MZRZ + increased antirollbar

[12/11/2017 9:37:07 PM][0.4.5][R2690][reyhard]

@ Fixed MZRZ sound configuration

[12/11/2017 8:46:37 PM][0.4.5][R2689][reyhard]

^ Improved PhysX configuration of HEMMT, M1117 & Caiman

[12/11/2017 3:58:03 PM][0.4.5][R2688][reyhard]

^ Improved FMTV PhysX configuration
^ Improved MZRZ4 PhysX configuration - final fix for suspension anims
enabled weighting for MZRZ
improved MZRZ PhysX geo lod
fixed MZRZ damageHide selections after adding cage anims

[12/11/2017 10:24:06 AM][0.4.5][R2687][reyhard]

fixed exhaust particle fps drop

[12/11/2017 8:23:20 AM][0.4.5][R2686][reyhard]

^ Adjusted Raven backpack mass
adjusted RG33/L physx memory points

[12/10/2017 8:57:12 PM][0.4.5][R2685][reyhard]

@ Fixed mMaxDroop typo in PhysX configs of many USAF vehicles
(cfg still need adjustments to match model.cfg)
^ Tweaked M1025 PhysX 

[12/10/2017 4:52:04 PM][0.4.5][R2684][reyhard]

testorino

[12/10/2017 4:05:36 PM][0.4.5][R2683][reyhard]

k

[12/10/2017 3:42:59 PM][0.4.5][R2682][reyhard]

good commit

[12/9/2017 5:23:40 PM][0.4.5][R2681][reyhard]

@ Fixed MELB camera twitching when switching to ground lock
^ Added vanilla FCS to AH64 & AH1Z autocannons
^ Zeus is now able to move vehicles during their engine startup 
@ AH-64 & AH-1z were missing gunBeg/End memory points definition

[12/9/2017 10:40:06 AM][0.4.5][R2680][da12thMonkey]

^ Disabled compatibility of forward-mounting Aimpoint T1s on M14 EBR, M24 and M40A5 where they would float in mid-air

[12/8/2017 2:02:59 PM][0.4.5][R2679][da12thMonkey]

Put some top-mounted PEQ-16s in the mix of USMC loadouts (weapons that used to have top-mounted PEQ-15s)

[12/8/2017 11:53:08 AM][0.4.5][R2678][da12thMonkey]

Updated PEQ-16's texture with Alex' reworked version

[12/7/2017 11:45:27 PM][0.4.5][R2677][da12thMonkey]

Added top rail mounting versions of PEQ-16

[12/7/2017 12:32:39 PM][0.4.5][R2676][da12thMonkey]

@ Minor M109 alpha sorting bug when viewing antennas through the wire mesh on the turret bustle

[12/6/2017 10:11:58 PM][0.4.5][R2675][da12thMonkey]

^ Replaced USMC units' AN/PEQ-15s with AN/PEQ-16s

Added PEQ-16s to ammo boxes, Eden objects etc.

[12/6/2017 8:01:24 PM][0.4.5][R2674][da12thMonkey]

+ AN/PEQ-16

[12/6/2017 11:49:53 AM][0.4.5][R2673][reyhard]

fixed wrong M1 peakTorque

[12/5/2017 9:25:49 PM][0.4.5][R2672][reyhard]

^ Increased TOW2 time of flight & speed characteristic according to following table - https://fas.org/man/dod-101/sys/land/tow-flight.gif
reduced recoil for m119
added cfgPatches entries for new M113

[12/5/2017 3:28:59 PM][0.4.5][R2671][reyhard]

another dorifto tweak to M1

[12/4/2017 9:42:40 PM][0.4.5][R2670][reyhard]

^ Reduced range of vehicles
^ Added new sounds for M1 (kudos to daskal from Steel Beast community)

[12/4/2017 8:55:00 PM][0.4.5][R2669][da12thMonkey]

Gave US helicopter pilots+copilots access to nav/gps info panel

[12/4/2017 7:42:03 PM][0.4.5][R2668][reyhard]

^ Added antiwater material to M113 interior

[12/3/2017 9:33:25 PM][0.4.5][R2667][reyhard]

small dorifto tweaking

[12/3/2017 9:24:20 PM][0.4.5][R2666][reyhard]

^ Added interior occluders to M113
^ Added improved PhysX to M109

[12/3/2017 2:51:46 PM][0.4.5][R2665][reyhard]

improved suspension for whole M1 family
reverted automatic sprungMass calculation
^ Improved M109 PhysX
tweaked recoil

[12/2/2017 11:45:50 PM][0.4.5][R2664][da12thMonkey]

@ IFF panels on M2A3 Bradley variants would shrink when using the "Hide IFF Panel" animation

[12/2/2017 10:18:04 PM][0.4.5][R2663][reyhard]

fixed sound paths

[12/2/2017 9:56:11 PM][0.4.5][R2662][reyhard]



[12/2/2017 9:52:55 PM][0.4.5][R2661][reyhard]

@ Fixed duplicate turret hitpoints .rpt spam for some of the vehicles
^ Added new sounds for M1 using soundSet technology 
^ Readded track driveOnComponent to M1
added additional gear to M1 to improve it's uphill performance
tweaked M1 suspension height

[12/2/2017 7:17:13 PM][0.4.5][R2660][da12thMonkey]

@ Unarmed M113 view gunner LOD missing selection names: animation to hide IFF panels did not work, and cupola was always showing desert camo

[12/2/2017 6:51:45 PM][0.4.5][R2659][da12thMonkey]

^ Replaced majority of M1911 mags in M1 Abrams inventory, with M9 mags (correct mags for resupplying crew sidearms)

[12/2/2017 3:11:06 PM][0.4.5][R2658][reyhard]

tweaked max speeds

[12/2/2017 2:33:48 PM][0.4.5][R2657][reyhard]

tweaked M113 PhysX config with new .exe
tweaked M2 track speed


[12/1/2017 9:09:47 PM][0.4.5][R2656][reyhard]

^ Improved M113 PhysX configuration

[11/30/2017 9:35:43 PM][0.4.5][R2655][reyhard]

changed track speed

[11/30/2017 8:44:22 PM][0.4.5][R2654][reyhard]

^ Added recoil coef to USAF vehicle magazines

[11/30/2017 6:18:57 PM][0.4.5][R2653][reyhard]

@ Fixed Mark V SOC Zeus hint 

[11/30/2017 3:24:21 PM][0.4.5][R2652][reyhard]

^ Linked CROWS PiP with current optic mode

[11/30/2017 1:11:27 PM][0.4.5][R2651][da12thMonkey]

^ Removing Longbow radar from AH-64D is now handled through Vehicle Customisation menu (classes for the old editor placeable unit can still be spawned, VhC hides radar model and disables active radar sensor)
- Redundant animation to hide AIM-9s on AH-64D, no longer shows in Vehicle Customisation (was made obsolete by Dynamic Loadouts)

Unified Dynamic Loadouts config for AH-64, in to one file

[11/29/2017 9:55:05 PM][0.4.5][R2650][reyhard]

^ Reduced headbanging when driving M113 & M2 Bradley
suspension anim test for M1

[11/29/2017 8:00:00 PM][0.4.5][R2649][da12thMonkey]

Updated M113 edPrev images

[11/29/2017 4:03:06 PM][0.4.5][R2648][reyhard]



[11/29/2017 2:50:49 PM][0.4.5][R2647][da12thMonkey]

^ Picture in Picture bounding box tech applied to vehicle models. For optimising non-scripted PiP screens

[11/29/2017 2:14:14 PM][0.4.5][R2646][da12thMonkey]

@ Editor option to fold MRZR roll cage, was not functioning

[11/29/2017 1:46:31 PM][0.4.5][R2645][da12thMonkey]

@ PiP view on FMTVs' passenger side mirrors, were inverted

[11/29/2017 12:19:01 PM][0.4.5][R2644][da12thMonkey]

Converted the remainder of the configs to use `global_macro_defines.hpp` (save for rhsusf_main)

PIP_BB for TOW

[11/29/2017 10:47:06 AM][0.4.5][R2643][da12thMonkey]

Defined PiP BoundingBoxes for HEMTT and M1025, transitioned their configs to globalmacro

[11/29/2017 10:40:16 AM][0.4.5][R2642][reyhard]



[11/29/2017 10:37:54 AM][0.4.5][R2641][reyhard]

tweaked suspension travel dir for M2 Bradley
some initial tweaks to M1 PhysX

[11/29/2017 4:00:23 AM][0.4.5][R2640][gurdy]

@ some missing geo in 90s M113

[11/29/2017 12:46:18 AM][0.4.5][R2639][da12thMonkey]

@ Some vehicles had missing author strings when running USAF standalone
@ Only one mirror was functioning in FMTV gunner's view

Initial set up of PiP bounding boxes on USAF vehicles (Caimans, RG-33Ls, M1117, FMTVs, MkV SOC so far)

Progressively switching vehicle configs to the root global_macro_defines.hpp and removing the old script_###.hpp files during the process of defining PiP BBox

`author=` string defined in global_macro_defines.hpp was the wrong one for USAF - missing author tags when running the mod standalone

[11/28/2017 11:39:42 PM][0.4.5][R2638][reyhard]

^ Added new PhysX to M2 Bradley family vehicles
^ Added interior occluders to M2 Bradley family vehicles

[11/28/2017 3:43:49 AM][0.4.5][R2637][ballistic09]

fixed proxy retex on new, early M113s

[11/28/2017 12:42:19 AM][0.4.5][R2636][gurdy]

+ initial injection of 1990s M113s

[11/27/2017 9:05:01 PM][0.4.5][R2635][reyhard]

+ Added partial gripod support for AI units when loadout is edited through Virtual Arsenal

[11/27/2017 5:42:10 PM][0.4.5][R2634][da12thMonkey]

@ SU-230/PVS (CX5395) version of SpecterDR, was not displaying the correct reticle in 2D optics

[11/27/2017 2:33:54 PM][0.4.5][R2633][da12thMonkey]

@ `rhsusf_mrzr4_w_mud` missing textures error

[11/27/2017 1:28:57 PM][0.4.5][R2632][da12thMonkey]

OEF-CP IOTVs generated by macro were not parsing correctly through rapify

[11/26/2017 3:39:00 PM][0.4.5][R2631][da12thMonkey]

^ Clean-up of M240 sections, UVsets and named properties

[11/26/2017 12:28:36 PM][0.4.5][R2630][Bek]

^ Tweaked XPS3 Textures

[11/25/2017 4:28:55 PM][0.4.5][R2629][reyhard]

^ Limited dynamic object drawing to Object Draw Distance

[11/25/2017 4:28:07 PM][0.4.5][R2628][reyhard]

^ Added additional seat to MH-6M to fix issues with LOAD waypoint

[11/22/2017 10:13:47 PM][0.4.5][R2627][reyhard]

^ Added displayNameShort to USAF magazines
added blank.rtm to force rapifing through zombified exe

[11/22/2017 1:12:37 PM][0.4.5][R2626][reyhard]

@ Fixed Doomsday mags ammo count

[11/19/2017 7:12:44 PM][0.4.5][R2625][da12thMonkey]

^ Improved Leupold MK4+M2010 scope alignment

Reverted `Heli_light_03_base_F` hitpoints configuration for testing in RC - please see if UH-1Y hitpoints error appears or not while running 1.78RC (Tac-Ops DLC)

[11/17/2017 9:15:20 AM][0.4.5][R2624][reyhard]

^ Cargo script is able to attach boats too
^ Forced AH6 & MH6 visibility in virtual garage

[11/11/2017 3:42:23 PM][0.4.5][R2623][da12thMonkey]

@ `Heli_light_03_base_F` missing hitpoints error

[11/10/2017 10:06:15 PM][0.4.5][R2622][reyhard]

some wip lead tweaks
@ Fixed NT4 shadows

[11/10/2017 9:44:26 PM][0.4.5][R2621][reyhard]

@ Fixed FMTV missing gunner proxies in fire geometry

[11/10/2017 8:46:45 PM][0.4.5][R2620][reyhard]

@ Fixed Caiman & FMTV 3rd person camera

[11/10/2017 8:05:30 PM][0.4.5][R2619][reyhard]

@ Fixed Duke hint being visible for everyone in MP

[11/10/2017 12:29:42 PM][0.4.5][R2618][reyhard]

@ Fixed MBAV Grenadier vest hitpoints inheritance

[11/9/2017 8:52:41 PM][0.4.4][R2617][Soul_Assassin]

Bumped version numbers

[11/9/2017 7:37:06 AM][0.4.4][R2616][ballistic09]

@ Fixed parts of M153 CROWS glass not rotating with the rest of the turret

[11/8/2017 11:12:10 PM][0.4.4][R2615][Soul_Assassin]

Version file now contains shortname of mod

[11/8/2017 8:34:58 PM][0.4.4][R2614][reyhard]

^ Adjusted A10A hitpoints

[11/8/2017 7:08:05 PM][0.4.4][R2613][da12thMonkey]

^ Cleaned out several redundant UV sets in M249+VFG models

[11/8/2017 4:22:42 PM][0.4.4][R2612][da12thMonkey]

^ Adjusted M249 weapon masses, based on their visual configuration (fitted rails, bipod etc.)

[11/7/2017 8:36:08 AM][0.4.4][R2611][reyhard]

bumped version number in pbo prefix

[11/6/2017 8:06:16 PM][0.4.4][R2610][da12thMonkey]

Reverting change to SR25 materials assignment

[11/5/2017 11:00:58 PM][0.4.4][R2609][keplager]

@ UH-60 Tweaked longitudinal cyclic ranges.

@ UH-60 Tweaked mixing values.

[11/5/2017 9:26:23 PM][0.4.4][R2608][reyhard]

some dangerous commit to improve ejection script

[11/5/2017 7:21:00 PM][0.4.4][R2607][da12thMonkey]

@ M1078A1R SOV speedometer movement was backwards
^ Reduced flickering of gauges in driver's view of SOV FMTVs

[11/5/2017 6:36:41 PM][0.4.4][R2606][reyhard]

ejection damage fix

[11/5/2017 5:29:03 PM][0.4.4][R2605][da12thMonkey]

Fixed: M1084A1R SOV cab was missing from `zbytek` selection
Placed woodland SOV FMTVs in hidden scope from editor - seems more efficient to use Vehicle Appearance Editor for this since SOCOM don't have separate Wdl/Des factions

[11/5/2017 3:15:17 PM][0.4.4][R2604][reyhard]

^ Adjusted A10A hitpoints

[11/5/2017 2:28:32 PM][0.4.4][R2603][da12thMonkey]

Added camo .rvmats to lower LODs of both SR25 rifles

[11/5/2017 1:47:34 PM][0.4.4][R2602][reyhard]

@ Removed M113 hatch movement from unarmed variant (didn't find way to somehow give control over rotation) - close T2297

[11/5/2017 1:12:05 PM][0.4.4][R2601][reyhard]

removed hiddenSelectionMaterials from mk18 & Block II

[11/4/2017 11:42:40 PM][0.4.4][R2600][Soul_Assassin]

Version number reverted to 0.4.4

[11/4/2017 11:27:35 PM][0.4.4][R2599][Soul_Assassin]

Readded missing string after Italian merge

[11/4/2017 11:25:00 PM][0.4.4][R2598][keplager]

@ UH-60 Fixed linearization of lateral cyclic in last update.

@ UH-60 Changed controls mixing and roll damper SAS gain.

[11/3/2017 10:44:38 PM][0.4.4][R2597][jastreb]

+ Italian strings by AtixNeon

[11/2/2017 12:56:46 PM][0.4.4][R2596][da12thMonkey]

Added: edPrev and Garage images for new SOCOM FMTV variants
Fixed: SOCOM FMTVs didn't apply correct woodland texture to some parts in Vehicle Customisation menu

[11/2/2017 11:27:10 AM][0.4.4][R2595][da12thMonkey]

+ Eden editor attribute for M1085 CBPS and M1078 CP Box deployment
^ Cleaned out redundant animation options from M1085 CBPS and M1078A1R M1084A1R SOVs in Virtual Garage

Configured smoke launchers for M1084A1R SOV driver
Adjusted alignment of memory points for M1084A1R SOV's M2 HMG

[11/1/2017 11:33:01 PM][0.4.4][R2594][keplager]

@ UH-60M adjusted curve of lateral cyclic controls.

[11/1/2017 10:32:36 PM][0.4.4][R2593][RichardsD]

@ Fixed SOV textures

[11/1/2017 9:34:54 PM][0.4.4][R2592][RichardsD]

+ Adds M1084 Special Operations Vehicle
@ SOV texture fixes

[10/31/2017 6:50:57 PM][0.4.4][R2591][ballistic09]

^ Removed manual guidance from Longbow Hellfire
^ Added manual guidance to DAGR

[10/31/2017 11:48:53 AM][0.4.4][R2590][reyhard]

@ Fixed typo in UH60 door eden attribute

[10/29/2017 10:06:05 AM][0.4.4][R2589][reyhard]

@ Fixed M113 driver KIA anims
@ Fixed rogue IFF proxy in of the m113a3 w/ m240 LODs

[10/28/2017 7:12:39 PM][0.4.4][R2588][reyhard]

^ Adjusted M1 coax FCS calculations

[10/28/2017 4:02:24 PM][0.4.4][R2587][reyhard]

^ Tweaked UH-1Y firegeometry & hitpoints

[10/28/2017 4:00:11 PM][0.4.4][R2586][reyhard]

added isNil check

[10/28/2017 1:29:38 PM][0.4.4][R2585][reyhard]



[10/28/2017 1:23:06 PM][0.4.4][R2584][reyhard]

revamped panels selection

[10/27/2017 10:22:11 AM][0.4.4][R2583][reyhard]

version number

[10/27/2017 10:20:38 AM][0.4.4][R2582][reyhard]

fixed agm65 max lock range

[10/26/2017 9:51:09 PM][0.4.4][R2581][HarryD]

^ Tweaked sensors range further
^ Tweaked CH-53 sensors and display range
^ got AGM-56B 3500m range back

[10/26/2017 9:06:25 PM][0.4.4][R2580][reyhard]

@ Fixed FMTV SOV get in memory points

[10/26/2017 8:41:47 PM][0.4.4][R2579][reyhard]

^ Tweaked UH-1Y & UH-60M hitpoints
^ Added manual control to laser guided Hellfires as interim solution to locking issues

[10/26/2017 7:57:35 PM][0.4.4][R2578][reyhard]

forgot to commit files for usaf

[10/26/2017 3:17:45 PM][0.4.4][R2577][reyhard]

+ Added Dynamic Object Drawing option to RHS Menu Options. In planes & helicopters it's possible to decide whether near zero pixel object chopping optimization should be applied to ground vehicles. Following options are available: Off, Limited by Object View Distance, Limited by Terrain Draw Distance. By default option is turned off

[10/26/2017 6:51:04 AM][0.4.4][R2576][reyhard]

badaboom

[10/25/2017 11:22:40 PM][0.4.4][R2575][HarryD]

Sensors range overhaul

[10/24/2017 11:21:50 PM][0.4.4][R2574][HarryD]

Tweaking Stinger params to improve the hit probability and target tracking. Inherited from M_Titan_AA instead of MissileBase now as well

[10/24/2017 10:16:33 AM][0.4.4][R2573][reyhard]

@ Fixed SU-230/PVS (CX5395) not being visible in Arsenal

[10/23/2017 8:18:51 PM][0.4.4][R2572][reyhard]

@ Fixed A10A RWR not showing detected threats properly
@ Removed manual control from some AGM65 missile variants

[10/23/2017 6:54:31 PM][0.4.4][R2571][reyhard]

^ Increased M1117 wheels protection
@ Fixed M113 missing right click zoom for driver
@ Fixed M622 6rnd smoke grenade mass
^ Some more tweaks to A10A TVM script

[10/23/2017 6:08:53 PM][0.4.4][R2570][reyhard]

@ Fixed Littlebird gravity boxes collision

[10/23/2017 3:49:43 PM][0.4.4][R2569][reyhard]

^ Added showAsCargo params to UH-1 & 60
@ Fixed A10A TVM not shutting down after firing all Mavericks
@ Fixed engine startup script

[10/23/2017 4:38:43 AM][0.4.4][R2568][RichardsD]

@ Fixes textures for SOV FMTV and adds new areas for upcoming SOV model

[10/21/2017 11:36:08 AM][0.4.4][R2567][da12thMonkey]

@ Typo in `RHS_MELB_AH6M_H` classname

[10/20/2017 8:51:57 PM][0.4.4][R2566][da12thMonkey]

Fixed LT660 + G33 holo collimator effect

[10/20/2017 11:46:49 AM][0.4.4][R2565][PuFu]

@ fixed LT660 holo collimator effect

[10/18/2017 6:17:46 PM][0.4.4][R2564][PuFu]

^ improved glock 17 diffuse textures

[10/18/2017 1:40:02 PM][0.4.3.1][R2563][Soul_Assassin]

Version bump to 0.4.4

[10/18/2017 1:16:39 PM][0.4.3.1][R2562][j0zh94]

Reuploaded fixed CH47 sound

[10/18/2017 9:04:51 AM][0.4.3.1][R2561][Soul_Assassin]

Updated version in main

[10/17/2017 9:10:58 PM][0.4.3.1][R2560][keplager]

@ UH-60M Slightly tweaked SAS and collective ranges.

[10/17/2017 5:52:21 PM][0.4.3.1][R2559][da12thMonkey]

Already got tagged in the changelog, so we'll let them have balance not bias this time :P

[10/17/2017 5:37:01 PM][0.4.3.1][R2558][reyhard]

USA bias

[10/17/2017 5:25:50 PM][0.4.3.1][R2557][reyhard]

^ Another tweak to engine startup script to improve it's behaviour in MP
@ A10A RWR should no longer detect IR missiles

[10/16/2017 6:57:58 PM][0.4.3.1][R2556][reyhard]

+ Added engine startup delay to A10A

[10/15/2017 8:57:07 PM][0.4.3.1][R2555][da12thMonkey]

@ FMTV exhaust pfx location
^ FMTV fording depth

[10/15/2017 4:36:41 PM][0.4.3.1][R2554][reyhard]

readded ch47 sounds

[10/15/2017 3:37:29 PM][0.4.3.1][R2553][reyhard]

test

[10/15/2017 9:02:17 AM][0.4.3.1][R2552][reyhard]

another attempt

[10/15/2017 8:11:11 AM][0.4.3.1][R2551][reyhard]



[10/15/2017 8:08:09 AM][0.4.3.1][R2550][reyhard]

test

[10/14/2017 9:55:07 PM][0.4.3.1][R2549][j0zh94]

@ Fixed iotv lod issue

[10/14/2017 2:49:43 PM][0.4.3.1][R2548][j0zh94]

@Improved Chinook rotor sound

[10/13/2017 6:03:30 PM][0.4.3.1][R2547][da12thMonkey]

Removed flag area from ACU personalisation selection (and renamed from 'patches' to 'identity'), per clima_x's intentions

[10/13/2017 2:41:23 PM][0.4.3.1][R2546][da12thMonkey]

Added the square rank patch to ACU customisation selection

[10/13/2017 1:53:35 PM][0.4.3.1][R2545][da12thMonkey]

+ Extra selection for flag patch and name tape customisation on ACU

[10/13/2017 9:25:21 AM][0.4.3.1][R2544][Soul_Assassin]

+ Added version file

[10/13/2017 8:53:35 AM][0.4.3.1][R2543][reyhard]

@ Corrected UH1 HUD position & tweaked FFAR ammo params

# Revision 2543 - reyhard

@ Corrected UH1 HUD position & tweaked FFAR ammo params

# Revision 2542 - reyhard

@ fixed some MAAWS ammo values

# Revision 2541 - reyhard

^ m242 lock disabled

# Revision 2540 - da12thMonkey

^ ESSS/EWS UH-60s missing from cfgPatches

# Revision 2539 - keplager

+ UH-60M Added Pitch Bias Actuator.

^ UH-60M improved SAS.

@ UH-60M adjusted cyclic and collective values.

# Revision 2538 - Redphoenix

@ Fixed wrong texture name for MRZRs in distant LODs

# Revision 2537 - reyhard

^ more tweaks to Mk211 particle effects

# Revision 2536 - reyhard

^ tweaked Mk211 particle effects
@ fixed BMG tracers

# Revision 2535 - reyhard

@ fixed Stinger inventory restrictions
^ tweaked Stinger ammo params

# Revision 2534 - da12thMonkey

@ Caiman transport capacity was wrong on a couple of variants

# Revision 2533 - PuFu

^removed ace_overpressure entries

# Revision 2532 - keplager

@ Changed UH-60Mcollective ranges.

@ Changed UH-60M ATRQ ranges.

# Revision 2531 - da12thMonkey

@ Last commit didn't like `Author_Macro_BIS_Port` macro, and F-22 isn't a BIS port anyway

# Revision 2530 - reyhard

@ fixed F-22 texture selection

# Revision 2529 - da12thMonkey



# Revision 2528 - da12thMonkey

^ Extended AGM-114 locking ranges to some degree. Following indications by gatordev that 4km is below average laser Hellfire performance
^ Extended AH-64D radar coverage in line with the changes to its main armament

# Revision 2527 - da12thMonkey

@ Forgot to replace the armed RG-33s in Army groups as well

# Revision 2526 - reyhard

@ removed gunner seat from ejection seats
^ tweaked M430 & M433 damage values 


# Revision 2525 - reyhard

@ reduced some the M1 HEAT rounds max lead

# Revision 2524 - da12thMonkey

@ "lever ramp" misspelling
^ US Army RG-33 groups now use the 6*6 models instead of the old outdated (and hidden) 4*4

# Revision 2523 - reyhard

^ increased M19 mine hit value

# Revision 2522 - reyhard

@ fixed AH1Z/AH64 gunner sensors

# Revision 2521 - keplager

^ Improved auto-trimmer functionality for UH-60M AFM

# Revision 2520 - reyhard



# Revision 2519 - reyhard

@ fixed broken inheritance of M16 & M24/M40 in sound config

# Revision 2518 - Redphoenix

@ Fixed Shadow inside A-10 speedbrakes

# Revision 2517 - da12thMonkey

^ Updated clima_x's bloody ACU jacket texture

# Revision 2516 - Soul_Assassin

^ Balanced USAF aircraft armor against AFRF counterparts

# Revision 2515 - Soul_Assassin

@ Fixed FCS script error

# Revision 2514 - da12thMonkey

^ Adjusted OGPK shadows on FMTV. Close T2279

# Revision 2513 - da12thMonkey

^ Copy-Pasted horizontal compass UI for Abrams gunner, as an interim solution to turret direction indication

# Revision 2512 - Soul_Assassin

@ Fixed MRZR bumper stickers.

# Revision 2511 - da12thMonkey

@ F-22 missing eject action
@ M2 HMG parts missing from LMTVR SOV's view Cargo LOD. Close T2280

# Revision 2510 - da12thMonkey

+ Adding clima_x bespoke ACU wound textures

# Revision 2509 - Fuxna

USAF ACU uniform

Corrected missing uv on shoe laces

# Revision 2508 - keplager

@ Changed some UH-60M ESSS/EWS variant torque values (missed in last change)

@ Moved UH-60 hinge angle slightly prograde.

# Revision 2507 - da12thMonkey

^ Wound .rvmats for ACU

# Revision 2506 - Redphoenix

wip Bumperstickers

# Revision 2505 - da12thMonkey

^ Reduced vertical stretching of insignia on Massif combat shirt

# Revision 2504 - da12thMonkey

^ Added macro for equipping units with ACU. Applied to UCP driver

# Revision 2503 - da12thMonkey

^ Support for insignia and clan patches on ACU

# Revision 2502 - ballistic09

+ Army Combat Uniform (copied over from SAF)

# Revision 2501 - Redphoenix

- Arbitray Decal Folder
@ Moved Bumper Stickers

# Revision 2500 - Redphoenix

@ Improved textures once more (unified them)
+ Missing LOD merged textures

# Revision 2499 - da12thMonkey

+ Army units equipped with MAAWS

# Revision 2498 - da12thMonkey

^ standardised MAAWS ammo and magazine names
^ added MAAWS to crates and Eden objects

# Revision 2497 - da12thMonkey

^ Added cluster bomb variant of A-10A, for Zeus' CAS module

# Revision 2496 - Redphoenix

+ MRZR ODA and MARSOC Decals
+ Olive MRZR textures
+ ODA Decals for MRZR
@ Final MRZR texture tweaks

# Revision 2495 - reyhard



# Revision 2494 - j0zh94

+ Injection of M3 MAAWS (all but smoke complete)

# Revision 2493 - keplager

+ Added AH-64 AFM

@ Marine helos Changed torque values for instrumentation/failure

@ Fixed issue where airspawned Marine helos would ramdomly explode.

@ Tweaked some AFCS settings for AH-1Z/UH-1Y

@ Added directional stability channel for CH-53E

# Revision 2492 - keplager

@ Changed torque values for instrumentation/failure

@ Fixed issue where airspawned marine helicopters running AFM would randomly explode

# Revision 2491 - keplager

@ Changed engine torque% gauges to match engine values.

# Revision 2490 - keplager

@ Changed instrumentation/failure torque values.

# Revision 2489 - reyhard

^ added LAU117 pylon using Jets DLC model
^ it's possible to adjust TVM in internal view even when camera is locked to certain grid

# Revision 2488 - reyhard

^ updated warning lights

# Revision 2487 - da12thMonkey

^ Reduced Maverick `maxTrackableSpeed` values (AGM-65BB now has some trouble tracking moving targets)

# Revision 2486 - reyhard

@ fixed mastersafe not workign after changing loadout

# Revision 2485 - reyhard

^ some tweaks to A10A TVM

# Revision 2484 - da12thMonkey

^ M109 driver anims. Close T2239

# Revision 2483 - reyhard

@ tahomab removal

# Revision 2482 - reyhard

^ MP optimization of FCS code
^ optimized A10A TVM

# Revision 2481 - reyhard

@ test fix

# Revision 2480 - j0zh94

^ Introduced M855 Ball ammunition+magazines. Replaced applicable magazines with M855. Minor adjustment to M4 sounds to better unify 5.56 weapons

# Revision 2479 - da12thMonkey

^ Changed Caiman CROWS usePiP value

# Revision 2478 - reyhard

^ some tweaks to A10A HUD

# Revision 2477 - reyhard

@ removed one M2 mag to test M113 .rpt spam

# Revision 2476 - da12thMonkey

^ Minor tweak to AGM-65E texture, for appearance in lower LODs

# Revision 2475 - reyhard

@ fixing space sign

# Revision 2474 - reyhard

@ macro fixing

# Revision 2473 - reyhard

@ replaced define with number

# Revision 2472 - Soul_Assassin

Unburn (trailing commas)

# Revision 2471 - reyhard

^ some final touches to A10A HUD

# Revision 2470 - reyhard

@ added missing semicolons  

# Revision 2469 - da12thMonkey

@ Typo in Maverick 'missileLockMinDistance' value (one too many zeros)

# Revision 2468 - da12thMonkey

^ Adjusted colour of Maverick motor band (more brown than pink now) and AGM-65D olive drab colour
^ revised Maverick sensor and locking capabilities

# Revision 2467 - reyhard

+ Very WIP TVM camera script - camera movement is attached to user15-18 actions. I assigned "Home","End","Delete","Pg Dn" keys for them & it's working pretty well in this combination
^ some tweaks to A10A interior - added new glass by da12thMonkey, decimal air speed indicator & improved some detail textures

# Revision 2466 - Redphoenix

^ Improved MRZR Textures
@ Fixed and replaced MRZR horn with something more appropriate than a truck horn

# Revision 2465 - Redphoenix

^ MZRZ PhysX

# Revision 2464 - da12thMonkey

@ MP7 optics slot wasn't centred

# Revision 2463 - Redphoenix

@ Fixed hole in front of SR25 Supressor

# Revision 2462 - da12thMonkey

^ Modified Laser Maverick's seeker

# Revision 2461 - da12thMonkey

+ Maverick variant models

# Revision 2460 - Redphoenix

+ Added new mesh in edit lod

# Revision 2459 - Redphoenix

@ New and Improved Normal Map for AGM65

# Revision 2458 - j0zh94

@Removed last round tracer and increased tracer every count to 5

# Revision 2457 - da12thMonkey

^ Config setup for anticipated Maverick variants

# Revision 2456 - j0zh94

@Removed last round tracer on all non tracer magazines 

# Revision 2455 - reyhard

^ some more tweaks and improvements 

# Revision 2454 - da12thMonkey

+ T1/G33 combo optic
^ Fixed a minor smoothing group error on the G33 mount

# Revision 2453 - da12thMonkey

^ Equipped MARSOC units with current crop of MBAV vests
^ Crewed M1078A1R SOV with the hidden Army SF rifleman

# Revision 2452 - ballistic09

@ Applied reyhard's IBAS CIV fix to gunner's sight as well, to fix another "no mag" condition in virtual garage that could also throw script errors

# Revision 2451 - da12thMonkey

^ Added some items that were missing from virtual ammobox and Eden
^ Hopefully fixed Vector 21 ranging numerals being cut off

# Revision 2450 - reyhard

^ some more tweaks to A10A cockpit

# Revision 2449 - reyhard

@ fixed IBAS errors when geting in on commander seat for first time
^ some tweaks to A10A cockpit & HUD

# Revision 2448 - reyhard

^ animated most of the cockpit gauges
^ some more WIP work on A10 HUD

# Revision 2447 - reyhard

@ defines fixing

# Revision 2446 - reyhard

@ added missing mem points after merging

# Revision 2445 - reyhard

^ added A10A weapon system functionality
^ changed A10A GAU8 ammo count to 1150

# Revision 2444 - da12thMonkey

+ Configured initial CBU-100 Rockeye and CBU-87 cluster munitions for USAF, as requested by reyhard (both are using Jets DLC Rockeye model in the interim)
^ Adjusted height of middle bomb rail on ported Tripple Ejector Rack - it looked too long in proportions to Mk82 diameter

# Revision 2443 - Redphoenix

+ AGM65

# Revision 2442 - da12thMonkey

@ A-10 pylon proxy numbers for added centreline pylon

# Revision 2441 - reyhard

^ some more work on A10A cockpit & it's indicators

# Revision 2440 - reyhard

something something missing file

# Revision 2439 - reyhard

^ some A10 work

# Revision 2438 - da12thMonkey

^ Adding some weapons and attachments that were missing from crates and Eden weaponHolder items
^ Hiding old 3D/PiP variants of scope items, since they are now swapped out according to users' settings anyway

# Revision 2437 - reyhard

^ added improved a10a interior

# Revision 2436 - da12thMonkey

^ LMTV SOV gunner's sight alignment

# Revision 2435 - da12thMonkey

^ Removed Longbow Hellfires from AH-6 loadouts menu (AGM-114L requires radar to lock)

# Revision 2434 - da12thMonkey

+ Dynamic loadouts setup for AH-6 MELB
^ Clean up of data and classes replaced by dynamic loadouts
+ CROWS version of M2 HMG proxy, with no hanging ammo belt. (Applied to Caiman)

# Revision 2433 - reyhard

^ removed physx barrel

# Revision 2432 - da12thMonkey

@ Cleaned up some trailing commas in arrays inside WIP A-10A HUD config, to pass build

# Revision 2431 - reyhard

^ improved ejection script
^ some early rework of A10A HUD

# Revision 2430 - da12thMonkey

@ Orbiting spare wheel technology removed from M1078 LMTV's bottom LODs
+ Garage icon for M1078A1R SOV
^ Applied fix for improper getin order, to vehicles that have 'enabledByAnimationSource' property in FFV seats

# Revision 2429 - reyhard

+ added new physx params to tracked vehicles (devbranch)

# Revision 2428 - reyhard

^ added missile firing anims to rest of the missiles/rockets - close T2156
^ disabled scripted flame hidding for tow
^ added soft launch anims for Javelin
^ some cleanup
^ adjusted dispersion of FFAR launcher

# Revision 2427 - reyhard

^ soundFly cleanup

# Revision 2426 - reyhard

@ fixed Mk19 max zeroing
^ added some zeroing steps to Mk19 mounted on vehicles
^ tweaked ejection seats

# Revision 2425 - reyhard

@ fixed TOW thrust hiding animations
^ tweaked size of TOW tracer

# Revision 2424 - da12thMonkey

^ Animated fins and exhausts on TOW missile models

# Revision 2423 - RichardsD

@ Actually fixed the texture for the M1078A1R this time

# Revision 2422 - RichardsD

@ Texture fix for M1078A1R SOV

# Revision 2421 - da12thMonkey

^ SOV damage .rvmats
@ M2 HMGs on FMTVs had no visible ammunition in view Gunner LOD

# Revision 2420 - reyhard

^ unified physx of M1A1 & M1A2 - close T2193

# Revision 2419 - da12thMonkey

Work on M1078A1R SOV:
+ EdPrev image
^ Moved truck to SOCOM faction (might knock together a hidden class for an Army ODA driver to crew it later)
^ Geo LOD and named properties stuff for proper buoyancy and fording
^ Cleared of userActions and Reflector classes relating to redundant SVC and Cabin lights
^ Set up vehicle for hiddenSelections and cleaned up sections count
^ Set `canhideGunner=0;` (useless to be able to turn in, if there's no gunner protection)
@ No crew proxy for configured third `transportSoldier` slot

# Revision 2418 - reyhard

@ added missing pboprefix to FMTV folder

# Revision 2417 - RichardsD

+ Adds M1078A1R "War Pig" Variant

# Revision 2416 - PuFu

.

# Revision 2415 - PuFu

T1 colimator tweak

# Revision 2414 - reyhard

@ disabled BI scripted ejection EH
^ improved z bias of interior + tweaks to gauges textures of fmtv
^ added geometry buoyancy lod to make fmtv less ship like
^ added buoyancy property to M1025ies

# Revision 2413 - da12thMonkey

^ Adjusting Caiman and FMTV fording behaviour (FMTVs are rather buoyant for some reason though)

# Revision 2412 - da12thMonkey

^ Replaced AIM-9X model with the one from Jets DLC

# Revision 2411 - da12thMonkey

@ Spent cases spawning from vehicle centre when firing M2 HMG on several vehicles (missing `nabojnicestart2`+`nabojniceend2` memory points)
@ tan PEQ-15 would turn black when switching initial laser/light mode on the HK416 variant of PEQ-15/M952V combo attachment

# Revision 2410 - da12thMonkey

^ Adjusted FMTV driver's hands to better fit steering wheel

# Revision 2409 - da12thMonkey

+ Forward-mounted variants of Aimpoint T1 (and script to switch them on appropriate AKs)

# Revision 2408 - da12thMonkey

- Clean up of accidental commit of forward-positioned T1 model I was testing yesterday. (Feature's not working without issues yet and might need fundamental changes. So best to revert for now)

# Revision 2407 - PuFu

^ T1 stringtables

# Revision 2406 - da12thMonkey

+ P1NGA's Vector 21-B, with basic rangefinding function and optics
^ Remade Lerca optics at higher resolution
@ Missing font error with Lerca rangefinder when running USAF standalone (there is still an error from `RHS_fnc_laserTarget` function call in rhs_leica_rf.sqf - laserTarget function depends on AFRF)

# Revision 2405 - Soul_Assassin

Sneaky scheeky breeky T1 rvmat tweak

# Revision 2404 - PuFu

^ T1 covers rvmats updates based on SA's feedback

# Revision 2403 - da12thMonkey

^ Adjusted position of Dynamic Loadouts menus to better accommodate "Pylon Owner" buttons added in 1.76

# Revision 2402 - reyhard

^ added global macro to USAF

# Revision 2401 - reyhard

@ fixed MP7 muzzle velocity

# Revision 2400 - reyhard

^ FFARs are now controlled by pilot

# Revision 2399 - da12thMonkey

@ .rvmat path typo in T1 model

# Revision 2398 - PuFu

forgot to add magic boxes

# Revision 2397 - PuFu

further T1 tweaks

# Revision 2396 - j0zh94

@Fixed and updated MRZR sounds

# Revision 2395 - PuFu

^ added AIMPOINT MICRO T1 scopes

# Revision 2394 - da12thMonkey

- Scoped out unfinished Plateframe from 0.43 release. Until it gets some LODs

# Revision 2393 - Soul_Assassin

Options menu version bumped to 0.4.3

# Revision 2392 - Redphoenix

@ Improved FMTV Engine and Braking PhysX

# Revision 2391 - reyhard

^ increased maxSpeed param for AH1Z & AH64 - rising fix

# Revision 2390 - da12thMonkey

^ Replace/rename 120mm (X)M1069 AMP ammunition with M1147 designated AMP. All old M1069 classes still exist for backward compatibility reasons, but are not in the Editor attributes selection menu. Close T2004
@ "Carnister" typo

# Revision 2389 - da12thMonkey

^ Moved Blackhawk ESSS/EWS wings in to the helicopter models rather than using proxies. For easier retexturing with the 'camo2' hiddenSelection

# Revision 2388 - reyhard

@ fixed Caiman Crows
@ removed duplicated DUKE

# Revision 2387 - da12thMonkey

^ Alignment of Caiman wheel shadow volumes

# Revision 2386 - reyhard

^ commented out aiDispersionCoefs for tank cannons since it's going to be enabled on devbranch soon - to be uncommented after release

# Revision 2385 - reyhard

^ configured dispersion for USAF rocket launchers

# Revision 2384 - reyhard

@ fixed updating base class errors 
^ updated cfgPatches of some addons
^ some minor clean up

# Revision 2383 - reyhard

^ improved particle effects of Stinger & flashbangs

# Revision 2382 - reyhard

@ fixed seat count on CH47

# Revision 2381 - PuFu

^ improved omega9k co texture map

# Revision 2380 - reyhard

@ fixed USF weapon holders

# Revision 2379 - Redphoenix

+ Animation for M1025 Temperature Gauges

# Revision 2378 - da12thMonkey

^ Animated M113 track brake levers in driver's interior

# Revision 2377 - da12thMonkey

^ Gunner stick anims for Caiman (might be supported in Dev only, for now)

# Revision 2376 - da12thMonkey

^ Applied mysterious hypercube technology to collimated optics. Black magic fix for alpha-sorting issues on some weapons

# Revision 2375 - da12thMonkey

+ steering yoke anims for the Bradley

# Revision 2374 - da12thMonkey

@ Adjusted M113 Driver anim and cargo proxy positions, to stop assorted arses and legs from poking out of the hull. Close T2150

# Revision 2373 - da12thMonkey

@ Fixing some selection issues in last LOD of FMTVs (wrong hiddenselection for spare wheel, stretching of verts welded to selections hidden by animation etc. etc.)

# Revision 2372 - da12thMonkey

+ FMTV Garage icons

# Revision 2371 - da12thMonkey

@ SOCOM units were missing NVG eventHandler

# Revision 2370 - da12thMonkey

@ FMTV backwards compatibility (restored ###_wd_### type classnames)

# Revision 2369 - da12thMonkey

@ Some parts of M1230A1 (Caiman ambulance) and M1084 (MTV) did not display damage materials. Close T2194
+ Eden preview images for FMTV variants to date

# Revision 2368 - da12thMonkey

^ Reduced insanely high impulse acceleration characteristics of AIM-9 and AIM-120 (equivalent to Mach 8.45 in 1 second) to a more realistic values

# Revision 2367 - j0zh94

^ Replaced AT4 sound with SMAW sound

# Revision 2366 - da12thMonkey

Forcing rebuild while Temp cache is clear

# Revision 2365 - da12thMonkey

@ Troop capacities for FMTV variants
@ Parts of FMTV passenger doors weren't animating
^ RHS Pistol laser/light slot for Glock, made compatible with new CBA Joint Rails pistol slot

# Revision 2364 - da12thMonkey

+ Added modified function to stop FMTV CP Box and CBPS variants from being able to drive when stairs/platforms deployed
^ Action to open CP box door is now accessed from outside, rather than the driver's seat
^ CBPS can now only be deployed when stairs/platform is deployed and the vehicle cannot move (and stairs/platform stowed only when CBPS is packed away)
^ Much improved solution to the 3rd axle of FMTV variants not touching the ground (adjusted geometry LODs and suspension memory points on all models)
@ Some parts of FMTV spare wheels would not hide when the customisation option was activated

# Revision 2363 - da12thMonkey

@ Caiman floating slightly above ground: adjusted suspension range of motion

# Revision 2362 - da12thMonkey

@ Wrong Copy&Paste inheritance with hide_bench anim source

# Revision 2361 - da12thMonkey

^ Configured flatbed versions of FMTVs, with cargo-carrying capabilities and no bench seats.
^ Scoped out "Open" FMTV variants (can be set up through Appearance menu anyway)
^ Adjusted mass distribution on M1083s to bring wheels closer to the ground
^ Shadow LOD improvements
@ Missing mirrors in top LOD of some B-kit cabins

# Revision 2360 - da12thMonkey

^ Defined M1084 cargo-carrying space
^ Set memory point `dimensions[]` for M1085 CBPS (native bounding box is too big to transport in Blackfish etc. because of tent)

# Revision 2359 - RichardsD

@ Adds M1084 5T with Load Handling Crane
@ Various texture updates (Cab, BKIT, CBPS)

# Revision 2358 - da12thMonkey

^ Some FMTV parts did not show visual damage (either missing from zbytek or .rvmat sets were not defined in `class Damage`)
^ Replaced M1085 CBPS rear deck wood penetration material, with metal

# Revision 2357 - Meatball0311

I updated the shoulder straps weighing and side straps.

# Revision 2356 - da12thMonkey

^ US pistol inventory/Arsenal icon aspect ratios made consistent with BIS

# Revision 2355 - da12thMonkey

+ Extra inventory images for various weapon accessories
@ Parts were missing from the `head` selection in lower LODs of one of the MICH helmets

# Revision 2354 - da12thMonkey

^ Minor adjustments to M1078 CP Shelter model: (Removed tailgate that clipped opening rear door, and  bench parts that were in the shadow LOD. Added shadow volume for A/C unit at the front of the shelter)

# Revision 2353 - da12thMonkey

^ FMTV Shadow LOD improvements
^ FMTV cabin light

# Revision 2352 - da12thMonkey

^ Antenna shadow alignment on M1220 Caimans

# Revision 2351 - da12thMonkey

^ Changed M1085 "MASH tent" references to CBPS (Chemical Biological Protective Shelter) as per the real-life vehicle
^ Streamlined M1085 CBPS shelter and deck deployment user-actions by merging animation steps to single animation sources

# Revision 2350 - RichardsD



# Revision 2349 - RichardsD

+ Adds new FMTV model
+ Adds new FMTV interior
+ Adds all new textures
+ Adds Mobile Army Surgical Hospital Variant
+ Adds CP Shelter Variant
- Removes Expandable van variant
@ Modifies Main String with variant names

# Revision 2348 - j0zh94

^Final update for the at4, finalised temporary sound

# Revision 2347 - j0zh94

@Actually committed fix this time for At4 sound...

# Revision 2346 - j0zh94

@Fixed AT4 sound change to be more streamlined

# Revision 2345 - j0zh94

^ Replaced AT4 sound for the time being, not perfect but better than vanilla

# Revision 2344 - j0zh94

^ Added new CH-47 sound

# Revision 2343 - ballistic09

+ M2A3 IBAS sight/FCS
(Thanks da12thMonkey!)
^ Increased M2A2 gunner sight fov

# Revision 2342 - da12thMonkey

@ Missing Arsenal/Garage `author` tags

# Revision 2341 - da12thMonkey

^ resolved some minor Z-fighting in G33 pilot LOD
^ Adjusted magnified G33 zeroing and weight to match unmagnified

# Revision 2340 - da12thMonkey

^ G33 Res LODs and first svLOD

# Revision 2339 - reyhard

^ improved responsiveness of accessories scripts 

# Revision 2338 - da12thMonkey

@ Fixed mistake in alpha sorting order

# Revision 2337 - da12thMonkey

^ Modified G33 for 3D optic

# Revision 2336 - ballistic09

+ G33/XPS3 combo
+ Ported over reyhard's magic sight switching script

# Revision 2335 - reyhard

^ adjusted fuel explosion force

# Revision 2334 - reyhard

@ added locality check for M119 spent shells spawning

# Revision 2333 - reyhard

^ more balancing

# Revision 2332 - reyhard

@ removed BIS ejection system

# Revision 2331 - reyhard

^ ballanced a little bit usaf missiles

# Revision 2330 - keplager

+ UH-60M Added Advanced Flight Model variants for ESSS and MEV models.

# Revision 2329 - reyhard

^ increased armour of M2 Bradley driver hatch
^ added viewDriverInExternal property to USF vehicles
^ added LODDriverTurnedOut & LODDriverTurnedIn parameter to USF vehicles
^ added M1A1 driver interior anim
^ tweaked engine start script

# Revision 2328 - reyhard

packing speed test

# Revision 2327 - reyhard

^ added new sound configuration for F-22

# Revision 2326 - ballistic09

+ Woodland camo variants of M4A1 PIP's, AFG, and M552 CCO
+ Camo variants of the HK416 D14.5
+ Black WMX flashlight variant
+ Camo variants of M2010 suppressor
^ Increased M240C Coax rate of fire to 950 rpm
^ Changed regular TOW flight profile to flat trajectory
^ Gave TOW 2B a more accurate HEAT penetrator (900mm from the top was a tad bit high :P )
@ AI fire-modes for M240C coax used default BI sounds
@ Wrong pathname in M113 textureSources

# Revision 2325 - reyhard

@ He-FRAG name fix

# Revision 2324 - reyhard

^ updated default key for lasing

# Revision 2323 - reyhard

@ fixed Time to Target indicator on Ka-52 & Mi-28

# Revision 2322 - da12thMonkey

^ Cut down M240H pistol grip

# Revision 2321 - da12thMonkey

^ Changed allocated texture and material set to the M240G (no weird ambient shadow from the missing heat-shield over the barrel)

# Revision 2320 - j0zh94

+ Added M240 for Pylon plan for the UH60

# Revision 2319 - da12thMonkey

@ `wrong 'pylonWeapon' in magazine` rpt errors for magazines using `rhsusf_weap_DummyLauncher`

# Revision 2318 - da12thMonkey

^ Minor tweaks related to dynamic loadouts
^ DataLinkSensorComponent for AH-64Ds (hopefully, radar-equipped Apaches should be able to provide targeting data for AGM-114Ls on Apaches without radar)

# Revision 2317 - da12thMonkey

+ Caiman Ambulance UI images

# Revision 2316 - da12thMonkey

@ M107 inherited laser/light attachments slot
@ M32 sinking units in the ground when deployed (no bipod mem point)
@ M32 SIDE proxy did not follow rail during magazine reload animation
^ Properly defined M32's laser/light slot with compatibility for RHS attachments, now that it has a proxy

# Revision 2315 - da12thMonkey

^ Standardised F-22A's Virtual Garage UI Picture (white silhouette)
@ C-130J was using the old classname for its DIRCM weapon

# Revision 2314 - keplager

@ UH-60M Changed MR flapping hinge angle (coupled directional moment should be gone now)

@ UH-60M Slightly adjusted some control gains

@ UH-60M Slightly changed some values with the vertical stabilizer

@ UH-60M Slightly reduced yawing moment at high sideslip angles

# Revision 2313 - keplager

@ UH-60M adjusted vertical stabilizer angle

@ UH-60M Changed orders of some control system functions

@ UH-60M increased range of cyclic dampers to full control range

# Revision 2312 - sykoCrazy

@ Fixed issue with landing gear going wild on the carrier.

# Revision 2311 - sykoCrazy

@ Fixed some rvmat/p3d issues in the HGU-56/P
+ More HGU-56/P variants

# Revision 2310 - reyhard

^ added dumy launcher
^ added AIM120 hp for Alca

# Revision 2309 - reyhard

^ removed autocenter = 0 & added buoyancy = 1 param

# Revision 2308 - da12thMonkey

@ CROWS Caiman had thermal-imaging mirrors
@ Desert-coloured Mk19 mount on Woodland Caimans
^ Sections, UVSets and named properties cleanup

# Revision 2307 - keplager

- UH-60M Removed yaw damper from control system

@ UH-60M Adjusted collective range

@ UH-60M Moved fuselage CoFE

@ UH-60M Lowered effectiveness of pitch and roll dampers

@ UH-60M Adjusted gains for cyclic control

@ UH-60M Adjusted auto-trim sideslip controller derivative and proportionality constants

@ UH-60M Increased maxTailRotorStress value to 60,000 (should prevent atrq failure at high speeds and high atrq commands)

# Revision 2306 - RichardsD

@ Fixed Caiman Mirrors not working - were over-ridden by a hidden selection previously
@ Fixed Hidden selections overall and fixed order
@ Added armor in pilot LOD for ambulance
@ Fixed face order in windows on Up-Armd variants of Caiman
@ Added rear marker lights on chassis and fixed text placement for "TRAILER CONNECTOR" label
@ Matched ambulance kit color with APK color
@ Centered the Red Cross on ambulance front
@ Fixed the get in animation to a lower one


# Revision 2305 - da12thMonkey

^ Changed medic Caiman's litter anims and cargo capacity

# Revision 2304 - RichardsD

+ Adds M1230A1 Heavy Armored Ground Ambulance Variant
@ Minor texture path fixes to Caiman series

# Revision 2303 - da12thMonkey

^ Updated FFAR firing sequence (no longer plays Fortunate Son)

# Revision 2302 - da12thMonkey

^ Made size/height of outer ESSS hardpoint more accurate

# Revision 2301 - RichardsD

+ Adds Caiman Range LODs

# Revision 2300 - RichardsD

@ Fix for WD Caimans - LWPK removed on M1230 WD variants

# Revision 2299 - da12thMonkey

^ Basic laser sensor for winged Blackhawks (so it can lock on JTAC-designated targets)
@ Short-winged Blackhawk's pylons priority weren't equal

# Revision 2298 - da12thMonkey

^ New and updated editor preview images for Blackhawks and Caimans

Stuff I forgot to mention in the last commit:

@ Blackhawk's right spotlight was always glowing (wrong selection name)
^ Some passengers were clipping in to each other in the transport Blackhawk
^ Made a separate Hardpoint definition for AGM-114Ls (so they are only selectable only on helicopters that have Longbow radar)

# Revision 2297 - da12thMonkey

+ UH-60s with ESSS and EWS wings with Dynamic Loadouts
+ Unarmed UH-60
^ Configured UH-60 fuel tank proxies as pylon pods
^ Belt loops on 101st Abn. 82nd. Abn and 10th Mtn. uniforms

# Revision 2296 - RichardsD

+ Added Caiman WD variants and camos

# Revision 2295 - keplager

^ CH-53E Added airspeed couple to the longitudinal cyclic axis to aid in hovering.

@ CH-53E Increased ground friction values on the main gear to prevent it from sliding down hills as much.

@ CH-53E Decreased fuselage drag coefficients

@ CH-53E Decreased collective range (it should beep less now)

@ CH-53E Slightly changed collective crossfeed to rudder (calibrated for a hover)

@ CH-53E Added slight left cyclic bias in AFCS

# Revision 2294 - keplager

^ UH-60M Added lateral cyclic crossfeed to pedals AFCS (Should help with the rolling couple caused by the canted anti-torque rotor.)

@ UH-60M Changed collective range

@ UH-60M Changed lateral cyclic linear interpolation ranges

@ UH-60M Changed airfoil table slightly in the high negative alpha ranges


# Revision 2293 - da12thMonkey

+ Interim model of Triple Ejector Rack, ported from A2's Harrier

# Revision 2292 - reyhard

^ tweaked ejection speed

# Revision 2291 - da12thMonkey

+ Forest Green versions of shemagh, from il_padrino

# Revision 2290 - sykoCrazy

+ HGU-56/P helmet with green, olive drab, black, pink and murica colors.

# Revision 2289 - da12thMonkey

@ Removed custom soldier protection values (low `armorStructural` value was causing ineffective body armour)

# Revision 2288 - da12thMonkey

^ MRZR with Meatball's roll-cage anims

# Revision 2287 - reyhard

@ fixed HBAO texture flickering in A10 & AH-64 cockpit

# Revision 2286 - Warden_1

adjusted the spec to match others

# Revision 2285 - Warden_1

other two p3ds of the WMX

# Revision 2284 - Warden_1

wmx why just why

# Revision 2283 - Warden_1

wmx fixes once again....

# Revision 2282 - Warden_1



# Revision 2281 - Warden_1

p3d fix of wmx light

# Revision 2280 - Warden_1

wmx light new model

# Revision 2279 - Warden_1

WMX new tex

# Revision 2278 - da12thMonkey

^ Added Mk82 GP bombs to F-22A for testing in place of JDAM

# Revision 2277 - reyhard

^ added PreloadAddons array for better compatiblity in multiplayer
@ fixed wrong .rvmat path in rhsusf_pallet.p3d

# Revision 2276 - da12thMonkey

^ "Final" air weapons data and classname cleanup/reorganisation for Dynamic Loadouts update (will certainly break some old missions using addmagazine etc. on aircraft, maybe more)

# Revision 2275 - da12thMonkey

@ SPC base vest Shadow LOD clipping on the left side
^ cleaned up SPC UV sets and names properties

# Revision 2274 - jastreb

+ initial configuration and files for Plateframe vest rigged by Meatball @Soul_Assassin

# Revision 2273 - da12thMonkey

+ Dynamic Loadouts for A-10A
^ Some moving/cleanup/renaming of missile data to fit new standards

# Revision 2272 - reyhard

^ added usePiP = 2 to M252 mortar

# Revision 2271 - reyhard

@ M32 was missing side slot proxies

# Revision 2270 - Kllrt

Fixed some paths in rvmats and p3ds, deleted redundant rvmat for goggles

# Revision 2269 - da12thMonkey

@ Some crew-served weapons had unintentional A3 v1.70 Fire Control System

# Revision 2268 - da12thMonkey

^ Defined loadouts for helicopter classes hidden in Dynamic Loadouts update (for backwards compatibility of missions)

# Revision 2267 - reyhard

@ removed forcenotalpha named property from AH64 geometry lod - fix for flickering texture in cockpit

# Revision 2266 - reyhard

^ added RWR to A-10A

# Revision 2265 - j0zh94

^ Updated Muzzle flashes on USAF vehicles to new muzzle flashes

# Revision 2264 - da12thMonkey

@ forgot to re-insert `pylonWeapon=` into heli sidewinder mags while reorganising classes/inheritance

# Revision 2263 - da12thMonkey

@ AIM-9 and AIM-120 locking was very limited (couldn't lock when flying above target, because of `GroundTarget` settings)
@ AIM-120 maxTrackableATL value was inverted (so couldn't lock on anything with a +ve altitude xD)
^ Increased AIM-9X HOBS envelope to 180 deg (i.e. 90 degrees from boresight on either side)

# Revision 2262 - da12thMonkey

@ Sidewinder would not lock on
^ adjusted position of sidewinder proxy model
+ Dynamic loadouts for F-22
+ Hatchet's AIM-120D model

# Revision 2261 - Warden_1

RVmat from previous commit of hk416 camo

# Revision 2260 - Warden_1

hk416 new camos added with SMDIs, use original normal: grassland des & wood, netting des & wood

# Revision 2259 - da12thMonkey

+ rhsusf_pylon_dummy.p3d reference proxy (prevents issues if specific weapon/pylon models are removed, renamed or moved)
^ Animated Hellfire rocket motor flame
^ Made AGM-114K/N/M launch effects match AGM-114L

# Revision 2258 - LAxemann

Lowered M240 SD volume


# Revision 2257 - LAxemann

Tweaked: General volume levels
Added: Suppressed m240 sounds


# Revision 2256 - LAxemann

Fixed: MMG1 SD tails
Added: New pp2000 sounds

# Revision 2255 - LAxemann

Added: MMG1 SD Tail Sounds and configs
Added: lmg_762 SD sounds
Tweaked: m249 closure sounds

# Revision 2254 - reyhard

^ removed sensor display from A-10A

# Revision 2253 - da12thMonkey

^ Adjusted DAGR pods firing sequence and mirroring

# Revision 2252 - da12thMonkey

^ Changed firing sequence of rockets in FFAR pods (proxy index order and Left/Right `mirrorMissilesIndexes[]`) to be accurate to reference material

# Revision 2251 - keplager

^ Re-added refined SC2011 airfoil tables (Should be a lot more stable now)

# Revision 2250 - da12thMonkey

+ WIP Dynamic Loadouts for UH-1Y

# Revision 2249 - keplager

@ Reverted UH-60M Airfoil due to control issues.

@ Changed UH-60M blade twist to -18 degrees to accommodate larger collective range.

# Revision 2248 - da12thMonkey

+ WIP Dynamic Loadouts for AH-64D and AH-1Z
(No clean-up of obsolete data yet)

# Revision 2247 - reyhard

@ fixed duplicated HMD on gunner station of AH-64 & AH-1W

# Revision 2246 - reyhard

^ adjusted air friction of canopies

# Revision 2245 - keplager

^ Improved UH-60 control system coupling and AFCS.

@ Changed some linkage ranges on CH-53E

@ Moved UH-60 CG slightly aft

@ Changed UH-60 collective and cyclic ranges.

# Revision 2244 - keplager

@ Changed rotors to conform to tables generated from analysis of SSC2110 airfoil.

^ Adjusted UH-60M AFCS to be hover stable for new rotors.

@ Lowered mechanical linkage ranges and adjusted AFCS on CH-53E. Aircraft should be slightly less nimble now.

# Revision 2243 - keplager

^ Slightly improved collective range based on known values.

^ Improved some torque values for UH-60M and CH-53E based off of known properties.

^ Improved longitudinal AFCS channel on CH-53E

@ Moved CG slightly forward on CH-53E

@ Moved UH-60M.XML from usf_a2port_air to usf_c_a2port_air

+ Added revision backup in preparation for UH-60M SC2110 airfoil addition.

# Revision 2242 - da12thMonkey

^ Flag proxies for USAF planes and helicopters

# Revision 2241 - reyhard

@ fixed missing ui for FMTV gunners
^ F22 exhaust damage smoke is tied to proper hitpoints now
^ casing of M1117 actions
@ possible fix for turning out bug

# Revision 2240 - ballistic09

Attempted build fix

# Revision 2239 - da12thMonkey

^ Missile sensor values

# Revision 2238 - LAxemann

Fixed: Quote error in the weapon configs

# Revision 2237 - da12thMonkey

^ Merging Harry's sensor and CM tweaks for aircraft
^ DIRCM launcher classnames standardised with rhsusf_weap names

# Revision 2236 - da12thMonkey

Caiman:
+ rtm for CROWS operator
+ Virtual Garage icon images
@ Antennas on M1230 up-armoured vehicles used the wrong axis 

# Revision 2235 - reyhard

^ improved naming consistency of 5.56 M855A1 magazine
^ reduced reflection on SU260 glass

# Revision 2234 - da12thMonkey

^ CH-53 info panels

# Revision 2233 - da12thMonkey

^ Improved accuracy of RG-33L speedometer

# Revision 2232 - da12thMonkey

^ Tweaked AH-64 sensor arcs to fit optics
^ Configured sensors and info panels for AH-1Z and UH-1Y
@ Woodland "Close Support" AH-1Z was equipped with AGM-114Ls that it can't use

# Revision 2231 - da12thMonkey

^ Configured AGM-114L radar-locking sensor
^ Tweaks to AH-64 sensors (visual and IR sensors follow TADS among other things)

# Revision 2230 - LAxemann

Beefed up the lmg762 punch sound (m240)

# Revision 2229 - LAxemann

Tweaked: Beefed up the lmg556 close punch sounds a bit
Added: Sounds and functions for initial magazine belt intakes (m249 and m240 for now, sounds are WIP)

# Revision 2228 - da12thMonkey

^ Sensors for laser-locking Hellfires

# Revision 2227 - da12thMonkey

+ Mk19 variants of Caiman with OGPK
^ Applied stringtable names
+ Option to hide wire protection kit on M1230

# Revision 2226 - da12thMonkey

^ Implemented AN/ALQ-144 on UH-60M
+ AN/ALQ-212 (ATIRCM) weapon class
^ Commented out Caiman woodland textureSource (to hide it in Garage/Attributes until wd textures are implemented)
^ Inventory images for USMC 8-Point Cover and Boonie

# Revision 2225 - da12thMonkey

@ Some AH-64s weren't configured with DIRCM
+ AN/ALQ-144, AN/ALQ-157 and AN/AAQ-24 weapons for DIRCM

# Revision 2224 - reyhard

^ code clean up

# Revision 2223 - da12thMonkey

@ Some crew proxies were duplicated in the Caiman 
^ Set up Caiman cabin lighting
@ RG-33L cabin light source had ambient values set to the wrong colour

# Revision 2222 - da12thMonkey

Caiman:
^ zbytek selection and fixed destruction materials (last of the error popups I hope)
^ configured animations for high/low beam headlights action (cabin lights still to do)
^ added flag proxies
^ configured relative zoom/FOV capabilities for CROWS day and thermal channels


# Revision 2221 - Soul_Assassin

^ Changed ACVC name in VA
+ Added ACVC ESS
+ Added ACVC icon in VA

CVC-H done :)

# Revision 2220 - LAxemann

Added: WIP m2 sounds

# Revision 2219 - da12thMonkey

^ M153 CROWS II optics and RSc
+ configured CROWS version of M2 HMG; can accept 400rnd magazines

# Revision 2218 - LAxemann

Added: lots of new sandbox content

# Revision 2217 - LAxemann

Fixed: baseSoundModeType inheritance
Huge updated regarding 3dprocessors and filters
Volume curve tweaks
New sound-sandbox content

# Revision 2216 - keplager

@ Lowered torque values for UH-60M/UH-1Y/AH-1Z

@ Changed stress damage values for UH-1Y/AH-1Z

^ Improved control responsiveness for CH-53E

^ Improved AFCS for CH-53E (less problematic coupled moments now)

^ Improved artificial stability characteristics for CH-53E

^ Improved AFCS for UH-1Y/AH-1Z (Added proportional collective coupling to tail rotor collective pitch value)

^ Improved Longitudinal stability characteristics for UH-1Y/AH-1Z

^ Improved moments of inertia based on known values (CH-53E/UH-1Y/AH-1Z).



# Revision 2215 - da12thMonkey

^ Caiman section optimisation and UV cleanup
^ crosshair overlay, animated turret direction indicator and illumination for PiP CROWS monitor
+ CROWS modelOptic (not yet integrated - I need to write RSc first)

# Revision 2214 - da12thMonkey

@ rhsusf_c_Caiman cfgpatches and pboprefix conflict with rhsusf_c_rg33l (Caiman would overwrite RG33L)
^ placeholder `picture` and `editorpreview` values for Caiman to stop annoying error popups
^ rhsusf_Caiman and and rhsusf_rg33l lacked pboprefix files

# Revision 2213 - Soul_Assassin

+ Added CVC alternative version

# Revision 2212 - RichardsD

+ First commit of the Caiman MRAP

# Revision 2211 - da12thMonkey

@ AH-1 `TransportCountermeasuresComponent` was in turret components instead of main components class, causing no entry errors

# Revision 2210 - keplager

@ Changed feathering, flapping angles and torque values.

# Revision 2209 - keplager

@ UH-1Y AFM Changed position of horizontal stabilizer for better longitudinal stability.

^ Changed file location of UH-1Y AFM for easier building.

+ Added AH-1Z AFM

+ Added CH-53E AFM

# Revision 2208 - Soul_Assassin

^ Improved scale of cvc
^ Tweaked green hue

# Revision 2207 - Soul_Assassin

+ New CVC-H model

# Revision 2206 - da12thMonkey

+ MBAV Medic variant
@ Some more inverted normals

# Revision 2205 - da12thMonkey

+ Grenadier's MBAV
@ Pouch shadow on the wrong side of operator/rifleman's MBAV
@ Some pouches had inverted normals
@ Wrongly pasted hitpoint name

# Revision 2204 - da12thMonkey

+ MBAV MG equipment
^ removed .rvmats from bottom LODs

# Revision 2203 - da12thMonkey

+ MBAV Rifleman/Operator equipment

# Revision 2202 - RichardsD

+ Added Caiman strings

# Revision 2201 - da12thMonkey

+ MBAV with basic set of pouches (light loadout)

# Revision 2200 - reyhard

@ fixed eject ctd by changing simulation of ejection seat
@ fixed CM not usable on vehicle that received sensor update
@ fixed missing throttle indicator
^ removed missile feed from A10A

# Revision 2199 - da12thMonkey

+ Laser/Light attachment slot for Glock 17, compatible with acc_flashlight_pistol (dev Branch)

# Revision 2198 - reyhard

@ fixed typo in HEDP rockets short description 

# Revision 2197 - keplager

@ Corrected UH-1Y CG in AFM.

# Revision 2196 - da12thMonkey

^ Adjusted Mk11 Suppressor length
+ nDo-generated _as material for MBAV
^ added mag pouch to MBAV texture/material negative space for optimisation of future variants

# Revision 2195 - reyhard

^ improved M1 damage handling script

# Revision 2194 - Bakerman

@ "rhs_vehicleRadioChatter" spelling
^ Option to disable radio chatter by setting "rhs_vehicleRadioChatter" to 0 for mission or vehicle
^ Option to disable spall simulation by setting RHS_SPALL_ENABLED to false - recommended to leave this enabled

# Revision 2193 - reyhard

@ fixed tank AI in player team refused to fire without explict command

# Revision 2192 - keplager

^ Updated C-130 FM to Utilize Apex configs.

# Revision 2191 - LAxemann

Tweaked: Many tail sounds

# Revision 2190 - reyhard

^ updated DUKE TFAR jamming script with tf_receivingDistanceMultiplicator & tf_transmittingDistanceMultiplicator variables 

# Revision 2189 - da12thMonkey

^ Reduced apparent whiteness of clear lens on Oakley goggles

# Revision 2188 - HarryD

Configured sensors for:
AH-1Z
AH-64
FIM-92
A-10
FGM-148

Configured target sizes for:
AH-1Z
AH-64
MELB
A-10

Tweaked lock detection for:
AH-1Z
AH-64
MELB
A-10

Tweaked lock type for:
FIM-92
FIM-92 double 
FGM-148

# Revision 2187 - da12thMonkey

Improved/Fixed Rotex 5.56mm suppressor visuals:
@ _as was using specular map info
@ normal map G was not inverted
^ cleaned up redundant UV sets
^ content-aware fill of negative UV space to increase _co and _as padding (reduce black seams)

# Revision 2186 - da12thMonkey

@ AH-1Z rotor spinning in the wrong direction
@ UH-1Y rotor spinning in the wrong direction and wobbling when banking
+ Option to hide UH-1Y cargo doors

# Revision 2185 - LAxemann



# Revision 2184 - reyhard

^ corrected ammount of smoke grenades launched by M1A1FEP & HC
@ USMC engineer was missing backpack with toolkit
^ prevented creation of two disposable tubes when removing them through inventory menu

# Revision 2183 - da12thMonkey

+ Cunico's MBAV vest (initial version with no pouches)
+ Cunico's Oakley goggles
+ Cunico's Shemaghs

# Revision 2182 - reyhard

@ fixed C130J invisible propellers 

# Revision 2181 - keplager

^ Added UH-60M AFM (Changed from Ghosthawk FM)
+ Added UH-1Y AFM

# Revision 2180 - reyhard

^ some more tweaks to animations collisions 

# Revision 2179 - reyhard

^ added collision geometry property to static weapons animations

# Revision 2178 - reyhard

^ changed magazines for M252 mortar due to problems with AI calling support

# Revision 2177 - Soul_Assassin

Updated version in ingame options menu

# Revision 2176 - reyhard

^ M1 loader speed is now also dependent on speed of vehicle

# Revision 2175 - LAxemann

Added: New Obstruction and Occlusion Parameters

# Revision 2174 - LAxemann

Added: New M590 sounds

# Revision 2173 - j0zh94

^ Darkened Dataplate on M72

# Revision 2172 - LAxemann

Added: New MP7 sounds

# Revision 2171 - da12thMonkey

^ CH-53 rotor shadows

# Revision 2170 - LAxemann

Added: New M242 (Bradley autocannon) sounds

# Revision 2169 - da12thMonkey

^ Improved CH-47 rotor shadows (no longer appear drooped when flying)

# Revision 2168 - da12thMonkey

^ Adjusted CH-47 fuselage shadow geometry

# Revision 2167 - reyhard

@ fixed path to CH-53 RTD config

# Revision 2166 - reyhard

^ new hitpoints & suspension for A10, C130J & F-22

# Revision 2165 - da12thMonkey

^ Made Mk211 Raufoss ammo explosion less apocalyptic (interim `BoundingMineExplosion` until a custom effect can be made)

# Revision 2164 - da12thMonkey

@ CH-53 rotors span in the wrong direction
@ Point for towing CH-53 with Leshrack's mod, was underground

# Revision 2163 - reyhard

@ fixed my devbranch boo boo with weapons inheriting from gatling_30mm
^ M230 & M197 30mm rounds have now HEDP penetration now

# Revision 2162 - da12thMonkey

@ M252 was still using "A2 Port" author string
@ Second M252 crew position wasn't working because it had a Gunner proxy name

# Revision 2161 - sykoCrazy

@ Fixed interior materials were too shiny on UH-1Y

# Revision 2160 - da12thMonkey

^ Completed M252 Res LODs

# Revision 2159 - da12thMonkey

^ Long M249 VFG variant didn't have selection for hasSuppressor anin
^ Adjusted suppressor position on SR25 EC

# Revision 2158 - reyhard

^ calibrated ACOGs & adjusted  USMC reticles appearance
@ fixed m112 magazines after defusing
^ improved M1 Fire Geometry around wheels 

# Revision 2157 - reyhard

^ reduced timeToLive of GAU ammunition due to issues with CCIP calculation being overloaded by increased amount of cycles to handle resulting in low fps

# Revision 2156 - da12thMonkey

^ 3rd M252 Res LOD

# Revision 2155 - da12thMonkey

^ A Second Res LOD for M252 mortar

# Revision 2154 - da12thMonkey

+ HK416 (SOPMOD Stock) with Sabre's camo textures

# Revision 2153 - da12thMonkey

^ Flag proxies for Bradley

# Revision 2152 - reyhard

@ wrong right elevator selection in shadowlod
^ inverted GAU8 ratio from 5*HE:1*AP to 5*AP:1*HE

# Revision 2151 - da12thMonkey

@ Rear position of flags was wrong on M978 tankers

# Revision 2150 - reyhard

@ attempt to fix M1 triplex issue while using 2560x1440 resolution

# Revision 2149 - reyhard

^ internal added flag proxies to M1117, M113 & MRZR
^ GAU mixed ammo is now selectable through hotkeys too

# Revision 2148 - da12thMonkey

^ Flag proxies for HEMTT
+ Customisation option to mount flag at the front or rear of HEMTT (for convoy procedure)

# Revision 2147 - da12thMonkey

^ Flag proxies for RG-33L
@ Filled out `units[]` array in RG-33L cfgPatches

# Revision 2146 - reyhard

@ elevator anim fix

# Revision 2145 - reyhard

^ added advanced hitpoints & suspension to A10 (WIP)
^ improved A10 MFD
^ A10 is now using mixed HE:AP rounds in 5:1 ratio

# Revision 2144 - reyhard

^ readded gearbox to M1 (test)

# Revision 2143 - da12thMonkey

@ Bipod in M249 shadow LOD was missing named selections (bipod shadow didn't animate when deployed)

# Revision 2142 - reyhard

^ added flag proxies to M1025IES, M109 & M1 Tanks
@ added locality check to M1117

# Revision 2141 - reyhard

^ improved hitpoints for UH-60M, Ch47 & AH-64
@ typo in firegeometry of UH-60M left doors
@ typo in rvmat path of UH-60M MEV
^ moved mortar weapon config to heavyweapons
@ fixed M252 camera movement
@ fixed M252 legs animations

# Revision 2140 - da12thMonkey

^ Adjusted HK416/M27 scale (closer to M4/M16 receiver length)
@ M27 didn't work correctly with some vert grips 

New `rhs_weap_m27iar_grip1` class for use with grip system. Existing `rhs_weap_m27iar_grip` with no grip slot allows for TD Grip+bipod setup

# Revision 2139 - reyhard

@ forgot to adjust 2 remaining m249 anims

# Revision 2138 - reyhard

^ Mark V SOC use now "deleted" event handler - additional roadway lod is removed in all cases now (i.e. while using VG or deleteVehicle script command)
^ M113 & RG33L now use turnIn/Out event handlers for handling hatches
^ moved some seats to reduce clipping with passengers on UH-1Y
^ hand on stock script is more flexible for use with 3rd party mods
^ added hand on M107 stock when deployed
^ adjusted M249 position
@ fixed M1 FCS overshooting targets
@ fixed some loadouts (USMC javeling carring SMAW missiles in backpack & overloaded units mainly)
@ fixed missing units in MZRZ cfgPatches
@ added new turret limits for M113 & RG33L FFV seats

# Revision 2137 - da12thMonkey

^ Improved bipod and grip proxy alignment on USAF weapons (centred and levelled)
@ BIS bipods floating below the rail
^ hasUnderBarrel anim for M16A4

# Revision 2136 - reyhard

^ modified position of M240 & M107
@ M24 was missing bipod memory point

# Revision 2135 - reyhard

@ fixed M252 inheritance

# Revision 2134 - p1nga

MOAR Mortars

# Revision 2133 - sykoCrazy

@ Tweaked some memory points in the UH-1Y
@ Removed rotor texture artifacts on UH-1Y
@ UH-1Y flight model is a bit more agile/flies less like a whale

# Revision 2132 - Soul_Assassin

@ Fixed typo in UH-1Y name

# Revision 2131 - p1nga

Updated M252 Optics Model + Added It To The Mortar

# Revision 2130 - Soul_Assassin

Version updated in menu options

# Revision 2129 - Soul_Assassin

^ Improved RG-33L lod switching 

# Revision 2128 - reyhard

^ tweaked damageHide selection for MRZR

# Revision 2127 - Soul_Assassin

Reconfigured M252 to work as the old configuration

# Revision 2126 - Soul_Assassin

Added PBOPREFIX files to P1NGA's M252 so it builds

# Revision 2125 - p1nga

Initial Updated M252 Mortar

# Revision 2124 - ballistic09

@ Fixed missing side skirts on M113 M2 variants

# Revision 2123 - da12thMonkey

+ MRZR setVehicleCargo load space for transporting small objects

# Revision 2122 - reyhard

@ replaced hasBipod with hasUnderbarrel

# Revision 2121 - reyhard

@ fixed inheritance of right rear wheel - close T2049

# Revision 2120 - reyhard

@ added missing baseWeapon param for USAF pistols - close T2096

# Revision 2119 - reyhard

^ added damageHide selections & damage rvmats for MZRZ

# Revision 2118 - da12thMonkey

^ Adjusted HK416-type rifle muzzle-flash
@ M27 IAR with TD grip would not accept some optics that fit the grip-less M27
@ M27 IAR flash-hider did not hide in viewPilot LOD when a muzzle attachment was fitted

# Revision 2117 - Redphoenix

@ Fixed RG-33L wheels not touching the ground - Close T2042

# Revision 2116 - Redphoenix

- Removed old PhysX file
@ Fixed Engine brake on MRZR close T2027

# Revision 2115 - da12thMonkey

^ added rhino to M1237 physX LOD (will now collide with vehicles and objects)

# Revision 2114 - da12thMonkey

^ added cabin lights to RG-33L

# Revision 2113 - reyhard

@ fixed F-22 lights

# Revision 2112 - LAxemann

Added: SD sounds for M4
Added: SD sounds for M249
Added: sd_rifle1 tail soundSet

# Revision 2111 - da12thMonkey

@ MRZR attenuationEffectType filter changed to OpenCarAttenuation

# Revision 2110 - da12thMonkey

Triggering build

# Revision 2109 - da12thMonkey

@ High/Low beam headlights weren't properly set up RG-33L

# Revision 2108 - LAxemann

Tweaked: M4 character sound is more shorter, representing the smaller calibre

# Revision 2107 - Redphoenix

@ lowered ARB force for RG-33L

# Revision 2106 - da12thMonkey

^ displayname for 6rnd M397 magazine was inconsistent with the single round version
^ added M397 HET grenades to supply crates
^ added M240 flash-hider to supply crates

# Revision 2105 - da12thMonkey

+ M240 4-prong flash-hider attachment

# Revision 2104 - Soul_Assassin

Fixed naming of the new sounds folder.

# Revision 2103 - reyhard

^ tweaked maxLeadSpeed parameter for HEATs & HE rounds

# Revision 2102 - LAxemann

Added: M249 sounds

# Revision 2101 - LAxemann

Added: New rhsusf_weaponSounds folder for the new sound "system".
Will make the current rhsusf_sounds obsolete over time.

Currently covered are test sounds for the M4 and M240

# Revision 2100 - da12thMonkey

@ ironsights on M4 w/ Magpul furniture were using the wrong discreteDistanceCameraPoint[] memory points set

# Revision 2099 - da12thMonkey

@ Flashlight attachments did not work on MP7 (SMG_01 Vermin parent class had an integral flashlight configured - changed parent class to SMG_02 Sting to avoid it)

# Revision 2098 - Festival

@ Fixed M14 AP mine smdi error

# Revision 2097 - Soul_Assassin

Fix for ejection seat CTD.

# Revision 2096 - Soul_Assassin

Reverted changes to custom hitpoint class.

# Revision 2095 - reyhard

^ removed custom hitpoints class
^ maxLeadSpeed param for ATGMs 

# Revision 2094 - da12thMonkey

^ Changed Lerca rangefinder weaponholder parent to Item_Base_F, hopefully fixes config errors
@ Lerca rangefinders were in the wrong Eden editor category/subcategory

# Revision 2093 - Hatchet

Attempting to fix M69 foo, because SoulAssasin. :D

# Revision 2092 - Hatchet

Attempting to fix M67 additions ... go me!!!

# Revision 2091 - da12thMonkey

> Added MP7 'bipod' mem point to reduce sinking in the terrain

# Revision 2090 - reyhard

^ reduced RG33L hull armour from 100mm (sic!) to 30mm
^ reduced RG33L addon armour from 152mm to 30mm & changed it CE protection to ~300mm
^ redefined zbytek selections for RG33L
^ tweaked hit hull points
^ added more damage materials to RG33L
@ position of RG33L wheels FG & hitpoints didn't match visual mesh
@ fixed CE modifiers not working on cars
@ fixed MELB AGM114K weapon name typo

# Revision 2089 - Hatchet

Tweaked MkV Physxfu & Soundfu.. (better turning, less wave slapping ... sounds reverted, much closer to real now.. but has a couple dead spots, still sorting. but if fine as-is for now.)

# Revision 2088 - Hatchet

Tweaked MkV Physxfu & Soundfu..

# Revision 2087 - Hatchet

Tweaked MkV Physxfu & Soundfu.. (better turning, less wave slapping ... sounds reverted, much closer to real now.. but has a couple dead spots, still sorting. but is fine as-is for now.)

# Revision 2086 - Hatchet

Tweaked RG-33L armoring (wheels)

# Revision 2085 - Hatchet

Added New M69 thrown model to USAF

# Revision 2084 - Hatchet

Added New M67 thrown model to USAF

# Revision 2083 - Hatchet

Added New M69 mag model to USAF

# Revision 2082 - Hatchet

Added New M67 mag model to USAF

# Revision 2081 - Hatchet

Corrected .smdi pathing in .rvmat for M14 Mine..

# Revision 2080 - Hatchet

Changed .rvmat in fireLods...

# Revision 2079 - 

@ 4 round AGM-114L magazines for multi-role Apache weren't defined as an accepted magazine for the AGM-114L launcher (rhs_weap_HellfireLauncher)

# Revision 2078 - 

^ Reduced CH-53E capacity to 24 seated, and re-spaced cargo proxies accordingly Close T1715

# Revision 2077 - 

^ removed laser lock from AGM114L
^ AH-64D with radar now use mix of AGM114L & K
^ added AH-64D without longbow radar
^ AH1Z use AGM114K now - close T739
^ disabled tablock on MELB

# Revision 2076 - reyhard

@ ejection ctd fix
@ some .rpt errors

# Revision 2075 - reyhard

^ disabled A10 tablock

# Revision 2074 - RichardsD

@@ Fixed: Glass between Pilot and Co-pilot no longer is high spec, in high light the vision will not be obscured. 

# Revision 2073 - da12thMonkey

@ Swivel-mounted Harris bipod leg extension limit close T1990

# Revision 2072 - da12thMonkey

+ AN/PAS-13G(V)1 5Mil reticle mode
^ AN/PAS-13G(V)1 Optics RSc now uses rhsusf_digital_font_var style font

# Revision 2071 - da12thMonkey

^ baseweapon definitions for MP7A2s

# Revision 2070 - da12thMonkey

@ Broken path in .rvmat

# Revision 2069 - da12thMonkey

@ RG33L fording behaviour (removed autocenter = 0, fixed "bouyancy" typo etc.)

# Revision 2068 - da12thMonkey

@ non-convex components in RG-33L Geometries

# Revision 2067 - da12thMonkey

^ Replaced old MP7A1 model with Zee's MP7A2 (previous "A1" classnames set to inherit from new "A2" classes, should not break missions)
+ Rotex-II MP7 (4.6mm suppressor)
^ Base MP7 handanim replaced with one appropriate for the new model without front grip
+ MP7 VFG and AFG handanims for grip attachment system
- Removed redundant MP7A1 .p3d, .paa and .rvmat files

^ Raised AN/PAS-13G(V)1 model slightly

# Revision 2066 - Festival

+ Added M14 AP mine
^ Added M19 AT mine icon
@ Fixed M19 AT mine deactivated model, shadow lod and description in Stringtable.xml




# Revision 2065 - da12thMonkey



# Revision 2064 - reyhard

^ M1117 now use CM for DUKE activation
^ added missing handles to TOW
^ added new gunner anim (with IK magic) to TOW
^ added PiP scope to gunner lod of tow

# Revision 2063 - da12thMonkey

@ Offroad dust particle effects spawning from the centre of RG-33L

# Revision 2062 - da12thMonkey

+ Cunico's FAST Maritime helmets (inc. versions with Peltor headsets)
^ MARSOC units's helmets switched from FAST Ballistic High Cut to FAST Maritime
^ Added Maritime helmets to USAF virtual boxes

# Revision 2061 - da12thMonkey

RG-33L stuff:
@ Ammobox holder didn't change to woodland colour with the rest of the vehicle
^ gunnerview memory point repositioned on M2 turrets, for better alignment with sights
^ More Eden editor attributes, for lowering Rhino and opening doors at init

# Revision 2060 - reyhard

@ removed smoke launch sound from duke

# Revision 2059 - da12thMonkey

@ Added missing fired eventHandler to RG-33L (DUKE is now fully functional)
^ Cleared up P:\ drive reference in RG-33L Pilot LODs and reduced sections count by 'Move Top/Move Bottom' operation

# Revision 2058 - da12thMonkey

^ RG-33L DUKE configuration (not yet fully functional)

# Revision 2057 - reyhard

^ damageHide selections to Mark V
^ added dead animations to Mark V
@ Mark V animations linking to deatState instead to uncociusnes 
^ added new IK anims to CH47 side gunners
^ added support for driver activated DUKE
@ disposable weapons locality check
@ fixed "incommingMissle" typo

# Revision 2056 - da12thMonkey

^ Tweaking RG-33L damage resistance

# Revision 2055 - Redphoenix

@ Fixed Typo in physx_config.hpp
^ Uped RG-33L Torque from 150% to 175%

# Revision 2054 - RichardsD

@ Fixed Tachometer and Speedometer (ALL FOR RG33L)
@ Added some interior details
@ Finalized interior textures
@ Fixed issue with wheel well shading

# Revision 2053 - da12thMonkey

^ RG-33L added antenna wobble animations and set up DUKE hitpoints and hiding anims
@ M16A4 carryhandle optics proxies aligned with the front sight in viewPilot LOD

# Revision 2052 - da12thMonkey

^ Simplified RG-33L hiddenSelections and TextureSources configuration
@ Woodland texture can now be selected from Garage/VhC and Attributes
@ Correct transportSoldier value
+ Woodland RG-33L editorPreview pics

# Revision 2051 - Redphoenix

@ Gave the RG-33L more torque, better suspension and new high-performance brakes - close T1968

# Revision 2050 - RichardsD

+ Adds woodland variants for RG33L (these still require the icon photos to be generated)
+ Adds interior normals for RG33L
@ Fixed a small issue where a texture still had P: mapping
@ Changed the hidden select classes and made sure they were uniform

# Revision 2049 - reyhard

^ ability to disable voice announcer
@ fixed hatch control script using wrong function
^ tweaked TOW statistics
^ added SACLOS script for TOW (copy paste from AFRF)
^ added support for TOW2B top down attack
@ fixed shell ejection mem points on M2 & HMMMWV w/ M2 
^ added tracer to TOWs & scripted TOW booster fire hide
^ TOW anims (WIP, gunner proxies not ready - need new anim & some IK magic)

# Revision 2048 - da12thMonkey

^ RG-33L param crewExplosionProtection = 1

# Revision 2047 - reyhard

@ rvmat link to non existing texture

# Revision 2046 - RichardsD

@ Working gauges for RG33L added

# Revision 2045 - da12thMonkey

+ RG33L editor previews and Arsenal icons
^ more optimised shadows, with selections defined for animated parts (turret etc)

# Revision 2044 - RichardsD

+ Adds Ranged LODs for RG33L
+ Adds Thermals for RG33L
+ Adds M1237 MK 19 

# Revision 2043 - RichardsD



# Revision 2042 - reyhard

@ MarkV SOC driver proxy missing in fire geo
@ M1025 w/ M2 had autocenter=0 param
@ corrected M919 penetration

# Revision 2041 - Redphoenix

^ Improved RG-33L PhysX

# Revision 2040 - Soul_Assassin

^ Cleaned up last lod of helmets

# Revision 2039 - Soul_Assassin

^ Improved lod switching on ACH and MICH helmets

# Revision 2038 - da12thMonkey

^ Crew proxies added to MRZR FireGeo LOD, so they can be shot and killed inside

# Revision 2037 - da12thMonkey

- Cleaned up unused LWTS models for PAS-13 combination variants (were just renamed copies of the PVS-27+scope models, left untouched)

Can recreate these in future with the proper PAS-13 if needs be, but for now they're just clutter

# Revision 2036 - da12thMonkey

^ Adjusted MRZR suspension arm anims to better match new damper offset values
+ Customisation attribute for tailgate hiding

# Revision 2035 - reyhard

@ fixed MRZR suspension
@ fixed mMaxDroop typo

# Revision 2034 - da12thMonkey

^ MRZR FFV (limits might still want some adjusting)

# Revision 2033 - reyhard

@ another fix to engine startup script

# Revision 2032 - reyhard

@ fixed fording depth for M1 & M109 vehicles
^ added bouyancy=1 to geometry of M1, M2 & M109 vehicles, so they properly slow down in water
+ added improved IK anims to M1025 with M2 & Mk19
^ M1 tank drivers use thermal camera for night operations 
^ tweaked M61 hit value to be more on par with rest of bullets
@ fixed wrong position of zeroing in ui of static weapons

# Revision 2031 - Redphoenix

@ MRZR Physx Update

# Revision 2030 - reyhard

+ added improved IK anims to M2 tripod static weapon
^ retextured M2 ammo tray

# Revision 2029 - da12thMonkey

^ MRZR front seats lowered and adjustments for better driver visibility

# Revision 2028 - ballistic09

@ M220A2 optics zoom levels corrected to match the rest of RHS optics

# Revision 2027 - da12thMonkey

@ "_ammo_ammo_" typo in classnames

# Revision 2026 - ballistic09

^ Improved static TOW launcher's sights
+ Added all main types of TOW missiles, including placeholder classes for TOW-2B which will need an expert in black magic (scripting) to get working properly
^ Replaced BGM-71D in TOW launcher and Bradley with BGM-71E and BGM-71H
@ Wrong ammo count for M40A5 and 1911 magazines

# Revision 2025 - reyhard

@ fixed SMAW spotting round behaviour
^ improved collider used for engine startup script

# Revision 2024 - da12thMonkey

^ MRZR blackout light, and driver action to turn on/off stop lights
^ Option to hide tailgate through VhC/Garage (add to attributes later)

# Revision 2023 - da12thMonkey

+ MRZR Eden previews, icon and UI pic

# Revision 2022 - da12thMonkey

^ Last couple of Res and SV LODs for MRZR

# Revision 2021 - da12thMonkey

^ Two more MRZR res LODs
+ A merged texture set for lowest res LODs (and an appropriate "camoMerged" selection)

# Revision 2020 - Redphoenix

@ improved Javelin weight
@ changed Javelin soldier loadout
+ Javelin missile bearer

# Revision 2019 - Redphoenix

- Removed unnecessary Javelin Rocket from AT
@ nerfed M249 and M240 magazines by 25%

# Revision 2018 - da12thMonkey

^ MRZR hitpoints and fire geometry LODs (armour and passthrough config values need doing)

# Revision 2017 - Redphoenix

@ reduced Javelin mass be 25% to make it more suitable for gameplay

# Revision 2016 - Redphoenix

@ USAF item, magazine and weapon mass unification

# Revision 2015 - da12thMonkey

^ Set up M249s to work with all 5.56mm muzzle attachments

# Revision 2014 - reyhard

@ some more M1 fixing

# Revision 2013 - da12thMonkey

+ Minimi Para model to be configured in SAF
+ Placeholders for modernised "lightweight" version of M249 (to be injected when we have a new buttstock model to match)

# Revision 2012 - da12thMonkey

^ Finished MRZR shadow LOD

# Revision 2011 - reyhard

@ hotfixed proxy leftover on M1 tanks
@ fixed rhs_dummy_mag rpt error
@ law changing eye point after fire
@ M1A2SEP tusk ii duke texture changing

# Revision 2010 - da12thMonkey

MRZR stuff
^ Mostly complete main SVLOD (front brush guard and some interior parts still to do)
^ Working tail lights (faces were inverted when I added brake lights)
@ Missing author parameter in config

# Revision 2009 - reyhard

@ rpt error fixing
^ optimized & cleaned up M1025ies, M113 & M1 tanks
+ added hidden selections to HK416
^ added improved hatch handler for M113 & RG33L
^ added some params for improved SPO-15 handling
^ tweaked AH1Z hitpoints

# Revision 2008 - da12thMonkey

@ OpticView memory points too low down on Leupold and Premier scopes - improves "scoping in" camera movement
@ M150 RCO w/ AN/PVS-27 would be replaced by a normal ACOG when mounted on a weapon (was inheriting 2D/3D/PiP preference script from parent ACOGs)
^ M8541A was missing glassy lens in Pilot LOD
^ Cleanup of extra UV sets and SVLOD UVs on Leupold and Premier scopes

Close T1933

# Revision 2007 - da12thMonkey

^ Another MRZR4 LOD (pls kill me)
@ Fixed minor UV mapping error in top LOD

# Revision 2006 - Soul_Assassin

Playing around with geo lod for B2 and mk18

# Revision 2005 - Soul_Assassin

Mk18 has one large box and autocenter=0 set. TEST!!

# Revision 2004 - da12thMonkey

^ another MRZR4 LOD

# Revision 2003 - da12thMonkey

^ MRZR4: working second resLOD (more to come), headlights and brake lights
- Deleted separate muddy model (is handled by VhC)

# Revision 2002 - LAxemann

Added: New tail sound curve
Tweaked: M2 closure sound
Tweaked: M590 sound
Tweaked: M107 sound
Tweaked: The way tails are handled
Removed: Most 50 and 150m distance steps for tails (saves quite a bit of disk space, too)

# Revision 2001 - reyhard

@ joint rails tweak

# Revision 2000 - Soul_Assassin

@ Missing bipod_hide anims in SOPMOD rifles

# Revision 1999 - Soul_Assassin

Mk18 imported from BIS TXT file.

# Revision 1998 - Soul_Assassin

Removed second to last lod in M4B2

# Revision 1997 - Soul_Assassin

Trigger rebuild on weapons 3

# Revision 1996 - Soul_Assassin

Removed last lod in M4B2 models.

# Revision 1995 - LAxemann

Tweaked: Improved M240 sounds

# Revision 1994 - LAxemann

Tweaked: M107 50m sounds are now bassier


# Revision 1993 - reyhard

^ bolt action tweak
@ fixed mine defuse error
@ potential fix for duke rain after crash damage

# Revision 1992 - Soul_Assassin

Reverted mat changes

# Revision 1991 - Soul_Assassin

Turned off hiddenMaterials on B2, Mk18 and SR25 to try to resolve the lod issue

# Revision 1990 - da12thMonkey

@ Consistent mass across M4 GL variants (M4+M320=103.72,M4+M203=98,reduced M4+M203S to 93.40)

# Revision 1989 - Soul_Assassin

@ Potential LOD switch issue fix for M4BII, Mk18 and Mk11 (EC)

# Revision 1988 - reyhard

+ added aimTransitionSpeed (speed of aiming down the sight)

# Revision 1987 - reyhard

@ removed duplicated strings
^ cleaned up SR25, M4BII & Mk18 from isolated verts 
@ UAV helper is now created on local machine only

# Revision 1986 - PuFu

further fixes and rvmat tweaks

# Revision 1985 - PuFu

further rvmat tweaks

# Revision 1984 - reyhard

@ fixed AT4 & M72 behaviour
@ after gathering enough money magazines of dipsosable launchers are available free of charge
@ restored accidently deleted variable in engine startup script

# Revision 1983 - PuFu

cleanup multiple UVs and SVL UVs

# Revision 1982 - PuFu

further tex tweaks

# Revision 1981 - PuFu

more changes for glock and omega

# Revision 1980 - PuFu

fix for double class

# Revision 1979 - PuFu

config for omega

# Revision 1978 - PuFu

silencerco omega 9k first commit

# Revision 1977 - reyhard

@ forgot to hide fcs weapon
^ removed turret based tablock introduced in 1.66

# Revision 1976 - reyhard

@ fixed M1A2SEPv1 bounding box
^ Leica now triggers Shtora
^ added airLock=1 to tank ATGMs & HEATs- AI should now engage helicopters with them
^ increased MPAT damage radius
+ added unified Bolt Action & Disposable script using new weapon EH
^ added script to handle changing of magazines on vehicles & marking Laser Range Finder usage. Vehicles now are able to change magazine from AP to HE 
^ further improvments to engine start script - added collider without component name & redefined physx collider to house class


# Revision 1977 - reyhard

@ forgot to hide fcs weapon
^ removed turret based tablock introduced in 1.66

# Revision 1976 - reyhard

@ fixed M1A2SEPv1 bounding box
^ Leica now triggers Shtora
^ added airLock=1 to tank ATGMs & HEATs- AI should now engage helicopters with them
^ increased MPAT damage radius
+ added unified Bolt Action & Disposable script using new weapon EH
^ added script to handle changing of magazines on vehicles & marking Laser Range Finder usage. Vehicles now are able to change magazine from AP to HE 
^ further improvments to engine start script - added collider without component name & redefined physx collider to house class


# Revision 1977 - reyhard

@ forgot to hide fcs weapon
^ removed turret based tablock introduced in 1.66

# Revision 1976 - reyhard

@ fixed M1A2SEPv1 bounding box
^ Leica now triggers Shtora
^ added airLock=1 to tank ATGMs & HEATs- AI should now engage helicopters with them
^ increased MPAT damage radius
+ added unified Bolt Action & Disposable script using new weapon EH
^ added script to handle changing of magazines on vehicles & marking Laser Range Finder usage. Vehicles now are able to change magazine from AP to HE 
^ further improvments to engine start script - added collider without component name & redefined physx collider to house class


# Revision 1977 - reyhard

@ forgot to hide fcs weapon
^ removed turret based tablock introduced in 1.66

# Revision 1976 - reyhard

@ fixed M1A2SEPv1 bounding box
^ Leica now triggers Shtora
^ added airLock=1 to tank ATGMs & HEATs- AI should now engage helicopters with them
^ increased MPAT damage radius
+ added unified Bolt Action & Disposable script using new weapon EH
^ added script to handle changing of magazines on vehicles & marking Laser Range Finder usage. Vehicles now are able to change magazine from AP to HE 
^ further improvments to engine start script - added collider without component name & redefined physx collider to house class


# Revision 1976 - reyhard

@ fixed M1A2SEPv1 bounding box
^ Leica now triggers Shtora
^ added airLock=1 to tank ATGMs & HEATs- AI should now engage helicopters with them
^ increased MPAT damage radius
+ added unified Bolt Action & Disposable script using new weapon EH
^ added script to handle changing of magazines on vehicles & marking Laser Range Finder usage. Vehicles now are able to change magazine from AP to HE 
^ further improvments to engine start script - added collider without component name & redefined physx collider to house class


# Revision 1975 - Soul_Assassin

^ Reduced hand size on G3 uniforms

# Revision 1974 - reyhard

^ further improvments to engine start script

# Revision 1973 - da12thMonkey

^ Smoothed and locked normals for small faces on Glock17 slide where Object Builder tries to force hard edges

# Revision 1972 - reyhard

@ potential fix for HEAT handler

# Revision 1971 - LAxemann

Added: New M107 sounds
Tweaked: Sniper1 tail soundset (only "meadows" so far)

# Revision 1970 - Kllrt

^ Improved G17 trigger animation (req by PuFu)

# Revision 1969 - reyhard

^ added new rotorLib based on Huron - thanks swissMAG!
^ removed belly armor from m1a1HC
^ cfgPatches for RG33L

# Revision 1968 - da12thMonkey

- Scoped out US Army 4*4 RG33s to be replaced by RG33L (USMC 4*4s remain)
@ OCP Joint Fires Observer was missing a helmet
@ M24 snipers had no scope or bipod
@ M40 AI loadouts had wrong Harris bipod variant
^ Updated editor preview images to reflect some recent loadout changes

# Revision 1967 - reyhard

^ added variable to disable engine startup - type RHS_ENGINE_STARTUP_OFF = true to disable
@ network sync


# Revision 1966 - Redphoenix

small mass stuff for HC

# Revision 1965 - Redphoenix

@ generalized the mass of all M1s to 63500kg according to @Damian

# Revision 1964 - PuFu

^updated glock17 nohq

# Revision 1963 - reyhard

^ added engine startup script to rest of USAF vehicles - close T945
^ disabled engine startup script in water due to how waves were handled

# Revision 1962 - reyhard

^ increased M1 startup sequence to 20s by using old engine start sound
^ added some vehicle chat to engine startup script, so player should be more aware what is going on
^ added commander turret servo sound
@ AI M1 tanks have wrong simulation refresh rate due to attaching to "house" type object. fixed by replacing it with "thing" simulation object
@ M1 engine get fixed when using that texture workaround

# Revision 1961 - reyhard

@ forgot to hide debug orb

# Revision 1960 - reyhard

^ added M1 damage texture workaround
+ added engine startup delay to M1 - work on T945

# Revision 1959 - reyhard

@ fixed setShotParents for multiple penetrators

# Revision 1958 - RichardsD

+ Adds RG33L plus with M2
@ Fixes texture paths from P to a generic directory




# Revision 1957 - reyhard

@ safemode hotfix

# Revision 1956 - reyhard

@ changed nvg script tag

# Revision 1955 - reyhard

^ added to M1025ies old bumper as a variant selctable through VG/eden
@ small BFT texture error
+ added M397 40mm grenade
^ added ability to change loadout of m252, m119 & m109
@ fixed parsenumber error
^ changed simulation of m119 spent case
^ added green tint to nvgs & cleaned up named properities
^ added some transparency to anpvs14
^ added script for automated equipment of nvg goggles during night
@ added rhs tag to skeleton of m252 mortar 

# Revision 1954 - Redphoenix

@ Finally fixed M1025 engine sounds 

# Revision 1953 - da12thMonkey

^ Minor improvement to clipping M1025 Geo LOD

# Revision 1952 - Redphoenix

@ Increased antirollbar force for M1025s - close T1851
@ Lowered turnCoef for M1025s

# Revision 1951 - reyhard

@ fixed non-convex components in geometry lod

# Revision 1950 - da12thMonkey

^ Hatch handling function for the RG33L FFV seats

# Revision 1949 - RichardsD

@@ Added MK 19 Version

# Revision 1948 - da12thMonkey

@ Fixed desert USMC Scout Snipers

# Revision 1947 - MistyRonin

+ Add missing M40A5 variants for AI 

# Revision 1946 - MistyRonin

+ Added USMC Scout Sniper with M40A5
+ Added Zeus placeable MDO
^ Updated USMC scout sniper string-line 

# Revision 1945 - MistyRonin

+ Add MDO scope to Virtual Ammo box. 

# Revision 1944 - da12thMonkey

@ RG33L couldn't fire in Left Rear FFV position

Attempted to fix ability to fire while turned in by setting `canPullTrigger = 0;` for each turned in animation state, but seems like other steps are needed

# Revision 1943 - RichardsD



# Revision 1942 - Soul_Assassin

Updated mod.cpp

# Revision 1941 - da12thMonkey

^ Finalising MDO with resolution LODs, shadow LODs and config tweaks (mass, inertia)
^ Added MDO as standard optic for USMC machine gunner's M240B (replaces RCO) and added to USAF weapon crate
@ Disabled M24 pointer slot - model has no provision to attach lasers/lights etc.

# Revision 1940 - Warden_1

MRZR LOD removal

# Revision 1939 - da12thMonkey

^ TA31RCO RMR mount LODs, shadow and other model optimisations

# Revision 1938 - Warden_1



# Revision 1937 - Warden_1

LWTS geo fix

# Revision 1936 - da12thMonkey

^ Initial RMR model added to MDO
+ Added ACOG TA31RCO variants with RMR

To do: LODs

# Revision 1935 - Warden_1

LWTS updated lens effect

# Revision 1934 - Warden_1

LWTS

# Revision 1933 - Warden_1

LWTS attempt 2

# Revision 1932 - Warden_1

LWTS: fixed lens effect, fixed texture brightness, hopefully fixed normal and flipped optic

# Revision 1931 - ballistic09

+ Initial LWTS config

# Revision 1930 - Warden_1

added potential LWTS and files

# Revision 1929 - da12thMonkey

^ MDO normal map tweak

# Revision 1928 - da12thMonkey

^ Changed MDO glass material

# Revision 1927 - da12thMonkey

+ Added initial SU-260/P ACOG TA648-MDO (LODs and further texture/material tweaks needed)
@ Solid stock M249 PIP made compatible with NT4 suppressor like other long-barreled M249 PIPs

# Revision 1926 - Soul_Assassin

Tweaked Harris bipod rvmat and texture.

# Revision 1925 - Soul_Assassin

Scoped out MTVR for now.

# Revision 1924 - Soul_Assassin

^ Significant reduction in M1117 sections in all lods.

# Revision 1923 - Warden_1

mrzr LODs

# Revision 1922 - reyhard

@ M1 FCS script not working with USAF mod only instaled

# Revision 1921 - da12thMonkey

@ poklop_gunner selection (loader's hatch) was missing some parts on M1A1SA models (m1a1aim...p3d). Closes {T1771}

# Revision 1920 - reyhard

+ added interior lights to M2, M113, M1117, C130, UH60, UH1
+ added low/high beams to M1025, M1117, HEMMT
+ added ViV support for flatbed HEMMTS
^ tweaked M1025ies glass reflection
^ increased spall amount
@ fixed M1 small shadow bug
@ fixed alpha sorting of HEMMT gauges
@ fixed c130j ramp in cargo lod
@ fixed c130j hud transparency
@ fixed c130j after leveling ramp there was no option to close or open ramp
@ fixed UH60 landing gear position & selections


# Revision 1919 - da12thMonkey

@ Wrong muzzle flash in solid stock M249's pilot LOD (updated to use reyhard's proxy)

# Revision 1918 - reyhard

^ tweaked M24 & M40 hand anims
+ added custom muzzle flashes to USF weapons

# Revision 1917 - reyhard

^ improved bipod compatibility with joint rails

# Revision 1916 - reyhard

@ small hotfix to the last commit

# Revision 1915 - reyhard

^ applied texture to mtvr & separated files into 2 folders

# Revision 1914 - da12thMonkey

@ Fixed texture stretching below MRZR tail lights, caused by collapsed UVs

# Revision 1913 - reyhard

@ adapted rhs arsenal to 1.64 changes
@ changed smaw sight to 2d version

# Revision 1912 - Warden_1

more mrzr texture improvements, darkened mud texture

# Revision 1911 - ballistic09

@ M240B missing side attachment/pointer slot
+ textureSources for woodland painted and muddy MRZR textures/materials

# Revision 1910 - Warden_1

fixed model config, sorry jenkins

# Revision 1909 - Warden_1

addded mud rvmats, normals, model files.

# Revision 1908 - Warden_1

fixed model.cfg missing blue (camo) selection

# Revision 1907 - Warden_1

fixed texture paths on mrzr

# Revision 1906 - Warden_1

added mrzr mud and woodland camo textures (painted)

# Revision 1905 - Warden_1

added LODs two to five to the mrzr file, they only have camo selections right now

# Revision 1904 - Soul_Assassin

^ Tweaks to MRZR rvmats

# Revision 1903 - Warden_1

mrzr selections fixed for decals & stickers

# Revision 1902 - Warden_1

updated MRZR textures, included decals & stickers

# Revision 1901 - Warden_1



# Revision 1900 - j0zh94

@ Fixed M32 performance issue

# Revision 1899 - LAxemann

Fixed: M590 sound config error

# Revision 1898 - reyhard

^ implemented setShotParents to spall & heat script
^ added flags to cfgFactions 

# Revision 1897 - sykoCrazy

@ Derp

# Revision 1896 - sykoCrazy

+ Driver rtm
^ More changes to PhysX parameters
^ p3d/config cleanup

# Revision 1895 - da12thMonkey

@ M320 sidearm could mount a pistol suppressor in Arsenal (compatibility inherited from Pistol_Base_F)

# Revision 1894 - zeealex

[+] New PEQ 15 textures 
[-] Locking pin on ANPEQ15

# Revision 1893 - zeealex

[+] MTVR textures

# Revision 1892 - da12thMonkey

@ M249 VFG (long variants) handanim definitions

# Revision 1891 - sykoCrazy

@ Wild bouncing MRZR no longer bounces wildy
+ Independent suspension animations (still needs some tweaking)
@ Some smdi maps had wrong gloss maps.
@ Started working on handling. Learning a lot.
- Removed cargo seats to make way for FFV seats. only driver seat is available at the moment

# Revision 1890 - sabre

[Textures] M8541 small update.

# Revision 1889 - da12thMonkey

^ missing $pboprefix$ for rhsusf_c_mtvr directory

# Revision 1888 - da12thMonkey

^ Adjusted swivel-mounted Harris specularPower (no change to _smdi yet)

# Revision 1887 - reyhard

@ mtvr config conflicting with melb
^ improved premier scope glass reflection

# Revision 1886 - da12thMonkey

+ Added USAF version of Shaft's Harris bipod, for mounting on M40 and M24 (is independent from the AFRF version)

# Revision 1885 - da12thMonkey

^ Set maxZeroing values for US sniper rifles and marksmen rifles to include their published effective range
^ Increased zeroing range of 20x Leupold scope so that M2010 and M107 can be used at their effective range
^ Increased M107 dispersion slightly from 1.3 MOA (from GM6 parent class), to 1.5 MOA based on published statements of accuracy for the rifle

# Revision 1884 - sabre

{Textures] Ye ole Green channel flip.

# Revision 1883 - zeealex

[+] New M24 Textures

# Revision 1882 - Soul_Assassin

@ Moved M113 cargo proxies to prevent helmet clipping through upper hull. Close T1557

# Revision 1881 - Soul_Assassin

@ Toned down camelback cap color to fit with the lighting better. Closes T1722

# Revision 1880 - Soul_Assassin

^ Improved M113 lod switching. Close T1724

# Revision 1879 - Soul_Assassin

^ Readded gasblock and gastube to MK18 and M4BII models. close T1712

# Revision 1878 - MistyRonin

@ M16A4 Carryhandle + M203 had no weight difference with M16A4 carryhandle

# Revision 1877 - da12thMonkey

+ Inventory icons for M40A5 and M8541 variants
^ Shadow LOD for M249 skeleton stock

# Revision 1876 - sabre

[Textures] M40a5 added wm.

# Revision 1875 - sabre

[Textures] M8541 Version 1

# Revision 1874 - sabre

[Textures] M40a5 Version 1

# Revision 1873 - da12thMonkey

^ Tweaked Mk1 M249 muzzle texture and materials

# Revision 1872 - da12thMonkey

+ New flash-hider model for M249 Mk1

# Revision 1871 - da12thMonkey

+ Added sight rail for solid stock M249 (shows if optics slot items are fitted and is hidden when without)

# Revision 1870 - da12thMonkey

^ Remodelled carry handle for old-type M249

# Revision 1869 - MistyRonin

@ Fix strings with extra quotation marks.

# Revision 1868 - gurdy

^ c-130 texture tweaks
@ stringtable fixes

# Revision 1867 - da12thMonkey

+ Initial MTVR config and injection
Wheels turn, suspension is kind of working, but the ride does not look comfortable!

# Revision 1866 - gurdy

@ c-130 color tweak

# Revision 1865 - gurdy

+ initial injection of MRZR 4

# Revision 1864 - da12thMonkey

^ Added bolt carrier mesh from Toadie's samples, to M249 top LODs to cover see-through backfaces in the ejection port

# Revision 1863 - Redphoenix

@ RG-33L PhysX

# Revision 1862 - RichardsD

@@ Adds the first iteration of the RG33L 6X6. Please do not submit bug reports yet, still heavily WIP and bugs being fixed and changed regularly. 

# Revision 1861 - RichardsD

@@ Adds the RG33L test string

# Revision 1860 - da12thMonkey

@ Fixed UV mapping error on the back of M16A4 buttstock caused by non-triangulated face(also cleaned up unused UV sets to reduce filesize)

# Revision 1859 - MistyRonin

+ Add M40A5 & M24 SWS rifle variants and their mags to Virtual Arsenal & Ammo crates
+ Add M8541 scope variants to Virtual Arsenal & Ammo crates
+ Add M40A5 & M24 SWS rifles as Zeus place-able objects

# Revision 1858 - da12thMonkey

^ Improved M40A5 handanim (prevent thumb clipping )
^ Added cheek rest to shadow LOD

# Revision 1857 - da12thMonkey

^ Completed M40A5 with resolution LODs

# Revision 1856 - da12thMonkey

^ Quick config setup for @J0zh94 M249 Mk1 (now class rhs_weap_m249)
^ Moved solid stock M249 PIP model to the previously defunct class rhs_weap_m249_pip
^ Additional low res shadow LOD for the M40A5


# Revision 1855 - j0zh94

+ Added m249 mk1, textures still need colour adjustment to match 249 before it's complete

# Revision 1854 - da12thMonkey

+ Added placeholders for camo S&B scopes for the M40, requested by Sabre

# Revision 1853 - da12thMonkey

Requested M40A5 changes for Sabre to work with:
^ Raised cheek-rest by 2cm in model
+ Added placeholder texture and material paths
+ Set up config classes for desert and woodland retexture variants by hiddenSelectionsTextures

# Revision 1852 - da12thMonkey

^ M40A5: Adjusted position, added first Shadow LOD and animated the striker on the back of the bolt (thanks to Kllrt)
+ Added initial handanim for M40A5 (right thumb still needs tweaking)

# Revision 1851 - da12thMonkey

^ Initial M40A5 injection

# Revision 1850 - Redphoenix

+ initial M40A5 commit @gurdy

# Revision 1849 - da12thMonkey

^ Yet more M249 model refinements: filled missing faces in pintle loop, improved gas block on Short PIP barrel

# Revision 1848 - da12thMonkey

^ More M249 improvements (fixes missing windage indicator in pilot views, short barrel muzzle brake missing geometry)

# Revision 1847 - da12thMonkey

@ Restored missing gas tubes in M249 top shadow LODs

# Revision 1846 - da12thMonkey

^ Purged M249 shadow LODs of assigned textures, materials and UV data/magazine
@ Fixed missing texture path error for M249 magazine ground model

# Revision 1845 - da12thMonkey

Missed a semicolon

# Revision 1844 - da12thMonkey

^ Some initial MTVR wheel animations (suspension, steering, driving)

# Revision 1843 - da12thMonkey

^ Texture merge and config for J0zh94's old-style M249

# Revision 1842 - da12thMonkey

+ Added straight vert grip handanim for M249 when using GripPod and TD Grip

# Revision 1841 - j0zh94

+ Added non PIP variant of M249

# Revision 1840 - da12thMonkey

Trivial change by orders of Bossman

# Revision 1839 - da12thMonkey

^ Major optimisation of M249s (reduced from 12 sections to 5)
^ Made M249 VFG variants now uses the grip attachment system (will make appropriate anims for straight grips)
+ Added SAW front grip as an attachment (currently only compatible with M249 itself)
- Removed redundant models, materials and textures from the M249 folder

# Revision 1838 - Soul_Assassin

@ Flipped Premier scope normals, tweaked rvmat

# Revision 1837 - reyhard

@ fixed M1025 engine smoke mem points
@ fixed m1025 damage textures
@ fixed hemmts autocenter & maxFordingDepth


# Revision 1836 - Soul_Assassin

Update version number is settings

# Revision 1835 - reyhard

^ more changes to grip system

# Revision 1834 - reyhard

@ fixed nvg visible in fpv 
@ fixed UH60M dampers wobbling
@ scoped = 1 base m107 magazine (was visible in all mags tab)
@ A-10 & F-22 no longer takes damage during proper landing
^ tweaked gripod structure in order to make it supporting 3rd party mods

# Revision 1833 - reyhard

^ tweaked Bradley ERA blocks

# Revision 1832 - j0zh94

@ added Temp PBOPrefix just in case

# Revision 1831 - j0zh94

@ Temporary fix for MTRV

# Revision 1830 - zeealex

[+] added MTVR base (needs hella fixing)

# Revision 1829 - reyhard

^ increased dispersion of m230 & m197 autocannons
@ M1 FCS manual correction bug

# Revision 1828 - reyhard

@ fixed M1 optics zooms levels
@ rhsusf menu option not working in standalone mode


# Revision 1827 - reyhard

@ rpt error fixes
@ fixed Gen 3 hitpoints
@ fixed Stinger pod get in mem points

# Revision 1826 - reyhard

^ configured spc hidden selections
^ spc patchless versions are handled by hidden selection textures & materials
^ spc light shadow lod tweaks
@ M62 20&5rnd mags tracers not working
@ Buckshot hit errors
@ fixed M1117 turned out commander was moving with main turret
@ fixed gunner view point clipping when aiming high - close T1723
@ fixed laser position on ANPEQs
@ calibrated Elcan 2D & 3D reticle

# Revision 1825 - reyhard

@ readded insignia & clan patches to upc & frog uniforms
^ optimized SPC & IOTV vests (sections count, more res lods, removed old camelback from pilot view)
^ added camo selections to SPC (not configured yet)

# Revision 1824 - da12thMonkey

^ S&B M8541 model tweaks: locked some normals in pilot LOD to workaround hard edges bug (ObjBldr + small faces), moved 1.5cm backwards for better seating on EBR rail.

# Revision 1823 - reyhard

@ bolt action rifles anims broken after throwing grenade
@ WMX + ANPEQ were missing proper entries for HK416 rail

# Revision 1822 - da12thMonkey

^ Removed 15x magnification level from S&B (M8541 is 3-12x, not 3-15x like M8541A)

# Revision 1821 - da12thMonkey

^ Uploaded temporary materials in 4096 res by mistake - replaced with smaller 2048s

# Revision 1820 - da12thMonkey

+ Added Schmidt & Bender M8541 to scopes. Just needs proper textures and materials from Sabre

# Revision 1819 - Kllrt

Fixed M72 texture - downscaled

# Revision 1818 - reyhard



# Revision 1817 - reyhard



# Revision 1816 - reyhard

@ removed titan silencer from m24sws

# Revision 1815 - reyhard

@ DUSK antenas selections were not selected in 2nd res lod
@ reverted M107 mass changes
^ reduced MELB engine & tail rotor armor

# Revision 1814 - reyhard

@ m1a1fep & hc commander mg fixed - close T1727
@ proper scoping out for smaw optic variants

# Revision 1813 - da12thMonkey

@ Fixed OD textures for M1025 LODs were too light

# Revision 1812 - sykoCrazy

^ Tweaked textures and rvmats for FMTV/HEMTT/M1025/CH-47/UH-60/M1117(UN Variant)
@ Fixed bad geometry and unnecessary UV channels in FMTV/HEMTT/M1025/CH-47/UH-60
^ lower res LODs for rocket pods
^ Squad XML positioning in CH-47/UH-60/AH-1


# Revision 1811 - zeealex

[+] Added LWH with black goggles (tan should still be default)
[^] Improved M8541A SSDS visuals
[+] Added Lower mounted version of premier

# Revision 1810 - gurdy

+ Missing M113A3 OD textures

# Revision 1809 - MistyRonin

^ Added Premier low placeholder asdg compatibility

# Revision 1808 - MistyRonin

+ Add premier low placeholder - per request

# Revision 1807 - Soul_Assassin

^ M107 nohq and smdi texture size reduced, materials tweaked and small smoothing group fixes.

# Revision 1806 - ballistic09

+ Added Olive Drab textureSources for M113's and M2 Bradleys
@ Fixed small hiddenSelections issue on woodland M2A3 BUSK I Duke antennas

# Revision 1805 - j0zh94

^ Fixed M1025 M2 shell casing ejection

# Revision 1804 - j0zh94

^ Fixed M113 M2 shell casing

# Revision 1803 - j0zh94

^Edit config of M2 for new shell casing, still needs tweaking...

# Revision 1802 - j0zh94

^ Tester, fixed M2 shell casings. Still needs further tweaking though so not ready...

# Revision 1801 - j0zh94

^ Added geometry to last LOD (high quality 6 sided box)

# Revision 1800 - reyhard

@ fixed small M1 bugs - close T1716

# Revision 1799 - reyhard

^ removed barrel from M1 phys lod
@ fixed M1A2 turret order
@ M1117 used wrong function (afrf reference)
^ tweaked rotation speed of M119A2

# Revision 1798 - da12thMonkey

+ SR-25 paint schemes (pls check for hsMaterials problems, but should work since the camo rvmats are now applied to the EC .p3d)
+ Empty Rhino mount for NVG slot (should have no NVG properties in Apex/1.62+)

# Revision 1797 - reyhard

^ gear visibility in cargo lod of uh60m (change visible for FFV seats)
^ tweaked FFV limits on UH1Y
^ tweaked cargo positions on UH1Y
^ tweaked amphibious physx of M113 (turning ratio, max speed)


# Revision 1796 - reyhard

^ added duke jamming to M1A1 FEP, M1A2SEP v2 & Bradleys
^ tweaked duke jamming script
^ tweaked M1117 destruction effects

# Revision 1795 - reyhard

@ fixed hemtt light points & hitpoints 
@ fixed Mark V SOC troop capacity
@ fixed vehicle M2 gunner boundingSphere size
^ added DUKE destruction to Bradleys & M1 tanks
^ added ability to hide DUKE antennas on Bradleys
^ M1025 engine damage selection

# Revision 1794 - reyhard

^ added wound texture for Gen 3
@ fixed wound textures for US Army uniforms

# Revision 1793 - reyhard

^ tweaked duke jamming & destruction scripts
^ added binoculars to M1117 cargo

# Revision 1792 - reyhard

^ added socom editor preview images
^ update rhsusf_c_troops cfgPatches to include ALL units
@ fixed SR-25 missing penetration .rvmats
@ PKAS collimator strings

# Revision 1791 - reyhard

@ fording depth for M1025ies
@ M1117 & hmmvies now properly slow down in water - close T1706
@ radio protocol fix for 1.62 - requires RC
+ DUKE jamming script (for now M1117 only. WIP)

# Revision 1790 - MistyRonin

^ Update US cfgconfigs

# Revision 1789 - reyhard

^ M1117 & M1025s were missing engine smoke effect
^ improved M1025s engine hitpoints
^ some fancy stuff added to M1117 (WIP) like:
 - optic destruction
 - duke destruction
 - updated cfgPatches
 - new FG & hitpoints
 - fixed selection names
 - 3 additional passenger seats inside
 - close T1701 & T1700
^ tweaked maxFordingDepth for M1025ies - need to redo it anyway since autocenter=0 seems to break water resistance ( https://community.bistudio.com/wiki/Arma_3_Ships_Config_Guidelines#LODs_.28included_in_Arma_3_boat_p3ds.29 ), on the other hand, without autocenter=0 values for maxFordingDepth need to be tweaked per model because autocenter algorithm will not always produce predictable results
^ integrated MELB weapons to RHSUSF configs
@ MELB Hellfire now use proper penetrator
@ removed pilot targeting pod from F-22, UH1Y & CH47
@ fixed A-10 TVM ui
@ UH60M (D) used wrong model & had fucked up cfg


# Revision 1788 - LAxemann

Fixed: Applied reyhards fix for cutting off sounds to all weapon tail configs (which caused it)

# Revision 1787 - reyhard

@ potential fix for sounds going off

# Revision 1786 - j0zh94

@ Fixed M4 Magazine thermal texture

# Revision 1785 - Redphoenix

First iteration of improved M1911 mats

# Revision 1784 - j0zh94

^ Improved M4a1 Thermal texture

# Revision 1783 - Bakerman

@ Body armour values

# Revision 1782 - LAxemann

Added: New M590 sounds

# Revision 1781 - LAxemann

Tweaked: Lowered M590 pump volume

# Revision 1780 - MistyRonin

+ First batch of MARSOC tweaks & unscope 

# Revision 1779 - Soul_Assassin

^ ACOG visual update texture and material tweaks

# Revision 1778 - Soul_Assassin

Cleaned up mk18 rail AS map

# Revision 1777 - Soul_Assassin

PROTEC work: material and texture tweaks, insides not see through anymore, shadow tweaks, new ui pics

# Revision 1776 - da12thMonkey

+ New Mk18 UI icons

# Revision 1775 - da12thMonkey

^ Aligned Mk18 and M4B2 viewPilot rail attachment proxy with other LODs
+ Added updated UI icons for M4B2 variants (still to do Mk18s icons)

# Revision 1774 - da12thMonkey

+ Configured ghillied M24
^ Swapped muzzle flash for a more suitable one

# Revision 1773 - LAxemann

Added: Autocannon tail sounds
Added: New M242 sounds

# Revision 1772 - Redphoenix

+ Bouyancy LOD for M1117
@ Geo Phys Lod for M1117
tried fixing M1117 slowing down when hitting water, shit doesnt work. kthxgggoodbye

# Revision 1772 - Redphoenix

+ Bouyancy LOD for M1117
@ Geo Phys Lod for M1117
tried fixing M1117 slowing down when hitting water, shit doesnt work. kthxgggoodbye

# Revision 1771 - Redphoenix

@ unified and improved M1025 engine hitpoint position
+ Bouyancy LOD for all M1025s
+ class Sound to M1025 and raised interior idle sounds

# Revision 1770 - da12thMonkey

@ Fixed Mk18 rails had wrong path in hiddenSelectionsMaterials
@ Tan TD grip had AFG UI icon (changed inheritance)

# Revision 1769 - da12thMonkey

^ Activated Mk18 rail hiddenSelections
^ Scoped in black Mk18s

# Revision 1768 - da12thMonkey

^ Scaled up suppressors

# Revision 1767 - Redphoenix

^ M1117 fording depth

# Revision 1766 - Redphoenix

^ M1025 fording depth

# Revision 1765 - sabre

[Textures] Added WD version of LWH acc texture with Black ESS and Cover.

# Revision 1764 - sabre

[Textures] Mk18 painted rails.

# Revision 1763 - LAxemann

Added: Old DynaSound placeholder sounds for the M230
Added: Old DynaSound placeholder sounds for the MK19
Tweaked: Lowered M249 closure volume
Tweaked: M2 sounds
Tweaked: M240 sounds
Added: Config entries for m230 and mk19 in order to match the new sound config
Removed: Old MK19 sounds

# Revision 1765 - sabre

[Textures] Added WD version of LWH acc texture with Black ESS and Cover.

# Revision 1764 - sabre

[Textures] Mk18 painted rails.

# Revision 1763 - LAxemann

Added: Old DynaSound placeholder sounds for the M230
Added: Old DynaSound placeholder sounds for the MK19
Tweaked: Lowered M249 closure volume
Tweaked: M2 sounds
Tweaked: M240 sounds
Added: Config entries for m230 and mk19 in order to match the new sound config
Removed: Old MK19 sounds

# Revision 1762 - reyhard

+ added elcan 3d variant 
@ removed non working pbo versioning from cfgPatches

# Revision 1761 - da12thMonkey

^ Re-baslined Pro-Tec helmet naming around the bare version rather than the one with Rhino

# Revision 1760 - reyhard

^ reduced acog glass reflection

# Revision 1759 - LAxemann

Tweaked: M249 0m sounds

# Revision 1758 - reyhard

^ synced m203 anim
^ changed m203 reload sound

# Revision 1757 - reyhard

@ fixed inheritance errors for Tanoa
@ fixed M4/M16 with M203 accepted top laser attachments
@ US Army & USMC grenadier had assigned top anpeq15

# Revision 1756 - da12thMonkey

Forgot to add the additional .p3ds to the commit, because I'm an idiot

# Revision 1755 - da12thMonkey

+ Pro-Tec helmet variants

# Revision 1754 - Soul_Assassin

Work on T1679

- lods
- size and position
- shadows

# Revision 1753 - reyhard

^ increased M2 antirollbar strength
^ improved M1A2 HMG handling
@ M240 inheritance
@ missing airweapons in sound cfgPatches

# Revision 1752 - LAxemann

Tweaked: M14 sounds
Changed: SR-Weapon family now uses AR15 (M16) closure sound

# Revision 1751 - LAxemann

Added: Sound config template
Added: Almost 300 sounds for categorized reverb tails
Added: All-new m4 sounds + configs
Added: All-new m16 sounds + configs
Added: All-new m249 sounds + configs
Added: All-new m240 sounds + configs
Added: All-new m136 sounds + configs
Added: All-new m14 sounds + configs
Added: All-new m2010 sounds + configs
Added: All-new tank cannon sounds + configs
Added: All-new howitzer sounds + configs
Added: All-new m107 sounds + configs
Added: All-new mp7 sounds + configs
Added: Probably much more
Removed: All old files that were left from the now re-made weapons


# Revision 1750 - Soul_Assassin

Bad sight axis on Mk18 M320

# Revision 1749 - Soul_Assassin

Small Mk18 tweaks.

# Revision 1748 - reyhard

+ added optic preference settings to rhs options menu
^ tweaked ACOG 3d variants
@ fixed Elcan PIP scale

# Revision 1747 - Soul_Assassin

^ Small tweak to PEQ 15 fresnel to make normals visible again.

# Revision 1746 - da12thMonkey

^ GL leaf sight for M4A1 Blk2

# Revision 1745 - da12thMonkey

^M24 handanim and icons

# Revision 1744 - reyhard

^ improved ACOG fibre cable, glass material & added 3d variant (all acogs are 3d temporarily - will add some preference menu tomorrow)

# Revision 1743 - da12thMonkey

^ Camo M4 variant stringtables
+ Configured camouflaged M4A1 Block 2s w/ M203

# Revision 1742 - reyhard

@ fixed author[] not an value error
^ added locality check to seat ejection script

# Revision 1741 - Soul_Assassin

Added M203 block II variant

# Revision 1740 - da12thMonkey

^ Specter 3D reticles scaled up to better match ballistics and ranging (ended up scaled slightly too small after I adjusted the scale of the whole sight before)

# Revision 1739 - MistyRonin

+ Add Mk 18 painted variants - I'll later add them to the crates and zeus. 

# Revision 1738 - da12thMonkey

@ Fixed: 40mm grenade was not following tube on Mk18 M320 (adjusted bone sequence in skeleton)

# Revision 1737 - Soul_Assassin

Mar tweaks on rails

# Revision 1736 - da12thMonkey

@ Fixed missing texture error in Mk18s (wrong HSTex/HSMat paths to M320)

# Revision 1735 - Soul_Assassin

Rails rvmat tweak

# Revision 1734 - Soul_Assassin

+ Added new Mk18 handguard


# Revision 1733 - Soul_Assassin

+ Added first iteration Mk18 rails

# Revision 1732 - reyhard

^ added magazineReloadPhase to M240, M249 & M4 (seems not to work with m4 pmags)

# Revision 1731 - sabre

[Textures] Block II DD rail desert.

# Revision 1730 - sabre

[Textures] Woodland M4 parts and more desert pieces. Some pending ingame lighting tweaks.

# Revision 1729 - MistyRonin

@ Wrong path for the M4A1 Block II KAC Woodland

# Revision 1728 - MistyRonin

+ M4A1 Block II painted configs and texture placeholders - For Sabre to swap 

# Revision 1727 - reyhard

^ updated cfgPatches
^ added script for ANPEQ15 handling - close T1625
^ added selections to Mk18 & M4 B2
^ reduced armorStructural for MELB & added script to improve crash survivability (seems not to work correctly - might need to revert before release)
@ it was possible to attach top accessories on side only rail
@ M4BII M203 reload anim (wrong bone) 

# Revision 1726 - reyhard

@ eden editor images issues with static weapons
@ some weapons were using acogd name

# Revision 1725 - Soul_Assassin

M24 updates:
- Material tweaks for new lighting
- Flip normals - fix T1668
- Anims and hidden selections work
- Flash gone

# Revision 1724 - da12thMonkey

@ Fixed MS2000 strobe hiddenSelectionsTextures paths for Ops-Core

# Revision 1723 - reyhard

+ added Eden Preview pictures for almost all USAF units (except fmtv) - still some issues with static weapons
^ moved eden preview pictures from a2port_air to separate folder
@ USMC squad leader was missing weapons due to typo in cfg
@ AH1Z GS had broken rockets
@ USMC RG-33 /w m2 had wrong turret texture

# Revision 1722 - da12thMonkey

^More language strings for "Black Rails"

# Revision 1721 - da12thMonkey

^Displayname/Stringtable edits for Block 2 M4s

# Revision 1720 - reyhard

^ added Editor Previews pictures for A2 Air ports
@ M1117 hatch stayed locked when jumping out from turned out position
^ Mk18 & M4BII missing from our VA boxes
@ M4BII black rail inheritance issues

# Revision 1719 - Soul_Assassin

+ Added new M4A1 Block II handguard

# Revision 1718 - reyhard

+ added turn out option for M1117 gunner & commander
@ fixed some commander pip screen errors

# Revision 1717 - Kllrt

Added WIP Pro-Tec SF helmet

# Revision 1716 - MistyRonin

+ M4A1 Block II Black Rail placeholders

# Revision 1715 - da12thMonkey

All USAF weapons model.cfg animationsources updated to v.1.60 StandardSound (anims wont work in v.1.58)

Source names changed:
^ reload -> reload.0
^ isEmpty -> isEmpty.0
^ isEmptyNoReload -> isEmptyNoReload.0
^ reloadmagazine -> reloadmagazine.0
^ reloadMagazine2 -> reloadMagazine.1
^ hasMagazine -> hasMagazine.0
^ zeroing1 -> zeroing.0

Additional modifications:

+ trigger.0 anim for rifle trigger (replaces reload source for trigger)
+ trigger.1 anim for UGL triggers (selections added to models)
+ grenade warhead hides when UGLs are fired (based on revolving.1 source)
^ 40mm grenade mesh in UGL barrels was modified so that the break between the "gl_bullet" and "gl_cartridge" selections is accurate.



# Revision 1714 - Stagler

@Even More NV Tweaking - T1659
@PVS-15 texture wasn't _co - T1659

# Revision 1713 - Stagler

@More NV Tweaking - T1659

# Revision 1712 - Soul_Assassin

^ Moved SOPMOD weapons to new pbo

# Revision 1711 - reyhard

+ added option to move inside of CH47 & CH53
+ added option to attach & paradrop items from CH47 & CH53
^ it's possible to hide cargo benches on CH-53E now
^ optimization to paradrop & move inside scripts
^ tweaked C130J mfd - it's no longer HMD but there is now bis bug visible with mfd elements being rendered through geometry (same as clock on bis civilian truck)
^ added eden attribute to attach boats to Mk V & boat loading finalization - close T1585

# Revision 1710 - Redphoenix

@ reduced visiblity of C130J HUD - close T1639

# Revision 1709 - reyhard

^ tweaked infantry footwear shadows
^ tweaked surefire shadow on ach helmets
^ automated monitor deploy for MELB copilot when going into optic view
^ tweaks to boat loading (still wip)

# Revision 1708 - MistyRonin

^ Assign new gloves to G3 uniforms

# Revision 1707 - reyhard

+ added option for manual rifle bolting in RO2 style
^ adjusted M320 reload anims for HK416 & M4 rifles
^ added some splash damage to canister round fletches 
^ increased version in options menu to 0.4.1.1

# Revision 1706 - sabre

[Textures] Mechanix colour variants. 

# Revision 1705 - Stagler

@Tweaked NVG positioning on PVS14 and 15. Should now fit all US helmets (OPSCORE, ACH, MICH w/ universal shroud, LWH) better generally.

# Revision 1704 - reyhard

+ added first version of boat loading menu to Mark V SOC
@ alpha issue with collimators on Mk18 & M4BII
^ removed not needed named properties from Mk18 & M4BII in order to fix random switching to last res lod on RC branch
@ Mark V irradiance map .rpt errors in diagnostic.exe
@ Mark V M134 particle effects pos
@ Mark V missing gunner get in points for both M2 & M134
@ Mark V - displays not working
^ tweaked Mark V res lods - reoargaized seats to allow easiers managment of proxy res lods
^ moved guns to separate compartments to unclutter action menu for Mark V
^ increased specular power of XPS3 glass

# Revision 1703 - da12thMonkey

Initial HK416 testbed for 1.60 weapon animation sources
+ trigger.0 anim for rifle trigger (replaces reload source for trigger)
+ grenade warhead hides when the M320 is fired (based on revolving.1 source)

Other anims sources updated:
^ reload -> reload.0
^ isEmpty -> isEmpty.0
^ isEmptyNoReload -> isEmptyNoReload.0
^ reloadmagazine -> reloadmagazine.0
^ reloadMagazine2 -> reloadMagazine.1
^ hasMagazine -> hasMagazine.0
^ zeroing1 -> zeroing.0

Please compare to M4 w/M320 and check if anything is broken



# Revision 1702 - MistyRonin

+ First batch of WIP configs for M24 SWS

# Revision 1701 - sabre

[Textures] Rolled over updated textures done for Spec4

# Revision 1700 - zeealex

fixed smoothing errors on M24

# Revision 1699 - zeealex

[+] Added M24 Raw files for config

# Revision 1698 - reyhard



# Revision 1697 - reyhard

@ zeus placable m107 was missing scope=2
@ mk18 ironsight anims
^ cleaned up named properities & tweaked ironsight rotation axis
@ muzzle flash rotation axis on rifles with UGLs

# Revision 1696 - reyhard

+ added UI menu for Mark V various options to reduce action menu cluster
+ added scripted workaround for getting on deck as rifleman for Mark V
^ added some basic reslods to reduce FPS drop (can be deleted later, didn't took me too much time to create them)


# Revision 1695 - reyhard

@ added missing author tag to EXPS3
^ added eden placable m249
^ added fron ironsight shadow on m107 
^ tweaked premiere scope shadow & added shadow res lod
^ tweaked Eotech 552 shadows

# Revision 1694 - reyhard

^ renabled TFAR LR radio (even though there is no radio inside)
^ changed 0-2 Aperture flipping on weapons with carry handle 

# Revision 1693 - reyhard

^ increased cargo capacity of Mark V
@ fixed M1A2SEP (non tusk) commander couldn't use his M2 when turned out
@ missing geometry in ejection port of Mk18 & M4 Block II
@ missing parts in shadow lod of M240G & B
@ fixed HK416 full auto mode ai distances

# Revision 1692 - reyhard

@ removed zeroing settings from M590
@ fixed more missing author tags for magazines
@ M203S shadow - close T1637

# Revision 1691 - reyhard

^ tweaked disposable launcher script
@ fixed M113 (ammo) variant texture randomization
@ spent disposable launchers adding magazine in inventory
@ increased M107 & it's magazines mass (similar, but not same as GM6 now)

# Revision 1690 - bek

^ Tweaked recoil to be more consistent across AFRF and USF

recoil = "recoil_mx";//416 D10 (was mxc) - lowered
recoil = "recoil_mxm";//416 D14.5 (was mx) - lowered
recoil = "recoil_mxm";//M4 (was mx) - lowered
recoil = "recoil_mx";// mk 18 (was mxc) - lowered

# Revision 1689 - Redphoenix

@ fixed NT4 normal map (again)

# Revision 1689 - Redphoenix

@ fixed NT4 normal map (again)

# Revision 1688 - Redphoenix

^ full revamp of NT4 model and textures - close T1643

# Revision 1687 - reyhard

@ fixed inheritance of desert M4 rifles
^ rewritten gripod system to use EHs instead of loop - increased performance & reliability

# Revision 1686 - da12thMonkey

@ Removed strap loop from the top of Bowman earpiece in MICH helmets, to stop clipping through

# Revision 1685 - reyhard

@ fixed M6A2 rpt errors

# Revision 1684 - reyhard

@ random texture picking in eden - close T1580

# Revision 1683 - reyhard

@ reverted m792 autodestruction
^ improved m113 driver view

# Revision 1682 - Redphoenix

^ corrected several USAF pilot stick animations close T1635

# Revision 1681 - reyhard

^ removed 1.60 targeting system
^ TOW now GHOT FLIR

# Revision 1680 - MistyRonin

^ Tweaks to Mark V SOC Crew

# Revision 1679 - reyhard

^ tweaks to M1 tanks hitpoints
^ removed double pintle_cover.p3d proxy from m1a1 tusk I & m1a1FEP

# Revision 1678 - reyhard

@ mirror for armed variants of rg33, fmtv & hemmts were not properly 
inherited (some engine change I guess) - close T1624
@ fixed missing LB script error - close T1614
^ tweaked hemmts mirrors uving
@ armed hemmts were missing some geometry in pilot lod

# Revision 1677 - Soul_Assassin

@ Attempt to fix faulty normals on sparewheel in HEMMTs

# Revision 1676 - Redphoenix

+ SMAW Spotting Rounds to Arsenal

# Revision 1675 - LAxemann

Fixed: MKV config so that the sounds work

# Revision 1674 - reyhard

@ fixed M240 anim changing script not working after reload

# Revision 1673 - LAxemann

Changed: MKV config to use new sounds

# Revision 1672 - LAxemann

Added: New sounds

# Revision 1671 - reyhard

@ Mark V alpha fix

# Revision 1670 - gurdy

@ texture fix on m1117

# Revision 1669 - da12thMonkey

@ Some weapons missing RHS author tags (M107s, MP7 camo variants etc.)

# Revision 1668 - Redphoenix

^ raised RG33 brake Force

# Revision 1667 - Redphoenix

^ FMTV Handbrake and other PhysX-related changes

# Revision 1666 - MistyRonin

^ Improve requested SWCC placeholder 
+ SPC patchless variant

# Revision 1665 - sabre

[Textures] SPC Textures sans USMC Flak patch.

# Revision 1665 - sabre

[Textures] SPC Textures sans USMC Flak patch.

# Revision 1664 - MistyRonin

^ Improved Mark V SOC physX
+ Add Armored Driver for FMTVs per request
+ Add placeholder SWCC crewman to Mark V per request
^ Updated US stringtable 

# Revision 1663 - da12thMonkey

@ Fixed rogue "camo2" selection on the gun mount in view Gunner LOD

Was interfering with the "Camo2" hiddenSelectionsTextures for the flatbed.
Lower-case meant "camo2" was a separate selection to "Camo2" and HStextures were being applied there instead.
Result was that desert vehicle had woodland flatbed in viewgunner LOD ingame. Repair and ammo models' selection names were okay.

# Revision 1662 - MistyRonin

+ Add new "Armored" driver in US Army, and assigned it to US HEMTTs

# Revision 1661 - MistyRonin

^ Changed HEMTT crews from driver to rifleman M4. 

# Revision 1660 - Redphoenix

more CfgPatches 

# Revision 1659 - Redphoenix

^ CfgPatches Fixes

# Revision 1658 - reyhard

@ M1025 doors sounds

# Revision 1657 - reyhard

@ AH64 & AH1Z gun particles position
@ HEMMT & RG-33 OGPK mirror were mirrored (fmtv are still bugged)
@ added pintle selection for armed hemmts
+ added turn in ability for armed M1025s, hemmts, fmtvs & rg33


# Revision 1656 - reyhard

@ c130 get in bug seems to be fixed - please test

# Revision 1655 - reyhard

turned off c130 for some local testing

# Revision 1654 - reyhard



# Revision 1653 - bek

@ Other USF rvmat referencing AFRF

# Revision 1652 - reyhard



# Revision 1651 - bek

@ RHSUSF rvmat referencing AFRF

# Revision 1650 - reyhard



# Revision 1649 - reyhard



# Revision 1648 - reyhard



# Revision 1647 - reyhard



# Revision 1646 - reyhard



# Revision 1645 - reyhard



# Revision 1644 - reyhard



# Revision 1643 - reyhard



# Revision 1642 - reyhard

^ more c130 testing

# Revision 1641 - reyhard

^ more c130 testing

# Revision 1640 - reyhard

@ c130 testing

# Revision 1639 - MistyRonin

@ Proper M203 anim for Bk2

# Revision 1638 - sykoCrazy

@ Fixed missing rocket magazines

# Revision 1637 - da12thMonkey

^ SOPMOD M4s fitted with legal ironsights from M27
^ side rail proxies moved forward

As per Misty's instructions

# Revision 1636 - sykoCrazy

@ Fixed missing ammo class

# Revision 1635 - reyhard

^ finalized hemmt - close T1487:
	- Added damage & destruction materials
	- Player is no longer able to go through wreck
	- Lights selections
	- Added res lods
	- Added spare wheel hidding
	- Fixed destruction selections
	- Fixed M2 UI
	- Fixed M2 attenuation effect
	- Added bed in geometry physx so it's possible to transport things inside
	- Added clan logo
	- Added engine smoke & fire effect
	- Added texture selection in VG
	- Fixed gunnerview mem point
	- Fixed some selections that didn't have rvmat

# Revision 1634 - Soul_Assassin

Unburn c_MELB

# Revision 1633 - sykoCrazy

+ FFAR rocket models
@ Rocket proxy weapons on helicopters
@ Littlebird texture detail

# Revision 1632 - zeealex

[*] Reduced Spectre Texture resolution

# Revision 1631 - Soul_Assassin

@ Removed broken FFV for now

# Revision 1630 - Soul_Assassin

^ Mk19 inserted into Mk V SOC, some alpha changes.

# Revision 1629 - zeealex

[*] Fixed PEQ ShadowLODS

# Revision 1628 - reyhard

@ potential fix for misty bug

# Revision 1627 - zeealex

{*] fixed flipped opscore NSW NOHQ green channel

# Revision 1626 - reyhard

+ added flagRight & flagLeft selections to G3 uniform

# Revision 1625 - da12thMonkey

^ Added an inner aperture to the M27's rear ironsight, as per Misty's instructions. Closes T1589

# Revision 1624 - reyhard

@ fixed XEH error logs
^ mark v soc is now compatible with CBA & our EH
^ added rhs prefix to mark V animation names
@ potential fix for Mark V ctd
@ attenuation effect in Mark V turrets
@ missing materials in Mark V FG
^ changed mark v weapons so they inherit from rhs counterparts
^ removed 1.60 crewAim indicators from Bradley & M1 tanks

# Revision 1623 - Kllrt

@ Renamed UH1Y skeleton for safety

# Revision 1622 - reyhard

^ removed recompile param from USF

# Revision 1621 - reyhard

@ added missing model.cfg to markvsoc anim folder
^ changed acc combo to cfg param reading version
^ engine fire change vehicle rvmats to damaged version

# Revision 1620 - Soul_Assassin

^ Mk V SOC port M2 changed

# Revision 1619 - Soul_Assassin

@ Resurrected missing geometry on loader guns of all M1A1 and A2

# Revision 1618 - MistyRonin

^ Improved SOPMOD 2 rifles hand anim

# Revision 1617 - MistyRonin

^ Unscope Mk 18 & M4 Block 2 - As we are now into SOCOM stuff, and they have the grips, iron sights and safety configured. 

# Revision 1616 - MistyRonin

+ Tan & OD variants for SU230 3D

# Revision 1615 - da12thMonkey

+ Basic UI icons for SU-230 SpecterDR and PVS-27 MUNS

# Revision 1614 - da12thMonkey

^ Moved Specters up by a few mm to stop rail clipping, following previous upscaling
^ Hidden Specter+PVS-27 model to use updated Specter mesh

# Revision 1613 - da12thMonkey

^ Scaled up SpecterDRs to be 153mm in length (Y position might need tweaking again to sit on rails)
- Removed "Addblend" renderflag from reticle .rvmat. Hopefully fixes T1586 but needs testing since I couldn't repro the original issue ingame
^ Made 3D reticle lines thicker and scaled up range numerals so they are easier to see in 4x 3D scopes

# Revision 1612 - MistyRonin

+ SU230 Tan and Olive variants

# Revision 1611 - MistyRonin

+ Add new glass texture to Mark V SOC

# Revision 1610 - MistyRonin

+ AN/PEQ-15 Black variants config (including combos)

# Revision 1609 - Soul_Assassin

Mk V - starboard M2 replaced, alpha sorting glass fixed

# Revision 1608 - da12thMonkey

@ Missed a small part when copying+pasting shadow LOD to other PVS-27 attachments

# Revision 1607 - da12thMonkey

+ PVS-27 Shadow LOD mesh

# Revision 1606 - zeealex

[+] Added texture variations for SpecterDR and PEQ 15

# Revision 1605 - da12thMonkey

^ Centred PVS-27 on rail axis to reduce minor clipping - closes issue T1582
^ Closed missing face on M16A4 RIS top rail segments (and reduced section count while I was at it)

# Revision 1604 - da12thMonkey

@ M27 pilot views: added missing parts magazine release and fence, dust cover etc. fixes {T1579}
^ Add renderflags to SU-230 reticle rvmats
^ Fixed triangulation artifact in SpecterDR

# Revision 1603 - Soul_Assassin

^ Fixed some geometry clipping issues in first person

# Revision 1602 - MistyRonin

+ Add SpecterDR 3D (CX) variant & SU230A 3D
^ Tweaks to SpecterDR configs
+ Add M4A1 Desert strings to stringtable - Close T1555

# Revision 1601 - da12thMonkey

^ Reworked SpecterDR pilot LOD for 3d scopes - commercial reticle for Misty
+ SU-230 model (M4/M249 reticle), 3D matches 2D scope
+ SU-230A model (7.62mm rifle/M240 reticle), 3D matches 2D scope
^ Added reticle illumination in 3d modes
^ Set BUIS zero to 200m

# Revision 1600 - Soul_Assassin

^ Improved M1117 config for parsing

# Revision 1599 - Soul_Assassin

SpectreDR work

# Revision 1598 - da12thMonkey

@ Updated texture & material paths in orange tracer model to the correct location

# Revision 1597 - zeealex

[^] Updated Specter DR model and textures

# Revision 1596 - Kllrt

@ Fixed paths on MkV boat

# Revision 1595 - MistyRonin

^ Update Mark V SOC files paths

# Revision 1594 - MistyRonin

^ Improved Mark V Hull texture

# Revision 1593 - da12thMonkey

+ Calibrated 2D optics for the SU-230/PVS (5.56mm) and SU-230A/PVS (7.62mm) SpecterDR 4x mode

Matching reticles will be added to .p3ds for the 1x mode and 3D 4x once the reworked model is finalised

# Revision 1592 - Soul_Assassin

^ Patrol cap scaled down and fits better

# Revision 1591 - MistyRonin

^ Tweaks to Spectre & PVS-27 combo

# Revision 1590 - MistyRonin

@ SpecterDR POV tweaks

# Revision 1589 - MistyRonin

@ Fix missing weapon for USMC SARC (D)
^ Tweak SpecterDR

# Revision 1588 - MistyRonin

^ Config tweaks for SpectreDR family
^ Allowed NT4 Suppressors for M249 with long barrel

# Revision 1587 - Soul_Assassin

^ Moved Elcan scopes to new Scopes pbo (please put all new scopes here)
^ SpectreDR size, texture/normal and rvmat tweaks, new shadow

# Revision 1586 - MistyRonin

+ Add Mark V SOC sounds

# Revision 1585 - MistyRonin

+ Mark V SOC raw files. 

# Revision 1584 - reyhard

@ removed gear from canopies & ejection seat - close T1570

# Revision 1583 - reyhard

@ fixed infinitive ammo thing - close T1569

# Revision 1582 - zeealex

[*] Flipped specterDR NOHQ G channel

# Revision 1581 - Soul_Assassin

@ XPS dlc logo and small config cleanup.

# Revision 1580 - MistyRonin

^ Set tracer p3d in rhsusf_weapons - where it should had been

# Revision 1579 - MistyRonin

^ Add new (and proper) reticle to SpectreDR 

# Revision 1578 - sykoCrazy

+ Elcan SpecterDR reticle

# Revision 1577 - da12thMonkey

@ Fixed - M151 spotting scope _icon type image was generating a missing texture error (due to the old weapon attachment icon method). Replaced _icon.paa with a newly made .paa and different filename formatting, as per wld427's suggestion

# Revision 1576 - MistyRonin

^ Tweaks to USMC Recon loadout. 

# Revision 1575 - reyhard

^ TOW tube hiding on reload

# Revision 1574 - reyhard

@ triangulated WMX shadow lod - close T1564

# Revision 1573 - MistyRonin

^ Add AS file path to RVMAT

# Revision 1572 - MistyRonin

+ Add Ambient Shadow texture for WMX

# Revision 1571 - bek

^ re-added eotech logo because I likes it
^ tweaked textures/rvmat

# Revision 1570 - MistyRonin

- Day visual mode from AN/PVS-27 for accuracy - thanks to Hatchet's info 

# Revision 1569 - da12thMonkey

+ UI icons for other HK416 variants

# Revision 1568 - bek

^ Removed l3 branding from xps3/data/xps3_co.paa
^ Reduced xps3 glass glossiness
+ xps3 inventory icon

# Revision 1567 - da12thMonkey

Minor HK416 model changes

^ Stowed M320 front grip
^ Slight reduction of section count on all models (removed reference to IAR texture in LOD 5 and merged some 'like' sections)

# Revision 1566 - bek

+ eotech xps3 (wip)
@ a3 eotech renamed to EXPS3

# Revision 1565 - da12thMonkey

Made HK416 entries in cfgPatches weapons[] array

+ Editor weaponholders for new HK416 variants

# Revision 1564 - MistyRonin

^ Add stringtable entries for Leupold (Desert) & Specter
@ Fix wrong texture in one of the Fast Opscore

# Revision 1563 - MistyRonin

^ 2nd batch of SpectreDR configs 
+ Leupold Mk4 Desert

# Revision 1562 - MistyRonin

+ Add Leupold mk4 desert p3d

# Revision 1561 - sabre

[Textures] Swapped out old RHARD pack texture.

# Revision 1560 - MistyRonin

+ Elcan SpecterDR first config

# Revision 1559 - sabre

[Textures] Eotech Desert removed some nasty seam errors

# Revision 1558 - zeealex

[+] Initial injection of SpecterDR raw files (misty's on config)

# Revision 1557 - da12thMonkey

More HK416 stuff:

+ Added variants D10 and D14.5 with M320 GL (should have all the necessary model.cfg anims)
+ Added version of the D10 with LMT SOPMOD stock (also classes for grip system)
^ Moved optics proxies 25mm backwards
^ Moved Magazine 10mm upwards
+ Handanim to fit the M320 (sits slightly lower and further forward than it does on the M4)
+ Strings (maybe change "SOPMOD stock" to "LMT stock"?)

# Revision 1556 - da12thMonkey

+ UI icons images (M107 and HK416 variants)

# Revision 1555 - Kllrt

^ Improved HK416 shadow and added new textures for rear anim sight hide

# Revision 1554 - MistyRonin

- Scope to 1 ANVIS NVG

# Revision 1553 - da12thMonkey

Activated the ironsight hide animation for HK416 pending texture/material changes

# Revision 1552 - reyhard

@ fixed initSpeed inheritance since marksman dlc...
+ added engine smoke effect to m113

# Revision 1551 - sabre

[Textures] Slight brightness increase for M2010 Desert paint.

# Revision 1550 - sabre

[Textures[ Mk4 detail fix.

# Revision 1549 - reyhard

@ M1A1 FEP WD had texture swichted with OD variant
^ added eden attribute for DUKE antenna hiding/unhiding
^ changed HK416 14,5 muzzle velocity

# Revision 1548 - sabre

[Textures] Desert texture for Leupold Mk4 ER/T(XM2010)

# Revision 1547 - MistyRonin

^ HK416 Tweaks based on the vanilla MXC (MX Compact)

# Revision 1546 - MistyRonin

+ New batch of missing gear for the Ammo Crates, Zeus, and Virtual Arsenal

# Revision 1545 - MistyRonin

^ Update Virtual Arsenal with new weapons, uniforms and gear
^ Update Ammo & Weapon Crates
+ Zeus placeable weapons
@ Fix Wrong Opscore string

# Revision 1544 - Kllrt

^ Improved muzzle slot on HK416

# Revision 1543 - MistyRonin

@Fixes for Desert M4A1 variants

# Revision 1542 - Soul_Assassin

^ Some res lods for M977A4 Ammo

# Revision 1541 - reyhard

^ reduced muzzle speed of 10 inch HK
^ tweaked M1 decal init
^ tweaked M1 hitpoints & fixed some selection errors in res lods
^ tweaked rocket impact point for ah64 - close T1531
^ added res lods to rg-33 since plenty of people use it anyway

# Revision 1540 - Soul_Assassin

^ SPCS shoulder weights adjusted

# Revision 1539 - Soul_Assassin

Updates to PVS27 rvmat and smoothing groups

# Revision 1538 - da12thMonkey

+ HK416 grip system classes (inc. cfgpatches entries)
^ HK416 displayname as stringtable

# Revision 1537 - da12thMonkey

fixed build - I cocked up commenting out a section of the model.cfg

# Revision 1536 - da12thMonkey

^ Zeroing and animation for rear HK416 ironsight

Is also set up to hide the irons when optics are attached (rear on the D14.5, front and rear on the D10) as suggested in {T1554}. However, I've disabled the animation because the rear sight has a baked-in AO shadow that is visible when the ironsight is hidden

# Revision 1535 - da12thMonkey

^ Adjusted alignment of proxies on HK416s (muzzle, muzzleflash and side)

# Revision 1534 - Soul_Assassin

Various stringtable fixes

# Revision 1533 - Kllrt

Added HK416 WIP

# Revision 1532 - aleksadragutin

Added a basic p3d file with textures of my HK416.

# Revision 1531 - reyhard

^ removed proxies from M1 tanks & added hidden selections (WIP - decal selections are not configured properly for now)
^ tweaked gun mantlet FG for M1 tanks
^ optimized res lods for M1 tanks
^ added ability to hide DUKE antena (in VG only for now)

# Revision 1530 - MistyRonin

+ Add more Desert M4A1 variants

# Revision 1529 - MistyRonin

@ Fix old texture path in M4 desert textures

# Revision 1528 - MistyRonin

@ Fix Desert M4A1 Hidden Selections 

# Revision 1527 - MistyRonin

+ M4A1s Desert & Eotech Desert 

# Revision 1526 - MistyRonin

+ Add US weapons desert textures - Configs coming next

# Revision 1525 - MistyRonin

@ Fix Eagle UCP (AR) wrong texture
^ Improve US Army & USMC pilots loadout

# Revision 1524 - MistyRonin

+ Add last Ops-Core helmets - Close T1525

# Revision 1523 - j0zh94

@Fixed M107 zeroing error, added bullet. Zeroing may need further tweaking

# Revision 1522 - zeealex

[^] Improved M107 Visuals slightly

# Revision 1521 - da12thMonkey

^ Improved PVS27 fresnel+specular base values (further tweaking of _smdi and values may be needed)

# Revision 1520 - MistyRonin

^ Improvements of AN/PVS-27

# Revision 1519 - reyhard

^ added engine smoke destruction effect to Bradleys
@ fixed missing element at the bottom of the Bradley ramp
@ destruction selections for M2A3 BUSK III - close T1537
@ missing bipod proxy for M4 mstock variant - close T1541
@ destruction selections & missing rvmats for M113 - close T1536

# Revision 1518 - reyhard

@ wrong f22 canopy name - close T1538

# Revision 1517 - MistyRonin

+ Add few more variants of Ops-Core

# Revision 1516 - MistyRonin

^ Less brighter texture for the WMX

# Revision 1515 - gurdy

@ path corrections

# Revision 1514 - MistyRonin

^ Some more WMX tweaks.

# Revision 1513 - MistyRonin

@ Fix WMX assignation 

# Revision 1512 - MistyRonin

+ Add WMX and WMX & PEQ combo configs

# Revision 1511 - MistyRonin

+ Add WMX Flashlight

# Revision 1510 - MistyRonin

- Remove last handguns from US OCP & USMC squad leaders. - For realism sake

# Revision 1509 - zeealex

[*] reduced PVS27 texture size to 2048

# Revision 1508 - MistyRonin

^ More improvements to AN/PVS-27 variants

# Revision 1507 - zeealex

[*] rescaled PEQ 15 texture maps

# Revision 1506 - MistyRonin

^ AN/PVS-27 improvements

# Revision 1505 - MistyRonin

^ Make AN/PVS-27 scopes compatible with ASDG

# Revision 1504 - MistyRonin

+ First AN/PVS-27 config

# Revision 1503 - zeealex

[^] improved AN PEQ15 normal map and specular map

# Revision 1502 - Soul_Assassin

^ Ballistic data correct for soft headwear in VA - close T1529

# Revision 1501 - zeealex

[+] added AN PVS27 Raw files for config

# Revision 1500 - Kllrt

@ Fixed M9 firing pin safety bar movement

# Revision 1499 - Kllrt

@ SR-25 (Mk.11) has correct supressor position - fixes T1542

# Revision 1498 - Kllrt

@ Glock 17 has correct texture in LOD4

# Revision 1497 - Soul_Assassin

Upped required arma version to 1.58 - close T1532

# Revision 1496 - MistyRonin

+ ANVIS BC with mount test

# Revision 1495 - sykoCrazy

+ Ground suprresion version of the UH-1Y(2x19-tube rocket pod/2x miniguns)

# Revision 1494 - zeealex

[+] Added New AN PEQ15 model - May need readjustments to beam

# Revision 1493 - MistyRonin

@ Final fix for the Ops Core helmet 

# Revision 1492 - MistyRonin

@ Fix OpsCore shadows - 3rd try

# Revision 1491 - MistyRonin

+ Add ANVIS-9 US NVG config - The model is missing the mount, Zee is on it.

# Revision 1490 - MistyRonin

@ Fix opscore shadows - 2nd try

# Revision 1489 - MistyRonin

@ Fix Ops-core shadows - First Try

# Revision 1488 - MistyRonin

@ Fix old path in Ops-Core helmets

# Revision 1487 - gurdy

+ OD M113A3 light config textures

# Revision 1486 - sykoCrazy

@ Missing mag for empty weaponproxy

# Revision 1485 - MistyRonin

+ Add first batch of the new ops-core helmets

# Revision 1484 - MistyRonin

^ Update tan comtac headset texture

# Revision 1483 - zeealex

[^] improved SR-25 standard stock scale

# Revision 1482 - MistyRonin

@ Add missing semi colons to c_melb

# Revision 1481 - sykoCrazy



# Revision 1480 - sykoCrazy

+ Rocket proxies to AH-1/AH-64/UH-1Y models
+ Littlebird eden attributes(e.g.:changing nose decal;adding tail number)

# Revision 1479 - Soul_Assassin

Unburn Misty

# Revision 1478 - MistyRonin

@ 2nd try to fix the opscore files

# Revision 1477 - MistyRonin

@ Fixing attempt for the opscore files. 

# Revision 1476 - MistyRonin

+ Add new US Opscore models and textures. 

# Revision 1475 - gurdy

@ scope out SRAW

# Revision 1474 - reyhard

^ SMAW tweaks

# Revision 1473 - reyhard

^ improved smaw handling - removed userActions solution (yay!) and replaced it with dynamic addAction loaded upon launcher selection

# Revision 1472 - reyhard

^ tweaked M249 last res lod


# Revision 1471 - reyhard

^ tweaked AT-4 shadow
^ tweaked m590 pump action anim

# Revision 1470 - Soul_Assassin

@ Temporary switch off HiddenSelectionMaterials to prevent no material loadind on MARPAT-D MICH helmets

# Revision 1469 - Soul_Assassin

^ Improved SPCS shoulder weights

# Revision 1468 - zeealex

[^] fixed Arm clipping on Crye Gen 3

# Revision 1467 - reyhard

^ updated cfgPatches

# Revision 1466 - reyhard

^ added bradley BUSK groups

# Revision 1465 - MistyRonin

+ Add Black Merrells to G3 Black uniform

# Revision 1464 - sabre

[Textures] Added Black Merrels texture

# Revision 1463 - MistyRonin

- Scoped the Frog M81 uniform to 1, and linked the G3 M81 to it for retro-compatibility. - As the Frog M81 was meant as a placeholder of the G3 one

# Revision 1462 - sabre

[Textures] Added G3 in Black, Tan & Ranger Green

# Revision 1461 - MistyRonin

@ Correct G3 Multicam wrong texture path

# Revision 1460 - MistyRonin

+ Add G3 Uniform configs for plain variants
^ Improved SOCOM uniforms configs

# Revision 1459 - MistyRonin

+ Add G3 Uniform placeholder textures for plain variants

# Revision 1458 - MistyRonin

@ Missing display name for US Army Airborne Rifleman (light)

# Revision 1457 - reyhard

@ facepalm fix - spalling script didn't worked because I used wrong namespace
@ fixed diagnostic.exe uv source error messages for elcan, acog & m68cco

# Revision 1456 - sabre

[Textures] G3 MC small wrinkles shifted.

# Revision 1455 - sabre

[Textures] G3 MC and M81 first versions.

# Revision 1454 - MistyRonin

@ Fix wrong characters at the end of infantry_socom file. 

# Revision 1453 - MistyRonin

+ Add G3 M81 placeholder uniform 

# Revision 1452 - MistyRonin

+ Add US G3 placeholder M81 texture

# Revision 1451 - MistyRonin

+ Add US Army Airborne groups

# Revision 1450 - Soul_Assassin

Fixed SPCS pistol pouches

# Revision 1449 - Stagler

+Added Falcon-II (MC)

# Revision 1448 - Soul_Assassin

^ Adjusted FROG uniforms to fit better with SPCS

# Revision 1447 - Stagler

^Updated Falcon textures

# Revision 1446 - reyhard

@ fixed inheritance error

# Revision 1445 - gurdy

^ Altered base ACH configuration

# Revision 1444 - sabre

[Textures] US Army Camelbak v1

# Revision 1443 - Soul_Assassin

Fixed weighing issues on SPCS Camelbak - work on T46

# Revision 1442 - richardsd



# Revision 1441 - MistyRonin

^ Update US Army Airborne configs - 2nd batch
+ Add M107s painted with Leupold AI variants
^ Changed Rifleman (M590) for Breacher 
+ Added Breacher backpack

# Revision 1440 - da12thMonkey

+Added unique gear icons for MP7A1s, M8541A SSDS and Leupold 6.5-20x50mm

# Revision 1439 - reyhard

@ fixed door toggle action for unarmed M1025
^ tweaked M1025 doors FG & geometry - close T1491

# Revision 1438 - Soul_Assassin

^ Improved ACH lod switching

# Revision 1437 - MistyRonin

@ Correct faction issue with US Army UCP Airborne

# Revision 1436 - MistyRonin

+ Add first batch of US Army Airborne configs 
+ Add M62 tracer 20rnd mag 7.62
^ Updated US Stringtable.xml
^ Updated US Vehicleclasses & EditorSubcategories

# Revision 1435 - sykoCrazy

^ AH-64/AH-1/AH-6/UH-1 weapon proxies
^ Rockets, hellfire/rocket pods for USMC and Army helicopters
^ Littlebird rvmats and textures
@ AH-64 body rvmat to make it look a bit less like shiny plastic

# Revision 1434 - MistyRonin

@ Fix missing M113 desert textures

# Revision 1433 - Soul_Assassin

@ Fixed M109A6 being too front heavy - close T1477

# Revision 1432 - reyhard

^ 3den variables are no longer transmitted over net
+ added ability to decide whether doors should be left opened after dismount from M1025 series vehicles. doors provide cover & it's possible to fire through them if window is lowered
+ added some decals to M1025ies
@ fixed something - close T1478
^ added geometry to M1025 doors so it's possible to rest on opened ones

# Revision 1431 - da12thMonkey

^ Minor optimisation of M249 models: removed duplicated sight rail mesh in top res LODs (was adding 466 tris and visible z-fighting)

# Revision 1430 - Soul_Assassin

Tweaked G3 kneepad size.

# Revision 1429 - da12thMonkey

+ Added Premier Reticles gen 2 mildot modeloptics for M8541A SSDS
@ Corrected M8541A SSDS magnification to 3-15x

# Revision 1428 - reyhard

@ cap anim fix - close T1483

# Revision 1427 - MistyRonin

@ Correct M72A7 weight (to 3.5kg)

# Revision 1426 - MistyRonin

@ Set proper weight for M72A7 - It should be about a third of a M136 (2.5 vs 6.7kg)

# Revision 1425 - MistyRonin

+ M72A7 to Ammo crates
+ M72A7 Rifleman to USMC sub-factions
+ M72A7 as placeable object in Zeus
+ New strings into US Stringtable related to M72A7

# Revision 1424 - reyhard

^ LAW & AT4 can now be carried in backpack
@ LAW & AT4 is now reloaded properly
^ configured reload sound for at4.p3d
^ changed LAW inheritance
^ increased Javelin locking time

# Revision 1423 - Soul_Assassin

@ Fixed inverted FROG normals
@ Fixed missing selection in MICH 2000 MARPAT helmet
Finilized G3 - closes task T1480

# Revision 1422 - Soul_Assassin

+ Scoped SPCS back in, configged, made lods and Rifleman variant
+ Scoped G3 back in, re-proportioned legs, tweaked materials

# Revision 1421 - zeealex

[+] Added Gen 3 Gloves 
[+] Added .rvmat files (Gen3 and mechanix) 
[^] Improved Gen3 weighting
[^] Improved Oakley glove weighting on US marine V2 (transferrable to other models)

# Revision 1420 - richardsd

@ Fixed: Clipping issue - Fixes Ticket 1469
- Removed: All proxies, as per 1.56 update
+ added: Desert Textures WIP

# Revision 1419 - MistyRonin

+ Add MP7 to ammo crates and as a Zeus placeable object

# Revision 1418 - MistyRonin

^ Assign US DLC to MP7s

# Revision 1417 - sabre

[Textures] SPCS v1

# Revision 1416 - gurdy

@ spcs scaling

# Revision 1415 - Soul_Assassin

More MELB author stuff

# Revision 1414 - Soul_Assassin

Added DLC and author name to MELB

# Revision 1413 - MistyRonin

+ US G3 uniform materials

# Revision 1412 - MistyRonin

^ Few fixes & improvements to US troops classes

# Revision 1411 - reyhard

^ tweaks for L-159

# Revision 1410 - j0zh94

^ Updated m72_smdi.paa for Rail

# Revision 1409 - reyhard

^ another round of safe mode optimisation & bugfixing

# Revision 1408 - reyhard

^ safemode & acc combo script now properly deinitalize after embarking vehicles

# Revision 1407 - reyhard

^ proxies adjustments for L159

# Revision 1406 - Soul_Assassin

Attempt to fix MELB packing

# Revision 1405 - sykoCrazy

+ Littlebirds from MELB mod

# Revision 1404 - MistyRonin

^ Update US Stringtable

# Revision 1403 - Soul_Assassin

Scoped out G3 uniforms

# Revision 1402 - MistyRonin

^ Assign M8541A to USMC SR-25 AI rifle combos. 

# Revision 1401 - MistyRonin

^ Give proper USMC designation, M8541A SSDS, to "Premier" scope 

# Revision 1400 - reyhard

^ autotrack improvments 

# Revision 1399 - reyhard

@ Lead hotfix

# Revision 1398 - reyhard

@ small fixes to paradrop & loadout script

# Revision 1397 - Soul_Assassin

^ IOTV rescale and reposition to fit better with new proportions - fixes T1453
@ Fixed ACU missing patches and redid a bit the proportions - fixes T1430

# Revision 1396 - Soul_Assassin

@ modelSides[] fixed for all US uniforms - fixes T1470.

# Revision 1395 - sykoCrazy

@ Rocket pods positioning issue

# Revision 1394 - richardsd

@ Fixed: Door Issue on APK (Ticket 1450)
@ Fixed: Cargo Tex More Worn
@ Fixed: Turret Texture

# Revision 1393 - sykoCrazy

@ Proxies repositioned in AH-1 and AH-64

# Revision 1392 - sykoCrazy

@ Repositioned rocket pod proxies on AH-1Z

# Revision 1391 - sykoCrazy

@ Fixed length of M260(19 tube rocket launcher)
@ Proxy positions for rocket pods on AH-64
^ model and textures for LAU-61C/A(19 tube USMC rocket launcher)


# Revision 1390 - reyhard

^ hidden selections for G3 fix

# Revision 1389 - reyhard

^ assigned Merrells texture & rvmat

# Revision 1388 - sabre

[Textures] Merrells v1

# Revision 1387 - reyhard

^ tweaked AH-64 speed
@ fixed paradrop wp custom completion radius 

# Revision 1386 - reyhard

@ fixed M1025 unarmed ghost lod
^ improved paradrop script
+ added paradrop waypoint
@ m590 sounds not working
^ calibrated FCS calculations for M1069 HE rounds

# Revision 1385 - sykoCrazy

@ M261 model issue
^ Rocket pod textures
^ M299 Helllfire pod(added to AH-64 & AH-1)

# Revision 1384 - Soul_Assassin

Kick Jenkins into rebuild of a2port_air

# Revision 1383 - sykoCrazy

@ Wrong file path

# Revision 1382 - sykoCrazy

@ Further tweaks to UH-60 cyclic movement
^ M261(19 shot FFAR pod) model and texture

# Revision 1381 - sykoCrazy

@ UH-60 rotors are now properly set in the Shadow LOD
@ UH-60 rotor blur texture no longer has yellow stripes
@ UH-60 cyclic left/right animation is no longer inverted
^ AGM-114 model and texture (first test of air weapons port from MELB mod)

# Revision 1380 - MistyRonin

@ Fixing the HEMTT fix - Author macro was not defined

# Revision 1379 - MistyRonin

@ Trying to fix missing HEMTT names

# Revision 1378 - richardsd

+ Added HEMTT A4

# Revision 1377 - reyhard

@ fixed M109 ghost lod

# Revision 1376 - Bakerman

^ RHSUSF_fnc_firedSaclos now uses cursorObject command

# Revision 1375 - MistyRonin

@ Fixed wrong ammo for UMSC Recon M107 snipers

# Revision 1374 - MistyRonin

^ Updates & tweaks to US troop configs

# Revision 1373 - MistyRonin

^ Updated US Weapons AI

# Revision 1372 - reyhard

^ limited number distribution for ch-53

# Revision 1371 - Soul_Assassin

+ Rest of USMC number decals - close T1405

# Revision 1370 - gurdy

^ MARPAT covers

# Revision 1369 - reyhard

^ changed AFM on CH-53 to CH-49 based

# Revision 1368 - reyhard

^ reduced & defined main rotor center

# Revision 1367 - reyhard

@ M1 eden ammo loadout typos
@ Wrong back door selection in 2nd res lod & missing interior proxies in res lod 3 & 4 - close T1440

# Revision 1366 - MistyRonin

@ Fix wrong RG33 Army spawning in USMC groups

# Revision 1365 - reyhard

@ upon ejection from ejection seat another ejection seat was created
@ some .rpt errors connected with ejection seats & canopy
^ reduced M1 tanks max ammo to 36 rounds (since to get those extra 6 rounds special operation is required involving rotating turret to specific angle. that what's Damian saying at least :P)

# Revision 1364 - reyhard

^ changed color of mastersafe action

# Revision 1363 - reyhard

+ added master safemode switch to A-10, F-22, AH-64 & AH-1Z. There is shortcut for that user action on "User Action 13" key. T1267 probably can be closed since master safe closes all bays on F-22
^ added proper tailBladeCenter point to CH-53, attempt at fixing T1425
^ added High ROF mode to A-10 gau (sound is getting weird on low fps, need to investigate method mentioned in that post - https://forums.bistudio.com/topic/187965-fmod-in-arma-3/#entry2995526 )
^ some small tweaks to A-10 MFD

# Revision 1362 - gurdy

@ USMC hat rvmat

# Revision 1361 - Kllrt

Fixed M72A7 (used) levitation bug

# Revision 1360 - reyhard

^ remaked F22 mfd, gun is now aligned
^ added canopy anim to f22
+ added seat ejection to f22
^ changed canopy simulation
^ tweaked seat ejection script
^ healed soldiers broken wrists when holding US weapons + corrected finger positions on m14 & sr25 - close T1419

# Revision 1359 - reyhard

+ added seat ejection script to A10
+ added eden rearming system to M1 tanks
^ WIP work on TV Maverick
^ reproxified A10 weapons 
^ aligned AGM65 & ALQ131 to zero position
@ a10 hud properly aligned now
^ tweaked M1117 proxies - close T1411 & T1408
^ added A10 variant with six AGM65 missiles 
@ changed Car vehicle class
@ fixed ANPVS-7 missing head selection & made new shadow lods - close T1394

# Revision 1358 - MistyRonin

^ USMC troops tweaks 

# Revision 1357 - Stagler

[^] Tweaked opscore cover textures again slightly

# Revision 1356 - Stagler

[^] Improved FG and CB Opscore cover textures
[^] Standardised texture Opscore names
[+] Added Opscore Peltor no helmet cover variants

# Revision 1355 - gurdy

+ USMC Boonie hats and 8-point cap

# Revision 1354 - j0zh94

^ New m72_smdi 

# Revision 1353 - Kllrt

Fixed M72A7 sights animation + added SIDE proxy for laser

# Revision 1352 - Kllrt

Added M72A7 sight anim

# Revision 1351 - Kllrt

Fixed M72A7 fired model

# Revision 1350 - reyhard

@ fixed misplaced UH1Y gunner
^ some more eden integration
^ added ability to hide benches in c130 & ch47 for more cargo duties
@ fixed minigun sound - close T1356
^ added hidden selections to covered MICH helmets

# Revision 1349 - reyhard

^ ongoing eden integration
^ improved m1911 reload anim
+ added weapon safety system - default combo ctrl+f, can be changed or disabled completely in menu option. WIP
^ added safety anims on m1911, m249, m4, m16, m27, m107, m9 & m320
^ added M792 shell auto destruction after ~3km
^ added filter selection to uh60
^ added reslods to standalone m320
@ added missing mass in geometry lod for MP7, M32, M320 &  M1911

# Revision 1348 - MistyRonin

@ Fix super-duper capacity for M1911 mag

# Revision 1347 - reyhard

^ female voice has now proper preview sound in VA

# Revision 1346 - reyhard

@ added scripted workaround for AI not engaging with autocannon when laserLock = 1
@ fixed M9 holster position
^ improved script handling after loading game

# Revision 1345 - reyhard

@ m72 was missing components in geo (physic not werking) & firegeo
@ FINALL ATTEMPT TO SORT ALPHAS ON M113 TRACK TEXTURES
@ front IFF panel hiding 
+ added ability to specify if disposable launchers are thrown away automatically after changing weapon in rhs menu options (by default turned on)

# Revision 1344 - reyhard

@ fixed MP7 textures & animations
^ various performance improvements to weapon handling scripts

# Revision 1343 - Soul_Assassin

+ Added US flag and map marker.

# Revision 1342 - MistyRonin

@ Attempt to fix MP7 main texture issue

# Revision 1341 - MistyRonin

^ MP7 configs tweaks

# Revision 1340 - reyhard

@ fixed M240 muzzle flash - close T1383
+ added M240 hand anim handle
@ fixed M1a2 woodland spent cases eject pos - close T1380
^ announcer & radio chat didn't fired up with AFM & gauges visible
@ removed searchlight from UH1Y observer seat

# Revision 1339 - Bakerman

4.6x30mm ammo redux

# Revision 1338 - MistyRonin

^ 2nd batch of MP7 configs (new mags & ammo)

# Revision 1337 - MistyRonin

+ MP7 first config - issues expected

# Revision 1336 - MistyRonin

+ MP7 files - Configs will come later

# Revision 1335 - Stagler

[^] Improved Falcon Textures

# Revision 1334 - reyhard

^ changed 0.50 cal bmg mag names
^ configured mk211 mag
^ added mem eye points for m107
^ added magazine picture for m107 mags

# Revision 1333 - reyhard

@ M72 fixes

# Revision 1332 - Kllrt

M72A7: US soldiers can now see front sight

# Revision 1331 - Kllrt

M72A7: Not-fixed, but better handanim

# Revision 1330 - Kllrt

WIP M72A7 changes

# Revision 1329 - LAxemann

Changed: New M240 reload sound that fits the new animation

# Revision 1328 - reyhard

- removed repeatString & getRandomArElement functions from decals
@ CH53 couldn't start flying in 3den - added RTD center mem point & moved whole model by 2 meters in Y axis
+ added 3den attributes to M1, M113, M109 & CH-53
^ added res lods to M109

# Revision 1327 - Bakerman

.50cal ammo

# Revision 1326 - Kllrt

Fixed M72A7 mem points and model.cfg

# Revision 1325 - Bakerman

T379 M72A7 ammo

# Revision 1324 - j0zh94

^ Added more selections to M72 for animation

# Revision 1323 - reyhard

@ weapons string fix
+ added hidden selections to M113
^ improved wheel shadows for m113
^ removed front addon armour from vehicles which didn't have them in res lods
+ added hidden selections to M109 (wip work)

# Revision 1322 - zeealex

[+] Added LC M107 (scope 1) 

# Revision 1321 - zeealex

[+] added model config for crye gen 3

# Revision 1320 - MistyRonin

^ Add materials to M107 painted variants

# Revision 1319 - j0zh94

@ Fixed broken M72 Hand anim

# Revision 1318 - zeealex

[*] Fixed US army happy hour weights
[*] Fixed missing texture path on Crye Gen 3s 
[^] removed patch textures from US army shirt (as they are using Geometry)

# Revision 1317 - MistyRonin

@ Fix wrong Leupold assigned to US Army M107

# Revision 1316 - MistyRonin

+ Add US Army & USMC Snipers with M107
+ Test SF Guy with G3 Uniform

# Revision 1315 - MistyRonin

+ Add M107 painted first configs

# Revision 1314 - zeealex

[^] Replaced US Army soldiers with the reproportioned models 
[NOTE] 10th mountain and 101st AB are missing their 3D patches, will weight and add as soon as I get them. 

# Revision 1313 - zeealex

[+] Initial injection of Crye Gen 3 Gear (pending changes)
[+] Added M107 Desert and Woodland textures and .rvmats 

# Revision 1312 - zeealex

{+] Added shadowLOD to Premier scope
[+] Fixed .RvMat issue on premier scope



# Revision 1311 - Soul_Assassin

SPCS scoped out - close T1360

# Revision 1310 - reyhard

@ fixes to grip system - close T1370
@ forgot to upload tan version of grips

# Revision 1309 - zeealex

[^] changed premier scope glass. 
[^] Adjusted M107 specular level
[^] Adjusted optics proxy on M107

# Revision 1308 - reyhard

^ added tan TD & AFG grip
+ added hidden selections to M16 & M240
^ tweaked ironsight texture

# Revision 1307 - Bakerman

^ Simple HEAT simulation for vehicles without composite armour
^ SMAW muzzle synchronization now runs on each frame

# Revision 1306 - zeealex

[^] Adjusted body NOHQ

# Revision 1305 - zeealex

[^] Specular Map Tweaks

# Revision 1304 - zeealex

[^] Darkened Premier Scope Texture
{+] added glass .rvmat to premier scopes
[^] changed M107 optics proxy postition
[^] Darkened M107 texture

# Revision 1303 - reyhard

@ minor fixes to m107

# Revision 1302 - Bakerman

Reverted anm14 damage script.

# Revision 1301 - reyhard

^ wip werk on m107:
replaced deploypivot point with bipod mem point (since cfg was pointing to it)
configured muzzle flash
synced reload anims
animated barrel
tweaked hand anims
fixed texture errors
tweaked shadow
@ fixed empty gui error while using grips
^ tweaked 0.5 BMG & winmag inheritance (should inherit suppresion, shake & other effects from bis bullets)
@ fixed some missing strings
^ added inventory pics for grips

# Revision 1300 - reyhard

@ AI weapons fix for weapons with grips

# Revision 1299 - reyhard

@ fixed pistol m320 max zeroing
@ fixed m249 mags initSpeed
^ changed m240 reload anim
^ changed M107 reload anim
+ added ironsight anims to M4BII, MK18, M240, M249, SR25 & Mk14
@ fixed m249 rvmats wrong texture path

# Revision 1298 - j0zh94

^ Improved M107 bipod animations, still need some more tweaking

# Revision 1297 - MistyRonin

@Fixed M107 classname error.

# Revision 1296 - MistyRonin

+ Add Premier scope to ASDG compatibility list

# Revision 1295 - MistyRonin

+ Add first config for Premier Scope & little fixes in US weapons accessories.

# Revision 1294 - reyhard

@ CBA compatibility attempt - T1361

# Revision 1293 - zeealex

[+] Added Premier Scope Raw Files

# Revision 1292 - zeealex

[^] Improved Barrett M107 model and textures. 

# Revision 1291 - reyhard

^ added initSpeed modifier to rifles - magazines has inits speed zeroed for m16 20 inch barrel
^ removed ironsight zeroing from m2010
^ reorganized weapons
+ added ironsight anims for m4, m16 & m27iar
+ added gripod handling system (gripods handled as underbarrel attachment)
@ fixed SpeechVariants for m113 & M2 bradley
- removed bis MK48 files


# Revision 1290 - j0zh94

^ Added M72 rocket + LOD

# Revision 1289 - j0zh94

^ Added new M72 textures/downscaled, fixed minor LOD issue

# Revision 1288 - MistyRonin

@ Correct US Army Sniper UCP loadout. 

# Revision 1287 - j0zh94

@ Fixed M72 upscaling

# Revision 1286 - Kllrt

Updated M72A7 WIP

# Revision 1285 - reyhard

^ improved m1117 gunner periscopes
^ reenabled rg33 proxy retexturing
^ replaced modelToWorld with modelToWorldVisual
+ added M1117 gunner feed on commander station handling
^ zeroed m1117 reticle

# Revision 1284 - reyhard

+ added ramp binding
+ added 120mm & 40mm carnister ammo
@ fixed 120mm HEATs & HEDP configuration
^ tweaked tusk searchlight
^ added eden categories for placable items
^ added short mag description for mk19 grenades
^ work on m1117 sight zeroing
+ added periscopes for m1117
@ fixed tow lock

# Revision 1283 - reyhard

^ M1117 - added cargo shadow lods, cleaned up cfg, wip optics, added door anims, tweaked light effects, tweaked particles, fixed texture errors, etc
^ added ramp key bind
Olive texture are missing!

# Revision 1282 - Bakerman

^ AN-M14 TH3 creates thermite droplets
T1252

# Revision 1281 - Bakerman

T1354 iNil check for acc_combo.sqf

# Revision 1280 - Kllrt

Removed extra TGAs from M72 (oops!)

# Revision 1279 - Kllrt

WIP M72A7

# Revision 1278 - Bakerman

^ Decreased suppressor velocity increase to 1%

# Revision 1277 - Bakerman

@ Suppressors no longer modify hit values

# Revision 1276 - ballistic09

@ wrong uniform on USMC woodland troops

# Revision 1275 - zeealex

^ darkened M107 Textures

# Revision 1274 - zeealex

* model cfg take two

# Revision 1273 - zeealex

+ Added M107 Bipod Anim (needs tweaking but will suffice)

# Revision 1272 - reyhard

@ muffled sound fix (works with 1.56)

# Revision 1271 - reyhard

^ experimental turret locking tweak

# Revision 1270 - MistyRonin

^ Update of M107 config - Experimental too so far.

# Revision 1269 - MistyRonin

+ Add M107 - First experimental test of M107 config

# Revision 1268 - zeealex

+ Added M107 Box Mag Replacement P3D

# Revision 1267 - zeealex

+ Added M107 Raw Model Pending setup (to be looked at immediately)

# Revision 1266 - reyhard

readded vehicle classes

# Revision 1265 - MistyRonin

+ Add Eden Group Pictures to US groups

# Revision 1264 - MistyRonin

^ Update US stringtable

# Revision 1263 - MistyRonin

@ Fix US Airborne patches.

# Revision 1262 - Stagler

-Attempted to fix Opscore Cover shadow bug

# Revision 1261 - MistyRonin

^ Adapted US configs to Eden Categories.

# Revision 1260 - bek

^ Fixed USF rifles recoil. T648
note: there is still room for improvement, such as giving weapons with different grips different recoil values. 

# Revision 1259 - MistyRonin

^ USMC soldiers decided to adopt the Mk318 as their standard bullet - As their real life counterparts. 

# Revision 1258 - Bakerman

^ HEAT warhead simulation performance & reliability

# Revision 1257 - reyhard

@ removed dispersion from m256 player mode

# Revision 1256 - reyhard

@ corrected at4 rocket rvmat
^ added AI dispersion for M256 cannon

# Revision 1255 - Bakerman

SRAW projectiles shadow and mass

# Revision 1254 - MistyRonin

@ Fixed missing strings in US Stringtable

# Revision 1253 - gurdy



# Revision 1252 - MistyRonin

+ Added new M4, M16 & M27 as Zeus placeable, in VA and in crates

# Revision 1251 - MistyRonin

^ Updated US troops with new grips, and scoped 2 SPCS vests

# Revision 1250 - MistyRonin

^ Updated M4,M16 and M27 model.cfg

# Revision 1249 - gurdy

^ added fixed vests

# Revision 1248 - MistyRonin

+ Add first US TD configs

# Revision 1247 - gurdy

@ readded grippod and made new vertgrip variants

# Revision 1246 - reyhard

^ fcs tweaks

# Revision 1245 - gurdy

@ change OCP names to OEF-CP

# Revision 1244 - gurdy

^ replace grippods with tangodown foregrip

# Revision 1243 - MistyRonin

- Removed M1117 UN config from US Project

# Revision 1242 - reyhard

^ increased M1 reload time without loader
^ tweaked M1 optics visuals
^ tweaked lead scripts
^ added fire on move script for M1

# Revision 1241 - MistyRonin

^ Updated M1117 crew (still temporary) 

# Revision 1240 - MistyRonin

^ Updated M1117 load out

# Revision 1239 - MistyRonin

^ Improved M2 effects position on M1117

# Revision 1238 - Redphoenix

+ ZaslehKulas for M1117 40mm gun

# Revision 1237 - LAxemann

Decreased M2010 bolt action sound volume

# Revision 1236 - LAxemann

Tweaked: M2010 reload sound stereo

# Revision 1235 - LAxemann

Added: M2010 reload sound
Tweaked: M240 reload sound parameters (Distance + volume)

# Revision 1234 - LAxemann

Added: M2010 bolt action sound function in rhs_m2010_handler.sqf

# Revision 1233 - LAxemann

Added: M2010 bolt action sounds

# Revision 1232 - MistyRonin

@ Add missing path for US Troops

# Revision 1231 - MistyRonin

@ Fix US Zeus items duplication 

# Revision 1230 - MistyRonin

+ Add more Zeus placeable gear (US ACH, Opscore, LWH Helmets)

# Revision 1229 - reyhard

@ rear FFV turrets get in/out memory points were inverted

# Revision 1228 - reyhard

@ rpt errors fix

# Revision 1227 - MistyRonin

@ Fix more M1117 paths, change UN variant side and add AT4 to loadout. 

# Revision 1226 - Stagler

-Added new (better + non-BIS) texture for Ranger Green Falcon-II pack.
-Added (better + non-BIS) Coyote Falcon-II pack.

# Revision 1225 - reyhard

@ mod.cpp fix

# Revision 1224 - gurdy

@ fix M1117 rvmats

# Revision 1223 - MistyRonin

@ Update M1117 OD & Fix data file names

# Revision 1222 - MistyRonin

@ Add M1117 OD Config

# Revision 1221 - gurdy

^ M1117 textures and added OD variants

# Revision 1220 - MistyRonin

+ Add new mag variants to be used by the M1117

# Revision 1219 - MistyRonin

^ Updated M1117 weapons & mags loadout

# Revision 1218 - gurdy

@ fixed M1117 exterior Materials

# Revision 1217 - gurdy

^ M1117 changes + initial texture :)

# Revision 1216 - Redphoenix

^Fixed File Path for M1117 damagewheel.p3d proxy

# Revision 1215 - Redphoenix

+ M1117 physx.hpp
^ M1117 file paths
^ M1117 does now show up ingame

# Revision 1214 - MistyRonin

@ Fix M1117 bad file reference

# Revision 1213 - MistyRonin

@ Update M1117 config

# Revision 1212 - MistyRonin

+ Inject M1117 - There may be issues due to some issues I had with PBO Project

# Revision 1211 - reyhard

- disabled proxy retexturing till RC come out

# Revision 1210 - reyhard

@ fixed CCO68
@ fixed typo in vest cfg (missing semicolon, dunno how it binarized before)

# Revision 1209 - MistyRonin

@ Unhide CVCs

# Revision 1208 - MistyRonin

+ Add more M32 rounds

# Revision 1207 - MistyRonin

+ 2nd batch of SRAW configs

# Revision 1206 - MistyRonin

+ First SRAW Configs

# Revision 1205 - j0zh94

^ M9 Berretta no longer has grey background (which caused glowing at certain ranges)

# Revision 1204 - LAxemann

Tweaked: Closure volume levels, weapon mechanics are now audible again when firing (Who lowered their volume?)

# Revision 1203 - reyhard

^ added rg33 proxy camo selections

# Revision 1202 - reyhard

@ AT4 loading conflict with AFRF
@ max flying height for C130j

# Revision 1201 - gurdy

^ SRAW textures

# Revision 1200 - reyhard

@ fixed at4 inv errors
^ added open sight anim
^ tweaked reachambering sequence

# Revision 1199 - gurdy

+ SRAW Models

# Revision 1198 - reyhard

^ added prone m590 reload anims
@ fixed m1025 /w m2 ammo belt clipping 
@ fixed AGM missiles penetrator
^ increased GAU bullet timeToLive - now they have to actually hit the ground
@ fixed missing anim rpt error for M1A2

# Revision 1197 - reyhard

@ fixed hitpoints compilation errors
^ reenabled rechambering anim for m590
+ added vest, uniforms & other stuff as placeable editor items

# Revision 1196 - reyhard

@ M1 Fixes
@ C130J error message
^ changed CH53 ui picture
^ changed javeling holding anim
^ changed M27 IAR hand anim
^ changed M590A1 magazine reload anim

# Revision 1195 - gurdy

+ SRAW Model

# Revision 1194 - reyhard

@ fixed M2A3 BUSK III shadow lods hiding after destruction
@ fixed M2 muzzle flash visibility on M113
@ fixed M2010 rechambering anims quirks
^ configured engine hitpoints for c130
^ made new firegeometry for Ch53 with working cargo proxies
^ added glass destruction effect for Ch53
^ VG options for CH53
^ added pilot anims for ch53
+ added CH53 announcer for all US aircrafts
@ rear top hatch not animated in cargo & pilot lod
^ tweaked shell ejections mem points on m113
^ tweaked CBA compatibility
^ tweaked m113 3rd person view
^ tweaked m113 ammot loadout

# Revision 1193 - MistyRonin

@Fix missing string for M18 Green smoke can

# Revision 1192 - MistyRonin

@ Fixes in US Weapons & troops configs

# Revision 1191 - MistyRonin

@ Tune US Army & USMC troops configs

# Revision 1190 - Bakerman

^ Vest HitPoints

# Revision 1189 - Soul_Assassin

Version updated. USAF Jenkins revival.

# Revision 1188 - reyhard

@ M1025 fixes
^ added ability to hide A2 parts (antenna, BFT, CIP) through arsenal - might be useful for 3rd party mods that want to include earlier versions
+ added ability to hide IFF Panels to M1, M2 & M109
+ added standalone versions of Surefire flashlight & PEQ15 Top mounting
@ fixed M240 CAP ammo belt clipping
@ fixed SR25 inventory icons errors
^ tweaked M32 GL reload anims
^ tweaked SR25 hand anim
+ added stock hand anims for m16 & m4
^ added collimator effect to M2A1 standalone
^ removed inverted shadow effect from M68 CCO
^ tweaked FCS calculations on slope for M1 tanks
^ increased static Stinger reload time
@ fixed M113 M2 WD ammo belt clipping 
@ fixed M230 not engaging infantry
^ unified M2 Bradley armor values
^ added ability to kill turned in driver for M1, M2, M113
^ increased amount of magazines for M113
^ added visual era destruction effect for Bradleys
^ AI driver bailout from tank if rest of crew is killed & gun is destroyed
+ spalling script for M1, M2 & M113 (WIP)

# Revision 1187 - Bakerman

^ Armor compatibility, hitPart function now runs on ALL vehicles
T1210

# Revision 1186 - reyhard

@ missing component selections names in at & smaw geometries
@ zeroing text offset fix
^ added opscores to virtualAmmoBox.sqf

# Revision 1185 - Soul_Assassin

FATS Helmets: straps, res lods and shadow

# Revision 1184 - reyhard

^ rear sight hiding for SR25

# Revision 1183 - Bakerman

USF menu version

# Revision 1182 - reyhard



# Revision 1181 - reyhard

^ added missing static weapons in cfgPatches
^ static M2 magazine mount
^ added muzzle flash rotation to M27 IAR

# Revision 1180 - Pufu

try fix 001

# Revision 1179 - Bakerman

^ Barrel heat refraction only visible on high graphical settings

# Revision 1178 - Bakerman

@ MICH, ACH & LWH UI pictures

# Revision 1177 - MistyRonin

@ USMC Recon strings fix

# Revision 1176 - Bakerman

Fixed bowman picture paths

# Revision 1175 - Bakerman

@ Bowman UI picture

# Revision 1174 - Bakerman

@ ESS UI picture
@ Vest armor descriptions
@ SPC UI picture
Added opscore UI picture

# Revision 1173 - MistyRonin

+ Add USMC Recon Fast helmet units & groups

# Revision 1172 - gurdy

@ some texture paths

# Revision 1171 - MistyRonin

@Fixing wrong filename

# Revision 1170 - MistyRonin

@Add missing folder to FAST helmet paths. 

# Revision 1169 - MistyRonin

@Fix opscore files paths

# Revision 1168 - MistyRonin

@ 1st batch of fixes for US headgear

# Revision 1167 - MistyRonin

@Fixes to save the World (US headgear).

# Revision 1166 - gurdy

+ Initial commit of New Ops-Cores

# Revision 1165 - Bakerman

^ Stacked EventHandlers for all vehicles
T1202 USF

# Revision 1164 - reyhard

@ corrected m119 mass
^ added destruction rvmats to static weapons
@ fixed M1025A2 M2 & unarmed snorkel selections
@ fixed rhsusf_mag_15Rnd_9x19_JHP ammo count
@ added fix for GC camera

# Revision 1163 - Bakerman



# Revision 1162 - reyhard

@ fixed M1025 snorkels
@ fixed m16a4 grip anims

# Revision 1161 - reyhard

@ raven fixes

# Revision 1160 - reyhard

@ ACVC fixes
@ opscore fixes

# Revision 1159 - reyhard

@ fixed AFRF references on M68 CCO and ACOG pip

# Revision 1158 - Soul_Assassin

World unburn

# Revision 1157 - Soul_Assassin

HEMTT interim fix.

# Revision 1156 - Kllrt

Fixed: M249 UI icons

# Revision 1155 - reyhard

duh

# Revision 1154 - reyhard

@ fixed LWH spam - close T1166
^ tweaked pilot lod glass on M2 Bradley

# Revision 1153 - Bakerman

Static TOW SACLOS function call

# Revision 1152 - gurdy

^ Naming

# Revision 1151 - gurdy

@ more names

# Revision 1150 - gurdy

@ Names

# Revision 1149 - reyhard

@ deployed UN troops on m113 to cease z-fighting - close T1126

# Revision 1148 - reyhard

^ added laserlock for AH64 chaingun

# Revision 1147 - Bakerman

^ Limb damage

# Revision 1146 - MistyRonin

@Removed space between M1A1 and SA in the M1A1 group strings - Damian you better be able to sleep properly with that tonight, or I'll give you my 7.62mm somniferous "pill"

# Revision 1145 - MistyRonin

^ Updated M1A1 group names - So Damian can sleep properly tonight :P

# Revision 1144 - Soul_Assassin

F-22 finilized for release - close T1016

 - weapons and weapon doors
 - radio
 - hitpoints and firegeo

# Revision 1143 - sykoCrazy

FIXED Missing main rotor geometry, firegeo and geo phys LOD

# Revision 1142 - Bakerman

Fixed SMAW script error, thanks @reyhard. Close T1125

# Revision 1141 - reyhard

^ added nohq texture to 105mm casing model
^ optimizations and fixes to smaw user actions

# Revision 1140 - MistyRonin

@ Corrected faces issue. 

# Revision 1139 - MistyRonin

@More corrections in USMC & US Navy side

# Revision 1138 - MistyRonin

@Last tweaks for USMC Recon

# Revision 1137 - MistyRonin

@Tweaks for USMC Recon.

# Revision 1136 - MistyRonin

@Fix crossed classnames

# Revision 1135 - MistyRonin

@Fast fix of the fast fix


# Revision 1134 - MistyRonin

@ Fast-fix for groups

# Revision 1133 - sykoCrazy



# Revision 1132 - sykoCrazy



# Revision 1131 - Soul_Assassin

F-22 Work - prep for T1016 and T1068

# Revision 1130 - MistyRonin

+ Add USMC Div Recon groups

# Revision 1129 - MistyRonin

@Fix string of USMC Recon Rifleman light

# Revision 1128 - Bakerman

+ M259 smoke launcher
+ L8A3 smoke shell
Close T1122

# Revision 1127 - MistyRonin

+ First addition of USMC Div Recon - work on T1124

# Revision 1126 - Soul_Assassin

@ M109 now has FireGeometry and Hitpoints set up correctly.

# Revision 1125 - reyhard

@ missing m119 files

# Revision 1124 - reyhard

@ fixed light hitpoints on m113
+ added light textures for m113
@ fixed weapon muffling for rhs vehicles - close T1119
+ added slingload ability to m119 - close T1111
@ fixed some missing gunner/driver get in memory points here and there
^ increased ramp speed
+ added KIA anims for FFV m113 positions (seems to be ignored anyway...)
^ tweaked M1 tanks hitpoints
- removed door anims from c130 - close T846

# Revision 1123 - Bakerman

String consistency

# Revision 1122 - Bakerman

^ Weapon strings

# Revision 1121 - Redphoenix

^ improved M1911 textures

# Revision 1120 - Bakerman

New TOW model config entry

# Revision 1119 - Soul_Assassin

opscore uncovered normal fix - work on T1108

# Revision 1118 - Soul_Assassin

^ Added thermal maps to M113

# Revision 1117 - reyhard

@readded missing function - close T1121

# Revision 1116 - reyhard

@ infantry damage fix

# Revision 1115 - reyhard

M113:
+ added buoyancy named properity
+ added new gunner anims
+ enabled reload/revolving anims on m240 & mk19 variants
@ fixed driver proxies in pilot lod
@ fixed glass movement in res lods
@ sorted alphas in res lods
+ added rear ramp anim
+ added FFV rear hatch positions
+ added destruction rvmats

^ tweaked decal script to read decals from cfgs
@ fixed muffled sound bug
+ added peephole anim for new m136
+ added fire selector anim for SMAW
+ added SMAW to virtualAmmoBox


# Revision 1114 - Bakerman

Updated SMAW loadout fix

# Revision 1113 - Bakerman

Updated SMAW loadout fix

# Revision 1112 - Bakerman

T377 Zero sync, added optics, misc fixes

# Revision 1111 - Soul_Assassin

@ Hovering dump pouch fixed on some SPC variants.

# Revision 1110 - MistyRonin

+ Adding spotting rifle mags to USMC assaultman

# Revision 1109 - Soul_Assassin

Lesh tow values added to CH-53

# Revision 1108 - Soul_Assassin

+ Added compatibility with Lesh's Tow Mod

# Revision 1107 - Bakerman

Added temporary weapon tails

# Revision 1106 - MistyRonin

@ Switched static TOW & HMGs to static category - as requested

# Revision 1105 - Redphoenix

^fixed shadowLOD bugs for several M16s/M4A1 - close T1112

# Revision 1104 - MistyRonin

@Fast fix to allow build

# Revision 1103 - gurdy

^ Naming convention change

# Revision 1102 - gurdy

@ small formatting corrections


# Revision 1101 - MistyRonin

@ Switch US statics to artillery. 

# Revision 1100 - gurdy

@ CH-53E Name

# Revision 1099 - gurdy

^ US Static weapon names


# Revision 1098 - Bakerman

T965 SPC upped to level 4 protection

# Revision 1097 - Bakerman

T377 SMAW loadout fix for realsies

# Revision 1096 - MistyRonin

@Test2: Add init line to assaultman to see if it can use the weapon.

# Revision 1095 - Bakerman

T377 SMAW loadout fix

# Revision 1094 - Bakerman

T377 SMAW sfx

# Revision 1093 - MistyRonin

@ Fix wrong soldiers in US static weapons & test fix for SMAW assaultmen.

# Revision 1092 - Bakerman

T377 SMAW script improved

# Revision 1091 - Bakerman

T965 USF armor definitions

# Revision 1090 - reyhard

@ fixed m113 commander slot in editor
+ added spent catridge script for m119
^ tweaks to static weapons

# Revision 1089 - MistyRonin

+ Adding USMC Assaultmen, additionally adding the SMAW to Zeus placeable and in non virtual ammo crates

# Revision 1088 - Bakerman

T377 SMAW green added to ui function

# Revision 1087 - Bakerman

T377 Removed pointer to missing sfx

# Revision 1086 - RichardsD

@ Re-scaled interior so there are no slight misalignmnets
@ Re-UV'ed the M978 so the rear is not stretched anymore
+ Ammo variant added

# Revision 1085 - Bakerman

T377 SMAW Fixes

# Revision 1084 - Bakerman

MICH2000 hitpoint armor

# Revision 1083 - Soul_Assassin

F-22 texture, material and performance updates. Work on T1016

# Revision 1082 - LAxemann

Tweaked: Added an isty bitsy bit of bass to the M4s

# Revision 1081 - Kllrt

Added: WIP SMAW

# Revision 1080 - reyhard

+ initial commit of US static weapons
@ F22 fixes
@ fixed potential c130 explosion during paradrop - close T745

# Revision 1079 - Bakerman

T965 USAF minor edits

# Revision 1078 - j0zh94

Moved M9 slightly higher to better fit US Army units

# Revision 1077 - Soul_Assassin

World fire put off

# Revision 1076 - Bakerman

M113 model.cfg fixed again

# Revision 1075 - Bakerman

Fixed M113  model.cfg bones

# Revision 1074 - Kllrt

Moved M136 files

# Revision 1073 - Kllrt

Added: BlackPixxel's M136, missing file

# Revision 1072 - Kllrt

Added: BlackPixxel's M136

# Revision 1071 - Kllrt

Fixed: Double semicolon in M27 model.cfg

# Revision 1070 - Soul_Assassin

@ Magnified scope ranging (Mildot/ELCAN/H59) - T1067
^ Leupold Mk4 Spotting scope uses H59 an can now be properly used.

# Revision 1069 - Bakerman

T1087 Fixed galix shells

# Revision 1068 - Soul_Assassin

Color touchup of CH-53 colors
CH-53 hidden selections added

# Revision 1067 - Soul_Assassin

@ M113 M2 reload feed cover animation - close T1088
^ M113 M2 ammo belt clipping in first person

# Revision 1066 - Redphoenix

^ maxSpeed for M1A2 - close T1094
- auto-brake for M1 tanks

# Revision 1065 - gurdy

+ New tow missile moddels

# Revision 1064 - Soul_Assassin

@ Fixed unarmed M113 FFV proxy placement in lods - close T957

# Revision 1063 - Soul_Assassin

More huhmvee lod issues fixed

# Revision 1062 - reyhard

@ fixed M109 commander FFV position
+ added travel lock to M109
+ added reload anim for pistol version of m320 - close T364
+ added proper reload animations for m203 & m320
^ texture sorting for m4
+ added hidden selections for M4
@ fixed M27 IAR full auto sound
+ added new hitpoints for US vests & helmets

# Revision 1061 - Soul_Assassin

@ M1025 LOD switching issues - T949

# Revision 1060 - Soul_Assassin

CH-53 texture updates and decals

# Revision 1059 - j0zh94

Reworked model + textures

# Revision 1058 - reyhard

^ ch53 tweaks

# Revision 1057 - Soul_Assassin

MICH helmet fixes - close T1077

# Revision 1056 - Redphoenix

- removed HEMTT A2 close T1074

# Revision 1055 - reyhard

+ added new turn limits for M1 tanks
^ tweaked armor structural for transport helis - close T1064

# Revision 1054 - gurdy

^ Bradley textures with correct camo colors

# Revision 1053 - Soul_Assassin

Ch-53 texture tweaking.

# Revision 1052 - Soul_Assassin

Ch-53 texture update

# Revision 1051 - Bakerman

^ Flare launcher modes

# Revision 1050 - MistyRonin

@Fixed Abrams loadouts - Close T971

# Revision 1049 - MistyRonin

@ Fixes in USMC configs & M240 mags

# Revision 1048 - Redphoenix

^fixed wrong magazine model for USF smoke grenades

# Revision 1047 - MistyRonin

@ Switch 3d model in M240 M62 bullets

# Revision 1046 - Soul_Assassin

Bringing out of dangerzone

# Revision 1045 - Soul_Assassin

Attempt to restart Jenkins

# Revision 1044 - Kllrt

Added: F22 - heavy WIP

# Revision 1043 - Kllrt

Fixed: CH53 Pilot position and sound path bug

# Revision 1042 - gurdy

@ Opscorestuffz

# Revision 1041 - Redphoenix

^ triangulated M978A4 fuel tank to get rid of the mesh error

# Revision 1040 - Kllrt

Added: Orange tracer for 5.56x45 (w/ sample ammo and mag)

# Revision 1039 - Kllrt

Fixed wrong path on M4A1_BlockII_M203

# Revision 1038 - j0zh94

Slight fix of M9's textures to remove LOD issue

# Revision 1037 - Kllrt

Fixed: CH53 leftover from CUP namespace

# Revision 1036 - MistyRonin

@Second test tweaks for the M27.

# Revision 1035 - MistyRonin

@First test tweaks for the M27 

# Revision 1034 - MistyRonin

@ adding missing code - that's why its bad to code when you haven't slept :P

# Revision 1033 - MistyRonin

@ Adding missing semicolon in CH53 config.

# Revision 1032 - MistyRonin

@ Switch CH53 to USMC factions

# Revision 1031 - Redphoenix

-removed stray vert from all HEMTTs

# Revision 1030 - Kllrt

Injected CH53 v2 (forgot some files sorry)

# Revision 1029 - Kllrt

Injected CH53E

# Revision 1028 - Redphoenix

^Improved ShadowLOD
^Fixed pathing for models for all HEMMTs
^Fixed some minor mishaps

# Revision 1027 - RichardsD

+ HEMTT A4 Model.CFG
^ Memory LOD points

# Revision 1026 - RichardsD

+ HEMTT A4 Strings

# Revision 1025 - RichardsD



# Revision 1024 - Soul_Assassin

CH-53 folders made

# Revision 1023 - MistyRonin

+ Add M9 handgun to US Troops (Army & USMC)

# Revision 1022 - gurdy

+ Added Coyote and Woodland DUKE Antennae textures

# Revision 1021 - gurdy

+ Improved Opscore test

# Revision 1020 - j0zh94

Fixed UI image for M9 Beretta

# Revision 1019 - Redphoenix

+M9 and M9 mags to VAS

# Revision 1018 - j0zh94

Injected M9 Beretta + 2x 15rnd Magazines

# Revision 1017 - Redphoenix

^flipped direction of icon_ch47f_ca.paa - close T1059

# Revision 1016 - Redphoenix

^small spelling mistakes in cfgHints.hpp - T1058

# Revision 1015 - Redphoenix

+shadow for AN/PEQ-15/M952V - close T1056

# Revision 1014 - Redphoenix

^40mm smoke rounds now use the correct 40mm slug model when fired - close T1055

# Revision 1013 - Redphoenix

@ correct ammo type for M249 magazines - close T1053
+ Interim M240 magazines
- removed ability to launch vanilla 3GL magazines

# Revision 1012 - Bakerman

Config entry for galix shell

# Revision 1011 - reyhard

@ fixed C130 ramp anims not visible from cargo lod
^ uploaded Kimi fixed HMD
@ fixed C130 turret inheritance 

# Revision 1010 - gurdy

+ Galix Projectile

# Revision 1009 - Soul_Assassin

Alternative bare MICHs now have Army style headsets for MARSOC - closes task T1038

# Revision 1008 - Redphoenix

+ rhsusf_infantry2 

# Revision 1007 - Redphoenix

-removed more animation frames to decrease file size for M4 variants

# Revision 1006 - Redphoenix

+first file cleanup of rhsusf_weapons
^Alpha Issue for ACOG family - close T1051

# Revision 1005 - Redphoenix

firest file cleanup of rhsusf_weapons2

# Revision 1004 - Redphoenix

.removed unnecessary keyframes from ach_base.p3d

# Revision 1003 - Soul_Assassin

+ Added more MICH helmets - work on T1038
@ Fixed lod color issues with ballistic glasses

# Revision 1002 - Redphoenix

reverting AT4 texture commit

# Revision 1001 - Redphoenix

@removed old lenses on all ACOG variants and replaced with shiny new ones - close T1047

# Revision 1000 - Bakerman

T924 Now with blinding flare and flesh melting fire

# Revision 999 - Soul_Assassin

@ UH-60M correct crew classes.

# Revision 998 - Bakerman

Fixed version

# Revision 997 - Bakerman

T924 Made effects 1000% more realistic

# Revision 996 - Bakerman

TF47 M136 & SMAW

# Revision 995 - MistyRonin

+ M27 troops - related to the last commit

# Revision 994 - MistyRonin

+ Added M27 to USMC troops & crates

# Revision 993 - Soul_Assassin

Finalized M27 - closes task T343

# Revision 992 - Bakerman

^ New AN-M14 TH3 effects
T924

# Revision 991 - Bakerman

Removed unwanted line in script

# Revision 990 - Bakerman

T879 Renamed M113 smoke selections

# Revision 989 - zeealex

+ Added wearable ESS goggles

# Revision 988 - Redphoenix

^M320GL now has fireselector set to F instead of S - close T956

# Revision 987 - Redphoenix

@top proxy in viewpilot now aligned with res0 LOD for M16A4_ris.p3d

# Revision 986 - Bakerman

Initial commit for M113 smoke launchers

# Revision 985 - Redphoenix

+ShadowLOD M27 IAR

# Revision 984 - Redphoenix

@ Silencer placement on M27
@ Laser placement on M27
+ FireGEO LOD on M27

# Revision 983 - Redphoenix

+ M27 IAR

# Revision 982 - Soul_Assassin

+ Added new SPC Camelbak model

# Revision 981 - MistyRonin

+ Adding Glock 17 as placeable item in Zeus.

# Revision 980 - reyhard

^ changed hitpoints to 1.52 ver + cfg should support changes to hitpoint class made in 1.54

# Revision 979 - reyhard

^ reenabled bolt action for m2010 - works with bipods now. hold fire button in order to halt rechambering animation
+ try on rechamber action for m590 :D

# Revision 978 - reyhard

@ workaround for directionStabilization quirks
@ fixed glass textures submarine like view
@ fixed ramp selection on m2a3
^ added custom pip handler for m113
^ tweaked m113 driver anim

# Revision 977 - reyhard

+ added magic antirollbar parametrs to US tracked vehicles in order to prevent silly AI flips

# Revision 976 - reyhard

@ fixes to M1 FCS code

# Revision 975 - Soul_Assassin

^ 82nd and Mountain patches lowered not to float over the uniform.

# Revision 974 - reyhard

+ added auto target track for UH1Y
^ M320 is no longer visible in holster slot
^ tweaked m1911 holster scale & holster offset point to fit (for now) bis vests
^ some tweaks to FCS code

# Revision 973 - Soul_Assassin

^ Added missing Author tags

# Revision 972 - Soul_Assassin

@ Disabled attachments on M32 GL

# Revision 971 - Pufu

@ fixed descriptionshort for 7.62x51 m240 100 rounds belt mags

# Revision 970 - Pufu

@ fixed duplicates Stringtable - close t980

# Revision 969 - Soul_Assassin

^ Javelin can lock on air targets

# Revision 968 - reyhard

@ fixed some heat refractions effects for MG's
^ tweaked UH1Y hud
@ fixed missing rvmat for ah1z

# Revision 967 - Soul_Assassin

@ Fixed FROG first-person hand position

# Revision 966 - reyhard

+ added usePiP=1; param for UH1Y Observer - should prevent strange head twisting
@ fixed some UH1Y flir screen errors

# Revision 965 - reyhard

@ fixed Bradley door handler (doors were closing even player used 'open ramp' action)
^ tweaked/added ui icons for uniforms
+ added door handling script for c130 - potential fix for T846
@ changed IR lock for TOW launcher since without that, AI refuse to engage enemies
^ tweaked mass of 6rnd grenade packs
^ tweaked initSpeed of m576 buckshot - should fix T862 (yet, maybe airfriction need some tweaks)
+ added M1A2SEPv2 TUSK II groups - close T930
@ fixed desert m6a2 in woodland tank groups
@ fixed M1025 destruction from 12.7 rounds
@ fixed FFAR ballistic - close T842

# Revision 964 - reyhard

@ fixed some "Error compiling '0.5 * (HitEngine1 + HitEngine2)' in 'HitEngine1'" rpt errors
@ fixed IK curve rpt errors
^ changed (and sometimes added) vehicles ui pictures in a3 style

# Revision 964 - reyhard

@ fixed some "Error compiling '0.5 * (HitEngine1 + HitEngine2)' in 'HitEngine1'" rpt errors
@ fixed IK curve rpt errors
^ changed (and sometimes added) vehicles ui pictures in a3 style

# Revision 963 - reyhard

@ fixed bradley wheels dustpos
^ tweaked m113 cfgPatches
^ tweaked collimator effect on m68cco & pip acog

# Revision 962 - reyhard

triggering weapons rebuild

# Revision 961 - reyhard

+ added new collimator effect to m68cco & m552 eotech
@ fixed minefield module

# Revision 960 - reyhard

@ fixed m107 popup error

# Revision 959 - MistyRonin

@ Update the US D & WD groups

# Revision 958 - Soul_Assassin

Cleanup

# Revision 957 - Redphoenix

@ Stringtable.xml Encoding set back to UTF-8
@ removed duplicate strings to clean RPT
@ removed duplicate key entries to prevent Stringforge from not opening Stringtable.xml
deleted d.txt - WTF was that even for?

# Revision 956 - USSRsniper

Fixed M1025 M2 muzzle flash

# Revision 955 - Bakerman

@ rhsusf_main script paths

# Revision 954 - USSRsniper

Fixes static M2 effects (muzzle smoke and chain links), and other vehicles that use M2 - fixes T950

# Revision 953 - USSRsniper

T950 - Fixed effects on static M2 machine gun

# Revision 952 - MistyRonin

@ Hide FR & MARSOC groups.

# Revision 951 - Soul_Assassin

[tag] Real first commit of 0.4

# Revision 950 - Soul_Assassin

@ Fixed M1A2 driver PiP

# Revision 949 - Soul_Assassin

@ Some major M113 model and texture fixes

# Revision 948 - Bakerman

Menu version set to 0.3.9.1

# Revision 947 - Bakerman

Reverted usf troops randomization

# Revision 946 - Bakerman

No random headgear for usf

# Revision 945 - Redphoenix

^ Mk262 and Mk318 now have red tracers - close T939
^ added missing quotes for M240 mags - close T937
+ added improved ACOG with different lense textures for visual improvement

# Revision 944 - Soul_Assassin

[tag] first commit of 0.4.0

# Revision 943 - Bakerman

Fixed M113 D M240 gun sights

# Revision 942 - Bakerman

Fixed M113 D M240 gun cloud

# Revision 941 - Redphoenix

^ fully fixed M113 unarmed FFV

# Revision 940 - Redphoenix

^ fixed M113 Unarmed FFV

# Revision 939 - Redphoenix

^fixed rhs_logobig_ca.paa

# Revision 938 - Bakerman

T934 one last time

# Revision 937 - Bakerman

T934 another hint update

# Revision 936 - Bakerman

T934 hint update

# Revision 935 - Bakerman

T934 another try at the logo

# Revision 934 - Bakerman

T934 logo

# Revision 933 - Bakerman

T934 USF few that I missed

# Revision 932 - Bakerman

T934 Logo

# Revision 931 - Bakerman

T934 USF

# Revision 930 - Soul_Assassin

Switch off thermals for M113 for now

# Revision 929 - Bakerman

Set M113A3 smoke to launch from hull

# Revision 928 - gurdy

@ Fixed Material on hatch

# Revision 927 - gurdy

^ Added PIP to the rest of the M113s

# Revision 926 - gurdy

+ M113A3 Pilot PIP setup

# Revision 925 - MistyRonin

^ Last tweak on M240 tracers. 

# Revision 924 - sykoCrazy



# Revision 923 - MistyRonin

^ Improved M240 tracer times - to make them more realistic

# Revision 922 - Bakerman

^ Game options button uses profile colour

# Revision 921 - Bakerman

^ Helicopter 20 & 30mm shell lifetime 

# Revision 920 - gurdy

^ Removed honeycomb from M68

# Revision 919 - gurdy

@ Fixed M81 pilot lod..

# Revision 918 - gurdy

@ M81 glove hidden sel fix

# Revision 917 - gurdy

@ Replaced M81 FROG's hands

# Revision 916 - gurdy

@ Fixed IAR grenade straps

# Revision 915 - gurdy

@ LWH texture padding

# Revision 914 - Soul_Assassin

@ Fixed M1025 fording depth (different for snorkel and no snorkel) - fixes T918
@ Snorkel visible again on appropriate M1025 versions - fixes T917

# Revision 913 - Soul_Assassin

Small option screen text fixes

# Revision 912 - Redphoenix

^ debloated M32 model.cfg
+ added 6 grenades to M32 for better look
@ M32 zeroing memory points
@ M32 ShadowLOD has now less vertices while retaining the same look
close T357

# Revision 911 - Soul_Assassin

M32 zeroing (as best as I can do) can hit up to 300m, further is anyones guess)

# Revision 910 - Soul_Assassin

SPC weighing and lods
scoped SPCS out
Added SPC variants to VA

# Revision 909 - gurdy

@ Mk. 64 alphas

# Revision 908 - gurdy

+ RG-33 and FMTV pictures

# Revision 907 - Bakerman

^ Heat refraction for vehicle machine guns

# Revision 906 - gurdy

@ More M1025 Fixes

# Revision 905 - Redphoenix

@M32 animations
^M32 memory point positioning
@M2A1 sight fixes

# Revision 904 - gurdy

@ Fixed M1097 antennae

# Revision 903 - gurdy

@ M113A3 M240 lod fix

# Revision 902 - gurdy

@ Hide M4A1+

# Revision 901 - Bakerman

Main now require 1.50

# Revision 900 - Bakerman

@ Minefields

# Revision 899 - Bakerman

Few more HEAT improvements

# Revision 898 - gurdy

@ More M113A3 interior testing

# Revision 897 - gurdy

+ M113A3 Interior LOD tests

# Revision 896 - gurdy

@ LOD material fix

# Revision 895 - gurdy

^ Initial M113A3 Main res LOD deletions

# Revision 894 - gurdy

@ Removed holo from M240

# Revision 893 - gurdy

^ Improved M113A3 proxy LODs

# Revision 892 - LAxemann

Added: Config for Hellfire, Sidewinder and FFAR sounds

# Revision 891 - gurdy

@ M113 LOD test 01

# Revision 890 - Bakerman

^ HEAT simulation

# Revision 889 - Bakerman

@ FFAR sound loop

# Revision 888 - LAxemann

Added: New M136 sounds with tail system

# Revision 887 - Redphoenix

+ monolithic M32 launcher
@ M2A1 sight texture improved

# Revision 886 - Bakerman

M109 sound configs
^ M109 turret traverse speed

# Revision 885 - LAxemann

Adjusted: Javelin and M136 audible range
Added: Prepared vehicle rocket pod sounds

# Revision 884 - LAxemann

Added: New AH-1 Interior sounds
Added: AH-1 distance sounds

# Revision 883 - LAxemann

Added: M197 sounds
Added: m197 sound config
Added: 155mm sounds (not yet used)
Added: UH60 sounds
Added: UH60 distance sound

# Revision 882 - LAxemann

Changed: UH60 sound configs now point to rhsusf_sounds
Added: UH60 distance sound config

# Revision 881 - gurdy

^ SPCS scale

# Revision 880 - gurdy

@ M4A1 camo visibility????

# Revision 879 - gurdy

@ Made SPCS public for testing

# Revision 878 - gurdy

+ Added camo M4s to virtual ammo box

# Revision 877 - gurdy

@ M4A1s visible

# Revision 876 - gurdy

+ Added new SPCS for texture testing

# Revision 875 - MistyRonin

+ Add realistic bullet and mags to the M240 - M993 hidden for retrocompatibility tho in real life its not used in the m240

# Revision 874 - gurdy

@ M4A1 Hidden Sels

# Revision 873 - gurdy

+ Camo M4A1

# Revision 872 - gurdy

@ Fixed antennae selection

# Revision 871 - gurdy

@M1025 Hidden selections

# Revision 870 - gurdy

^ M1025 textures

# Revision 869 - gurdy

^ SPC Tweaks

# Revision 868 - MistyRonin

@Fix in Stinger missile lock system.

# Revision 867 - LAxemann

Tweaked: M4 closure volume

# Revision 866 - LAxemann

Added: All new M4 sounds 

# Revision 865 - LAxemann

Added: Missing M16 forest tail samples

# Revision 864 - LAxemann

Added: M2 mechanic sounds
Added: M134 Minigun servo sounds
Tweaked: Volumes

# Revision 863 - Bakerman

T909 minor script updates

# Revision 862 - Bakerman

@ FCS target lead
+ Option to disable/enable FCS target lead
T909 M1 target lead fixed

# Revision 861 - LAxemann

Added: All new M249 sounds. Yum.

# Revision 860 - LAxemann

Added: New M16 sounds
Fixed: Volume rebalance of almost all US handheld weapons
Fixed: Audible distance of most weapons increased to fit the current A3 standard


# Revision 859 - MistyRonin

@ Tweaked USMC weapon loadouts - per request

# Revision 858 - gurdy

@ Battlebelt clipping

# Revision 857 - MistyRonin

@ Fixes in USMC config - to allow Jenkins to work

# Revision 856 - MistyRonin

@Add new vests to USMC troops.

# Revision 855 - gurdy

+ Added SPC variants

# Revision 854 - gurdy

+ A2 Propper Camelback

# Revision 853 - MistyRonin

+ Adding missing ammo to US launchers crates

# Revision 852 - Soul_Assassin

Added mass to pallet

# Revision 851 - Soul_Assassin

Gear 2 for SPC complete

# Revision 850 - Bakerman

T868 APS script update

# Revision 849 - Bakerman

T868 General script improvements for USAF

# Revision 848 - MistyRonin

@ Last fixes to US Ammo & Weapons crates

# Revision 847 - MistyRonin

@ Fixes to US Ammo & Weapons crates

# Revision 846 - MistyRonin

+ Add missing Glock mags (also to VA)

# Revision 845 - MistyRonin

+ US Weapon crates

# Revision 844 - Redphoenix

^ ShadowLOD fix for US Supply Crate

# Revision 843 - Redphoenix

+ Test ShadowLOD 1000

# Revision 842 - Redphoenix

+ propper US Supply Crate

# Revision 841 - gurdy

^ LWH textures

# Revision 840 - gurdy

@ LWH textures

# Revision 839 - Redphoenix

^ Arma 3 will now use "RedHammerStudios" as pbo author in rpt - AFRF
+ added missing $PBOPREFIX$

# Revision 838 - Redphoenix

@ M1025 Windows should now have less glare - close T776

# Revision 837 - Redphoenix

@ M1 Abrams series should now create dust particles on the propper places 

# Revision 836 - Redphoenix

@ M1 Abrams now consumes fuel - close T894
+ M1 Abrams Engine Stop sounds - close T880
^ M1 Abrams now uses the right sounds in the right place^
@ Adjusted M1 Abrams Sound levels

# Revision 835 - Redphoenix

^ M1911 Texture & RVmat update
^ Moved eye mem point for M1911

# Revision 834 - gurdy

^ SPC crotch flap

# Revision 833 - MistyRonin

@Fixing old US Army faction references

# Revision 832 - Soul_Assassin

M113 M2 desert lod fixes

# Revision 831 - MistyRonin

@ Fixing faction of USMC (LAR) Desert. 

# Revision 830 - MistyRonin

@ Little corrections on the USMC faction configs.

# Revision 829 - Soul_Assassin

Added lods to desert M113 w M2

# Revision 828 - Redphoenix

@ M1 Abrams fuel consumption - NEEDS TESTING & TWEAKING

# Revision 827 - gurdy

^ Improved SPC crotchflap texture

# Revision 826 - Soul_Assassin

^ Updated mod logo

# Revision 825 - gurdy

@ Added test crotchflap to spc rifleman

# Revision 824 - gurdy

@ Removed camelback from spc test

# Revision 823 - gurdy

@ Revert IOTV Rifleman to old model

# Revision 822 - LAxemann

Added: M32 sounds

# Revision 821 - LAxemann

Changed: Drastically decreased compression on the M2. The punch is back!

# Revision 820 - LAxemann

Changed: New M240 sounds

# Revision 819 - Redphoenix

^ upgraded M1025 series tire armor - close T854

# Revision 818 - Soul_Assassin

Darkened SPC pouch textures

# Revision 817 - MistyRonin

@Fix of wrong faction issue for USMC (LAR)

# Revision 816 - MistyRonin

+ Adding missing files

# Revision 815 - MistyRonin

@ Updated USMC configs 

# Revision 814 - Soul_Assassin

SPC Texture fix

# Revision 813 - Soul_Assassin

First pass SPC gear 1 texture

# Revision 812 - Bakerman

@ M249 sounds
@ M18 hidden selections

# Revision 811 - Redphoenix

^final M1025 cockpit gauges improvement - close T728

# Revision 810 - Redphoenix

^M1025 cockpit gauge animation T728

# Revision 809 - gurdy

@ Another MGO fix...

# Revision 808 - gurdy

@ M145 MGO ARD fix

# Revision 807 - gurdy

+ Smoke Grenade Setup for M113A3

# Revision 806 - gurdy

+ M150 MGO (ARD)

# Revision 805 - gurdy

@ ACOG RVMAT

# Revision 804 - gurdy

@ Elcan Scale

# Revision 803 - gurdy

^ ACOG FP appearance 

# Revision 802 - Soul_Assassin

Fixed M32 inventory icon - close T891

# Revision 801 - Soul_Assassin

Fixed Frog hand placement - close T888

# Revision 800 - Soul_Assassin

Fix M2A1 position - Close T886
Fix wrong texture assignmnet on Eotech 

# Revision 799 - Bakerman

T868 Corrected tiny script omission

# Revision 798 - Bakerman

T868 firedSaclos made compatible with AI gunners

# Revision 797 - Bakerman

T868 TOW atgm marked as SACLOS

# Revision 796 - MistyRonin

@Solved Zeus error message - Close T887

# Revision 795 - Bakerman

^ Zues compatibility for weapon fire camera shake

# Revision 794 - Bakerman

Build test

# Revision 793 - Soul_Assassin

Fix @MistyRonin booboo

# Revision 792 - MistyRonin

@ Updated stringtable and factions - Few optimizations for a future commit

# Revision 791 - sykoCrazy

Gravity geo boxes "component" selection removed to avoid ingame collision

# Revision 790 - sykoCrazy

Gravity geo boxes "component" selection removed to avoid ingame collision

# Revision 789 - Bakerman

^ Updated CE penetration & protection script
Also fixed a bunch of errors

# Revision 788 - Soul_Assassin

^ LWH now have distance lods and hiddenselections work - closes T876
SPCS hidden - closes T875
FROG2 lods added and wighing fixed around the crotch and butt area - closes T872

# Revision 787 - MistyRonin

@Corrected stringtable entry.

# Revision 786 - sabre

[Textures] USMC FROG v2 Desert first version.

# Revision 785 - MistyRonin

+ New Gunner class for light vehicles and addition of variants of LWH helmets

# Revision 784 - sabre

[Textures] FROG Version 2 First Woodland MARPAT textures.

# Revision 783 - Bakerman

T868 Removed hint

# Revision 782 - Bakerman

T868 USF vehicle laser range finders now trigger shtora

# Revision 781 - Soul_Assassin

Cleanup launcher fovs

# Revision 780 - MistyRonin

+ Add extra fuel to UH-60 with ESSS external tanks - Before they had the same as the normal UH-60.

# Revision 779 - reyhard

@ added dummy wound texture to frog02 to prevent popup error on mission launch

# Revision 778 - Soul_Assassin

@ Weapon default FOV changed to 0.25 - work on T851

# Revision 777 - Soul_Assassin

@ Fixed forgotten sound attenuation values in M998 classes

# Revision 776 - zeealex

^ improved marine V2 hand weights

# Revision 775 - Soul_Assassin

LWH shadows and material fixes

# Revision 774 - gurdy

+ Added pictures for M1A1, M1A2, and M109

# Revision 773 - MistyRonin

@ Fixed: Wrong helmet in USMC Desert spotter

# Revision 772 - Bakerman

T857 40mm training round smoke puff

# Revision 771 - gurdy

^ Corrected ACH Norotos UCP config

# Revision 770 - gurdy

^ Improved LWH Acc textures

# Revision 769 - gurdy

^ New helmet selection fixes

# Revision 768 - MistyRonin

@ Fixed US Army Gunner for USMC M1025

# Revision 767 - gurdy

+ Added ACH (Norotos) 

# Revision 766 - gurdy

+ Added more LWH versions

# Revision 765 - MistyRonin

+ Grenadier (M32) class - plus different fixes 

# Revision 764 - MistyRonin

@ Fix Glock 17 stringtable & magazine definition 

# Revision 763 - Redphoenix

@ moved some 40mm rounds to folder weapons2/magazines/40mm
+ M576 Buckshot Round

# Revision 762 - reyhard

@ fixed desert m113 w/ m2

# Revision 761 - Redphoenix

@fired version of 40mm grenades

# Revision 760 - Redphoenix

^rotated M781 so it flies correctly
^changed config for M781 so it actually starts flying

# Revision 759 - gurdy

+ Added test SPCS versions

# Revision 758 - Redphoenix

+ M443 HEDP model and textures
+ M781 Practice Round model, config and textures

# Revision 757 - Redphoenix

@M32 ShadowLOD
^M32 model.cfg fixes
^M32 textures and RVMat
^M2A1 sight RVmat and textures


# Revision 756 - gurdy

vest fixes

# Revision 755 - gurdy

+ Readded updated IOTV

# Revision 754 - zeealex

@ Gurdy's Marine V-2 fix
+ MLOD for IOTV with no neckguard+ crotchflap
+ MLOD for SPC rifleman with crotchflap

# Revision 753 - Redphoenix

2nd pboproject crash fix

# Revision 752 - Redphoenix

fixed PboProject crash (missing ;)

# Revision 751 - Redphoenix

+ M32 animation
+ M32 config
+ 6Rnd 40mm magazines
+ M32 Inventory Pictures
+ M32 Initial model.cfg
+ added rhsusf_40mm_HE ammo class
@ rhs_mag_M441_HE and rhs_mag_M433_HEDP now use rhsusf_40mm_HE as ammo
@ M32 RVmat and textures

# Revision 750 - Pufu

Added FMJ and JHP ammo - Spartan's ballistics

# Revision 749 - Soul_Assassin

Strings reverted and merged

# Revision 748 - Redphoenix

@ M32 textures now use the correct texture suffixes
# M2A1 GL sight Injection

# Revision 747 - Pufu

TI map addded, emissive night sights

# Revision 746 - Redphoenix

+ Initial Injection of M32

# Revision 745 - gurdy

^ Fixed FROG2 rvmat


# Revision 744 - Pufu

more shadowlod fiddle...

# Revision 743 - Pufu

further fixes (eye further away - similar to BI)

# Revision 742 - Pufu

shadow LOD fix

# Revision 741 - Pufu

glock inventory icon added.

# Revision 740 - Pufu

second Glock config. Needs ammo class via Spartan.

# Revision 739 - Soul_Assassin

Glock fix

# Revision 738 - MistyRonin

+ Initial config for Glock 17.

# Revision 737 - gurdy

^ Fixed FROG D hidden selection 

# Revision 736 - gurdy

+ Added Temp texture to FROGv2

# Revision 735 - Pufu

first commit glock 17 gen 4 - all LODs + anims in. needs config

# Revision 734 - gurdy

^ Improved M1025 textures and added additional Green options

# Revision 733 - gurdy

^ Texture improvements from Snorri and RVMAT adjustments 

# Revision 732 - gurdy

^ LWH scale tweak


# Revision 731 - gurdy

^ Improved LWH model and added textures

# Revision 730 - reyhard

@ fixed small alpha dots on wheels textures
@ sorted alpha chanells (not completly) on m113 tracks/wheels

# Revision 729 - Soul_Assassin

@ Major stringtable fixes (Schmeisser)

# Revision 728 - reyhard

@ fixed small hole in  turret rear of M1 FG

# Revision 727 - gurdy

^ Fixed M113 texture paths

# Revision 726 - MistyRonin

@ Corrected a few errors in M113 config.cpp

# Revision 725 - gurdy

+ Added remaining M113 variants and textures

# Revision 724 - Soul_Assassin

@ Fixed addon dependency problem causing crashes on Linux servers when using M136

# Revision 723 - reyhard

+ added PIP driver optic to M1 tanks

# Revision 722 - reyhard

^ increased armour around TOW launcher for Bradleys
^ tweaked aiming point for AI for M1 tanks (experimental - tweak by moving zamerny mem point)
@ fixed various destruction errors for M1 - close T787
^ tweaked few hitpoint for M1 tanks
@ readded missing icons for m113

# Revision 721 - gurdy

^ Added correct weapons to M113s

# Revision 720 - gurdy

+ M113A3 M240 name string

# Revision 719 - gurdy

^More M113A3 corrections

# Revision 718 - gurdy

+ Added Improved M113A3 textures, variants, and shadows

# Revision 717 - reyhard

^ improved M1025ies destroyed textures & fixed some missing elements
^ standarized a little bit HEAT hit values so new & old system go along a little better

# Revision 716 - Soul_Assassin

^ Bradley turning

# Revision 715 - Redphoenix

^ Improved Turning for Abrams (possible fix for jerky turning)

# Revision 714 - gurdy

+added WIP shadow lod to edit 30 of *_d_M2, added test shadows to some proxies

# Revision 713 - gurdy

+M113 Icons

# Revision 712 - gurdy

+Added updated M113 track textures

# Revision 711 - gurdy

^added new interior textures and fixed remaining materials

# Revision 710 - Redphoenix

^ reduced specular power for M113A3
@ fixed physx
@ fixed paths to materials and textures in m113a3_d_unarmed.p3d

# Revision 709 - gurdy

+Added new pintle and M113A3 variants

# Revision 708 - reyhard

@ fixed strange proxy path for m1a1 tusk I D

# Revision 707 - reyhard

@ fixed m1 damage selections
@ fixed m1a2 tusk commander cupola shields


# Revision 706 - reyhard

^ reduced minimal lase range for m1 - 200m main cannon & 50m coax - calculations at those distance are WIP!
^ tweaked M1025ies res lods
@ fixed missing damage rvmats for a2 parts
^ tweaked FG of m1 around loader & commander stations
^ tweaked movement ranges for loader mg

# Revision 705 - reyhard

@ changed m1 & m2 commander anim to fix visible rifle while turned in
@ some rpt errors

# Revision 704 - Soul_Assassin

trying to unfuck the m113

# Revision 703 - gurdy

+Added M113A3 stringtable names

# Revision 702 - gurdy

+ Initial Injection of M113A3 (Expect breakage)

# Revision 701 - reyhard

@ restored displayNameShort for US grenades as it was impossible to cycle through grenade types
^ tweaked m1 fcs calculations a little bit

# Revision 700 - Bakerman

Reduced heavy muzzle refraction

# Revision 699 - Bakerman

Reduced heavy refraction

# Revision 698 - reyhard

+ added bipod legs extending anim
@ rotated bipod proxy - close T735

# Revision 697 - Bakerman

T807: Fixed javelin sound reference. Added M249 muzzle up memory points. Added M249 muzzle refraction. Reverted M249 sounds to original. Updated M249 gun particles. Updated M249 description and library. Removed Mk48 material files. Removed faulty M249 receiver material reference.

# Revision 696 - reyhard

CTI:
+ added cantCreateAI=1; param for CTI exclusion (m1a2 mg turrets shouldn't be manned now)

# Revision 695 - gurdy

^hid spec ops rifles and GLs

# Revision 694 - gurdy

^ Improved M109WD textures

# Revision 693 - reyhard

+ added custom arsenal function to prevent load bug - work on T573

# Revision 692 - reyhard

+ added abilitiy to heal at FMTV medcenter
@ fixed AH64 sidewinder errors - Close T820
@ fixed UH60M getin errors - close T819

# Revision 691 - Redphoenix

^ scope = 2 for FMTV Shelter

# Revision 690 - Bakerman

+ Ability to disable vehicle decals with object variables 'RHS_Decal_Enabled', 'RHS_Decal_Symbol_Enabled' & 'RHS_Decal_Number_Enabled'

# Revision 689 - reyhard

^ added missing units to cfgPatches
+ added FMTV shelter animations

# Revision 688 - Bakerman

@ M1 decals are now networked synchronized

# Revision 687 - reyhard

@ fixed weap_m240_base name

# Revision 686 - reyhard

+ added rhsusf_c_troops to CfgPatches of various vehicle addons to prevent rare bug with missing entry in addons list which cause loading errors on dedidcated server
@ fixed m249 & m240 inheritance in sounds pbo - close T808
@ fixed middle cargo seat in uh1y

# Revision 685 - Soul_Assassin

^ Lowered MOI of Abrams wheels to induce better loss of speed

# Revision 684 - reyhard

+ added offset calculations for m1
^ tweaked delpoy points for m249
+ added reslods to marines
^ changed bradley moi to prevent speed bug - YET, ai can't maitan their topspeed 

# Revision 683 - Soul_Assassin

@ SR-25 suppressor image fixed

# Revision 682 - MistyRonin

^ Adding new M249 to AI weapons.

# Revision 681 - Soul_Assassin

long shotgun texture fix

# Revision 680 - Soul_Assassin

fixed boo boo

# Revision 679 - gurdy

^ Reorganized M249s

# Revision 678 - Soul_Assassin

further weapon reference fixes

# Revision 677 - Soul_Assassin

weapon references corrections

# Revision 676 - MistyRonin

^ Adding RHS magazines compatibility to the M249

# Revision 675 - Soul_Assassin

Abrams M240 path fixes

# Revision 674 - zeealex

@ fixed m240 .rvmat filepaths

# Revision 673 - Soul_Assassin

+ M249 and derivatives (toadie2k)

# Revision 672 - Bakerman

^ Small arms barrel refraction is more subtle

# Revision 671 - Soul_Assassin

initial moving of weapons2

# Revision 670 - Redphoenix

^ lowered Center of Mass for Bradley to prevent rolling

# Revision 669 - Redphoenix

^ Bradley PhysX
^ M1-series PhysX
^ FMTV-Shelter SMDI files

# Revision 668 - zeealex

+ added Leupold mk4 entry in virtual ammo box

# Revision 667 - zeealex

^ added auxillary LODS to mk4
@ fixed alpha issue with mk4 reticle. 

# Revision 666 - Bakerman

T712 Removed 'vehicleSpeedY' from moveVelocity

# Revision 665 - Bakerman

T712 Cartridge ejection for M249 & M240 with correct size and timing. Also fixed the double cartridge effect caused by GunParticles inheritance

# Revision 664 - Redphoenix

@ Leica ShadowLOD now use Hard Edges

# Revision 663 - Redphoenix

^ Leica size
^ Leica LODs

# Revision 662 - zeealex

@ removed Rangefinder UI from Leupold Mk4

# Revision 661 - zeealex

@ fixed missing }; in  rhsusf_misc

# Revision 660 - zeealex

@ fixed incorrect filepaths in Leupold mk4 in config

# Revision 659 - Bakerman

T712 Updated cartridge particle velocity to be twice as fast

# Revision 658 - Bakerman

T712 Updated cartridge particle inheritance

# Revision 657 - zeealex

+ Leupold Config (didn't commit)
@ Reversed Green Channel on Leupold NOHQ

# Revision 656 - zeealex

@ Fixed duplicated "</Key>" in string table

# Revision 655 - zeealex

+ Leupold Mk4 Spotting scope (pending correct animation)
@ Fixed incorrect string table entries for Lerca 1200 (Tan)

# Revision 654 - Redphoenix

^ added shell and link ejection for M249 - T712

# Revision 653 - Soul_Assassin

config fixes

# Revision 652 - Redphoenix

^ US grenade family now uses strings for displayName
@ US grenade family has proper/correct descriptionShort - close T795
@ SR-25 now has correct inventory pictures - close T794
^ SR-25M/EC now uses strings instead of normal displayName
@ Harris Bipod has now the correct descriptionShort

# Revision 651 - Redphoenix

^ added missing geometry to M240 feed tray cover selection

# Revision 650 - Redphoenix

^ fixed missing comma in line 176 addons/rhsusf_m1a2/model.cfg

# Revision 649 - gurdy

+ added ERA selections to M1 model.cfgs

# Revision 648 - gurdy

+ M1 script fixes

# Revision 647 - gurdy

+added fixed TUSK I textures

# Revision 646 - zeealex

@fixed M1A1SA config to use new optics modes. 

# Revision 645 - MistyRonin

- Removing tracers from AH-1, AH-64 and A-10.

# Revision 644 - Bakerman

Fixed particle reference for m240

# Revision 643 - Bakerman

@ Correct size for 7.62 ejected cartridges

# Revision 642 - Redphoenix

@ m240B_CAP.p3d no ejects ONLY shells from the bottom ejection port

# Revision 641 - Redphoenix

^ Bullet casings now eject through the correct bottom port
@ Fixed wrong classnames for M240 in virtualAmmoBox.sqf

# Revision 640 - Soul_Assassin

% Fixed M1A1 and A2 lod issues

# Revision 639 - Soul_Assassin

fixed wrong texture and rvmat for tusk 1

# Revision 638 - Soul_Assassin

fixed wrong rvmat on m1 tusk

# Revision 637 - Soul_Assassin

% Fixed buggy soldier leg memory points

# Revision 636 - gurdy

^ clarified M109 names

# Revision 635 - gurdy

^ improved M1A2 spec maps

# Revision 634 - gurdy

+ Updated M109A6 textures


# Revision 633 - gurdy

+Added Update M1A1 TUSK I textures

# Revision 632 - gurdy

^more M1A1 fixes

# Revision 631 - gurdy

^correct barrel art index scripts


# Revision 630 - gurdy

+more barrel art

# Revision 629 - gurdy

^remove slat from base M1a2s

# Revision 628 - gurdy

M1A1SA Fixes

# Revision 627 - gurdy

+ initial injection of M1A1SA TUSK I

# Revision 626 - gurdy

^M109A6 textures

# Revision 625 - Bakerman

All USF weapons now have refraction, updated particles

# Revision 624 - MistyRonin

@Fixed ammo cost for US shells .

# Revision 623 - Soul_Assassin

% UH1Y bounding box fixed

# Revision 622 - gurdy

hidden sel fix

# Revision 621 - gurdy

revert vest models

# Revision 620 - MistyRonin

@Corrected US EOD & Marksman configs

# Revision 619 - Soul_Assassin

class name capitalization improved for documentation

# Revision 618 - gurdy

fixed new barrel art

# Revision 617 - gurdy

more abrams fixes

# Revision 616 - gurdy

adjusted white on barrel art

# Revision 615 - MistyRonin

@Fixed RG-33 editor wrong factions 

# Revision 614 - Soul_Assassin

Closes issue T779- M240 shadows

# Revision 613 - Redphoenix

^ fixed broken rhsusf_c_weapons/rhsusf_weap_rifles.hpp - two class GunParticles

# Revision 612 - Soul_Assassin

^ Refraction points added to rest of rifles

# Revision 611 - Soul_Assassin

% Javelin tube sparks when hit

Closes issue T778

# Revision 610 - gurdy

added ballistic shield glass

# Revision 609 - gurdy

added updated barrel art

# Revision 608 - gurdy

added MILES plates and corrected LODS

# Revision 607 - Bakerman

+ Muzzle heat refraction for USF weapons

# Revision 606 - gurdy

added final MILES textures


# Revision 605 - Redphoenix

+ added usti hlavne up memory points for most USF weapons

# Revision 604 - Bakerman

Working barrel refraction on M4 base

# Revision 603 - Bakerman

12gauge ammunition configuration with effects

# Revision 602 - Redphoenix

@ usti hlavne had 2 memory points in selection

# Revision 601 - Redphoenix

+ testing Heat Haze for Weapons (not functional)

# Revision 600 - MistyRonin

@Fixing little mishap I did in my last commit. 

# Revision 599 - MistyRonin

@Fixed US vests' values.

# Revision 598 - kenji

add miles hide animation

# Revision 597 - MistyRonin

@STANAG mags allowed in M249 - Added for realism sake, tho it won't be shown in the appearance. 

# Revision 596 - gurdy

added test MILES plate


# Revision 595 - Bakerman

12gauge ammunition configuration, not complete yet

# Revision 594 - Redphoenix

@ Lerca Rangefinder now uses strings
@ Shotgun 12g ammo now uses strings

# Revision 593 - Redphoenix

^ FMTV configs improvements

# Revision 592 - Redphoenix

- removed PhysX Test Version from M1A2 for release

# Revision 591 - gurdy

added improved textures

# Revision 590 - Redphoenix

+ added 3 more 12gauge ammo for shotguns (Slugs, HE-ET, FRAG)

# Revision 589 - Soul_Assassin

% Fixed various M1A2 Tusk lod issues

# Revision 588 - gurdy

tweaked RVMATs

# Revision 587 - gurdy

M1 fixes

# Revision 586 - gurdy

upgraded M1A1s

# Revision 585 - MistyRonin

@ Fixed US accessories' wrong inherited inertia values.

# Revision 584 - MistyRonin

- Removed Radar from UH60, UH1, CH47
@ AH1 & M2 Radars changed to Tactic display. - Work on T739

# Revision 583 - MistyRonin

@Various fix in US troops configs - (D & UCP explosive class, helmets, etc.

# Revision 582 - Soul_Assassin

% Hopefully fixed Abrams texture  error

# Revision 581 - gurdy

fixed SPC hidden sels


# Revision 580 - Soul_Assassin

% Fixed config error for packing

# Revision 579 - Soul_Assassin

% Fixed new vests

# Revision 578 - LAxemann

Fixed: Interioir tails for M240 and M249
Fixed: UGL sounds
Soon to come: New sounds. Yay!

# Revision 577 - MistyRonin

@Update US configs to show icons - close T765
+Added Explosives class (equipping the new M112 charges)

# Revision 576 - Soul_Assassin

Fix builds

# Revision 575 - gurdy

fixed spc naming convention


# Revision 574 - gurdy

added new vests

# Revision 573 - zeealex

^Improved Bowman and associated textures, re-scoped the class to 2.

# Revision 572 - Soul_Assassin

^ insideSoundCoef added and adjusted to all vehicles to provide better compatibility with ACRE

# Revision 571 - Soul_Assassin

% Wrong RVMAT on Squadleader IOTV

# Revision 570 - Soul_Assassin

^ UH-60M rotor startup animation
% UH-60M rvmat reference error

# Revision 569 - Soul_Assassin

% M1025 armor value added

# Revision 568 - Soul_Assassin

^ IndirectHitRange of M230 cannon set to 3m

# Revision 567 - Soul_Assassin

% M1 Abrams Loader now able to zero his M240

# Revision 566 - Bakerman

^ Damage and penetration values updated for USF heavy AP rounds

# Revision 565 - Soul_Assassin

Fixes T750

# Revision 564 - Soul_Assassin

Formatting fixes

# Revision 563 - zeealex

+ vest models added for sabre to look at. (no config, figuring it out.)

# Revision 562 - gurdy

fixed M1A2 TUSK 1 D turret tex

# Revision 561 - gurdy

added improved textures


# Revision 560 - gurdy

added upgraded textures

# Revision 559 - gurdy

added new M1A2 TUSK versions

# Revision 558 - Redphoenix

Initial Injection of several FTMV Variants

# Revision 557 - Redphoenix

@ Injection of DPV - no config

# Revision 556 - gurdy

LWH rescale... again

# Revision 555 - gurdy

lwh rescale

# Revision 554 - sabre

[Textures] M240B&G First version. No plastic .rvmats yet.

# Revision 553 - zeealex

+Added Insignia to version 1 FROG

# Revision 552 - reyhard

@ fixed typo in virtualAmmoBox.sqf

# Revision 551 - reyhard

- removed gear indicator from ah1z hmd
@ fixed m112 textures
@ fixed too many FFV turrets for unarmed UH1Y
^ tweaked vehicle paradrop

# Revision 550 - MistyRonin

+ Injection of M112 charges
+ Inserted LWH to arsenal and to certain units
@ Fixed LWH textures

# Revision 549 - zeealex

+ injection of US female name sets
+ added p3d of FROG version 2 (needs configuring)

# Revision 548 - gurdy

added LWH helmets

# Revision 547 - LAxemann

Added: New M249 sounds
Added: New M240 sounds

# Revision 546 - Bakerman

+ Camera shake for AH-1Z M197 cannon fire

# Revision 545 - Redphoenix

^ muzzleFlash for M1911A1 not positioned correctly

# Revision 544 - gurdy

abrams texture updates

# Revision 543 - gurdy

hid SOCOM rifles


# Revision 542 - gurdy

cleaned up RHS headgear

# Revision 541 - MistyRonin

@ Rollback of US Factions - Work on T746

# Revision 540 - Redphoenix

^ improved again textures for Silencers

# Revision 539 - MistyRonin

^ M107 scoped to 0 per request

# Revision 538 - MistyRonin

+ Initial injection of M107 Barrett - It still needs texture and proper anims.

# Revision 537 - Redphoenix

^ darker diffuse maps for NT4

# Revision 536 - Redphoenix

^ viewPilot LOD for NT4 TAN does not use black texture
^ shadowLOD10 is not inheriting any texture

# Revision 535 - Redphoenix

+ added NT4 QDSS supressor - close T725

# Revision 534 - Redphoenix

+ M1 PhyX Test Version
+ Missing seat_pack_nohq.paa for C130

# Revision 533 - MistyRonin

+ Add 50 rounds mag for the M240
+ Add M240B (CAP) & M240G spawnable in zeus.

# Revision 532 - gurdy

@ M240 fixes

# Revision 531 - gurdy

added M240B with cloth bag

# Revision 530 - gurdy

readded new M1A2 textures

# Revision 529 - gurdy

model fixes

# Revision 528 - gurdy

adjusted memory points in M240 models

# Revision 527 - gurdy

injected M240 model

# Revision 526 - MistyRonin

^ Corrected faction assignation of 2010 US AA & APCs

# Revision 525 - reyhard

@ fixed wrong implementation of underbarrel JR
^ removed cursors from air weapons
@ fixed CH47 seats count

# Revision 524 - Redphoenix

- removed Test M1A2 (accidental commit)

# Revision 523 - Redphoenix

^ M1025s now use stringtable.xml names
^ Final M1025 A2 PhysX Update
^ renamed several files in rhsusf_M1025_c with dependencies

# Revision 522 - sabre

[Textures] OGPK version 1.

# Revision 521 - Redphoenix

^ further HMWWVA2 engine refinements based on new data

# Revision 520 - reyhard

@ fixed uh1y observer get out bug - close T727

# Revision 519 - reyhard

@ fixed m134 wrong inheritance in sound cfg resulting in low rof

# Revision 518 - Soul_Assassin

[TAG] First commit of 0.3.8


# Revision 517 - reyhard

@ attempt to fix packing errors

# Revision 516 - gurdy

@ fixed M1025 shadow lod and fixed normal

# Revision 515 - reyhard

@ fixed M2 commander turned out anims
@ fixed missing M2 era hitpoints

# Revision 514 - reyhard

^ another fix for broken M1025 hidden selections

# Revision 513 - reyhard

- removed .tga textures
^ improved attachments inheritance
@ fixed issues with dumping lead in M1 FCS
^ tweaked once again gunner optic stabilization for AH-1 & AH-64

# Revision 512 - zeealex

^ removed bysta proxy from M81 FROG

# Revision 511 - reyhard

@ fixed muzzle attachments for m4 - close T724
@ fixed M1025 hidden selections

# Revision 510 - gurdy

@ more M1025 fixes

# Revision 509 - gurdy

@ commited non-broken textures

# Revision 508 - gurdy

@ A2 parts texture improvement

# Revision 507 - gurdy

@ M1025 Texture Fixes

# Revision 506 - gurdy

@ M998 interior _as fix

# Revision 505 - Redphoenix

^ updated M1025 PhysX to A2-standard

# Revision 504 - reyhard

@ fixed M1025ie vertices limit bug
+ added M1025 antenna anims
+ configured uh60 & M1 sounds
+ added one, non stabilized, gunner mode for ah64

# Revision 503 - gurdy

@ reverted M1A2 textures

# Revision 502 - gurdy

@ fixed armed M1025 meshes

# Revision 501 - gurdy

+ Initial injection of A2 M1025 Parts

# Revision 500 - LAxemann

Changed: New M4 sounds (First sounds made with professional recordings)

# Revision 499 - zeealex

@ Incorrect/Absent IOTV and SPC .rvmat references (T721)
^FROG Weighting issues (T720)

# Revision 498 - reyhard

- removed m2010 bolt action anim

# Revision 497 - reyhard

^ tweaked m1 sound cfg
@ fixed uh1y reflectors
+ added directionStabilized = 1; to uh1y, ah1z & ah64
+ ported a2 cruise missile - to use [getpos start,getpos target] spawn rhs_fnc_cruiseMissile_launch

# Revision 496 - MistyRonin

^ Fixed subfaction strings that prevented USMC helos from being listed. 

# Revision 495 - reyhard

^ some improvments to flir camera script
^ tweaked uh1y pilot reticle

# Revision 494 - reyhard

+ added collimator effect to uh1y pilot hud
+ added UH1Y flir camera script
^ improved flir camera view
+ added polish stringtables by Gienkov
^ improved compatibility with TFAR

# Revision 493 - MistyRonin

+ Add Harris bipods to US weapons used by AI. 

# Revision 492 - MistyRonin

^ Updated Bradley ammo - close T713
^ Updated M829 mag count to 30 - close T714
^ Updated RG33 & M1025 armed variants' ammo count - Work on T391
^ Optimized US Air crew macros

# Revision 491 - gurdy

M1A2 Texture Test

# Revision 490 - gurdy

AR-15 fixes


# Revision 489 - reyhard

^ updated asdg jr compatibility code for marksman dlc
- removed marks fix for a3 1.40 version

# Revision 488 - MistyRonin

+ Added all US Weapons to Zeus/Editor spawn list (launchers & handguns included) - Work on T695.

# Revision 487 - reyhard

@ fixed duplicated weapons in arsenal

# Revision 486 - MistyRonin

+ Add Helicopter D / WD subfaction for each 2010/2014 USMC factions - Work on T267

# Revision 485 - reyhard

+ added UH1Y and AH1Z (WIP) - close T272
+ added category class to vehicles (fixes zeus cost module recognition + 3rd party mods may use it for better vehicle class recognition)
@ fixed flashbang errors for standalone USAF mod
@ fixed armed M1025 leaning - close T704
+ added/tweaked supply points for FMTV & M1025 - close T692
+ added new monitors for CH47 & UH60
+ added VG support for US helicopters
- removed radar from CH47
^ tweaked destruction materials for CH47 & AH64
+ added AH64 with sidewinders (+ability to equip it via VG to all variants)
^ improved config for AH64 sounds
+ added hideWeaponsGunner=1 param to Bradley (introduced due to requirment to draw player weapon for turned out FFV which Bradley doesn't use for now)
+ added turret traversee sound for M1
+ added new hand anim for M4+M320
+ added deploy pivot point for western weapons
@ fixed placable lerca errors (missing pictures/classnames)
^ changed M1 loader turned out recognition to isTurnedOut command (marksman dlc)
+ added visible on ground magazines
+ changed m4/m16 built in bipods into linked item 
^ changed UIs initialization (marksman dlc preparation)
^ changed recoil for M1911 so it's inherited from base clas (recoil not working on devbranch)
+ added new firegeometry & ramp anim to rest of Bradleys

# Revision 484 - MistyRonin

+ Added all US Weapons to Zeus/Editor spawn list - Work on T695.

# Revision 483 - LAxemann

Added: All new M240 reload sounds

# Revision 482 - LAxemann

Added: Sounds for the M1911A1
Added: Config entries for the M1911A1 in sounds

# Revision 481 - Bakerman

T701 USF ce_penetrators updated to array format

# Revision 480 - MistyRonin

+ Added first group of spawn equipment to Zeus/Editor  - Work on T695

# Revision 479 - reyhard

+ added hasBipod param to weapons with integrated bipod
^ tweaked moving in flying c130 script
@ fixed duplicate in stringtable

# Revision 478 - MistyRonin

^ Fast fixes 2 of div per years - Related to T697 .

# Revision 477 - MistyRonin

^ Fast fixes of div per years - Related to T697 

# Revision 476 - MistyRonin

^ Divide US Factions in two time periods (2010 & 2014) - Close T697 (yey!!!)

# Revision 475 - reyhard

change to trigger jenkins

# Revision 474 - reyhard

@ fixed JR CTD after marksman dlc tweaks
+ added temporary fix for missing underbarrel.p3d (delete that .pbo if you use devbranch - shouldn't cause any errors anyway)

# Revision 473 - MistyRonin

^ Updated tankers' load-out - Close T693

# Revision 472 - zeealex

^ Weights of Base Marine Model Improved
@ Scale of SPC Fixed(Gurdy) and weighting improved


# Revision 471 - MistyRonin

+ Added NVG & caps for the US Forces in a smarter manner. - Work in T508
^ Updated M1025 loadout to be coherent with the future new lods - Work in T391

# Revision 470 - reyhard

fixed M1025 transparency sea bug
added open & flatbed fmtv variants
added shadow lods for FMTV
fixed FMTV getin memory point
added map icons for all FMTVs
added spare wheel & cover hide anims for FMTV (compatibile with virtual garage)
increased RG33 wheel durability
decreased RG33 speed with wheels destroyed
configured harris bipod (marksman DLC preparation)
added new underbarrel proxies to western rifles (marksman DLC preparation - expect missing proxy error on stable branch)
fixed mk18 m320 shadows & axis
changed penetration material for weapons to new weapon_plate (marksman DLC preparation)
added map icon for rg33
reworked map icons for M1025ies
added virtual garage support for m113 & m2 bradley (notice ability to change armanent on m2a2)

# Revision 469 - MistyRonin

- Removed NVG from US soldiers & marines default load-out.

# Revision 468 - gurdy

+ new canvas covers to before empty frame proxies for FMTVs

# Revision 467 - reyhard

+ added test ability to move inside flying c130
- removed overlaping cargo seat in fmtvs
+ added glass destruction rvmats & sections in model.cfg to fmtv

# Revision 466 - MistyRonin

- Removed colored ballistic glasses from US soldiers & marines default loadout - Close T681

# Revision 465 - MistyRonin

^ Updated US Armor water fording - Work on T597

# Revision 464 - reyhard

@ fixed missing m2 muzzle flash on M1025 after adding FFV seats 
^ tweaked M2 MG feedtray cover axis on various vehicles
+ added missing hide animations for OGPK turret on RG33
^ tweaked glass hitpoints on rg33
+ configured armed FMTV variants

# Revision 463 - reyhard

@ fixed missing UH60MEV copilot
@ fixed duplicated binoculars in marine loadout
@ fixed jenkins ctd with FMTV (begin of FMTV M2 setup)
@ fixed some missings strings in female RP (still a lot ahead) + it should be possible to use female RP with our US soldiers
+ added some test m1 gas turbine sounds (doesn't sound good)

# Revision 462 - MistyRonin

^ Additional sideweapons for US tankers and tweaked M1A1 M1A2 tank loadout. - Updated T391 and T508

# Revision 461 - gurdy

@ FMTV Turret Hatch Size
+ FMTV (M2) base models

# Revision 460 - MistyRonin

^ Improved water fording depth for: RG-33 M1A1 M1A2 FMTV LMTV - Work on T597

# Revision 459 - reyhard

+ added mirror material to unarmed rg33 mirrors (no black squares while PIP is off)
^ tweaked M2A2 Firegeometry
^ tweaked M2A2 Geometry & added roadway lod - it's possible to get inside now
+ added option to manualy open ramp in M2
^ reduced cost for western missiles (rearming fix)
@ fixed some missing sections errors in devbranch
+ added reslods to shotguns
^ improved shotgun bolt animation
- removed axis bones from m1911
@ fixed non convex component in ch47 geometry (possible CTD fix)
@ fixed few missing sources bugs connected to non existing m240 MG in ch47
@ fixed missing anim src glass7 for uh60m
+ added isPersonTurret=0 to M1A2 commander gun & for loaders (marksman dlc preparation)
^ increased TUSK gunner light intensity
^ configured turned out angles for M1 commanders (marksman dlc preparation)
+ added reslods for M1 FEP tanks
+ added m240 & m2 (sep only) anims to M1 tanks
@ fixed M1A2 commander seat sometimes locked permantelty while vehicle not local
+ added female radio protocol (WIP - connected only to AAF soldiers right now)
+ added some FFV positions to UH60 MEV version wo/ ESS wings
+ added few more get in memory points for uh60
+ added vehicle paradrop script to C130J

# Revision 458 - Redphoenix

^improved M1911A1 smdi map

# Revision 457 - Redphoenix

^ More Resolution/Distance LODs for M1911A1

# Revision 456 - Redphoenix

Final Overhaul of M1911A1 (animations, strings, ammo) - close T581

# Revision 455 - MistyRonin

Add M1911 to US troops (officers, SL and snipers)
Corrected USAF uniform.

# Revision 454 - reyhard

tweaks to m1911

# Revision 453 - Redphoenix

Initial Injection of M1911A1

# Revision 452 - MistyRonin

Hotfix for missing ; 

# Revision 451 - reyhard

added test bipod configuration for m249 & m240
fixed m4a1 pip m203s inheritance
fixed some arsenal CTD in devbranch
removed top & side slot from shotguns 

# Revision 450 - reyhard

fixed usmc decals (alpha sorting) on M1025ies
added some small anims (engine & gear switch)
fixed m1025 driver high getin memory pos
fixed right mirror view on armed m1025
added FFV & window lower/raise action to m1025
added rotor destruction effect to western helis
tweaked door handling on uh60
fixed medic IOTV camo selections in last res lod
added wound textures to US soldiers
added reslods to FROG uniforms
added new fire geometry for m2a2 ODS (WIP)
added ramp anim for m2a2 ODS (WIP)
added Kimi HMD for HMD (work on T510)

# Revision 449 - gurdy

M4 fixes

# Revision 448 - gurdy

m4 model.cfg fix

# Revision 447 - gurdy

added more M4 GL variants

# Revision 446 - MistyRonin

Corrected HMMMWV fording depth values* and add differentiation for USMC.

As exact meter values didn't work (thanks to BI), I used relative values. 

# Revision 445 - reyhard

added door & ramp sounds to helis, c130, M1025ies & rg33
fixed iotv grenadier vest (last lod was containing ref stuff)
fixed some errors with balistic computer on m1 tanks
tweaked once again   HeadAimDown param

# Revision 444 - Redphoenix

Fixed: M113 MG squad has no 2 GPMG instead of M249 - clsoe T532

# Revision 443 - Redphoenix

Fixed: Bradleys now have the same mobility as Abrams - close T650

# Revision 442 - reyhard

fixed uh60 MEV geometry proxies
close T621 - tweaked HeadAimDown param
close T619 - added pmag round count
fixed bolt clipping on M590a1
increased a little bit fireSpreadAngle for shotguns

# Revision 441 - MistyRonin

Updated US hitpoint & armor values (no longer the US faction inherits values from alien factions with an additional armor; now inherits values from NATO )
Updated US vests. 
Now US helmets weight something, and have proper resistance to perforation.  

# Revision 440 - sabre

[Textures] M203 version 1. Added 's' textures that will need to be assigned to the short versions when they are added.

# Revision 439 - zeealex

Improved Grenadier IOTV weights (T617) Leaving it open for suggestions for the time being. 

# Revision 438 - reyhard

tweaked shotguns ironsights
reduced shotgun shell spread  
increased SR25 accuracy
SR25 use for now M14 sounds
increased ver number in options menu
fixed m1a2 tusk & M1A1FEP geometry (ability to go into hull)
added test configuration of M320 on pistol slot

# Revision 437 - reyhard

added sound attenuation to 130
increased zoom for 3d elcan
tweaked eotech reticle
tweaked m203 zeroing
close T616 - fixed pip optics wallhack
fixed m240 ironsight visible in pip optics

# Revision 436 - Redphoenix

Fix: changed frictionVsSlipGraph to prevent oversteering when turning - close T657

# Revision 435 - gurdy

rescaled SR-25

# Revision 434 - reyhard

added handanim for m203 variants
added missing m203 shadow for m16a4

# Revision 433 - reyhard

configured more or less m203 gl with ultra hacky method -yet it's still lacks proper zeroing on 200&250m
initial improvment to M1 FCS zeroing
added player autoloading of AT launchers

# Revision 432 - MistyRonin

HEMTTA2, FR and MARSOC scoped 1

# Revision 431 - MistyRonin

Add M203 to USMC soldiers.

# Revision 430 - gurdy

add M203s


# Revision 429 - MistyRonin

Update US flares, close T640

# Revision 428 - toadie2k

Synced reload anim to character animation

# Revision 427 - reyhard

added a10 to zeus cas module
added m19 at mine to minefield module

# Revision 426 - reyhard

cargo nvg visible in open M1025ies, c130 & ch47
added res lods to silencers & muzzle brakes
fixed m16a4 carryhandle ironsight view

# Revision 425 - reyhard

close T622 - mk18 & b2 front sight folding added
close T623 - added eject option for 130j
close T624 - lowered hit value (smaller recoil) for mk19 + added some new round (HEDP)
close T630 - sr25 optics proxies changed
fixed ah64 hellfire alpha bug
changed order of turret in helicopetr - compatibility with TFAR
increased 3d acog zoom
3d acog zoom now use 16:9 aspect ratio (investigating currently way to have compatibility with different ratios)
removed for now global variable clean up code

# Revision 424 - Redphoenix

Added: Inventory Pictures for Black & Clear Ballistic Glasses - close T631
Added: Orange & Yellow Ballistic Glasses - close T629
Fixed: M993 7.62 has no 20 rounds instead of 30 - close T626

# Revision 423 - MistyRonin

Added first USMC FR groups

# Revision 422 - reyhard

merged menuoptions.hpp changes from russian side
added shadow vollume 10 lod to sr25
tweaked sr25 firegeometry

# Revision 421 - Soul_Assassin

[TAG] First commit of 0.3.7

# Revision 420 - Soul_Assassin

[Fixed] Russian translations

# Revision 419 - Redphoenix

Stringtable.xml  German Translation Update

# Revision 418 - MistyRonin

Updated USMC configs & stringtable

# Revision 417 - reyhard

added reslods to m2010 & eotech
added keybinding support for M1 FCS & western accessories/weapons
configured sr25
fixed typo in m2010 reload anim
removed lockon from m240
improved menu script, added some tooltips


# Revision 416 - gurdy

added KAC stocks to SOPMOD weapons, added (for now, unused) SR-25 files

# Revision 415 - sabre

{Textures] Reduced the brightness of the brown on the DD Rails, more changes to spec etc may come later.

# Revision 414 - sabre

[Textures] MARPAT & M81 Boonies.

# Revision 413 - sabre



# Revision 412 - gurdy

FROG M81 model setup

# Revision 411 - sabre



# Revision 410 - MistyRonin

Add Marsoc groups
Updated US stringtables

# Revision 409 - MistyRonin

Added USMC groups

# Revision 408 - reyhard

added keybinding configuration to option menu

# Revision 407 - MistyRonin

Added US Army groups for RG-33 
Updated US stringtable

# Revision 406 - Redphoenix

USF Stringtable.xml german translation update

# Revision 405 - MistyRonin

Add USMC RG-33 - Close T610

# Revision 404 - gurdy

update display names of M1025s pending model upgrade

# Revision 403 - reyhard

added additional m4 to prevent inventory item spam (LOL)
rg33 gunner is now in same compartment as rest of cargo

# Revision 402 - MistyRonin

Update navy SARS to inherit MARSOC uniform.

# Revision 401 - reyhard

close T609 - added UH60 MEV wo/ ESSS
fixed M1 FEP alpha sorting errors

# Revision 400 - reyhard

added hint while switching Flashlight/Laser combo
added new stuff to virtualAmmoBox.sqf
fixed cargo view of rg33 w/ m2

# Revision 399 - gurdy

added FROGs in M81 and booniehat variants

# Revision 398 - Soul_Assassin

[Removed] Radio chatter from land vehicles

# Revision 397 - zeealex

quick fix of first person view issues on the FROG uniform

there may be weighting problems, I was in the middle of fixing the model weights when the report came in. 

# Revision 396 - Soul_Assassin

[Fixed] Some more russian translations

# Revision 395 - Soul_Assassin

[Fixed] Some russian translations

# Revision 394 - zeealex

Fixed flipped normals issue on FROG uniform 

# Revision 393 - reyhard

added proper inside crew anims for m1 tanks & m2 ifv
close T434 - added new m113 driver anim
added PIP to m113 driver station
close T449
close T555 - alpha issues sorted out
added simple bolt action script for m2010
configured rg33 turret

# Revision 392 - Soul_Assassin

[Added] Inventory icon for FROG

# Revision 391 - Soul_Assassin

Lowered radio chatter volume for US and choppers use jet chatter

# Revision 390 - reyhard

added jet volume macro

# Revision 389 - Redphoenix

slightly louder Jet radio chatter

# Revision 388 - Soul_Assassin

[Fixed] UCP IOTV vests capacity same as OCP (from 80 to 120)

# Revision 387 - Soul_Assassin

[Fixed] M552 has correct inventory icon - closes T601
[Added] Some accessory translations: @RedPhoenix and @MistyRonin please review languages

# Revision 386 - Soul_Assassin

[Fixed] Proper inventory icons for muzzle breaks - closes T598

# Revision 385 - Soul_Assassin

[Fixed] RG-33 M2 stringtable entry

# Revision 384 - gurdy

added RG-33 with test O-GPK and O-GPK base model

# Revision 383 - gurdy

M109A6 pintle removal

# Revision 382 - sabre

[Textures] Fixed small boot part on shirt uv island issue.

# Revision 381 - sabre

[Textures] Work In Progress. Version 1. Woodland and Desert FROG Uniforms. Edited to MICH Covered textures to closer match. Version 2 SPC texture.

# Revision 380 - reyhard

configured jet sounds

# Revision 379 - Redphoenix

2nd HOTFIX for rhsusf_radio ......

# Revision 378 - Redphoenix

HOTFIX - config-cpp for rhsusf_radio

# Revision 377 - Redphoenix

initial injection of more jet radio chatter

# Revision 376 - reyhard

changed required addons for various addons to prevent missing addon error on dedicated server

# Revision 375 - MistyRonin

Updated USAF gear as requested :P

# Revision 374 - MistyRonin

Updated USMC factions adding new helmets with headsets

# Revision 373 - Soul_Assassin

[Removed] Old stringtables

# Revision 373 - Soul_Assassin

[Removed] Old stringtables

# Revision 372 - Soul_Assassin

Trucks stringtable update

# Revision 371 - reyhard

added option menu

# Revision 370 - reyhard

fixed bowman cap missing textures

# Revision 369 - reyhard

fixed helmets errors
fixed missing , in virtualAmmoBox.sqf

# Revision 368 - zeealex

added new MICH helmets to the ammobox

# Revision 367 - zeealex

configured bare helmets + bowman headsets 

# Revision 366 - Soul_Assassin

[Fixed] Minimum arma version required bumped to 1.38. Mod version bumped to 0.3.6 - T571

# Revision 365 - Soul_Assassin

[Fixed] Hellfire lock on cone increased to +-30deg

# Revision 364 - MistyRonin

Add author to the doc dept. of the navy :P

# Revision 363 - Redphoenix

added custom jet pilot and normal pilot for US Air Force

# Revision 362 - MistyRonin

Fixed UCP Uniform

# Revision 361 - MistyRonin

Correction in weap_AI

# Revision 360 - MistyRonin

Updated SPC with "extra invisible space" and given it to all USMC personnel ( same with tan boonies for "light units" ).

# Revision 359 - zeealex

fixed wrong texture path in bowman_cap

# Revision 358 - Soul_Assassin

[Fixed] FROG uniform weighing and model improvements

# Revision 357 - Soul_Assassin

[Fixed] OD variant reduced sections

# Revision 356 - zeealex

added bare MICH helmet + Bowman variations and changed cap colour for bowman+cap

# Revision 355 - reyhard

added ability to cycle through different grenades types
fixed: some grenades short name too long
improved an/m14 inc. effect

# Revision 354 - Redphoenix

- added 7.62 M80A1EPR
- tweaked 7.62 M80
- checked ammo values = all good
close T307


# Revision 353 - Soul_Assassin

[Fixed] Elcan correctly zeroed - closes issue T540

# Revision 352 - Soul_Assassin

[Fixed] Russian translation for new roles

# Revision 351 - MistyRonin

Add new roles to MARSOC & FR
Fix Navy Corpsman mis-located
Update US Stringtable

# Revision 350 - Redphoenix

USF German Stringtable update (this time with Stringforge :P )

# Revision 349 - toadie2k

Rechamber sequeunces cleaned up, pending script

# Revision 348 - reyhard

close T567 - alpha sorting on eotech
fixed helmets missing textures error
added missing helmets to virtualAmmoBox.sqf
tweaked pip script 
tweaked acog glass

# Revision 347 - sabre

[Textures] EOTech retextured to suit RHS. Trademark removed.

# Revision 346 - sabre

[Textures} Surefire SOCOM breaks. Version 1.

# Revision 345 - MistyRonin

Add all the 40mm and hand grenades, and other ammo to US stringtable
Add HEMTT to US stringtable
Fully translate US stringtable to Spanish

# Revision 344 - Soul_Assassin

[Fixed] Removed phantom flashlight shadow from MICH helmets

# Revision 343 - Soul_Assassin

[Fixed] Minor stringtable fixes

# Revision 342 - zeealex

Fixed positioning of 82nd airborne and 10 Mtn Division patches so they don't clip as much

# Revision 341 - zeealex

fixed bowman.rvmat paths to point to the right location. 

# Revision 340 - Soul_Assassin

[Fixed] Stringtables fixed - Closes issue T521

# Revision 339 - MistyRonin

Add tracer color pictures for STANAG mags
Add USMC JFO

# Revision 338 - reyhard

added steering wheel anim for fmtvs
added lodnoshadow=1 param to proxies of fmtv & hemtt, added shadows to fmtvs covers

# Revision 337 - reyhard

acog reticle hotfix

# Revision 336 - reyhard

close T563 - nerfed shotgun
fixed headgear hidden selections
improved stability of pip optic
added test 3d elcan


# Revision 335 - MistyRonin

USMC config ( add new muzzle breaks )

# Revision 334 - gurdy

ucp patch color fixes


# Revision 333 - reyhard

improved 3d acog look
3d acog supports zeus controlled units 

# Revision 332 - reyhard

close T554 - potential fix for strange m14 reload

# Revision 331 - MistyRonin

Corrected & updated USMC configs and weapAI ( used new Eotech and new versions of the helmets ).

# Revision 330 - gurdy

fixed M1A1 OD rvmat


# Revision 329 - zeealex

added MICH helmets with Bowman headsets

# Revision 328 - gurdy

added M1A1FEP in OD

# Revision 327 - reyhard

added test 3d acog optic using pip
added driver interior (visors not working now)
fixed eotech

# Revision 326 - gurdy

initial (non-functioning) commit of Eotech 552

# Revision 325 - reyhard

added new uniforms to virtualAmmoBox.sqf

# Revision 324 - reyhard

added new weapons & acc to virtualAmmoBox.sqf
configured alternate muzzle fire
added missing memory lod to new muzzle brakes 
removed textures from shadow lod 
corrected positioning of muzzle slot on m16
corrected positioning of muzzle brake on m4
removed all p:\ drive references
added missing "muzzle brake" bone

# Revision 323 - MistyRonin

Configured US 82nd, 101st and 10th Div uniforms

# Revision 322 - gurdy

fixed typo

# Revision 321 - gurdy

muzzle brake fixes


# Revision 320 - gurdy

fucking stringtable

# Revision 319 - gurdy

added more patched uniforms

# Revision 318 - zeealex

fixed broken texture paths

# Revision 317 - MistyRonin

Fast fix  AR15, should build but may CTD in-game.

# Revision 316 - gurdy

added USMC AR-15s

# Revision 315 - MistyRonin

Update USMC configs & stringtable ( adding certain MOS names, various tweaks and new additions to the FR )

# Revision 314 - Redphoenix

- fixed weird icon behavior (THANKS REYHARD)

# Revision 313 - reyhard

replaced radar with compass on M1025ies

# Revision 312 - MistyRonin

Add USMC drivers & crew members
Update USMC config
Changed UAV backpack design

# Revision 311 - reyhard

fixed sight folding

# Revision 310 - reyhard

added joint rail support

# Revision 309 - MistyRonin

Corrected Abrams AT4 count and changed M6's Javelins for Stingers for consistency. 

# Revision 308 - MistyRonin

Updated US vehicles loadouts ( Please test and check them )

# Revision 307 - reyhard

changed rando radio chatter to playSound instead of vehicle chat as temp solution
configured frog uniforms & SPC vest
added shadow lod to SPC vest
tweaked BIS acc compatibility
added new uniforms & vest to virtualammobox

# Revision 306 - MistyRonin

Updated USMC configs
Updated String-table
Corrected US clean vests
Modified US common vests cargo capacities

# Revision 305 - MistyRonin

Update US stringtable

# Revision 304 - MistyRonin

Correcting broken USMC D uniform macro

# Revision 303 - MistyRonin

Correcting US Vest supply values to match the vanilla & Russian counterparts 

# Revision 302 - gurdy

added new SOCOM and Navy logos

# Revision 301 - gurdy

committed marine stuff

# Revision 300 - MistyRonin

Adding USMC config files

# Revision 299 - Soul_Assassin

[Fixed] M68 better fits the rails - Closes issue T499 

# Revision 298 - MistyRonin

Adding author info. Close 514

# Revision 297 - MistyRonin

Updated US flares to add intensity values and change of classnames. 

# Revision 296 - Redphoenix

FINAL Lerca texture update.....

# Revision 295 - MistyRonin

Improved 40mm flares ( duration and brightness ) Close T524

# Revision 294 - zeealex

Added entry for SPC in model config file

# Revision 293 - zeealex

-Reweighted IOT Vests* (T501) may need tweaks based on test results 
-initial weights of FROG and base SPC (T506)**

*Issues on the left shoulder of the medic vest are known.
** FROG and SPC aren't configured in RHSUSF folder, but were tested separately and both are working with no major issues.



# Revision 292 - laxemann

Removed: Old m134 sounds
Added: New M134 sounds

# Revision 291 - gurdy

fixed MICHs again


# Revision 290 - gurdy

readded MICH variants

# Revision 289 - Redphoenix

Lerca Texture Fix
Deleted unused texture files

# Revision 288 - reyhard

fixed backpack rvmat error

# Revision 287 - reyhard

increased penetrator timeToLive
added basic radio chatter

# Revision 286 - Redphoenix

fix for rrhs?

# Revision 285 - Redphoenix

FIX - deleted redundant config parameter "envelope" to prevent building crash

# Revision 284 - reyhard

tweaked c130 params

# Revision 283 - MistyRonin

Optimize, fix and update US troop configs

# Revision 282 - MistyRonin

Optimized weapons config (moved AI weapons to an additional file to avoid a crowded config)
Add additional AI weapons

# Revision 281 - sabre

Added fake trademarks to ACOG as it was breaking some peoples immersions.

# Revision 280 - MistyRonin

String-table update

# Revision 279 - sabre

Eagle AIII Coyote ingame value's edit. rvmat shine removed.

# Revision 278 - MistyRonin

Few more tweaks to US Weapons config.

# Revision 277 - Soul_Assassin

[Fixed] Filled missing strings with values

# Revision 276 - reyhard

cannon AI dispersion tweak

# Revision 275 - Redphoenix

Interim M1025 proxy update (not final)

# Revision 274 - reyhard

tweaked behaviour of zeus controled M1 FCS

# Revision 273 - MistyRonin

M16A4 (bipod): sound provisional ( and non-elegant ) fix. 

# Revision 272 - MistyRonin

Standardize US troops config files ( creating a file for each faction as in the Russian side ). 

# Revision 271 - MistyRonin

Add ammo to the RG-33
Muzzle suppressor Speed corrected in M2010 ( In fact instead of reduce the speed, it should had increase it slightly )


# Revision 270 - Soul_Assassin

[Updated] Moved all stringtables to xml

# Revision 269 - Redphoenix

Packaging Hotfix (missing ; )

# Revision 268 - Redphoenix

Injection of single ammo box cal50
Leica RF texture update (both versions)

# Revision 267 - reyhard

rg33:
fixed "cannot load rvmat" error
tweaked interior
added camo selections in cargo lod
tweaked elcan zeroing

# Revision 266 - reyhard

updated main model.cfg! perform update in main dir!
tweaked rg33 materials

# Revision 265 - MistyRonin

Tweaked Ballistic Glasses' "Randomizer"

# Revision 264 - reyhard

close T481 - added clan selection on US uniform

# Revision 263 - reyhard

close T484 - added landContact lod for m109
added new groups - M1025 & fmtv
tweaked anpvs15 (green glow)
fixed FMTV & HEMMT cfgPatches (visibility in zeus)
added random gogles distribution

# Revision 262 - MistyRonin

Added Fire Support Officer and Joint Fires Observer to the US Army. 

# Revision 261 - MistyRonin

Assigned AN/PVQ-31A to US Rifles

# Revision 260 - gurdy

added AN/PVQ-31A config

# Revision 259 - reyhard

close T486 - added lockWhenDriverOut param for bradleys
close T478 - tweaked m2a3 commander turret elevation
fixed gau8 spinning anim

# Revision 258 - reyhard

error sound ported

# Revision 257 - MistyRonin

Add RQ11 operator and update 109's loadout with modern grenades

# Revision 256 - sabre

[Textures] Removed strap shadow so texture can be used on two versions.

# Revision 255 - MistyRonin

Update M1A1 transport load

# Revision 254 - MistyRonin

Standardizing US helmets' armor values.

# Revision 253 - MistyRonin

Updated US infantry armor values to absolute. 

# Revision 252 - MistyRonin

Updating US helmets and vest to have an absolute armor value so it can be displayed properly in the Virtual Arsenal

# Revision 251 - Soul_Assassin

[Fixed] Missing ESS from various helmet lods

# Revision 250 - zeealex

Initial Injection of Bowman Elite II Headset (T455)

# Revision 249 - MistyRonin

Removing Star Wars equipment from AH64 and adding contemporary one :P Close T485

# Revision 248 - reyhard

code cleanup
added support for zeus controled units
changed uav classname
added uaz classname to virtualammobox
changed author string name

# Revision 247 - Redphoenix

cleaned Stringtable.csv and relinked name parameters in several files to STR_RHSUSF_XXX

# Revision 246 - gurdy

added MICH textures and versions

# Revision 245 - Redphoenix

Abrams PhysX Update (new engine parameters, new gearbox setup ratios)
close T479

# Revision 244 - Redphoenix

added rhsusf_a2port_car and rhsusf_c_a2port_car for uaz and ural animation
Known bug:
Warning Message: Cannot load texture ca\weapons\data\fim92stinger_co.paa
fixed: FMTV missing "" in several arrays

# Revision 243 - Redphoenix

fixed Tank Exhaust particles.hpp

# Revision 242 - reyhard

uav:
cleaned up .rpt spam (unknown attribute shadowColor)
fixed pop up error 'no entry config.bin.''.'

# Revision 241 - Redphoenix

added particles.hpp and rhs_ejector_30mm.sqf to addons/rhsusf_c_heavyweapons/ejectors

# Revision 240 - Redphoenix

First Batch of changes to seperate USAF from AFRF
See T76 for changes

# Revision 239 - reyhard

some more uav debuging

# Revision 238 - reyhard

configured rq11 (ctd because of missing userconfig.hpp)
tweaked m113 hitpoints
tweaked rotex shadows
added ability to take control for ah64 gunner
configured eagle III hidden selections

# Revision 237 - Bakerman

T306: Edited camera shake for AH-64

# Revision 236 - Redphoenix

FMTV PhysX Update

# Revision 235 - Redphoenix

Tweaked position of muzzle proxies close T468

# Revision 234 - sabre

Added Coyote Eagle AII pack. Will test colour after it's in properly.

# Revision 233 - Redphoenix

Replaced Rotex 5 (Grey) with right texture

# Revision 232 - Redphoenix

Initial Injection of Rotex5 Silencer (Tan + Grey)

# Revision 231 - Soul_Assassin

Added MICH helmets to virtualAmmoBox.sqf

# Revision 230 - reyhard

added new AH-64 armanent variants
enabled C130
tweaked destruction materials for m113
tweaked M113 hitpoints & FG

# Revision 229 - toadie2k

M2010 Prone Reload corrected, should be fine ingame now

# Revision 228 - Redphoenix

Lerca LOD Update
Added AS map for Lerca

# Revision 227 - MistyRonin

AH-64 Recovering OIF/OEF gray painting.

# Revision 226 - gurdy

added MICH desert models and material


# Revision 225 - gurdy

fixes for MICH d variants

# Revision 224 - MistyRonin

Tweaked M4/M4A1 mass values to uniform them. 

# Revision 223 - reyhard

added headlights & brake lights to FMTVs & Bradleys
added wheel hitpoints for FMTV & HEMTTs
added destruction textures for FMTVs
added driver anim for HEMTTs
tweaked FMTVs firegeometry
fixed M590 penetration materials
fixed HEMTT materials
configured HEMTT CPK variants
added some missing weapon icons
added selection for PiP in A10 cockpit
close T447 - fixed alpha chanels on Bradley
close T448 - tweaked insignia selection
tweaked Bradley Busk III armored glass in firegeometry, so it protects commander actually

# Revision 222 - Redphoenix

final fix for T446

# Revision 221 - Redphoenix

workaround for missing Lerca TAN Inventory Logo

# Revision 220 - gurdy

add slingload capability to LMTVs

# Revision 219 - gurdy

hidden sel fixes for MICHs

# Revision 218 - gurdy

added USMC Michs (still some issues with hidden selections)

# Revision 217 - gurdy

readded RG-33 for fun

# Revision 216 - reyhard

initial FMTV configuration

# Revision 215 - MistyRonin

Adding fancy rangefinders to not so fancy US snipers.

# Revision 214 - reyhard

LRF tweaks

# Revision 213 - Redphoenix

Updated M109 physx_config.hpp
close T264

# Revision 212 - reyhard

muzzle flash fixes for uh60 & ch47
shadow, res lod & animation fixes for m4 bII & mk18
added LRF gui & reticle

# Revision 211 - Redphoenix

added Lerca 1200 TAN
New Textures for Lerca 

# Revision 212 - reyhard

muzzle flash fixes for uh60 & ch47
shadow, res lod & animation fixes for m4 bII & mk18
added LRF gui & reticle

# Revision 211 - Redphoenix

added Lerca 1200 TAN
New Textures for Lerca 

# Revision 210 - Redphoenix

added Lerca LAF 1200 Rangemaster 

# Revision 209 - reyhard

changed classname of rhs_m4_m320 into rhs_weap_m4_m320, previous weapons is still avaiable with scope=1
changed M136 postioning

# Revision 208 - Redphoenix

added version of grenades for throw animation (without clip and safety ring)

# Revision 207 - gurdy

reweighted US combat uniform by Alex

# Revision 206 - MistyRonin

Adding M200 rounds for the M249 too. 

# Revision 205 - MistyRonin

Adding children-proof M200A1 5.56mm bullets

# Revision 204 - toadie2k

M2010 Reload aniamtions added. Prone reload is functional placeholder.

# Revision 203 - MistyRonin

Fast fix to avoid building crash. 

# Revision 202 - gurdy

delete bases


# Revision 201 - gurdy

added LMTV models


# Revision 200 - MistyRonin

Tweaking Bradleys

# Revision 199 - reyhard

fixed m14 IK error in rpt
fixed visibility of weapon bags (m2/mk19)
added weapon bags to virtualAmmoBox.sqf
added ability to fold at4 peephole (working on 1.38)

# Revision 198 - reyhard

close T422 - added initElev=5 to  M1 tanks
inertia & mass tweaking
added Mk18 & block II to ammbox
fixed opscore shadows (named properities cleanup_

# Revision 197 - reyhard

fixed vest capacity

# Revision 196 - gurdy

fixed acc colors

# Revision 195 - gurdy

MK18 fixes

# Revision 194 - gurdy

added Mk 18s and M4 Block IIs

# Revision 193 - MistyRonin

Tweaking and updating ammo loadout

# Revision 192 - MistyRonin

Add ballistic glasses to ammo box 

# Revision 191 - gurdy

added M2 boxes and M2 MG (for looks)

# Revision 190 - reyhard

added pip panel for AH64 gunner

# Revision 189 - MistyRonin

Add ballistic glasses to US soldiers. 

# Revision 188 - gurdy

fix ballistic glasses

# Revision 187 - MistyRonin

Adding 3d models for the fancy glasses ( that I forgot to upload )

# Revision 186 - reyhard

fixed anpvs 15 positioning
configured grenades

# Revision 185 - MistyRonin

Adding new smoke grenades to the soldiers loadout

# Revision 184 - gurdy

new stringtable, lod, and tex fixes

# Revision 183 - MistyRonin

Injecting Fancy protective glasses ( still require some tweaks tho )

# Revision 182 - MistyRonin

M2 Bradley TOW tweaks

# Revision 181 - reyhard

fixed m1a1 tusk leaning
fixed some rpt errors

# Revision 180 - Redphoenix

added Grenade set for US Forces
added grenades to Virtual Ammobox
close T365

# Revision 179 - reyhard

sorted mirrors on M1025ies
changed M590 name to be consistent with rest of weapons
fixed m4 with afg shadows
added hand anims for M4 with AFG & m590
added shadows to m590

# Revision 178 - reyhard

fixed russian translations

# Revision 179 - reyhard

sorted mirrors on M1025ies
changed M590 name to be consistent with rest of weapons
fixed m4 with afg shadows
added hand anims for M4 with AFG & m590
added shadows to m590

# Revision 178 - reyhard

fixed russian translations

# Revision 177 - reyhard

ULTIMATE M1025IE FIX

# Revision 176 - reyhard

named properities cleanup

# Revision 175 - reyhard

tweaked at4 zeroing
removed debug info from peephole script
removed autocenter=0 param from bradleys and m1a1 geometry - look at issue T328

# Revision 174 - reyhard

added ability to fold/unfold at4 peephole (won't work completly till a3 1.37 version) - use / (optics mode)
added deletion of ai disposed AT launchers after 300s

# Revision 173 - MistyRonin

Added rifleman with M590

# Revision 172 - reyhard

added new fire modes to bradley autocannon
damage selections fixes for M1025ies

# Revision 171 - reyhard

increased flashlight power
added rudder pedal anims to ah64 & uh60
improved ah64 interior

# Revision 170 - reyhard

light hotfixes

# Revision 169 - reyhard

reduced cost for javelin missile
changed lod numbering for weapons & accesories

# Revision 175 - reyhard

tweaked at4 zeroing
removed debug info from peephole script
removed autocenter=0 param from bradleys and m1a1 geometry - look at issue T328

# Revision 174 - reyhard

added ability to fold/unfold at4 peephole (won't work completly till a3 1.37 version) - use / (optics mode)
added deletion of ai disposed AT launchers after 300s

# Revision 173 - MistyRonin

Added rifleman with M590

# Revision 172 - reyhard

added new fire modes to bradley autocannon
damage selections fixes for M1025ies

# Revision 171 - reyhard

increased flashlight power
added rudder pedal anims to ah64 & uh60
improved ah64 interior

# Revision 170 - reyhard

light hotfixes

# Revision 169 - reyhard

reduced cost for javelin missile
changed lod numbering for weapons & accesories

# Revision 173 - MistyRonin

Added rifleman with M590

# Revision 172 - reyhard

added new fire modes to bradley autocannon
damage selections fixes for M1025ies

# Revision 171 - reyhard

increased flashlight power
added rudder pedal anims to ah64 & uh60
improved ah64 interior

# Revision 170 - reyhard

light hotfixes

# Revision 169 - reyhard

reduced cost for javelin missile
changed lod numbering for weapons & accesories

# Revision 171 - reyhard

increased flashlight power
added rudder pedal anims to ah64 & uh60
improved ah64 interior

# Revision 170 - reyhard

light hotfixes

# Revision 169 - reyhard

reduced cost for javelin missile
changed lod numbering for weapons & accesories

# Revision 168 - sabre

[Textures] M590A1 version 1

# Revision 167 - MistyRonin

M2010 increased zeroing values.

# Revision 166 - reyhard

m113 & M1025ies use hidden selection textures now

# Revision 165 - RedPhoenix

Fixed FMTVs and gave them proper names/factions/classes
PhysX Dataset update 
close T359

# Revision 164 - MistyRonin

Removed Radar for the M6 too.

# Revision 163 - MistyRonin

Remove Bradley's Radar ( but M6 ), close T358

# Revision 162 - reyhard

fmtv fixes

# Revision 161 - MistyRonin

Temporary patch to allow Jenkins to create the US version :)

# Revision 160 - reyhard

added new m2 ammo
reduced iotv (without pouches) capacity 
added separate magazines & picture to m14ebr
tweaked 7.62 ammo + added some new mags
reduced cost ammo for stinger missile (ai should use it now more often)
configured m320 sounds on m4


# Revision 159 - MistyRonin

M1A1FEP Removed invisible Gunner's M2. Close T356

# Revision 158 - MistyRonin

Removing invisible M2 from M1A2SEPv1 ( no tusk ) gunner, close T353

# Revision 157 - MistyRonin

Adding 200 round mags for the M249, close T352

# Revision 156 - gurdy

M4 stock fixes


# Revision 155 - gurdy

injected M1083A1P2 models

# Revision 154 - reyhard

tweaked ammo belt anim on m113
hotfixed lead calculations for M1 tanks

# Revision 153 - reyhard

removed debug info from balistic computer gui
fixed missing muzzle flash in desert m113 gunner view
close T330 - added to M1A1FEP same gunner view as in M1a2SEP
close T334 & T291 - fixed M6A2 stinger lock-on
improved M1A2 & M1A1 lower hull armor
reduced turret & gun armor on M1 tanks

# Revision 152 - Soul_Assassin

Added M590 to crate

# Revision 151 - gurdy

fixed again


# Revision 150 - gurdy

M590 fixes


# Revision 149 - gurdy

injected M590A1

# Revision 148 - MistyRonin

Add additional STANAG mag without any tracer; Remove tracer rounds from M2010 mag; close T332

# Revision 147 - reyhard

fixed m113 wobbling at ~60km/h
fixed slingload point for uh60
fixed rtd_center for ch47 (separated slingload & rtd_center vertices)


# Revision 146 - Soul_Assassin

- first commit of 0.4
- hemtt reenabled in editor

# Revision 145 - Soul_Assassin

-  ch47 slingloading fixed

# Revision 144 - Soul_Assassin

- fixed M2 minitripod pose

# Revision 143 - reyhard

close T326 - decreased M4 dispersion

# Revision 142 - reyhard

locked Abrams M2 turret (AI not getting in) + readded getin memory points (no more injuries during while geting out from m2 turret)

# Revision 141 - reyhard

improved belt anims on mk19 & M2

# Revision 140 - reyhard

hotfixed anpvs14 green glow selection

# Revision 139 - reyhard

fixed strange M1A2SEP shadows

# Revision 138 - reyhard

close T151 - added muzzleflash, tweaked airFriction, hit damage, reload time & accuracy

# Revision 137 - laxemann

Added: New sounds for the MK19 GMG
Added: New sounds for the M134 Minigun

# Revision 136 - reyhard

fixed armed M1025ies damageHide selections

# Revision 135 - reyhard

tweaked ch47 suspension
close T321 - added open/close ramp action to FFV positions

# Revision 134 - reyhard

rtd center tweak
removed tusk m2 from m1a2sep desert version

# Revision 133 - Soul_Assassin

Further FDM work

# Revision 132 - reyhard

close T323 - changed M19 trigger
close T322 - reduced explosion shielding on bradley tracks

# Revision 131 - Soul_Assassin

Closes issue T148 - H58 sight calibrated
Magazine on the M2010 changes correctly.

# Revision 130 - Soul_Assassin

Closes issue T319 - Mildot and sighting with 3.5-10x Leo Mk4 is now accurate

# Revision 129 - MistyRonin

Removed M320 from 1st Cav SL & TL, close T316

# Revision 128 - reyhard

hotfixed desert m1a2v1 gunner m2 proxies

# Revision 127 - reyhard

hotfixed missing string in group config

# Revision 126 - reyhard

removed zoom from driver triplex
close T32 - fixed M2 clipping - animations are not possible right now
close T33 - new M2 turret handling (might be useful for t72 NSVTs)
fixed turned out commander of M1A2 had thermal camera & CITV zooms 
close T243 - reduced loader pintle moving angles
close T139 - fixed commander MG to fire when inside for M1A2
close T310 - M113 Tracks resistance
added CCP balistic computer to M1A1 (M1A2 use it temporarily too)
added new view modes & zooms for CITV
added new reticles for M1A2 & proper zooming levels


# Revision 125 - Soul_Assassin

arma 2 vehicle thermal fixes

# Revision 124 - reyhard

tweaked disposable script (ai bug - still need testing if it's working on dedidcated server)
another try on exploding a10 on dedicated server
added res lods for nv gogles
tweaked m68 cco res lods
fixed m1 abrams m2 ammo belt clipping
tweaked hatch anims on m1a1
added initial lead calculations for m1 tanks
added turn out ability for m1 tanks drivers

# Revision 123 - reyhard

tweaked M4/M16 + anpeq/surefire combo resolution lods
added different method for calling disposable script - better cross compatibility
close T300 - removed ability to mount supressor on m249
close T301 - added new zeroings

# Revision 122 - reyhard

reduced m84 flashbang damage
lowered crewExplosionProtection for M1025ies with tarp doors
added crewVulnerable = 1; to M1025ies - ai should engage MG & FFV gunners 
some tweaks to mk19 model

# Revision 121 - Bakerman

T304 - Added missing sqf files

# Revision 120 - Bakerman

Closes issue T304 - Added cannon fire camera shake for US air vehicles.

# Revision 119 - reyhard



# Revision 118 - reyhard

close T38 - added new rear sight + zeroings to M136
close T169 -added M1025 with Mk19 GL
close T283 - configured AN/peq15/surfire combo - light/laser change binded to next CM key (default ctrl+c)
added new M136 versions - HP & HEAT
fixed M1025 trunk action
increased a little bit IOTV protection
added pilot nameSound to pilots
added ammoCoef to AT soldiers
added static weapons - mk19 & M2
added patchless infantry model with insignia support
improved M68 CCO red dot visibility during night

# Revision 117 - gurdy

decal fixes

# Revision 116 - reyhard

increased liftForceCoef so it's possible to lift m113 with ch47

# Revision 115 - reyhard

added ability to slingload m113
changed m16 inheritance so sounds get replaced correctly (and it seems to be more logic)
added different prone recoil for weapons with bipod
cleaned up accessory config - removed pg up/down zeroing from acogs & elcan

# Revision 114 - reyhard

M1025 packer ctd fix test 

# Revision 113 - reyhard

added door anims to UH60
added FFV to UH60 & CH47
fixed iotv view pilot lod camo selection
NVG should be visible in M1025ies

# Revision 112 - MistyRonin

Add Riflemen m16 close T295

# Revision 111 - laxemann

Fixed: Silenced sounds for the M2010 now work

# Revision 110 - laxemann

Added: M2010 silenced sounds
Changed: Tweaked M2010 sounds

# Revision 109 - reyhard

added FFV to M1025ies (there are no antiretardation zones - need feedback on that)
added M1025 M1025 w/ M2
some tweaks to M1025ie shadows & models 
readded MANW removed weapons in virtualAmmoBox.sqf
cleaned up backpack config
removed M2 texture (as it's present in a3 itself)

# Revision 108 - gurdy

fixed US army UCP loadouts

# Revision 107 - gurdy

name rollbacks 

# Revision 106 - MistyRonin

Add AR backpack with ammo, close T294

# Revision 105 - MistyRonin

Add MG soldiers a backpack to carry more ammo. close T293

# Revision 104 - MistyRonin

US c_troops correction

# Revision 103 - laxemann

Added: New silenced sounds for AK family

# Revision 102 - MistyRonin

Add AR Assistant ( M249 ), close T289

# Revision 101 - gurdy

fixed afg pilot lod

# Revision 100 - sabre

ACOG overly glossy fix rvmat

# Revision 99 - gurdy

fixed name of m4a1 afg

# Revision 98 - sabre

M4, M4A1 & M16A4 Colt and FNHUSA Trademarks restored.
ACOG Fixed over glossy look.
KAC Rail Cover brightness increased.

# Revision 97 - gurdy

rail fixed and laser placement fix

# Revision 96 - gurdy

added KAC RC's on M4s and M16s

# Revision 95 - gurdy

added KAC rail covers

# Revision 94 - sabre

Leupold Mark 4 6.5–20×50mm ER/T M5 Textures 1st version.

# Revision 93 - gurdy

reverted pre-manw stuff and added new M4 barrels

# Revision 92 - Soul_Assassin

- removed hemtts

# Revision 91 - reyhard

corrected m830 speed
added m1069 round to fcs + not very accurate calculations for coax MG

# Revision 90 - Stagler

T197
-Added US assistant MG pack UCP + OCP
-Added US assisntant MG pack to AMG units.


# Revision 89 - Stagler

https://dev.rhsmods.org/T197

- Created M4a1 with scopes configs
- Added M4a1 to all OCP troops.
- Added extra magazines to all us troops
- Added smokeshells to all us troops

# Revision 88 - RedPhoenix

M829A3 fix- raised ammocount from 25 to 30

# Revision 87 - RedPhoenix

close T268
close T270

# Revision 86 - reyhard

moved lo poly lod to edit lod on m2 bradley
some experiments with m2 suspension (M2A2 ODS wo/ busk variant)
temporary MANW weapon removal from virtualAmmoBox

# Revision 85 - gurdy

replaced gloved hands with bare hands 

# Revision 84 - laxemann

Changed: Tweaked the M16 sounds (more treble)

# Revision 83 - Soul_Assassin

closes ticket T247 - MANW related wepons fixes

# Revision 82 - laxemann

Added: New reload sounds for the AR-15 family
Added: New Firemod switch sounds for the AR-15 family

# Revision 81 - reyhard

added m67 grenade to throw muzzle
added m67 to virtualAmmoBox.sqf
changed m67 short name

# Revision 80 - gurdy

fix new leupold model

# Revision 79 - RedPhoenix

Bradley section instead of single Bradley
close issue T253

# Revision 78 - RedPhoenix

cfgSounds.hpp for Bradley
Physx Update for Bradley

# Revision 77 - gurdy

added M67 grenade and gave NVGs to troops

# Revision 76 - gurdy

bradley texture fixes and woodland setup

# Revision 75 - gurdy

brighten black platoon markers

# Revision 74 - gurdy

fixed USMC M1A1 name 

# Revision 73 - gurdy

added M2010 scope 
fixed carryhandle AR-15 proxies
added refined weapon/attachment compatability
added AR-15 variants

# Revision 72 - RedPhoenix

PhysX Update for Bradleys (propper engine config)
High sprungMass - possible fix for braking when driving over a bump

# Revision 71 - reyhard

close issue T221 - M109: Right side track teeth do not animate.
close issue T235 - Config AN/PVS-14 and AN/PVS-15
close issue T159 - HMWVV driver sits very high
close issue T134 - Add AGM Javelin TopDown mode
fixed M1025 chassis shadow
added shadow res lod for HMWVVie
fixed M2A3 Busk III antena shadows
fixed missing driveOnComponents message for m109

# Revision 70 - RedPhoenix

fixed tracer mags
added tracer every 4 rounds to M249 mag
fixed silencer for M4/M16 family (now uses 5.56 silencer instead of 6.5)
added 5.56 silencer to RHSUSF virtual ammobox

# Revision 69 - toadie2k

Added reload sequences to M4, M16 Rifles. 

# Revision 68 - Soul_Assassin

fixed all M2 cog

# Revision 67 - Soul_Assassin

Bradley cog tweaks for testing

# Revision 66 - Soul_Assassin

Closes issue T31 - deforming strap on iotv. More consistency in lod transitions on various vests.

# Revision 65 - gurdy

added AN/PVS14 and 15

# Revision 64 - RedPhoenix

raised maxBrakeTorque

# Revision 63 - RedPhoenix

fixed unresponsable suspension on both M1025s

# Revision 62 - reyhard

added minTotalDamageTreshold to M113
added some missing weapons to virtualAmmoBox.sqf
close issue T223 fixed m1 damgeHide selections

# Revision 61 - sabre

Acc texture update 1

# Revision 60 - sabre

M2010 Texture size increased due to poor UV for FP.

# Revision 59 - Soul_Assassin

Closes issue T103 - M109A6 thermals fixed

# Revision 58 - sabre

Moved Surefire M952v position forward.

# Revision 57 - sabre

M4 Fixed texture path error. Added version 1 magpul ctr and afg textures.

# Revision 56 - gurdy

m4 accessory model fixes


# Revision 55 - Stagler

- Changed Ultra low poly woodland texture to not be lime green.

# Revision 54 - reyhard

set explosionShielding to 0 for hithull
added new m2 cfg for m113 (because of sounds)
reduced javelin explosion damage
changed LOD numbering for PEQ15

# Revision 53 - sabre

M2010 Texture update to include AAC muzzle brake.

# Revision 52 - laxemann

Changed: New 120mm sounds 

# Revision 51 - laxemann

Added: Sounds for the M256
Added: Sounds for the M2
Added: Sounds for the M230
Added: Sounds for the M242

# Revision 50 - reyhard

changed some more "" into ' in c130 & ch47 UserActions
close issue T71 added Coax muzzle flash to Bradleys
fixed poklop_commander inheritance in m2 skeleton
fixed TOW selection in second res lod in M2A2
fixed rhsusf_m113d_usarmy: Recoil - unknown animation source recoil_source rpt error
fixed unknown animation source zaslehROT_HMG2 rpt error on M1a1
close issue T200 - added new lights config for m113
fixed zbytek selection in res lods of m113

# Revision 49 - gurdy

added M4 variants and accessories

# Revision 48 - gurdy

fixed proxies on M2010

# Revision 47 - reyhard

changed some more "" into ' in M1025ie user actions
close issue T192 - Abrams tracks turning the wrong way

# Revision 46 - reyhard

probably fixed crouch bug with aia tp

# Revision 45 - RedPhoenix

fixes critical error occured in rUSAFDEV42

# Revision 44 - gurdy

added test version of fixed interior

# Revision 43 - gurdy

add m2010 to ammo box, config silencer

# Revision 42 - gurdy

added updated M2010 and reenabled

# Revision 41 - reyhard

fixed issue T184 (TOW locking)
fixed missing ; errors in m1 config
changed mass of M19 mine

# Revision 40 - gurdy

added more CIP panels and added M1A1HC WD

# Revision 39 - reyhard

fixed wheel reference not initialized rpt errors on m113

# Revision 38 - reyhard

fixed m113 gunner hand anims
removed decal related rpt spam

# Revision 37 - reyhard

fixed m4a1 full auto sound

# Revision 36 - sabre

[Optics] M145 Textures, Shine reduced, company and model name returned.

# Revision 35 - reyhard

fixed m136 sound as "safemode" is not used anymore

# Revision 34 - reyhard

tweaked m1a1 EH
fixd proxy on M1a1 HC
tweaked launcher pen values
fixed missing legs in rhsusf soldier model (forgot to copy paste that, ha)

# Revision 33 - gurdy

M977 texture progress


# Revision 32 - gurdy

added CH-47 textures by CptDavo

# Revision 31 - gurdy

add HEMTTs with armored cabs

# Revision 30 - Soul_Assassin

all pbos now require 1.32 minimum

# Revision 29 - reyhard

fixes for pboproject

# Revision 28 - RedPhoenix

- deleting redundant config.bin

# Revision 27 - RedPhoenix

- bouyancy fixes 

# Revision 26 - reyhard

tweaked hemtt Center of Mass (was leaning slighty left)
added config.cpp to models

# Revision 25 - RedPhoenix

- new PhysX dataset for HEMTT A2

# Revision 24 - RedPhoenix

- further M113A3 PhysX adjustments

# Revision 23 - reyhard

hotfixed hemmt weight

# Revision 22 - reyhard

fixed acog missing uvset in diagnostic exe
tweaks to geometry, shadows & suspension of hemmt
added RedPhoenix physx config

# Revision 21 - gurdy

added HEMTT fuel


# Revision 20 - Soul_Assassin

removed temp folder

# Revision 19 - reyhard

fixed M1025 passanger mirror view
added very early hemtt configuration
fixed medic iotv variant shadows in distant lods
fixed t119 - m109 pboprefix

# Revision 18 - RedPhoenix

- further tweaking of Abrams PhysX
- deleting redundant config.bin in addons/rhsusf_c_m113/ 

# Revision 17 - RedPhoenix

- fixed maxBrakeTorque on M113A3
- raised tankTurnForce on M1A1

# Revision 16 - RedPhoenix

- fixed typo for M1A1 enginePower

# Revision 15 - RedPhoenix

- new PhysX dataset for M1A1 Abrams

# Revision 14 - reyhard

added res lods for m1a1
tweaked res lods for m1a2
improved m68 cco hex texture
fixed T69 - added rocket motor fire to agm-65

# Revision 13 - RedPhoenix

- new Physx Dataset for M113A3

# Revision 12 - reyhard

added numberPhysicalWheels param to various vehicles
tweaked commander HMG script
tweaked M113 res lods (iff panel visible in every res lod)
tweaked m1a2 tusk hitpoints
completed res lods for m1a2
some res lods for m1a1
tweaked m136 power

# Revision 11 - reyhard

fixed sound paths after pboprefix change

# Revision 10 - gurdy

M977A2 Initial injection

# Revision 9 - gurdy

added pboprefix to rhsusfsounds

# Revision 8 - laxemann

M4 and M16 now have different sounds
Added: New sounds for the M16
Changed: Old M16 sounds are now the "new" M4 sounds

# Revision 7 - laxemann



# Revision 6 - reyhard

res lods for m1a2sep desert versions

# Revision 5 - reyhard

fixed muzzlepos error in rpt for javelin & stinger
tweaked vest shadows (removed lod no shadow, tweaked shadow lod 10)
added driveoncomponents for m113
added resolution lods for US weapons & accessories
added resolution lods for us soldier model
tweaked us soldier view pilot view (copy past of pockets from res lod 0)

# Revision 4 - sabre

US Army Infantry - Uniform 'shine' removed.

# Revision 3 - reyhard

replaced weapon modes with isSelected on at launchers
fixed stinger missile still inside tube after launch
added sight folding on at4
changed bradley he-t tracer
reduced lag in gunner view while firing bradley autocannon
added slingload max cargo mass params to ch47 & uh60

# Revision 2 - reyhard

updated webpage in mod.cpp
fixed & improved heli hitpoints
added slingload ability to ch47 & uh60
removed radar from bradley
fixed maxFordingDepth for M1, M2, M109 & M113
fixed m113 bottom textures
added res lods to m113
improved m113 fire geometry
improved m113 gunner view
added new muzzle flash to m113a3
fixed m1 hitpoints (added track hitpoints, tweaked turret hitpoints)
added slingload ability to m1025
fixed elcan mipmaps
changed m249 magazine mass
