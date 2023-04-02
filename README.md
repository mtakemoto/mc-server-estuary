# Minecraft Server - Estuary
> Running All of Fabric 6

## Description
This folder contains customizations for Matt's semi-custom Minecraft server.

## Server Optimization Notes
https://github.com/YouHaveTrouble/minecraft-optimization

https://gist.github.com/Obydux/55b967f5dcc00633fe895e5a473363d5

## Server Upgrade Instructions
1. Download AOF Server Pack https://www.curseforge.com/minecraft/modpacks/all-of-fabric-6
1. Stop Server from Server Management > Console
1. Start Server Backup from Server Management > Backup
1. After backup has completed, make any required changes to Minecraft version or Fabric Loader in Server Management > Settings
1. Unzip AOF Server Pack locally and manually merge the files in this repo with the server pack. #TODO Create diff and patch to apply changes.
1. Rezip modified server pack
1. Download backup and extract world files #TODO change this procedure to stash the world files in a temp directory so we don't have to download/upload
1. Delete all files on server from control pannel
1. SFTP modified server modpack and worldfiles to the server
1. Unzip modified server modpack on the server
1. Start server

## Script Dev
1. install pipenv with `pip install --user pipenv`
1. run `pipenv install --dev`
1. run `pipenv --py` to get the path to the 🐍 virtualenv executable
1. `ctrl-shift-p` and type `python interperter`
1. Paste in the path from the previous command
1. You've got VSCode linting now 👍

## Rollback
1. From backup control Panel, choose restore.

## Server Upgrade Automation
TODO