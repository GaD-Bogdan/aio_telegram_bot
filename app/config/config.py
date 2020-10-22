import os
import yaml


USER_CONFIGS_DIR = f'config/user_configs/'
config = {}


def read_configs(dir_with_configs):
    configs_list = os.listdir(dir_with_configs)
    for config_file in configs_list:
        if 'example' in config_file:
            continue
        config_path = os.path.join(dir_with_configs, config_file)
        with open(config_path, 'r') as f:
            cnf = yaml.load(f, Loader=yaml.FullLoader)
            if cnf:
                config.update(cnf)


read_configs(USER_CONFIGS_DIR)
