from distutils import text_file
import os
import csv
csvpath = os.path.join("/Users/camillejensen/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv")

#Variables
total_months = []
total_profits = []
profit_changes = 0
monthly_changes = []
previous_profit = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_reader = next(csvreader)
    csvheader = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(row[1])

    print(len(total_months))

    total_profits=[int(x) for x in total_profits]
    total_profits_sum=sum(total_profits)
    print(total_profits_sum)

    for i in range(len(total_profits)-1):
        monthly_changes.append(total_profits[i+1]-total_profits[i])

greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

max_increase_month = monthly_changes.index(max(monthly_changes)) + 1
max_decrease_month = monthly_changes.index(min(monthly_changes)) + 1

print("Financial Analysis")
print("--------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profits)}")
print(f"Average Change: ${round(sum(monthly_changes)/len(monthly_changes),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(greatest_decrease))})")

textfile = os.path.join("/Users/camillejensen/Desktop/Python-Challenge/PyBank/analysis/Financial_analysis.txt")
with open(textfile,'w') as file:
    

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profits)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_changes)/len(monthly_changes),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(greatest_decrease))})")
