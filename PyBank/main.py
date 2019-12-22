# Import Dependencies
import os
import csv

# Set and check path for CSV file
budgetData = os.path.join(".","Resources","budget_data.csv")
currentDirectory = os.getcwd()
print(currentDirectory)
print(budgetData)

# Assign file path
# I copied and pasted the resources folder into my homework folder for simpler pathing  
budget_csv = os.path.join(".","Resources","budget_data.csv")

# Read in the CSV file
with open(budget_csv, 'r', newline='') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Account for header row
    header = next(csvreader)
    
    # create months list array
    monthslist = []
    
    # create profit/loss array 
    profitlosslist = []
    
    # loop through csv file and build month and profit/loss lists 
    for row in csvreader:
        monthslist.append(row[0])
        profitlosslist.append(int(row[1]))

    # Return total number of months
    print(f'Total months: {len(monthslist)}')
    
    # Return net profit loss 
    print(f'Net profit/loss: ${sum(profitlosslist)}')

# Attempted but incomplete code : ----------------------------------------------------------------------

    # Profit loss change list and calculations 
    profitlosschangelist = []
    for row in csvreader(2, len(profitlosslist)+1):
        profitlosschange = row+1[2] - row[2]
        profitlosschangelist.append(profitlosschange)
        
    # calculate average profit/loss change  
    profitlosschangeavg = sum(profitlosschangelist)/len(profitlosschangelist) 
    print(profitlosschangeavg)

    #The greatest increase in profits (date and amount) over the entire period
    maxprofitincrease = max(profitlosschangelist)

    for row in csvreader
        for x in profitlosschangelist
            if x == maxprofitincrease
                print(f'{month " : " maxprofitincrease})

        # Didn't know how to get max profit increase to speak to original data to pull the correct code
        maxmonth = csvreader.index(profitlosschangelist.index(maxprofitincrease)),0
        print(f'The largest profit increase of ' maxprofitincrease ' was in ' maxmonth)


    #The greatest decrease in losses (date and amount) over the entire period
    maxlossreduction = min(profitlosschangelist)

    for x in profitlosschangelist
        if x == maxlossreduction
            print(f'{month " : " maxlossreduction})
    
    # Didn't know how to get max profit increase to speak to original data to pull the correct code