import pandas as pd
import numpy as np
import os
import sys

def main(country):
    os.chdir('linflow')

    df = pd.read_csv(country + "/inter/BLAST.txt", sep="\t", header=None)

    # length greater than 29800
    df = df[df[3]>29800]

    df_new = df.iloc[:, [1,2, 3, 4, 8, 9]]
    df_new.rename({1:"sseqid", 2:"identity%",3: "length", 4:"mismatches", 8:"sstart",9:"send"},axis =1, inplace=True)

    arr = df_new['sseqid'].array
    new_arr = []
    strain_arr = []
    for i in range(len(arr)):
        temp = arr[i].split('|')
        new_arr.append(temp[1] + ".fasta")
        strain_arr.append(temp[1])

    df_new['sseqid'] = new_arr
    df_new['strain'] = strain_arr

    # N 
    folder = country + "/inter/"

    cmd = "unzip "+ folder + country + '_fastas.zip'
    os.system(cmd)

    files = df_new["sseqid"].to_numpy()
    sequences = []

    for i in range(len(files)):

        f = open(country + "/inter/fastas/" + files[i], "r")
        seq = ""
        for line in f:
            if (line[0] != ">"):
                seq = seq + line.replace('\n', '')
        sequences.append(seq)
        f.close()

    N = []
    for i in range(len(sequences)):
        N.append(sequences[i].count("N"))

    df_new["num_N"] = N

    df_new["%N"] = df_new["num_N"]/df_new["length"]

    df_new = df_new[df_new["%N"] < 0.01]

    cmd = "rm -r " + folder + "fastas"
    os.system(cmd)

    df_new.to_csv(country + "/inter/blast_list.csv", index=False)

    os.chdir('../')

if __name__ == "__main__":
    main(sys.argv[1])