# Import
import os
import csv

from sympy import maximum

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    row = next(csvreader)
    #print(csv_header)
    #for row in csvreader:
        #print(row) to see dataset
    

    # Assign variables
    month = []
    monthly_profitloss = []
    months_total = 0
    total = 0
    largest_increase = 0
    largest_increase_month = 0
    largest_decrease = 0
    largest_increase_month = 0


    # Assign variables for rows
    total += int(row[1])
    previous_row = int(row[1])
    largest_increase = int(row[1])
    largest_increase_month = row[0]
    largest_decrease = int(row[1])
    largest_decrease_month = row[0]

    # Determine total of months
    months_total += 1
    
    
    # Read each row in the dataset
    for row in csvreader:
        

        # Calculate total of months in dataset
        months_total += 1
        
        # To see if total of months is correct use:
        #print(months_total)
    

        # Calculate total of profits and losses in the dataset
        total += int(row[1])

        # To see if total is correct use:
        #print(total)
    

        # Calculate changes from each month
        month.append(row[0])
        change = int(row[1]) - previous_row
        monthly_profitloss.append(change)
        previous_row = int(row[1])
        

        # Calculate average of profits and losses
        average = sum(monthly_profitloss)/ (months_total - 1)
    
        # To see if average is correct use:
        #print(f"$:{average}")


        # Find month with largest increase
        if  change > largest_increase:
            largest_increase = change
            largest_increase_month = row[0]
            Maximum = max(monthly_profitloss)


        # Find month with largest decrease
        if  change < largest_decrease:
            largest_decrease = change
            largest_decrease_month = row[0] 
            Minimum = min(monthly_profitloss)


# Print results
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {months_total}")
print(f"Total: ${total}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: {largest_increase_month} (${Maximum})")
print(f"Greatest Decrease in Profits: {largest_decrease_month} (${Minimum})")


# Export results to Analysis folder and write in txt file
output = os.path.join('Analysis', 'financial_analysis_results.txt')

with open(output, "w") as results:
    results.write("Financial Analysis\n")           
    results.write("-----------------------\n")
    results.write(f"Total Months: {months_total}\n")
    results.write(f"Total: ${total}\n")
    results.write(f"Average Change: ${average:.2f}\n")
    results.write(f"Greatest Increase in Profits: {largest_increase_month} (${Maximum})\n")
    results.write(f"Greatest Decrease in Profits: {largest_decrease_month} (${Minimum})\n")