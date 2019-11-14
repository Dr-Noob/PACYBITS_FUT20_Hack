# PACYBITS FUT20 HACK (ANDROID ONLY)

This repository contains code to hack the game, so you can obtain all the cards in the game,infinite coins and tokens

### WIP!
This is a wip, currently only supports adding all the icons

### Usage
1. You need to get the base xml file (`com.pacybits.pacybitsfut20.preferences.xml`). This file is located in android at `/data/data/com.pacybitsfut20/shared_prefs`. You will need root permissions to get and replace this file. Then, run the `hack.py` script, giving it the file as argument. The script will generate a hacked xml, which you will need to copy to the same folder, replacing the old one. 
2. In my case, I also need to restore SELinux permissions on the file, since writing a new file sets different SELinux permissions from the files already present there. Therefore, I must restore the permissions to default (this is easy in Root Explorer).
3. It seems that you also need to change the file `com.google.android.gms.measurement.prefs.xml`, modifying the `last_pause_time` field. You must change the timestamp to be after the modification time of the other file.

### Files
* hack.py: Needs a base xml file and creates a hacked one (with all the players)
* decrypt.py: Decodes the base xml file (which is encoided in base64) to plain text
* encrypt.py: Encodes a decoded xml file to base64 again
