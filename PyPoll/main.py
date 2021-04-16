import os
import csv

file_path = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = {}

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        total_votes += 1
        if row[2] in candidates:
            candidates[row[2]] = int(candidates[row[2]])+1
        else:
            candidates[row[2]] = 1

winner = sorted(candidates.items(), key=lambda x: x[1], reverse = True)

print(f'''
Election Results
--------------------------------
Total Votes: {total_votes}
--------------------------------
{candidates}
--------------------------------
Winner: {next(iter(winner))[0]}
--------------------------------
''')

