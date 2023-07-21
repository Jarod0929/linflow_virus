import os
import sys

def main(country):
    folder = country + "/inter/"

    cmd = "unzip " + folder + "filtered_" + country + "_fastas.zip"
    os.system(cmd)

    os.chdir('../linflow')

    cmd = "python -m linflow init "+ country + "_virus"
    os.system(cmd)

    cmd = "python -m linflow genome " + country + "_virus "\
        + "-i ../virus_transform/" + folder + "filtered_fastas "\
        + "-d ../virus_transform/" + country + "/output/metadata.csv "\
        + "-s 1 "\
        + "--no-qc"
    os.system(cmd)

    cmd = "python -m linflow summary " + country + "_virus"
    os.system(cmd)

    cmd = "mv workspaces/" + country + "_virus/lin_summary_scheme1.csv ../virus_transform/" + country + "/inter"

    cmd = "python -m linflow remove " + country + "_virus"
    os.system(cmd)

    os.chdir('../virus_transform')

    cmd = "rm -r " + folder + "filtered_fastas"
    os.system(cmd)

if __name__ == "__main__":
    main(sys.argv[1])