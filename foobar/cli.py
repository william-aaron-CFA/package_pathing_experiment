"""
Configured run of the packaged functions from the command line

TODO: Find the best cli implementation method for the package to handle running on
pre-configured instances
https://packaging.python.org/en/latest/guides/creating-command-line-tools/
"""
import os
import argparse
import sys
print(sys.path)
from foobar import print_config
from foobar import write_junk_file

from configparser import ConfigParser, ExtendedInterpolation
_CONFIGS = ConfigParser(interpolation = ExtendedInterpolation(), default_section='primary')
_CONFIGS.read('config.ini')

def get_options():
    parser = argparse.ArgumentParser(description="Random file functions.")
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

def main():
    #: Determine Config Section
    args = get_options()
    config = load_config(args.mode)
    print_config.print_config(config)
    write_junk_file.write_junk_file(config)

if __name__ == "__main__":

    main()