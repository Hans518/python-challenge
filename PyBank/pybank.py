# Modules
import os
import csv

pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

   
with open(pybank_csv, 'r') as csvfile:
    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    row_count = 0
    pnl = 0
    max_pnl = 0
    min_pnl = 0

    header = next(csvreader)

    for row in csvreader:

        #Count the number of months
        row_count = row_count + 1

        #Add up the net profit and loss
        pnl = pnl + int(row[1])

        #Average profit and loss
        ave_pnl = pnl / row_count

        #Largest profit increase
        if int(row[1]) > max_pnl:
            max_pnl = int(row[1])
            max_date = row[0]
        #Largest profit loss
        if int(row[1]) < min_pnl:
            min_pnl = int(row[1])
            min_date = (row[0])

    print("------------------------------------------------------")
    print("              Financial Analysis")
    print("------------------------------------------------------")
    print(f"There are {row_count} months")     
    print(f"The net profit/loss is {pnl}") 
    print(f"The average profit/loss is {round(ave_pnl)}") 
    print(f"The largest profit increase is: {max_date} {max_pnl}")
    print(f"The largest profit decrease is: {min_date} {min_pnl}")
    print("------------------------------------------------------") 