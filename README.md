# Allium: Smart Minecraft server config merge tool

## Goals
- Provide a low-code way to manage Minecraft server and mod settings across multiple versions of a modpack
- Problem:
  - You have a modded Minecraft server that has some config changes in various files like `server.properties`, the `ops.json` file and various modpack configs (e.g. waystones)
  - When a new modpack version comes out, those changes need to be applied to the latest version of the modpack
  - Modpack updates can be frequent, so automation is helpful
  - You could fork the modpack repo and rebuild it, but that...
    - Requires you to be fairly skilled with Git (able to merge upstream changes, handle conflicts)
    - And even if you are, you'll still have to deal with merge conflicts in your spare time.  Wouldn't you rather be playing on your server?
  - Mods may intoduce breaking config changes

## Solution (?)
Allium allows you to maintain a patch folder.  This is a folder with identical structure to your server, with each file **containing only the changes** (not the entire file) that you've made on top of the server defaults.
For each of these patch files, Allium will load the corresponding file in your new server pack and update the value.

## Requirements
- Python 3.x
- Pipenv (?)
- TODO: make it easier to run the tool without cloning the directory

## Usage
1. Download your server modpack locally and run the installer
1. When finished, copy the path
1. Run Allium (instructions TBD)
  1. `python apply-patch.py -t "path-to-your-server-folder"`
1. ???
1. Go play Minecraft

## Script Dev
1. install pipenv with `pip install --user pipenv`
1. run `pipenv install --dev`
1. run `pipenv --py` to get the path to the 🐍 virtualenv executable
1. `ctrl-shift-p` and type `python interperter`
1. Paste in the path from the previous command
1. You've got VSCode linting now 👍