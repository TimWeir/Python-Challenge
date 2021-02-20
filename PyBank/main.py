#PyBank
import os
import csv

#Fix file path for source file
budget_file = os.path.join("Resources", "budget_data.csv")
#Call the file to write results
output_file = os.path.join("Analysis", "PyBank_results.txt")

#define lists
months = []
amounts = []
change = []
curr_amt = 0
last_amt = 0
row_count = 0
total_amount = 0

#Open source file as read only
with open(budget_file, newline='') as csv_source:
    csvreader = csv.reader(csv_source, delimiter=",")
    # Trick to ignore the header row as it is not involved in the analysis
    csv_header = next(csv_source)

    #for amounts in csv_source:
    for row in csvreader:
        
        #add months to list
        months.append(row[0])
        
        #add profit/loss amounts to list
        curr_amt = row[1]
        amounts.append(curr_amt)

        #total amount for output
        total_amount = total_amount + int(row[1])

        #find change with exception for 0 condition on first instance
        #"if" statement handles first condition
        if row_count == 0:
            change.append(0)
            row_count = row_count + 1
            last_amt = curr_amt
        #"else" statment handles all other conditions
        else:
            difference = int(curr_amt) - int(last_amt)
            change.append(difference)
            row_count = row_count + 1
            last_amt = curr_amt

    # OUTPUT
    # Header of the analysis
    print("") #bumpity bump
    print(f"Financial Analysis by Tim")
    print(f"----------------------------")
    # Print the months
    print(f"Total months: {row_count}")
    # Print the sum of all amounts
    print(f"Total amount: ${total_amount}")
    #print other metrics
    print(f"Average Change: ${round(sum(change)/(len(change)-1),2)}")
    print(f"Greatest Increase in Profits: {months[change.index(max(change))]} (${max(change)})")
    print(f"Greatest Decrease in Profits: {months[change.index(min(change))]} (${min(change)})")
    print("") #bump for next row spacer

#write file for results
with open(output_file, 'w') as txtwriter:
    #write results
    txtwriter.write(f"Financial Analysis by Tim\n")
    txtwriter.write(f"----------------------------\n")
    txtwriter.write(f"Total months: {row_count}\n")
    txtwriter.write(f"Total amount: ${total_amount}\n")
    txtwriter.write(f"Average Change: ${round(sum(change)/(len(change)-1),2)}\n")
    txtwriter.write(f"Greatest Increase in Profits: {months[change.index(max(change))]} (${max(change)})\n")
    txtwriter.write(f"Greatest Decrease in Profits: {months[change.index(min(change))]} (${min(change)})\n")