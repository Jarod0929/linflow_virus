import pandas as pd
import numpy as np
import shutil
import sys
import os

def main(country):
    df = pd.read_csv(country + "/inter/blast_list.csv")

    folder = country + "/inter/"

    cmd = "unzip "+ folder + country + '_fastas.zip'
    os.system(cmd)

    cmd = "mkdir " + folder + "filtered_fastas"
    os.system(cmd)

    arr = df['sseqid'].array
    not_in = []
    for i in range(len(arr)):
        if (arr[i] in os.listdir(folder + "fastas")):
            shutil.copyfile(folder + "fastas/" + arr[i], folder + "filtered_fastas/" + arr[i])
        else:
            not_in.append(arr[i])

    print("These fastas are not in:",not_in)

    cmd = "zip -r " + folder + "filtered_" + country + "_fastas.zip " + folder + "filtered_fastas" 
    os.system(cmd)

    cmd = "rm -r " + folder + "filtered_fastas"
    os.system(cmd)

    cmd = "rm -r " + folder + "fastas"
    os.system(cmd)

if __name__ == "__main__":
    main(sys.argv[1])