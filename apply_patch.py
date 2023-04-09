import os

import lib.any_format
import lib.properties
import lib.json5
import lib.get_settings

#TODO: Abstract the path and extension logic out to handle things dynamcially
#TODO: Automatically grab and run the script from Curseforge.  Provide a CLI
# arg for running this on an already downloaded world vs fresh init.  CLI arg for version or "latest" nice to have too.
#TODO: Add error handling for missing files on patch side
#TODO: Add migration warning for missing keys on target side

config = lib.get_settings.read_args()

#Apply OPS file
opsPath = os.path.join(config.target_folder, "ops.json")
lib.any_format.file_copy('./srv/ops.json', opsPath)

# Apply properties file
print("Copying server.properties config over...")
propertiesDestPath = os.path.join(config.target_folder, "server.properties")
lib.properties.copy_config('./srv/server.properties', propertiesDestPath)

# Copy mods over
print("Copying mods over")
modsPath = os.path.join(config.target_folder, "mods")
lib.any_format.folder_copy('./srv/mods', modsPath)

# Set mod configs
## Set waystone config
print("Copying waystone config")
fwaystone_dest_path = os.path.join(config.target_folder, 'config/fwaystones/config.json5')
lib.json5.copy_config('./srv/config/fwaystones/config.json5', fwaystone_dest_path)

#TODO: delete the world folder at the destination that's generated with initial start
#TODO: zip the patch server folder for upload
