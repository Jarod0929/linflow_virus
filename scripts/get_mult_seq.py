import pandas as pd
import numpy as np

import os
import sys

def main(country):
    os.chdir('linflow')

    cmd = "unzip " + country + "/inter/filtered_" + country + '_fastas.zip'
    #os.system(cmd)

    df = pd.read_csv(country + "/inter/prot_blast_list.csv")

    headers = []
    sequences = []

    for index,row in df.iterrows():

        f = open(country + "/inter/filtered_fastas/" + row["sseqid"], "r")
        seq = ""
        for line in f:
            if (line[0] != ">"):
                seq = seq + line.replace('\n', '')
            else:
                headers.append(line)
        sequences.append(seq[row["sstart"]: row["send"] + 1])
        f.close()

    temp = open(country + "/output/prot_" + country + ".fasta","w")
    for i in range(len(sequences)):
        temp.write(headers[i])
        t = sequences[i]
        while(len(t) > 80):
            temp.write(t[:80])
            temp.write("\n")
            t = t[80:]
        temp.write(t)
        temp.write("\n")

    temp.close()


        


    os.chdir('../')

if __name__ == "__main__":
    main(sys.argv[1])