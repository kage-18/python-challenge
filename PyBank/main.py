import os
import csv
from statistics import mean

file_path = os.path.join("Resources", "budget_data.csv")


with open(file_path, 'r') as open_file:
    csv_reader = csv.reader(open_file, delimiter=",")
    next(csv_reader, None)
    first_row = next(csv_reader, None)
    months = 0
    previous_val = int(first_row[1])
    net_total = 0 + previous_val
    max_increase = [first_row[0], previous_val]
    max_decrease = [first_row[0], previous_val]
    changes = []
    for row in csv_reader:
        months += 1
        changes.append(int(row[1])-previous_val)
        previous_val = int(row[1])
        net_total += int(row[1])
        if int(row[1]) >= max_increase[1]:
            max_increase = [row[0],changes[-1]]
        if int(row[1]) <= max_decrease[1]:
            max_decrease = [row[0],changes[-1]]

print(f'''
Financial Analysis
---------------------------
Total Months:{months}
Total: ${net_total}
Average Change: ${round(mean(changes), 2)}
Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})
Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})
''')
