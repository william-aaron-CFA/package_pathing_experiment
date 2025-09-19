#!/proj/sot/ska3/flight/bin/python
import os
import package
import argparse
from configparser import ConfigParser, ExtendedInterpolation
_CONFIGS = ConfigParser(interpolation = ExtendedInterpolation(), default_section='primary')
_CONFIGS.read('config.ini')

def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices = ['primary', 'secondary', 'test'], required = True, help = "Determine configuration of script run.")
    return parser.parse_args()

def load_config(mode):
    """
    Function to prepare the selected configuration for the script run of package
    """
    config = _CONFIGS[mode]
    if mode == 'test':
        #: Create test directories for file output when testing a new development.
        os.makedirs(config['OUTPUT_DIR'], exist_ok = True)
    return config

if __name__ == "__main__":
    #: Determine Config Section
    args = get_options()
    config = load_config(args.mode)
    package.print_config(config)
    package.write_junk_file(config)