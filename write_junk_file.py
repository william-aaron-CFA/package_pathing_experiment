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

if __name__ == "__main__":

    args = get_options()
    #config = ConfigParser()
    config = ConfigParser(interpolation = ExtendedInterpolation())
    config.read('config.ini')
    #write_junk_file(config[args.mode]['OUTPUT_DIR'])
    write_junk_file(config.get(args.mode, 'OUTPUT_DIR'))