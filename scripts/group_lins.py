import pandas as pd
import os
import sys

def main(country):
    df_blast = pd.read_csv(country + "/inter/blast_list.csv")
    df_meta = pd.read_csv(country + "/output/metadata.csv")

    df_lin = pd.read_csv(country + "/inter/lin_summary_scheme1.csv")

    df = df_blast.merge(df_meta, on='strain', how='left')

    df.rename({"genome file": "filePath"}, axis = 1, inplace=True)

    df = pd.merge(df, df_lin, on=["filePath"])

    df.sort_values(["lineage", "LIN"], inplace= True)

    df.to_csv(country + "/output/result.csv", index=False)

if __name__ == "__main__":
    main(sys.argv[1])
