# Changelog Legend

+ Added

- Removed

@ Fixed

^ Improved

# 0.4.8

## ADDED IN 0.4.8
{CHANGESADDED}

## IMPROVED IN 0.4.8

^ Reduced cost of 45ACP ammo - AI should no longer prefer using Colt over rifle

^ Reduced AH-64 FCR range to 8km from 11

^ Increased emissive value of AH-64 MFDs

^ Improved PNVS accuracy (missing AGL to ASL conversion)

^ SU-230A SpecterDR scopes `descriptionShort` now denotes them as being for 7.62mm weapons

^ Improved PNVS deinitialization

^ Added flashing cross in flight mode when PNSV is out of its limits

^ Increased SLAT armor minimal hit - no longer destroyable with small firearms

^ Moved back AH-64 pilot cockpit light to reduce flare effect during night

^ Added proper nameSound parameter to smoke shells

^ IHADSS PNVS view is no longer working when PNVS or cockpit electronic systems are damaged

^ Tweaked Bunker Busters TOWs with submunition parameters - they should be able to penetrate light structures and spread thermobaric blast wave inside

^ Another tweak to Hellfire accuracy

^ Added maddog autoseek to AIM-120 missiles

^ Tweaked M230 AI dispersion coef - AI should be more accurate

^ Increased Mk82 bomb damage to be in line with GBU-12

^ Improved HIMARS cargo shadow LOD

^ Added dedicated driver anim to HIMARS

^ Adjusted default radar range in info panels

^ Added geometry occluder to HIMARS cargo LOD

^ Tweaked HP of ERA blocks on USAF vehicles

^ `descriptionShort` property for MLRS/HIMARS magazines

^ Added experimental IHADSS workaround for user with triple monitor setup (PiP ratio)

^ Increased minimal hit for ERA blocks so they are no longer triggered by 12.7mm rounds

^ Corrected SLAP bullets muzzle velocity

^ Adjusted tracks armor for USAF vehicles

^ Added scripted particle effects to HIMARS (workaround for fire particles not working with pylon weapons - still WIP, missing dust circle and position has sometimes inncorrect offset)
{CHANGESIMPROVED}

## FIXED IN 0.4.8

@ Fixed Mk-14 ironsight

@ Fixed M2 Bradleys hull hitpoints being immortal

@ Fixed M2A2 (basic without BUSK) was missing tracks hitpoints

@ Fixed CH-53 joystick was moving in wrong direction

@ Fixed woodland AH-64 crew was missing IHADSS helmet during night

@ Fixed PNVS turning off after going into optic mode

@ Fixed AI units with gripods were selecting pistols after spawning

@ Fixed script error after being killed when using IHADSS

@ Fixed AH-64 MFD had big 0 when using AFM & extra gauges were enabled in options

@ Glass on HIMARS right-hand door did not follow door opening animation

@ Disabled 'top' versions of laser attachments on MP7A1. They don't fit

@ PNVS movement limits were inverted (forgot that min & max values in pilotCamera class are inverted...)

@ Fixed potential script error in MFD switching script

@ Some cfgweapons classes (mainly headgear) missing `dlc = "RHS_USAF";` attribute

@ Vehicle-in-Vehicle `dimensions[]` memory points were not properly set up in several FMTV and HEMTT variants

@ Fixed M109 destruction materials

@ Fixed some rare script error when TADS view was shown on MFD

@ M2 Bradley cargo had fault cargoProxyIndexes

@ Fixed AH-64 & AH-1Z helicopter HMD target icon

@ Removed M142 HIMARS driver turn out action

@ Fixed A10A landing gear light

@ Fixed gripod system so it keeps currently loaded magazine when transforming

@ SPC marksman vest shadow would break when the vest was retextured (rogue 'camo' selection in SVLOD)
{CHANGESFIXED}

## REMOVED IN 0.4.8

- Cleared out some unused magazine classnames for 12x MLRS rockets. No longer needed for their intended purpose
{CHANGESREMOVED}

