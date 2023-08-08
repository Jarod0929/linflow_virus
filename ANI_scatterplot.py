import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import sys

def main(country):
    os.chdir("linflow")

    df_ANIm = pd.read_csv(country + "/output/combined_ANIm.csv")

    df_pyani = pd.read_csv(country + "/output/pyani_combined_ANIm.csv")

    ANIm = []
    mism = []

    for col in range(len(df_ANIm.columns) - 1):
        for row in range(col):
            if not (col-1 == row):
                arr = df_ANIm[df_ANIm.columns[col]][row].split(sep="/")
                ANIm.append(1 - float(arr[0]))
                mism.append(float(arr[1]))

    pyani = []

    for col in range(len(df_pyani.columns) - 1):
        for row in range(col):
            if not (col-1 == row):
                arr = df_pyani[df_pyani.columns[col]][row].split(sep="/")
                pyani.append(1 - float(arr[0]))

    a, b = np.polyfit(pyani, mism, 1)

    plt.scatter(pyani, mism)
    
    # Line of best fit

    pred_mismatches = [x * a + b for x in pyani]

    plt.plot(pyani,pred_mismatches, "b")

    # Line of predicted mismatches

    L = 29903
    pred_mismatches = [L * x for x in ANIm]

    plt.plot(ANIm, pred_mismatches, "r")

    plt.xlabel("1 - ANIm")
    plt.ylabel("mismatches")

    plt.savefig(country + "/output/ANIm_scatter.png")

    os.chdir("../")


if __name__ == "__main__":
    main(sys.argv[1])
