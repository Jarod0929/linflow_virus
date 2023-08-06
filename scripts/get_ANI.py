import pandas as pd

import os
import sys
def main(country):
    cmd = "mkdir " + country + "/inter/ANIm_dir"
    os.system(cmd)

    cmd = "average_nucleotide_identity.py -i " + country + "/inter/filtered_fastas/ -o " + country + "/inter/ANIm_dir -m ANIm -g -f"
    os.system(cmd)

    cmd = "mv " + country + "/inter/ANIm_dir/ANIm_percentage_identity.tab " + country + "/inter/"
    os.system(cmd)

    cmd = "rm -r " + country + "/inter/ANIm_dir"
    os.system(cmd)

if __name__ == "__main__":
    main(sys.argv[1])
