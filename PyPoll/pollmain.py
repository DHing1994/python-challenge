import os
import csv

TotalVotes=0
Candidates={}

csvpath=os.path.join('.','Resources','election_data.csv')
with open(csvpath, encoding="utf") as csvfile:
    pollreader=csv.reader(csvfile,delimiter=",")   
    pollreader.__next__()
    for row in pollreader:
        TotalVotes+=1
        if row[2] not in Candidates:
            Candidates[row[2]]=1
        else:
            Candidates[row[2]]+=1

print("Election Results")

print("-----------------------------------------------")
print(str(TotalVotes)+" votes cast")
print("-----------------------------------------------")
for key,value in Candidates.items():
    print(key + ": " + str(round(((value/TotalVotes)*100),3)) + "% (" + str(value) + ")")
print("-----------------------------------------------")

print("Winner is " + max(Candidates, key=Candidates.get))

with open('Poll.txt' , 'w') as f:
    f.write(str(TotalVotes)+ ' votes cast' + "\n")
    for key,value in Candidates.items():
        f.write(key + ": " + str(round(((value/TotalVotes)*100),3)) + "% (" + str(value) + ")" +"\n" +
        "Winner is " + max(Candidates, key=Candidates.get))

