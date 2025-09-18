#!/proj/sot/ska3/flight/bin/python

#from configparser import ConfigParser
from configparser import ConfigParser, ExtendedInterpolation
import argparse

def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', choices = ['primary', 'secondary', 'test'], required = True, help = "Determine configuration of script run.")
    return parser.parse_args()

def write_junk_file(dir):

    with open(f"{dir}/test.txt", 'a+') as f:
        f.write("I am writing junk.\n")

def print_config_section(config_section):
    for key,value in config_section.items():
        print(f"{key} = {value}")

if __name__ == "__main__":

    args = get_options()
    #config = ConfigParser()
    config = ConfigParser(interpolation = ExtendedInterpolation(), default_section='primary')
    config.read('config.ini')
    #write_junk_file(config[args.mode]['OUTPUT_DIR'])
    #write_junk_file(config.get(args.mode, 'OUTPUT_DIR'))

    print_config_section(config[args.mode])

