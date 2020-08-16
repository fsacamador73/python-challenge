import os
import csv

filepath = os.path.join("Resources", "budget_data.csv")
outputpath = os.path.join("Output", "pybank.txt")

Months = 0
SumofPL = 0
PLinBaseRow = 0
PLinUpperRow = 0
MChange = []
MDate = []

with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        #print(row)
          
        Months += 1
        #print(Months)

        PLoftheMonth = float(row[1])
        SumofPL += PLoftheMonth
        #print(SumofPL)

        PLinBaseRow = float(row[1])
        DifferenceMonthToMonth = float(PLinBaseRow) - float(PLinUpperRow)
        MChange.append(DifferenceMonthToMonth)
        PLinUpperRow = PLinBaseRow

        Date = str(row[0])
        Dates = Date
        MDate.append(Dates)

#print(MChange)
#print(MDate)

SumofDiff = sum(MChange[1:])
#print(SumofDiff)

LengthofMChange = len(MChange) - 1
#print(LengthofMChange)

AveofChange = round(SumofDiff / LengthofMChange, 2)
#print(AveofChange)

MaxofMChange = max(MChange[1:])
#print(MaxofMChange)
MaxIndex = int(MChange.index(MaxofMChange))
#print(MaxIndex)

MinofMChange = min(MChange[1:])
#print(MinofMChange)
MinIndex = int(MChange.index(MinofMChange))
#print(MinIndex)

MaxDate = MDate[MaxIndex]
#print(MaxDate)
MinDate = MDate[MinIndex]
#print(MinDate)

print("Financial Analysis")
print("-------------------------------------")
print("Total Months:  " + str(Months))
print("Total:  " + "$" + str(SumofPL))
print("Average Change:  " + "$" + str(AveofChange))
print("Greatest Increase in Profits:  " + str(MaxDate) + "  " + "($" + str(MaxofMChange) + ")")
print("Greatest Decrease in Profits:  " + str(MinDate) + "  " + "($" + str(MinofMChange) + ")")

with open(outputpath, 'w') as txt:
    txt.write("\n")
    txt.write("Financial Analysis" + "\n")
    txt.write("-------------------------------------" + "\n")
    txt.write("Total Months:  " + str(Months) + "\n")
    txt.write("Total:  " + "$" + str(SumofPL) + "\n")
    txt.write("Average Change:  " + "$" + str(AveofChange) + "\n")
    txt.write("Greatest Increase in Profits:  " + str(MaxDate) + "  " + "($" + str(MaxofMChange) + ")")
    txt.write("\n")
    txt.write("Greatest Decrease in Profits:  " + str(MinDate) + "  " + "($" + str(MinofMChange) + ")")
    txt.write("\n")
    txt.close()