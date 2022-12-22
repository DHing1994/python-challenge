#importing libraries
import os
import csv

#Total vote is running count for votes
TotalVotes=0
#Candidates is a dictionary to track candidate votes
Candidates={}

#set filepath to find source document
csvpath=os.path.join('.','Resources','election_data.csv')
with open(csvpath, encoding="utf") as csvfile:
    pollreader=csv.reader(csvfile,delimiter=",")
    pollreader.__next__()

    #check each row for new candidate entries, then add vote to their dictionary value
    for row in pollreader:
        TotalVotes+=1
        if row[2] not in Candidates:
            Candidates[row[2]]=1
        else:
            Candidates[row[2]]+=1

#print header output
print("Election Results")
print("-----------------------------------------------")

#print Total vote count
print(str(TotalVotes)+" votes cast")
print("-----------------------------------------------")

#print candidate names and their vote counts
for key,value in Candidates.items():
    print(key + ": " + str(round(((value/TotalVotes)*100),3)) + "% (" + str(value) + ")")
print("-----------------------------------------------")

#print winner
print("Winner is " + max(Candidates, key=Candidates.get))

#write the results into a text doc in the analysis folder
with open('./analysis/Poll.txt' , 'w') as f:
    f.write(str(TotalVotes)+ ' votes cast' + "\n")
    for key,value in Candidates.items():
        f.write(key + ": " + str(round(((value/TotalVotes)*100),3)) + "% (" + str(value) + ")" +"\n" +
        "Winner is " + max(Candidates, key=Candidates.get))

