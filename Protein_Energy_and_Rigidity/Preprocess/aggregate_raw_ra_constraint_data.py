import sys
import os
import csv


#Input configuration
dir = "./preliminary_exp_output/"
pdbID = sys.argv[1].upper()
outFilename = pdbID+"_raw_ra_bond_data.csv"
if(len(sys.argv) > 2):
    if sys.argv[2] == "-b":
        dir += "baselines/"
        outFilename = "base_"+outFilename

dir += "multiMutant_out/"

tmp = os.listdir(dir)
mutName = ""
for folder in tmp:
    if folder[:len(pdbID)] == pdbID:
        mutName = folder
        break
dir+=mutName
#example dir: "/preliminary_exp_output/multiMutant_out/2DM8G2837:2843_out/"

#Output configuration
columns = ["PDBID", "MUTATION", "CONSTRAINT", "COUNT"]

outDir = "processed_data/"+pdbID

if not os.path.exists("processed_data"):
    os.makedirs("processed_data")
if not os.path.exists(outDir):
    os.makedirs(outDir)

out = open(outDir+"/"+outFilename,"w+")
writer = csv.writer(out, delimiter=",")
writer.writerow(columns)


numRows = 0

# Get the list of mutations from the directory entries
mutations = os.listdir(dir)

# For each mutation, open the rigidity analysis log file and add all constraint counts to the output file
for mutation in mutations:
    fileNameRoot = "{0}/{1}/{2}.all.ra.out_RA/{2}.all.processed.pdb/user/{2}.all.processed.pdb".format(dir,mutation, pdbID)
    if len(pdbID) > 4:
        fileNameRoot = "{0}/{1}/{3}.all.ra.out_RA/{3}.all.processed.pdb/user/{3}.all.processed.pdb".format(dir,mutation,pdbID,pdbID[:4])
    filename = fileNameRoot+"_MetricsPDB.txt"
    if os.path.exists(filename):
        log = open(filename, "r") 
        mutationStr = mutation.split(".")[1]
        reachedContstraitTypes = False
        for line in log:
            line = line[:-1].strip()
            if( not reachedContstraitTypes):
                if line == "=========================":
                    reachedContstraitTypes = True
            else:
                split = line.split(": ")
                data = [pdbID, mutationStr, split[0], split[1]]
                writer.writerow(data)
                numRows += 1
        log.close()

# Finish
out.close()
print("Aggregated {0} logs into {1}, {2} rows".format(len(mutations), outFilename, numRows))