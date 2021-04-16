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
candidate_keys = list(candidates.keys())
# for person in candidates:
#     name = person
#     percentage = round(int(candidates[person])/total_votes)
#     votes = int(candidates[person])

print(f'''
Election Results
--------------------------------
Total Votes: {total_votes}
--------------------------------
{candidate_keys[0]}: {round(int(candidates[candidate_keys[0]]) / total_votes, 2)*100}% ({int(candidates[candidate_keys[0]])})
{candidate_keys[1]}: {round(int(candidates[candidate_keys[1]]) / total_votes, 2)*100}% ({int(candidates[candidate_keys[1]])})
{candidate_keys[2]}: {round(int(candidates[candidate_keys[2]]) / total_votes, 2)*100}% ({int(candidates[candidate_keys[2]])})
{candidate_keys[3]}: {round(int(candidates[candidate_keys[3]]) / total_votes, 2)*100}% ({int(candidates[candidate_keys[3]])})
--------------------------------
Winner: {next(iter(winner))[0]}
--------------------------------
''')

output_file_path = os.path.join("Analysis", "analysis.txt")
with open(output_file_path, 'w') as output_file:
    output_file.write(f'''
                        Election Results
                        --------------------------------
                        Total Votes: {total_votes}
                        --------------------------------
                        {candidate_keys[0]}: {round(int(candidates[candidate_keys[0]]) / total_votes, 2)*100}% ({int(candidates[candidate_keys[0]])})
                        {candidate_keys[1]}: {round(int(candidates[candidate_keys[1]]) / total_votes, 2)*100}% ({int(candidates[candidate_keys[1]])})
                        {candidate_keys[2]}: {round(int(candidates[candidate_keys[2]]) / total_votes, 2)*100}% ({int(candidates[candidate_keys[2]])})
                        {candidate_keys[3]}: {round(int(candidates[candidate_keys[3]]) / total_votes, 2)*100}% ({int(candidates[candidate_keys[3]])})
                        --------------------------------
                        Winner: {next(iter(winner))[0]}
                        --------------------------------
                        ''')

