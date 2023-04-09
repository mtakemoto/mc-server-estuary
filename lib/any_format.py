import shutil

from loguru import logger

def copy2_verbose(src, dst):
    logger.info('Copying {0}'.format(src))
    shutil.copy2(src,dst)

def file_copy(source_file, dest_file):
    logger.info(f'Copying ${source_file} file...')
    shutil.copy2(source_file, dest_file)
    logger.success("File copy finished")

def folder_copy(source_path, dest_path):
    try:
        shutil.copytree(source_path, dest_path, copy_function=copy2_verbose, dirs_exist_ok=True)
    except OSError as err:
        logger.info(err)