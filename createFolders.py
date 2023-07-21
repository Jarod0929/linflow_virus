import os
import sys

def main(country):
    cmd = "mkdir " + country
    os.system(cmd)

    cmd = "mkdir " + country + "/input"
    os.system(cmd)

    cmd = "mkdir " + country + "/output"
    os.system(cmd)

    cmd = "mkdir " + country + "/inter"
    os.system(cmd)

if __name__ == "__main__":
    main(sys.argv[1])