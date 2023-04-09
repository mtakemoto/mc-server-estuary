import argparse
import os

class Config:
    target_folder: str

def read_args() -> Config:
    my_config = Config()
    parser = argparse.ArgumentParser(
                        prog='Allium - A Minecraft server config tool',
                        description='Handles merging of server customizations with a new modpack version',
                        epilog='Whats an epilog')

    parser.add_argument('-t', '--target_folder', type=os.path.abspath)
    args = parser.parse_args()

    if(args.target_folder is None):
        print("Please download and initialize the new modpack before running this script on it")
        my_config.target_folder = input('Path to the new modpack version: ')
    else:
        my_config.target_folder = args.target_folder

    return my_config
