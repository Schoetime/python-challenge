# Modules
import os
import csv

pypoll_csv = os.path.join("Resources","election_data.csv")

# lists to store data
count = 0
candidatelist = ["Khan","Correy","Li","O'Tooley"]

#open as csv

with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        
        #total votes
        count = count + 1

        #List of candidates
        candidatelist





    


print("Election Results")
print("---------------------")
print("Total Votes: " + str(count))
print("---------------------")
print("")

#this was as far as I got before I ran out of time

