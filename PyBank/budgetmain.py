
#import libraries
import os
import csv

#define variables for following code
Months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Count=0
Total=0
Old=0
AvgC=0
Max=0
Min=0
TotalChange=0
FirstV=0

#set filepath to find source document
csvpath=os.path.join('.','Resources','budget_data.csv')
with open(csvpath, encoding="utf") as csvfile:
    bankreader=csv.reader(csvfile,delimiter=",")
    
    #check to skip header row
    for row in bankreader:
        if row[1]=="Profit/Losses":
            continue
        #storing value of row
        Current=int(row[1])

        #storing first value of source
        if FirstV==0:
            FirstV=int(row[1])

        #Counting number of months
        if (row[0][0:3]) in Months:
            Count=Count+1
            Total=Current+Total
            Change=Current-Old

        #Setting a max value and date
        if Change>Max:
            Max=Change
            MaxDate=str(row[0][0:6])

        #Setting a min value and date
        if Change<Min:
            Min=Change
            MinDate=str(row[0][0:6])

        #shifting value of Old for month count function
        Old=Current

    #calculate average change
    AvgC=round((Current-FirstV)/(Count-1),2)

    #print output
    print("Financial Analysis \n")
    print("----------------------------------------------\n")
    print("There are "+str(Count)+" months")
    print("The Profit/Loss was $"+str(Total))
    print("The average change was $" + str(AvgC))
    print("The greatest gain was $"+str(Max) + " on the " + MaxDate)
    print("The greatest loss was $"+str(-Min) + " on the " + MinDate)

    #write output to text doc in analysis
    with open ('./analysis/Election.txt' ,  "w") as f:
        f.write("There are "+str(Count)+" months" + "\n" + 
        "The Profit/Loss was $" + str(Total) + "\n" +
        "The average change was $" + str(AvgC) +"\n" +
        "The greatest gain was $"+str(Max) + " on the " + MaxDate + "\n" +
        "The greatest loss was $"+str(-Min) + " on the " + MinDate)

        

        

