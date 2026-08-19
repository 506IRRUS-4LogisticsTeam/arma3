# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.5.6

## ADDED IN 0.5.6

+ 40mm Cluster Star (5x signal flare) magazines for M203/M320/M79 type single-shot, low-velocity grenade launchers. M585 white cluster, M663 green cluster, M664 red cluster

## IMPROVED IN 0.5.6

^ Slight adjustment to WMX200 flashlight scale

^ Added supply points to various vehicles - http://feedback.rhsmods.org/view.php?id=6319

^ Tweaked CLU hiding logic - http://feedback.rhsmods.org/view.php?id=6313

^ Tweaked ignition delay and burn time of 40mm flares to realistic values

^ Replaced `rhs_mag_M585_white` flare with `rhs_mag_M583A1_white` flare (M585 is a star cluster flare IRL). rhs_mag_M585_white class is now hidden but can still be loaded, though its displayname is also changed to M583

^ Adjusted green and red flare particles so that they don't look identical to white flares during daylight (green flares do still look quite white, as they do IRL)

^ Increased size and observable distance of M257 Hydra rocket's flare effect

^ Added `affectedByWind = 1;` property to US signal/illum flares (countermeasure flares unchanged)

^ Improved 105mm and 155mm ILLUM rounds: Converted to use submunitions system, added realistic burn times for flares and increased their illumination capability

^ Reduced thermobaric wave effects & disabled pp effects

^ Increased illumination capability of 40mm flares

^ Improved damage/destruction visuals of M1A2SEPv2

^ Adjusted HEAT submunition initial speed to take into account air friction - http://feedback.rhsmods.org/view.php?id=6110

^ Added some missing editor previews

^ Regenerated editor previews

^ Added experimental function to fix texture randomization on dedicated server

## FIXED IN 0.5.6

@ Fixed weapon holder path in macro

@ Script error using Leica rangefinder when running RHSUSAF standalone

@ Fixed error in towing system when memory point is used for determining of attach point

@ Fixed non-convex geometry component in GMV M134-carrier turret and regenerated components names for all GMVs

@ M781 40mm Prac grenade was not sorted next to other RHS 40mm magazines in the Virtual Arsenal for weapons with an M320 UGL

@ 40mm stun grenade ammo class required AFRF

@ Fixed ghost LOD on Mk18 with M320

@ Fixed spawning of destroyed DUKE antennas when vehicle is completely destroyed - http://feedback.rhsmods.org/view.php?id=6330

@ Fixed SACLOS guidance was affected by gun FCS - http://feedback.rhsmods.org/view.php?id=5985

@ One of the addons was missing in load order list

@ Removed obsolete accessory from weapon crate

## REMOVED IN 0.5.6

- Removed macro-generated `Item_rhs_mag_M585_white` ground holder class (added in RHSUSF 0.5.5) for deprecated M585 magazine (legacy rhs_magazine_rhs_mag_M585_white still exists in hidden scope)

