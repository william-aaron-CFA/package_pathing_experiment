#!/proj/sot/ska3/flight/bin/python

def write_junk_file(config):
    dir = config['OUTPUT_DIR']
    with open(f"{dir}/test.txt", 'a+') as f:
        f.write("I am writing junk.\n")