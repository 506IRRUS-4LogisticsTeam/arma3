# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.5.5

## ADDED IN 0.5.5

+ Added T15

+ Added towing system to ZU-23-2 & D-30 (ongoing Work In Progress). Those 2 heavy weapons can be only towed AFRF cars & trucks for now! For more info please go to following page -  http://www.rhsmods.org/w/towing

+ Afghanka uniforms in many different varieties and camouflages

+ KLMK oversuit

+ OMON uniform

+ Cossak uniform

+ VKPO uniform

+ 6B2 with variants

+ 6B3 with variants

+ Belt pouches with variants

+ Suspender equipment with variants

+ Lifchik chest rig with variants

+ Chicom chest rig

+ 6Sh117 with variants

+ 6B45 with variants

+ Pilotka

+ Afghanka field cap with many variants

+ VKPO field cap

+ Ushanka

+ OMON cap

+ Cossack visor caps

+ Cossak Papakha

+ OMON Beret

+ Early VDV Beret

+ SSh60

+ New SSh68

+ STSh-81 Sphera

+ New 6B47

+ 6B48

+ RD-54

+ New RPG pack

+ R-148

+ Added 6M2 and 6M2-1 Headphones inc. headgear, glasses and NVG slot variants, plus 6B47 helmet models with integrated headphones

+ Added RPG-18 from Arma 2

+ Added 6B5 vests from GREF to AFRF, to compliment the addition of other Soviet uniforms and equipment

+ R-187P1 Azart inventory item for radio-slot

+ R-169P-1-01 inventory item for radio-slot

+ Added RPK-74M

+ 6L31 60 round, quad-stack 5.45x39mm magazine

## IMPROVED IN 0.5.5

^ Adjusted opticType on AFRF accessories

^ Autotrack system is now using getVehicleTIPars

^ Regenerated icons for AKS74U

^ Added recoil force to aircraft mounted GSh cannons - http://feedback.rhsmods.org/view.php?id=5962

^ Tweaked AK74 animations a little bit

^ Tweaked hit points & fire geometry of D30 & ZU-23-2 - they should no longer explode from single grenade + they have now turret & gun hitpoints configured

^ Added spalling to vanilla HEAT submunition

^ Added additional particle effects to ZU-23-2

^ BTR-80 and 80A optimized definitively

^ Improved resolution LODs Crates and Wheels from the BTR70 / Habar.

^ Added SVD muzzle accessories to Joint Rails (asdg_MuzzleSlot_762R_SVD )

^ Added compatibility entries for BIS accessories

^ Improved resolution LODs BMP2

^ Improved resolution LODs BMP1.

^ Improved resolution LODs wooden ditching beam

^ Improved resolution LODs Konkursz.

^ Tweak to towing weapon helper function

^ Improved BMP1/BMP1D/BMP1K camo selections missing.

^ Improved resolution LODs BMK_T

^ Heavy weapon variables related to dragging are properly deinitalized when action is cancelled

^ Improved resolution LODs URAL : optimization of the last lod, which was too square.

^ Improved resolution LODs BMD/Habar : optimization of all the content : additions of 3 lods.

^ Improved resolution LODs PMP pontoon : added 3 lods.

^ Improved resolution LODs AK74

^ Improved resolution LODs ZIL131 : added lod 4 and 5.

^ Added glass panels to Kamaz-5350 last LOD

^ Made RSP-30 & TR-8 icons more consistent

^ Reduced Pchela-1T protection against HE rounds

^ Improved gear/backpack : added landcontact lod.

^ Added special function for handling of dragging heavy weapons by AI (can be only used by mission makers)

^ Added buoynacy=1 to fake towing vehicle

^ Tweaked what weapons are visible in Eden ammo crate

^ Tweaked visibility of folded weapons in VA - http://feedback.rhsmods.org/view.php?id=6037

^ Added PG-1, PG-1M & basic implementation of OP4-M45 sight

^ Added optics hitpoint to D-30 & 2B14

^ Small tweaks to ZU-23-2

^ Tweaked 2B14 optic animation + disabled barrel stabilization

^ Improved resolution LODs T-72/T-90 series tanks

^ Improved resolution LODs NSVT : addition of a fifth lod

^ Tweaked vehicles door sounds

^ Added damage textures to new ZU-23-2 model + small color tweak to texture

^ Reduced inventory mass of bakelite and polymer 7.62x39mm AK 30-round magazines

^ Improved resolution LODs T-80 series tanks

^ Added experimental function which removes engine fire particle effects after vehicle was repaired & engine was turned on

^ Few logic tweaks to rhs_fnc_engineCheckDamage function

^ Separate AFG slot proxy definition in AFRF. Avoids USAF dependency if this feature is needed for RU weapons (or community addons) in future

^ Tweaked 9M117 max range & flight time (there are still some issues with guiding them above 5km though) - http://feedback.rhsmods.org/view.php?id=6150

^ Tweaked launchers recoil (kudos to PSZ team!)

^ Regenerated CfgPatches & ground holders for place able items. Warning! Old editor weapons received scope = 1

^ Reduced 2A28 dispersion for AIs

^ Proper Eden editor preview images for VDV Recon units

^ Tweaked VOG-30/17 max time to live + added self destruct timer - http://feedback.rhsmods.org/view.php?id=6056

^ Tweaked ZSU-23-4 max speed - http://feedback.rhsmods.org/view.php?id=6057

^ Tweaked BTR-60 PhysX configuration - http://feedback.rhsmods.org/view.php?id=6091

^ Added new T3 scope to ZU-23-2 & calibrated ZAP-23

^ Adjusted get in points & actions on static weapons + prepared them for 2.04 update

^ Reduced turn out limits on Tigr & Kamaz to reduce chance of seeing your own back - http://feedback.rhsmods.org/view.php?id=6063

## FIXED IN 0.5.5

@ Removed accidental PhysX override

@ Hide Igla pod missiles from Virtual Arsenal

@ Hide some FCS laser magazines from Virtual Arsenal

@ D30 & ZU-23 gun packing was incorrectly locking seats in MP

@ Fixed folding weapon stock with safe mode turned on would result with one magazine missing - http://feedback.rhsmods.org/view.php?id=5886

@ Fixed AK74M safe mode animation

@ UAZ was still using old spare tire model in interior LOD

@ Fixed MiG-29SM missile feed - http://feedback.rhsmods.org/view.php?id=5990 http://feedback.rhsmods.org/view.php?id=5525

@ Fixed issue when folding weapon or attaching NPZ could magically spawn new muzzle attachment - http://feedback.rhsmods.org/view.php?id=5991

@ Fixed NIT-A reticle tint

@ Fixed number of available seats on open ZiL-131

@ Fixed KrAZ-255 door selections in interior LOD

@ Fixed errors related to missing ti textures & replaced them with procedural ones for now

@ Fixed Zil-131 door selections in LOD 3 & 4

@ Towing variables are properly deinitialized when vehicle gets detached

@ Some of the Russian ATGMs inherited tandem heat property - http://feedback.rhsmods.org/view.php?id=6021

@ Fixed missing detail in KrAZ-255 interior view

@ Fixed some floating bits near middle KrAZ-255 wheel

@ SVD bolt stays in back position after firing last round

@ Fixed MiG-29SM distance to waypoint text clipping in one of the MFDs - http://feedback.rhsmods.org/view.php?id=6042

@ Fixed T-72 startup sounds - http://feedback.rhsmods.org/view.php?id=6045

@ Fixed scripted turrets not being locked properly in MP - http://feedback.rhsmods.org/view.php?id=5894

@ Fixed smoke effect on OG-7V - http://feedback.rhsmods.org/view.php?id=6062

@ Fixed model.cfg for BM-21 rockets ("Invalid parent bone 's13' for 'fire'" .rpt error)

@ AK-103 (Zenitko) handanims when grips were attached

@ AK-103 (Zenitko) was able to attach side-rail optics when the stock was folded

@ Tweaked T72/T90 fire geometry around ammo carousel - http://feedback.rhsmods.org/view.php?id=6146

@ Fixed small typo in Su-25 flight model config - http://feedback.rhsmods.org/view.php?id=6167

@ Fixed assert when turning out on 2S25, T80A & T80U series vehicles - http://feedback.rhsmods.org/view.php?id=6189

@ Fixed 2A28 AI rate of fire - http://feedback.rhsmods.org/view.php?id=6201

@ Fixed recoil related errors in single use launchers config - http://feedback.rhsmods.org/view.php?id=6194

@ Typo in class rhs_weap_ak74m_fullplum_folded `baseweapon` parameter

@ Fixed T90AM commander zeroing was affecting AI - http://feedback.rhsmods.org/view.php?id=6195

@ Fixed bipods reappearing when dismounting gripod - http://feedback.rhsmods.org/view.php?id=6218

@ Fixed camo selections on 6B47 - http://feedback.rhsmods.org/view.php?id=6073

@ Fixed light going through BTRs hull - http://feedback.rhsmods.org/view.php?id=6099

@ Fixed typo in 9M521 tooltip - http://feedback.rhsmods.org/view.php?id=6128

@ Fixed issue with AI getting into Tigr-M was restarting players view mode - http://feedback.rhsmods.org/view.php?id=6092

@ Fixed .rpt errors related to TR-8 - http://feedback.rhsmods.org/view.php?id=6226