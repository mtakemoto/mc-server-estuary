import json
from jsonmerge import merge

def copy_config(source_file, dest_file):
    with open(source_file, 'r', encoding='UTF-8') as f:
        fwaystone_patch = json.load(f)
        with open(dest_file, 'r+', encoding='UTF-8') as dest_fd:
            fwaystone_dest = json.load(dest_fd)

            #overwrite 1st file with 2nd patch
            result = merge(fwaystone_dest, fwaystone_patch)
            result_str = json.dumps(result, indent=4)
            dest_fd.seek(0)
            dest_fd.truncate()
            dest_fd.write(result_str)