# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.9

## ADDED IN 0.4.9

+ European ScarH versions

+ added SCAR H DMR role soldier in Airborne troops

+ Added new inventory icons for uniforms

+ PBG-40 is now using magazine proxies

+ Added 2S1

+ Added functional M79 grenade (port from GREF RKG-3EM)

+ Netting-style face veil (available as glasses slot headgear and Veil+M97 helmet combination) 

+ HT-40 helicopter (Mi-8T)

+ SAF Opfor factions (Army and Airforce)

## IMPROVED IN 0.4.9

^ Minimi Para grip/bipod slot configuration on par with USAF M249s

^ Updated M10 desert uniform texture

^ M93 uniform TI texture

^ RHS Vehicle icons in Virtual Garage should be visible on Steam branch release

^ Added separate name for development branch version

^ Readded proxies to characters shadow LOD

^ Some more improvements to characters fire geometry

^ Added SAF loadorder

^ Improved addons loadorder

^ Some modification to M84's shadow geometry in the buttstock area

^ Set up G36s to use common community `magazineWell[]` (class CBA_556x45_G36)

^ Added facewear proxy to pilot LOD of SAF uniforms

^ Many SAF weapons will now accept magazines compatible with CBA JAM

^ Reduced section count of MD12 M70 rifleman vest

^ replaced T72S tank with T72B3

^ PBG40 now use soundsets

^ Updated green HT-48 (Mi-17) texture to similar standard as the new camo Mi-8T texture, and made it available for selection in Virtual Garage etc.

^ TI map for M10 uniform

^ TI maps for helmets

## FIXED IN 0.4.9

@ Fixed G-36 pop error when editing crate loadout

@ Fixed some unnecessary tex1 reference in rvmat which were causing .rpt spam in Diag.exe

@ Fixed missing head shadows in View Pilot LOD

@ Added penetration materials, armor & explosion shielding parameter to all RHS explosives

@ Fixed characters hands being screwd in last res LOD - added shadowlod param

@ Fixed some minor issues with new character firegeometry

@ M84 had several vertices in the buttstock marked as Hidden Verts. Seems that sometimes the whole buttstock could be invisible ingame

@ AG36 was not utilising the common BIS 40mm `magazineWell[]` used by other 40mm GLs in the mod (class UGL_40x36)

@ Some parts of MD12 vest did not have camo hiddenselection defined

@ Helmet shadow LODs contained `camo` retexture selections
