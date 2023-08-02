import os
import sys

def main(country):
    # RUNS BLAST
    if not os.path.isfile("linflow/" + country + "/inter/BLAST.txt"):
        cmd = "python scripts/blast.py "+country
        os.system(cmd)

    #FILTERS BLAST
    if not os.path.isfile("linflow/" + country + "/inter/blast_list.csv"):
        cmd = "python scripts/filter_blast.py "+country
        os.system(cmd)

    #SPLITS FASTA FILES
    if not os.path.isfile("linflow/" + country + "/inter/" + country + "fastas.zip"):
        cmd = "python scripts/split_fasta.py "+country
        os.system(cmd)

    #FILTERS FASTA FILES
    if not os.path.isfile("linflow/" + country + "/inter/filtered_" + country + "fastas.zip"):
        cmd = "python scripts/filter_fasta.py "+country
        os.system(cmd)

    #RUNS tblastn
    cmd = "python scripts/tblastn.py "+country
    os.system(cmd)

    #FILTERS tblastn
    cmd = "python scripts/filter_tblastn.py "+country
    os.system(cmd)

    #CREATES multseq file
    cmd = "python scripts/get_mult_seq.py "+country
    os.system(cmd)

if __name__ == "__main__":
    main(sys.argv[1])