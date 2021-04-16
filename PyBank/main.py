import os
import csv
from statistics import mean

file_path = os.path.join("Resources", "budget_data.csv")

months = []
net_total = 0
max_increase = ["",0]
max_decrease = ["",0]

with open(file_path, 'r') as open_file:
    csv_reader = csv.reader(open_file, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        if row[0] not in months:
            months.append(row[0])
        net_total += int(row[1])
        if int(row[1]) >= max_increase[1]:
            max_increase = [row[0],int(row[1])]
        if int(row[1]) <= max_decrease[1]:
            max_decrease = [row[0],int(row[1])]

print(f'''
Financial Analysis
---------------------------
Total Months:{len(months)}
Total: ${net_total}
Average Change: ${net_total/len(months)}
Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})
Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})
''')
        
