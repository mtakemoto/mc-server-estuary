from jproperties import Properties
import shutil
import os
import json
from jsonmerge import merge

def copy2_verbose(src, dst):
    print('Copying {0}'.format(src))
    shutil.copy2(src,dst)

print("Please download and initialize the new modpack before running this script on it")
newModpackPath = input('Path to the new modpack version: ')

# Apply OPS file
print("Copying ops file...")
opsPath = os.path.join(newModpackPath, "ops.json")
shutil.copy2('./ops.json', opsPath)
print("Done")

# Apply properties file
print("Copying server.properties config over...")
propertiesDestPath = os.path.join(newModpackPath, "server.properties")
patchConfig = Properties()
print("Done")

with open('./server.properties', 'rb') as config_file:
    patchConfig.load(config_file)

with open(propertiesDestPath, 'r+b') as dest_file:
    destFileConfig = Properties()
    destFileConfig.load(dest_file)
    for item in patchConfig.items():
        key,value = item
        print(f'Setting {key} to {value.data}')
        destFileConfig[key] = value.data

    print(f'Writing properties file to {propertiesDestPath}')
    dest_file.seek(0)
    dest_file.truncate()
    destFileConfig.store(dest_file)

# Copy mods over
print("Copying mods over")
modsPath = os.path.join(newModpackPath, "mods")
try:
    shutil.copytree('./mods', modsPath, copy_function=copy2_verbose, dirs_exist_ok=True)
except OSError as err:
    print(err)

# Set mod configs
## Set waystone config
fwaystone_dest_path = os.path.join(newModpackPath, 'config/fwaystones/config.json5')
with open('./config/fwaystones/config.json5', 'r') as f:
    fwaystone_patch = json.load(f)
    with open(fwaystone_dest_path, 'r+') as dest_fd:
        fwaystone_dest = json.load(dest_fd)

        #overwrite 1st file with 2nd patch
        result = merge(fwaystone_dest, fwaystone_patch)
        result_str = json.dumps(result, indent=4)
        dest_fd.seek(0)
        dest_fd.truncate()
        dest_fd.write(result_str)
