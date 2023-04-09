from jproperties import Properties

def copy_config(source_file, dest_file):
    patch_config = Properties()

    with open(source_file, 'rb') as config_file:
        patch_config.load(config_file)

    with open(dest_file, 'r+b') as dest_fd:
        dest_file_config = Properties()
        dest_file_config.load(dest_fd)
        for item in patch_config.items():
            key,value = item
            print(f'Setting {key} to {value.data}')
            dest_file_config[key] = value.data

        print(f'Writing properties file to {dest_file}')
        dest_fd.seek(0)
        dest_fd.truncate()
        dest_file_config.store(dest_fd)