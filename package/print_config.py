#!/proj/sot/ska3/flight/bin/python

def print_config(config):
    for key,value in config.items():
        print(f"{key} = {value}")