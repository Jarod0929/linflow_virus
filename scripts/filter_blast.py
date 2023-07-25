import pandas as pd
import os
import sys

def main(country):
    os.chdir('linflow')

    df = pd.read_csv(country + "/inter/BLAST.txt", sep="\t", header=None)

    df = df[df[3]>29800]

    df_new = df.iloc[:, [1,2,4 8, 9]]
    df_new.rename({1:"sseqid",2:"identity%", 4:"mismatches" 8:"sstart",9:"send"},axis =1, inplace=True)

    arr = df_new['sseqid'].array
    new_arr = []
    strain_arr = []
    for i in range(len(arr)):
        temp = arr[i].split('|')
        new_arr.append(temp[1] + ".fasta")
        strain_arr.append(temp[1])

    df_new['sseqid'] = new_arr
    df_new['strain'] = strain_arr

    df_new.to_csv(country + "/inter/blast_list.csv", index=False)

    os.chdir('../')

if __name__ == "__main__":
    main(sys.argv[1])