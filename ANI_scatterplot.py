import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import sys

def main(country):
    os.chdir("linflow")

    df_ANIm = pd.read_csv(country + "/output/combined_ANIm.csv")

    ANIm = []
    mism = []

    for col in range(len(df_ANIm.columns) - 1):
        for row in range(col):
            if not (col-1 == row):
                arr = df_ANIm[df_ANIm.columns[col]][row].split(sep="/")
                ANIm.append(1 - float(arr[0]))
                mism.append(float(arr[1]))

    a, b = np.polyfit(ANIm, mism, 1)

    plt.scatter(ANIm, mism)
    
    pred_mismatches = [x * a + b for x in ANIm]
    plt.plot(ANIm,pred_mismatches)

    plt.xlabel("1 - ANIm")
    plt.ylabel("mismatches")

    plt.savefig(country + "/output/ANIm_scatter.png")

    os.chdir("../")


if __name__ == "__main__":
    main(sys.argv[1])
