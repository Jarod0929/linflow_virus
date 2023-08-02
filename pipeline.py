import os
import sys

def main(country):

    # RUNS BLAST
    cmd = "python scripts/blast.py "+country
    os.system(cmd)

    #SPLITS FASTA FILES
    cmd = "python scripts/split_fasta.py "+country
    os.system(cmd)

    #FILTERS BLAST
    cmd = "python scripts/filter_blast.py "+country
    os.system(cmd)

    #ALTERS METADATA
    cmd = "python scripts/alter_metadata.py "+country
    os.system(cmd)

    #FILTERS FASTA FILES
    cmd = "python scripts/filter_fasta.py "+country
    os.system(cmd)

    #RUN LINFLOW
    cmd = "python scripts/run_linflow.py "+country
    os.system(cmd)

    #GROUPS LINS
    cmd = "python scripts/group_lins.py "+country
    os.system(cmd)

if __name__ == "__main__":
    main(sys.argv[1])