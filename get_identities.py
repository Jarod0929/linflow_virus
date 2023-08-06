import pandas as pd

from Bio import pairwise2
from Bio.Seq import Seq

import os
import sys

def main(country):

    os.chdir("linflow")

    df_ANIm = pd.read_csv(country + "/inter/ANIm_percentage_identity.tab", sep='\t')

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
                seq = seq + line.replace('\n', '')
        sequences.append(seq)


    for col in range(1,len(df_ed.columns)):
        name_col = df_ed.columns[col]

        for row in range(1,col+1):
            name_row = df_ed.columns[row]
            print(col, row)

            if col == row:
                val = 1
            else:
                seq1 = Seq(sequences[col-1])
                seq2 = Seq(sequences[row-1])

                alignments = pairwise2.align.globalms(seq1,seq2, 2, -3, -5, -2)

                ali_seq1 = alignments[0][0]

                ali_seq2 = alignments[0][1]

                identities = sum(a == b for a, b in zip(ali_seq1, ali_seq2))
                alignment_length = len(ali_seq1)

                val = identities / alignment_length



            df_ed[name_col][row-1] = val
            df_ed[name_row][col-1] = val


    df_ed.to_csv(country + "/inter/global_identities.csv", index=False)

    os.chdir("../")

if __name__ == "__main__":
    main(sys.argv[1])
