import sys
import os
import csv


# Input configuration
dir = "./preliminary_exp_output/"
pdbID = sys.argv[1].upper()
outFilename = pdbID+"_raw_em_step_data.csv"
if(len(sys.argv) > 2):
    if sys.argv[2] == "-b":
        dir += "baselines/"
        outFilename = "base_"+outFilename

dir +="additional_EM_logs/"+pdbID+"_EM_logs/"


# Output configuration
columns = ["PDBID", "MUTATION", "TS", "BOND", "ANGLE", "DIHED", "IMPRP", "ELECT", "VDW", "BOUNDARY", "MISC", "KINETIC", "TOTAL", "TEMP", "POTENTIAL", "TOTAL3", "TEMPAVG"]
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

# For each mutation, open its energy minimization log file, and write each of the steps to the output file
for mutation in mutations:
    filename = dir + mutation + "/" + mutation + "_min.log"
    if os.path.exists(filename):
        log = open(filename, "r") 
        mutationStr = mutation.split(".")[1]
        for line in log:
            if not line.isspace():
                meta = line.split(":")
                if len(meta) > 1 and meta[0] == "ENERGY":
                    data = meta[1].split()
                    data.insert(0, mutationStr)
                    data.insert(0, pdbID)
                    writer.writerow(data)
                    numRows += 1
        log.close()

# Finish
out.close()
print("Aggregated {0} logs into {1}, {2} rows".format(len(mutations), outFilename, numRows))