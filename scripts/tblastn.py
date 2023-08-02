import os
import sys

def main(country):
    os.chdir('linflow')

    cmd = "makeblastdb -in " + country + "/input/"+country+"_full.fasta -dbtype nucl -out blast_"+country
    os.system(cmd)

    cmd = "tblastn -query ../seq/membrane_p.fasta -db blast_"+country+" -out " + country + "/inter/prot_BLAST.txt -outfmt 6"
    os.system(cmd)

    cmd = "rm blast_"+country+".nhr"
    os.system(cmd)
    cmd = "rm blast_"+country+".nin"
    os.system(cmd)
    cmd = "rm blast_"+country+".nsq"
    os.system(cmd)

    os.chdir('../')

if __name__ == "__main__":
    main(sys.argv[1])