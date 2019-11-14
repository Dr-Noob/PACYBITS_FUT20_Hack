# PACYBITS FUT20 HACK (ANDROID ONLY)

This repository contains code to hack the game, so you can obtain all the cards in the game,infinite coins and tokens

### WIP!
This is a wip, currently only supports adding all the icons

### Usage
You need to get the base xml file (com.pacybits.pacybitsfut20.preferences.xml). This file is located in android at `/data/data/com.pacybitsfut20/shared_prefs'. You will need root permissions to get and replace this file.

### Files
* hack.py: Needs a base xml file and creates a hacked one (with all the players)
* decrypt.py: Decodes the base xml file (which is encoided in base64) to plain text
* encrypt.py: Encodes a decoded xml file to base64 again
