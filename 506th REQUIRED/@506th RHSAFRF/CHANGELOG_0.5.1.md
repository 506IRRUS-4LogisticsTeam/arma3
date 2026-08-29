# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.5.1

## ADDED IN 0.5.1
{CHANGESADDED}

## IMPROVED IN 0.5.1

^ Pontoon bridge improvements:

^ Converted T tanks autoloader sound to SoundSet tech

^ Removed explosion sound from penetrator base class

^ Lowered volume of autoloader in interior view

^ Added few more tank groups (T14, 2S1 + new T72/90 tanks) for AFRF

^ Tweaked T-72 & 90 bottom hull side fire geometry - work on http://feedback.rhsmods.org/view.php?id=5378

^ Add VehicleTransport to GAZ66 and Ural

^ Added VG icon to BMK-T

^ Added some basic model.cfg to BMK-T

^ Removed some obsolete functions

^ Tweaked pontoon water resistance

^ Added ViV, slingloading, reflectors, passenger with turnout & improved BMK-T physics - http://feedback.rhsmods.org/view.php?id=5382

^ Added some basic sounds, destruction & shadow LOD to BMK-T

^ Tweaked skin injury materials

^ Added few more faces from Contact DLC to Russian identity pool

^ Tweaked Mi-28 ejection script so dead AIs are no longer ejected - http://feedback.rhsmods.org/view.php?id=5462

^ Tweaked ERA blocks durability against HEATs

^ Tweaked PKAS ADS view

^ TM62M is now triggered only on contact - placing mines in the middle of road will be no longer effective

^ TM62M is now using additional penetrator to simulate blast damage

^ Tweaked behavior of T tanks tracks when on reverse gear - http://feedback.rhsmods.org/view.php?id=5503

^ T80B is now using 1100HP engine to represent later production model (typo fixing) - http://feedback.rhsmods.org/view.php?id=5486

^ Testing Ka-52 assisted missile firing for AI

^ Increased HEAT & ATGM indirectHit range - http://feedback.rhsmods.org/view.php?id=5431

^ Unified explosion effects of PG9 & PG15 - http://feedback.rhsmods.org/view.php?id=5401

^ Disabled env map switching on Mi24 glass and changed env texture to jet variant

^ Added VG40MD to AFRF ammo crate - http://feedback.rhsmods.org/view.php?id=5428

^ Tweaked glass tint on 1P87 & EKP-8 - http://feedback.rhsmods.org/view.php?id=3611

^ Tweaked NIT-A FOV - http://feedback.rhsmods.org/view.php?id=4954

^ Added additional turret related hitpoints & firegeomtry to Tigr-STS

^ Added optic destruction to AGS-30

^ Tweaked PKM firegeometry

^ Tweaked geometry phys of Metis,  NSVT & KORD - http://feedback.rhsmods.org/view.php?id=2130

^ Removed autocenter = 0 from SPG-9 & Kornet - those vehicles might end up in different locations!

^ Added buoyancy param to static weapons

^ Updated RHS loader to Old Man update

^ Added new inventory icons for UMBTS backpacks

^ Tweaked load of UMBTS backpack - http://feedback.rhsmods.org/view.php?id=5622

^ Updated icon for SVD mag - http://feedback.rhsmods.org/view.php?id=5616

^ Tweaked default magazines on plum variants of AK74 & AKS74 - http://feedback.rhsmods.org/view.php?id=5615

^ Improved PSO-1 ADS handling with some more exotic weapons and Zeus

^ Improved camera movement on static weapons

^ Tweaks to weapon inertia

^ Tweaks to JR configuration

^ Added tooltips for some of the Russian missiles
{CHANGESIMPROVED}

## FIXED IN 0.5.1

@ Fixed PBO prefixes of new addons - revision version was not stored correctly in them

@ Fixed convexity of PG7VL magazine proxy

@ Fixed T90AM/SM was able to use searchlight which it doesnt have - http://feedback.rhsmods.org/view.php?id=5373

@ Some of the tank ATGMs were missing from magazine well

@ Renamed BMK tug to BKM Tug, changed all pathing

@ Fixed BMD-1/2 secondary explosion

@ CfgPatches fixes for MSV troops

@ Fixed build problems with shadow volume 1000 in GAZ66, renumbered to 100

@ 1P78 had references to RHS: USAF mod

@ Returned BTR 70 & 80 interior cargo capacity to 8 seats - http://feedback.rhsmods.org/view.php?id=5389

@ Mi-8 gunners are now longer marked as primaryGunners - attempt to fix http://feedback.rhsmods.org/view.php?id=5398

@ Mi-8MTV3 was missing supply memory point - http://feedback.rhsmods.org/view.php?id=5399

@ Fixed BMK-T ghost LOD - http://feedback.rhsmods.org/view.php?id=5444

@ Fixed VOG-25P trigger reliability - http://feedback.rhsmods.org/view.php?id=5464

@ Fixed auto track on modern T tanks was loosing lock too easily

@ Fixed Mi-28 ejecting dead AIs

@ Fixed typo in T80B enginePower - http://feedback.rhsmods.org/view.php?id=5486

@ Fixed Tochka-U driver initial view - http://feedback.rhsmods.org/view.php?id=5424

@ DIRCM was affecting radar guided missiles - http://feedback.rhsmods.org/view.php?id=5502

@ DTK had non triangulated faces in 2nd shadow LOD

@ Fixed missing tracer on 7BT3 magazine - http://feedback.rhsmods.org/view.php?id=5439

@ Mi-24 cargo compartment wasn't using interior glass material - http://feedback.rhsmods.org/view.php?id=5427

@ Fixed T80 engine startup sound was missing range - http://feedback.rhsmods.org/view.php?id=5421

@ Fixed Ka-52 & Mi-28 horizon movement in HUD - http://feedback.rhsmods.org/view.php?id=5504

@ SPO-15 now reports radars which are configured as a static weapon - http://feedback.rhsmods.org/view.php?id=5529

@ MiG29SM gun indicator now properly shows ammo count again after moving flares to pylons

@ UAZ middle mirror was mirrored in wrong way - http://feedback.rhsmods.org/view.php?id=5534

@ Cleaned up geomtries of rhs_pylon_m_9m127_6x.p3d - http://feedback.rhsmods.org/view.php?id=5546

@ Fixed duplicated hitpoints error on Tigr-STS - http://feedback.rhsmods.org/view.php?id=5545

@ Readded LG munition to D30 & 2S1 - http://feedback.rhsmods.org/view.php?id=5551

@ Fixed .rpt error about "dimension should be array of 2" for static weapons

@ GAZ Tigr hull hitpoint was tied to fuel memory points resulting in quite easy explosion of whole vehicle - http://feedback.rhsmods.org/view.php?id=5533

@ Fixed PSO-1 zeroing changes when switching to ironsights - http://feedback.rhsmods.org/view.php?id=5561

@ Fixed non closed 2nd shadow LOD on 1PN138 - http://feedback.rhsmods.org/view.php?id=5608

@ Fixed wrong selection in last LOD of RShG-2 - http://feedback.rhsmods.org/view.php?id=5607

@ Fixed typo in Russian translation - http://feedback.rhsmods.org/view.php?id=5614

@ Fixed Tigr STS & Tigr M geometries - http://feedback.rhsmods.org/view.php?id=5634

@ Fixed some reload sounds on static weapons

@ Fixed missing NVG shadow in view pilot

@ Triangulated 2nd shadow lod of Tigr wheels
{CHANGESFIXED}

## REMOVED IN 0.5.1
{CHANGESREMOVED}

