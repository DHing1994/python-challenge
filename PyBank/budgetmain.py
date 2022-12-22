
import os
import csv

Months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
Count=0
Total=0
Old=0
AvgC=0
Max=0
Min=0
TotalChange=0
FirstV=0




csvpath=os.path.join('.','Resources','budget_data.csv')
with open(csvpath, encoding="utf") as csvfile:
    bankreader=csv.reader(csvfile,delimiter=",")
    for row in bankreader:
        if row[1]=="Profit/Losses":
            continue
        Current=int(row[1])
        if FirstV==0:
            FirstV=int(row[1])
        if (row[0][0:3]) in Months:
            Count=Count+1
            Total=Current+Total
            Change=Current-Old

        if Change>Max:
            Max=Change
        if Change<Min:
            Min=Change

        Old=Current

    AvgC=round((Current-FirstV)/(Count-1),2)

    print("There are "+str(Count)+" months")
    print("The Profit/Loss was $"+str(Total))
    print("The average change was $" + str(AvgC))
    print("The greatest gain was $"+str(Max))
    print("The greatest loss was $"+str(-Min))

    with open ('Election.txt' ,  "w") as f:
        f.write("There are "+str(Count)+" months" + "\n" + 
        "The Profit/Loss was $" + str(Total) + "\n" +
        "The average change was $" + str(AvgC) +"\n" +
        "The greatest gain was $"+str(Max) + "\n" +
        "The greatest loss was $"+str(-Min)) 

        

        

