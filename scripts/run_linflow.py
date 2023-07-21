import os
import sys

def main(country):
    os.chdir('linflow')

    folder = country + "/inter/"

    cmd = "unzip " + folder + "filtered_" + country + "_fastas.zip"
    os.system(cmd)

    cmd = "python -m linflow init "+ country + "_virus"
    os.system(cmd)

    cmd = "python -m linflow genome " + country + "_virus "\
        + "-i " + folder + "filtered_fastas "\
        + "-d " + country + "/output/metadata.csv "\
        + "-s 1 "\
        + "--no-qc"
    os.system(cmd)

    cmd = "python -m linflow summary " + country + "_virus"
    os.system(cmd)

    cmd = "mv workspaces/" + country + "_virus/lin_summary_scheme1.csv " + country + "/inter"
    os.system(cmd)

    cmd = "python -m linflow remove " + country + "_virus"
    os.system(cmd)

    cmd = "rm -r " + folder + "filtered_fastas"
    os.system(cmd)

    os.chdir('../')

if __name__ == "__main__":
    main(sys.argv[1])