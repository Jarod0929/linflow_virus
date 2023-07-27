import pandas as pd
import numpy as np
import editdistance

import os
import sys

def main(country):
    #CREATED NEW ENV with pyani

    os.chdir("linflow")

    cmd = "unzip " + country + "/inter/filtered_" + country + "_fastas.zip"
    os.system(cmd)

    #pyani

    cmd = "mkdir " + country + "/inter/ANIm_dir"
    os.system(cmd)

    cmd = "average_nucleotide_identity.py -i " + country + "/inter/filtered_fastas/ -o " + country + "/inter/ANIm_dir -m ANIm -g -f"
    os.system(cmd)

    cmd = "mv " + country + "/inter/ANIm_dir/ANIm_similarity_errors.tab " + country + "/inter/"
    os.system(cmd)

    cmd = "rm -r " + country + "/inter/ANIm_dir"
    os.system(cmd)

    # #edit distance

    df_ANIm = pd.read_csv(country + "/inter/ANIm_similarity_errors.tab", sep='\t')

    df_ANIm.rename(columns={df_ANIm.columns[0]:"genome_file"}, inplace=True)


    df_ed = pd.DataFrame(columns = df_ANIm.columns)
    df_ed["genome_file"] = df_ANIm["genome_file"]

    sequences = []
    for i in range(1, len(df_ed.columns)):
        name_col = df_ed.columns[i]
        f = open(country + "/inter/filtered_fastas/" + name_col + ".fasta", "r")
        seq =""
        for line in f:
            if (line[0] != ">"):
                seq = seq + line
        sequences.append(seq)

    for col in range(1,len(df_ed.columns)+1):
        name_col = df_ed.columns[col]

        for row in range(1,col):
            name_row = df_ed.columns[row]
            print(col, row)

            if col == row:
                val = 0
            else:
                val = editdistance.eval(sequences[col-1], sequences[row-1])
            df_ed[name_col][row-1] = val
            df_ed[name_row][col-1] = val

    df_ed.to_csv(country + "/inter/editdistance.csv", index=False)

    cmd = "rm -r " + country + "/inter/filtered_fastas"
    os.system(cmd)

    #combining two matrices
    df_ANIm = pd.read_csv(country + "/inter/ANIm_similarity_errors.tab", sep='\t')
    df_ed = pd.read_csv(country + "/inter/editdistance.csv")

    df = pd.DataFrame(columns = df_ANIm.columns)
    df_ANIm.rename(columns={df_ANIm.columns[0]:"genome_file"}, inplace=True)
    df["genome_file"]= df_ANIm["genome_file"]

    df = df.astype("string")

    for col in range(1, len(df_ANIm.columns)):
        name_col = df_ANIm.columns[col]
        for row in range(0, len(df_ANIm.columns)-1):
            df_ANIm[name_col][row] = str(df_ANIm[name_col][row]) + "/" + str(df_ed[name_col][row])

    df_ANIm.to_csv(country + "/output/combined_ANIm.csv", index=False)

    os.chdir("../")

if __name__ == "__main__":
    main(sys.argv[1])
