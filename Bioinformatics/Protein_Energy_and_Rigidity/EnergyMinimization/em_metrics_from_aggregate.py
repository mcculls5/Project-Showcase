import csv

#Constants

pdbBaseline = {
    #Step0, Step10, Step500
    "2DM8": [211742.8247, 137066.4115, 153.5236],
    "3RL7": [107396.2114, 84121.3893, -1683.6450],
    "MBDLG": [4138635.5726, 135386.7659, 746.4241],
    "2BYG": [404799.5093, 357807.9499, 14764.8495],
    "MBDLG2HB008": [151026.6855, 122965.1753, -1454.3302],
    "MBDLG2HB010": [124172.9443, 95512.1972, -744.2225],
    "2HE2": [61954.5214, 44311.6039, -1899.4989],
    "MBDLG3": [9999999999.9999, 45110.0224, -1189.0972]
}

groups = {
    "mbDLG_1": ["2DM8", "3RL7", "MBDLG"],
    "mbDLG_2": ["2BYG", "MBDLG2HB008", "MBDLG2HB010"],
    "mbDLG_3": ["2HE2", "MBDLG3"]
}


# Prepare output columns
columns = ["PDBID", 
           "MUTATION", 
           "INITIAL", 
           "FINAL", 
           "STEP10"]


percentThresholds = ["25", "50", "75", "90", "95"]
decimalThresholds = [0.25, 0.5, 0.75, 0.9, 0.95]

for i in range(len(percentThresholds)):
    columns.append("STEPS_MT_"+percentThresholds[i])

for i in range(len(percentThresholds)):
    columns.append("STEPS_MT10_"+percentThresholds[i])

for i in range(len(percentThresholds)):
    columns.append("STEPS_WT_"+percentThresholds[i])

for i in range(len(percentThresholds)):
    columns.append("STEPS_WT10_"+percentThresholds[i])
columns.append("STEPS_WT_100")

#For each pdbID, compute the various threshold values and metrics for both single and double-point mutations
for group in groups.keys():
    for pdb in groups[group]: # Each PDBID
        for i in range(2): # Single and Double mutations
            
             # Input configuration
            mut = ""
            if(i == 1):
                mut = "_2"
            print("../"+group+"/"+pdb+"/"+pdb+"_raw_em_step_data"+mut+".csv")
            mFile = open("../"+group+"/"+pdb+"/"+pdb+"_raw_em_step_data"+mut+".csv", "r")
            mData = csv.reader(mFile)
                
            out = open("../"+group+"/"+pdb+"/"+pdb+"_em_metrics"+mut+".csv","w" ,newline='')
            writer = csv.writer(out, delimiter=",")
            writer.writerow(columns)
            
            #Calculate the baseline thresholds
            diff = float(pdbBaseline[pdb][0]) - float(pdbBaseline[pdb][2])
            diff10 = float(pdbBaseline[pdb][1]) - float(pdbBaseline[pdb][2])
            wtThresholds =[]
            wt10Thresholds =[]
            for i in range(len(percentThresholds)):
                wtThresholds.append(float(pdbBaseline[pdb][0]) - (decimalThresholds[i]*diff))
                wt10Thresholds.append(float(pdbBaseline[pdb][1]) - (decimalThresholds[i]*diff10))

            
            
            #Prepare the output data structure
            data = {}
            
            #skip header
            next(mData)
            
            #Initialize the output data structure
            for row in mData:
                if row[1] not in data.keys():
                    data[row[1]] = {
                        "INITIAL": 0,
                        "FINAL": 0,
                        "STEP10": 0,
                        "STEPS_WT_100": 1000
                    }
                    for i in range(len(percentThresholds)):
                        # #These need to be initialized above the max stepcount (500)
                        data[row[1]]["STEPS_MT_"+percentThresholds[i]] = 1000
                        data[row[1]]["STEPS_MT10_"+percentThresholds[i]] = 1000
                        data[row[1]]["STEPS_WT_"+percentThresholds[i]] = 1000
                        data[row[1]]["STEPS_WT10_"+percentThresholds[i]] = 1000
                        
                        
                    data[row[1]]["PDBID"] = pdb
                    data[row[1]]["MUTATION"] = row[1]
                
                if int(row[2]) == 0:
                    data[row[1]]["INITIAL"] = float(row[3])
                if int(row[2]) == 10:
                    data[row[1]]["STEP10"] = float(row[3])
                if int(row[2]) == 500:
                    data[row[1]]["FINAL"] = float(row[3])
                        

            # Calculate initial metrics
            for mutant in data.keys():
                diff = data[mutant]["INITIAL"] - data[mutant]["FINAL"]
                diff10 = data[mutant]["STEP10"] - data[mutant]["FINAL"]
                for i in range(len(percentThresholds)): 
                    data[mutant]["MT_"+percentThresholds[i]] = data[mutant]["INITIAL"] - (decimalThresholds[i] * diff)
                    data[mutant]["MT10_"+percentThresholds[i]] = data[mutant]["STEP10"] - (decimalThresholds[i] * diff10)


            mFile.seek(0)

            next(mData)

            #Calculate the dynamic percetage thresholds
            for row in mData:  
                for i in range(len(percentThresholds)):
                    if float(row[2]) < data[row[1]]["STEPS_MT_"+percentThresholds[i]] and float(row[3]) < float(data[row[1]]["MT_"+percentThresholds[i]]):
                        data[row[1]]["STEPS_MT_"+percentThresholds[i]] = int(row[2])
                        
                    if float(row[2]) < data[row[1]]["STEPS_MT10_"+percentThresholds[i]] and float(row[3]) < float(data[row[1]]["MT10_"+percentThresholds[i]]):
                        data[row[1]]["STEPS_MT10_"+percentThresholds[i]] = int(row[2])
                        
                    if float(row[2]) < data[row[1]]["STEPS_WT_"+percentThresholds[i]] and float(row[3]) < float(wtThresholds[i]):
                        data[row[1]]["STEPS_WT_"+percentThresholds[i]] = int(row[2])
                        
                    if float(row[2]) < data[row[1]]["STEPS_WT10_"+percentThresholds[i]] and float(row[3]) < float(wt10Thresholds[i]):
                        data[row[1]]["STEPS_WT10_"+percentThresholds[i]] = int(row[2])
                        
                        
                if float(row[2]) < data[row[1]]["STEPS_WT_100"] and float(row[3]) < float(pdbBaseline[pdb][2]):
                    data[row[1]]["STEPS_WT_100"] = int(row[2])    
        
            for mutant in data:
                for i in range(len(percentThresholds)):
                    if data[mutant]["STEPS_MT_"+percentThresholds[i]] == 1000:
                        data[mutant]["STEPS_MT_"+percentThresholds[i]] = -1
                        
                    if data[mutant]["STEPS_MT10_"+percentThresholds[i]] == 1000:
                        data[mutant]["STEPS_MT10_"+percentThresholds[i]] = -1
                        
                    if data[mutant]["STEPS_WT_"+percentThresholds[i]] == 1000:
                        data[mutant]["STEPS_WT_"+percentThresholds[i]] = -1
                        
                    if data[mutant]["STEPS_WT10_"+percentThresholds[i]] == 1000:
                        data[mutant]["STEPS_WT10_"+percentThresholds[i]] = -1
                        
                        
                if data[mutant]["STEPS_WT_100"] == 1000:
                    data[mutant]["STEPS_WT_100"]= -1 
                row =[
                    data[mutant]["PDBID"], 
                    data[mutant]["MUTATION"], 
                    data[mutant]["INITIAL"], 
                    data[mutant]["FINAL"],
                    data[mutant]["STEP10"]
                ]
                
                #Write to the output file
                
                for i in range(len(percentThresholds)):
                    row.append( data[mutant]["STEPS_MT_"+percentThresholds[i]])

                for i in range(len(percentThresholds)):
                    row.append( data[mutant]["STEPS_MT10_"+percentThresholds[i]])

                for i in range(len(percentThresholds)):
                    row.append( data[mutant]["STEPS_WT_"+percentThresholds[i]])
                    
                for i in range(len(percentThresholds)):
                    row.append( data[mutant]["STEPS_WT10_"+percentThresholds[i]])
                
                row.append(data[mutant]["STEPS_WT_100"])
                
                writer.writerow(row)
                
            # Finish with this PDBID
            out.close()
            mFile.close()