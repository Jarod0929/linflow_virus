import pandas as pd
import os
import sys

def main(country):
    df_blast = pd.read_csv(country + "/inter/blast_list.csv")

    df_meta = pd.read_csv(country + "/input/metadata.tsv", sep="\t")

    df_meta = df_meta[["Accession ID", "Collection date", "Location", "Lineage"]]

    df_meta.rename({"Accession ID":"strain", "Collection date":"collection date", "Location":"location", "Lineage":"lineage"}, axis=1, inplace=True)

    df = df_blast.merge(df_meta, on='strain', how='left')

    df.rename({"sseqid": "genome file"}, axis=1, inplace=True)

    df.to_csv(country + "/output/metadata.csv", index=False)

if __name__ == "__main__":
    main(sys.argv[1])
