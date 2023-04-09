import argparse
import os

class Config:
    source_folder: str
    target_folder: str

def read_args() -> Config:
    my_config = Config()
    parser = argparse.ArgumentParser(
                prog='Allium - A Minecraft server config tool',
                description='Handles merging of server customizations with a new modpack version',
                epilog='Whats an epilog')

    parser.add_argument('-s', '--source_folder', type=os.path.abspath, default='./srv')
    parser.add_argument('-t', '--target_folder', type=os.path.abspath, required=True)
    args = parser.parse_args()

    my_config.source_folder = args.source_folder
    my_config.target_folder = args.target_folder

    return my_config
