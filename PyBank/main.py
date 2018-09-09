# PyBank
import os
import csv

# path to collect data from csv
budgetcsv = os.path.join('C:/Users/EKR/Desktop/BootCampPy/python-challenge/PyBank/budget_data.csv')

print("Financial Analysis")
print("------------------------------")
# read in csv file
with open(budgetcsv, newline = "\n") as csvfile:
    # split data
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # 1. Calculate Total Months
    budgetlist = []     # FYI creating another list this way messes everything up. Just reference this one
    for row in csvreader:
        budgetlist.append(row)

    totalmonths = len(budgetlist)
    print(f"Total Months: {totalmonths}")


    # 2. The total net amount of "Profit/Losses" over the entire period
    def totalnet(data):     #"data" could have been any word, just not a word/variable used previously
        profitloss = 0
        for row in data:
            profitloss += int(row[1])
        return profitloss

    print(f"Total: ${totalnet(budgetlist)}")


    # 3. The average change in "Profit/Losses" between months over the entire period
    def monthchange(data):
        profitlist = []
        for row in data:
            profitlist.append(int(row[1]))
        return(round((profitlist[85] - profitlist[0]) / (len(profitlist) - 1), 2))
    print(f"Average Change: ${monthchange(budgetlist)}")

    monthlist = []
    for row in budgetlist:
        monthlist.append(row[0])
    #print(monthlist)

    # 4. The greatest increase/decrease in profits (date and amount) over the entire period
    # How to create a list that can be iterated, from the results of a function?
    profitlist2 = []
    for row in budgetlist:
        profitlist2.append(int(row[1]))
    #print(profitlist2)

    changelist = []
    for i in range(1, len(profitlist2)):   #use range(1,len) because the first loop run will attempt row 0 - (-1 : last row of data)
        changelist.append(profitlist2[i] - (profitlist2[i-1]))
    print(f"Greatest Increase in Profits: {max(changelist)}") # how to locate/return month associated
    print(f"Greatest Decrease In Profits: {min(changelist)}") # how to locate/return month associated
    #print(changelist)


### BRAINSTORMING NOTES ###
        #profitloss = int(budgetcsv[1])
        # change = ??? (profitloss of i) - (profitloss of (i - 1))
        #for i in 2 To 100
        #if Cells(i,1).value <> Cells(i-1,1)
        # temp variable that keeps track of previous row
        #skip first month
        # for row in budgetcsv:
            # changelist.append(change)
    # avgchange = sum(changelist) / float(len(changelist))
    # print(f"Average Change: ${avgchange}")
