import os
import sys

def main(country):

    os.chdir('linflow')

    cmd = "mkdir " + country + "/inter/fastas"
    os.system(cmd)
    
    f = open(country + "/input/" + country + "_full.fasta", "r")
    for line in f:
        if ">" == line[0]:
            if ("temp" in locals()):
                temp.close()
            arr = line.split(sep="|")
            temp = open(country + "/inter/fastas/" + arr[1] + ".fasta","w")
            temp.write(line)
        else:
            temp.write(line)
    temp.close()
    f.close()

    cmd = "zip -r " + country + "/inter/" + country + "_fastas.zip " + country + "/inter/fastas"
    os.system(cmd)

    cmd = "rm -r " + country + "/inter/fastas"
    os.system(cmd)
    
    os.chdir('../')

if __name__ == "__main__":
    main(sys.argv[1])