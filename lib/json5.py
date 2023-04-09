import json
import os
from jsonmerge import merge
from loguru import logger

#TODO: this should use the actual JSON5 library.
def copy_config(source_file, dest_file):
    logger.info(f'Merging JSON file {source_file}')
    with open(source_file, 'r', encoding='UTF-8') as f:
        fwaystone_patch = json.load(f)
        with open(dest_file, 'r+', encoding='UTF-8') as dest_fd:
            not_empty_file = os.stat(dest_file).st_size > 0
            dest_dict = {}
            if not_empty_file:
                dest_dict = json.load(dest_fd)

            #overwrite 1st file with 2nd patch
            result = merge(dest_dict, fwaystone_patch)
            result_str = json.dumps(result, indent=4)
            dest_fd.seek(0)
            dest_fd.truncate()
            dest_fd.write(result_str)

    logger.success(f'Successfully merged JSON file {dest_file}')
