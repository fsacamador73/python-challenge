import os
import csv

filepath = os.path.join("Resources", "election_data.csv")
outputpath = os.path.join("Output", "pypoll.txt")

TVoterID = []
TCandidate = []
Names = {}
WCandidate = {}

with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        Voter = str(row[0])
        VoterID = Voter
        TVoterID.append(VoterID)
        TotalVotes = len(TVoterID)

        Candidate = str(row[2])
        CandidateName = Candidate
        TCandidate.append(CandidateName)

print("")
print("Election Results")
print("------------------------------")
print("Total Votes:  " + str(len(TVoterID)))
print("------------------------------")

from collections import Counter
def CName(input):
    Names = Counter(input)

    for (key,value) in Names.items():
        print(key,":  ",round(((value/TotalVotes)*100),3),"%  ","(",value,")")
                
        tuple(Names.keys())
        winner = tuple(Names.keys())[0]
        winner1 = winner
        #print(winner1)
        WCandidate["name"] = winner1
        #print(WCandidate)

CName(TCandidate)

print("------------------------------")
print("Winner:  " + WCandidate['name'])
print("------------------------------")
print("")

with open(outputpath,'w') as txt:

    txt.write("\n" )
    txt.write("Election Results" + "\n")
    txt.write("------------------------------" + "\n")
    txt.write("Total Votes:  " + str(len(TVoterID)) + "\n")
    txt.write("------------------------------" + "\n")
    txt.write("\n")
    txt.write("------------------------------" + "\n")
    txt.write("Winner:  " + WCandidate['name'] + "\n")
    txt.write("------------------------------" + "\n")
    txt.write("\n")
    txt.close()