import os
import csv

# pull in CSV to work with
budgetcsv = os.path.join('C:/Users/39319362/Desktop/python-challenge/PyBank/budget_data.csv')
# Give location for output text file
outputtxt = os.path.join("C:/Users/39319362/Desktop/python-challenge/PyBank/output.txt")

# Set location to track variables and counters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]
total_revenue = 0

# Read the csv and convert it into a list of dictionaries
with open(budgetcsv) as revenue_data:
	csvreader = csv.reader(revenue_data, delimiter=",")
	header=next(csvreader)

	for row in csvreader:

		# Track the total - Count Total Months through Loop
		total_months = total_months + 1
		# Calculate total revenue by adding through loop to end of data
		total_revenue = total_revenue + int(row[1])

		# Track the revenue change
		revenue_change = int(row[1]) - (prev_revenue)
		prev_revenue = int(row[1])

		#Create location for revenue change to be listed
		revenue_change_list = revenue_change_list + [revenue_change]
		month_of_change = month_of_change + [row[0]]

		# Calculate the greatest increase
		if (revenue_change > greatest_increase[1]):
			greatest_increase[0] = row[0]
			greatest_increase[1] = revenue_change

		# Calculate the greatest decrease
		if (revenue_change < greatest_decrease[1]):
			greatest_decrease[0] = row[0]
			greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


# Generate result in terminal
output = (
	f"\nFinancial Analysis\n"
	f"----------------------------\n"
	f"Total Months: {total_months}\n"
	f"Total Revenue: ${total_revenue}\n"
	f"Average Revenue Change: ${revenue_avg:.2f}\n"
	f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
	f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)


# Give text to be put in file
with open(outputtxt, 'w') as text_file:
	text_file.write(output)


    
