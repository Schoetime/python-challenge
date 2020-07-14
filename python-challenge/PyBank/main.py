# Modules
import os
import csv

pybank_csv = os.path.join("Resources","budget_data.csv")

# lists to store data
month = []
pl = []
date = []

#Starting Values

count = 0
initalprofit = 0
totalprofit = 0
totalchangeprofit = 0

#open as csv

with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
   
    for row in csvreader:
        
        #months total
        count = count + 1

        #net total of p/l
        totalprofit += int(row[1])

        #avg of changes in p/l
        lastprofit = int(row[1])
        monthlychange = lastprofit - initalprofit
        month.append(monthlychange)

        totalchangeprofit = totalchangeprofit + monthlychange
        initalprofit = totalchangeprofit

        averagechange = (totalchangeprofit/count)

        #date definition for increase/decrease
        date.append(row[0])

        #greatest increase in profit (date and amount)

        greatestincrease = max(month)
        dategreatestincrease = date[month.index(greatestincrease)]

        #greatest decrease in profit (date and amount)
        greatestdecrease = min(month)
        dategreatestdecrease = date[month.index(greatestdecrease)]

print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(count))
print("Total Profit: $" + str(totalprofit))
print("Average Change: " + str(int(averagechange)))
print("Greatest Increase in Profits: " + str(dategreatestincrease) + " $" + str(greatestincrease))
print("Greatest Decrease in Profits: " + str(dategreatestdecrease) + " $" + str(greatestdecrease))

#Export text file

with open("Financial Analysis", 'w') as text:
    text.write("Financial Analysis"+"\n")
    text.write("---------------------"+"\n")
    text.write("Total Months: " + str(count)+"\n")
    text.write("Total Profit: $" + str(totalprofit)+"\n")
    text.write("Average Change: " + str(int(averagechange))+"\n")
    text.write("Greatest Increase in Profits: " + str(dategreatestincrease) + " $" + str(greatestincrease)+"\n")
    text.write("Greatest Decrease in Profits: " + str(dategreatestdecrease) + " $" + str(greatestdecrease)+"\n")

#I couldn't figure out how to move it to a new folder called "Analysis" so I just left it in the same folder as main.py