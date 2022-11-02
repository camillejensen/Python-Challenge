import os
import csv
csvpath = os.path.join("/Users/camillejensen/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv")

#Variables
total_months = []
total_profits = []
profit_changes = 0
monthly_changes = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_reader = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(row[1])

    print(len(total_months))

    total_profits=[int(total_profits) for x in total_profits]
    total_profits_sum=sum(total_profits)
    print(total_profits_sum)
for i in range(len(total_profits)-1):
    monthly_changes.append(total_profits[i+1]-total_profits[i])
