#!/proj/sot/ska3/flight/bin/python

from configparser import ConfigParser, ExtendedInterpolation
import argparse
from write_junk_file import write_junk_file

_CONFIGS = ConfigParser(interpolation = ExtendedInterpolation(), default_section='primary')
_CONFIGS.read('config.ini')

def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', choices = ['primary', 'secondary', 'test'], required = True, help = "Determine configuration of script run.")
    return parser.parse_args()

def print_config_section(config_section):
    for key,value in config_section.items():
        print(f"{key} = {value}")

if __name__ == "__main__":
    #: Determine Config Section
    args = get_options()
    CONFIG = _CONFIGS[args.mode]
    print_config_section(CONFIG)
    write_junk_file(CONFIG)