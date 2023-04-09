import os
import pathlib
import sys
from loguru import logger

import lib.any_format
import lib.properties
import lib.json5
from lib.get_settings import Config, read_args

#TODO: Add error handling for missing files on patch side
#TODO: Automatically grab and run the script from Curseforge.  Provide a CLI
# arg for running this on an already downloaded world vs fresh init.  CLI arg for version or "latest" nice to have too.
#TODO: Add migration warning for missing keys on target side
#TODO: delete the world folder at the destination that's generated with initial start
#TODO: zip the patch server folder for upload

def splice_path(source_path: pathlib.Path, source_base_dir: str, target_base_dir: str) -> str:
    # Get path relative to local patch folder e.g. ./srv
    source_relative = source_path.relative_to(source_base_dir)
    dest_path = pathlib.Path(target_base_dir).joinpath(source_relative)

    return dest_path.absolute()

def handle_special_folders(entry: pathlib.Path, config: Config):
    if entry.name == 'mods':
        logger.info("Copying mods over")
        mods_path = os.path.join(config.target_folder, "mods")
        lib.any_format.folder_copy(entry.absolute(), mods_path)
    else:
        logger.info(f'Found folder in special folders but no method available to handle it: ${entry.absolute()}')

def handle_file(source_file: pathlib.Path, dest_file: str):
    ext = source_file.suffix
    if ext == '.json' or ext == '.json5':
        lib.json5.copy_config(source_file.absolute(), dest_file)
    elif ext == '.properties':
        lib.properties.copy_config(source_file.absolute(), dest_file)
    else:
        logger.warning(f'Unsupported file format {ext}')

def iterate_source_dir(directory: pathlib.Path, config: Config):
    for entry in directory.iterdir():
        if entry.is_file():
            dest_path = splice_path(entry, config.source_folder, config.target_folder)
            #logger.info(f'source: {entry.absolute()} | target: {dest_path}')
            handle_file(entry, dest_path)
        elif entry.name in special_folders:
            handle_special_folders(entry, config)
        else:
            iterate_source_dir(entry, config)

def validate_directory(input_path: str, name: str) -> pathlib.Path:
    path = pathlib.Path(input_path)
    if not path.exists():
        logger.error(f'{name} path {input_path} does not exist')
        return False

    if not path.is_dir():
        logger.error(f'{name} path must be a directory')
        return False

    return path

##----------------------------------------------

app_config = read_args()
special_folders = ['mods']

logger.info("Starting config merge")
src_path = validate_directory(app_config.source_folder, "Source")
tgt_path = validate_directory(app_config.target_folder, "Target")

if not src_path or not tgt_path:
    sys.exit(-1)

iterate_source_dir(src_path, app_config)
logger.success("Done")
