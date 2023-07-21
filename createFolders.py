import os
import sys

def main(country):
    cmd = "mkdir linflow/" + country
    os.system(cmd)

    cmd = "mkdir linflow/" + country + "/input"
    os.system(cmd)

    cmd = "mkdir linflow/" + country + "/output"
    os.system(cmd)

    cmd = "mkdir linflow/" + country + "/inter"
    os.system(cmd)

if __name__ == "__main__":
    main(sys.argv[1])