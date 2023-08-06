import pandas as pd
import numpy as np
from Bio import Align

import os
import sys

def get_mismatch(alignment, seq1, seq2):
    tup = alignment[0].aligned
    pos1 = 0
    pos2 = 0
    mis = 0

    if len(tup[0]) == 0 or len(tup[1]) == 0:
        return 0
    
    t1 = tup[0][pos1][0]
    t2 = tup[1][pos2][0]

    while(True):

        if (t1 >= tup[0][pos1][1]):
            pos1 += 1
            if (pos1 >= len(tup[0])):
                break
            t1 = tup[0][pos1][0]
        
        if (t2 >= tup[1][pos2][1]):
            pos2 += 1
            if (pos2 >= len(tup[1])):
                break
            t2 = tup[1][pos2][0]

        if (seq1[t1] != seq2[t2]):
            mis += 1

        t1 += 1
        t2 += 1
        
    return mis

def get_gaps(alignment, seq1, seq2):
    tup = alignment[0].aligned

    gap1 = 0
    prev = 0
    for i in range(len(tup[0])):
        gap1 = tup[0][i][0] - prev + gap1
        prev = tup[0][i][1]

    gap2 = 0
    prev = 0
    for i in range(len(tup[1])):
        gap2 = tup[1][i][0] - prev + gap2
        prev = tup[1][i][1]

    ex_gap = abs(len(seq1) - len(seq2)) - abs(gap1 - gap2)

    return gap1 + gap2 + ex_gap

def main(country):
    #CREATED NEW ENV with pyani

    os.chdir("linflow")

    cmd = "unzip " + country + "/inter/filtered_" + country + "_fastas.zip"
    #os.system(cmd)

    # #pyani
    if not os.path.isfile("linflow/" + country + "/inter/ANIm_percentage_identity.tab"):
        cmd = "python scripts/get_ANI.py "+country
        os.system(cmd)

    #edit distance
    if not os.path.isfile("linflow/" + country + "/inter/global_alignment.csv"):
        cmd = "python scripts/global_alignment.py "+country
        os.system(cmd)


    cmd = "rm -r " + country + "/inter/filtered_fastas"
    #os.system(cmd)

    #combining two matrices
    df_ANIm = pd.read_csv(country + "/inter/ANIm_percentage_identity.tab", sep='\t')
    #df_ANIm = pd.read_csv(country + "/inter/global_identities.csv")
    df_ed = pd.read_csv(country + "/inter/global_alignment.csv")

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
