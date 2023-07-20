import csv
import os

election_csv = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("AnalysisPyPoll", "resultsPyPoll.txt")


with open(election_csv,"r") as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")

     next(csvreader)

     total_votes = 0
     candidates_votes = {}

     for row in csvreader:
          total_votes += 1
          candidate = row[2]

          if candidate in candidates_votes:
               candidates_votes[candidate] += 1
          else:
               candidates_votes[candidate] = 1
               

winner = None
max_votes = 0


print("Election Results")     
print("----------------------------")    
print(f"Total Votes: {total_votes}")  
print("----------------------------")

analysis_results = (
     f"Election Results\n"
     f"----------------------------\n"
     f"Total Votes: {total_votes}\n"
     f"----------------------------\n"
)

for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    analysis_results += f"{candidate} : {percentage:.3f}% ({votes})\n"
    

    if votes > max_votes:
         max_votes = votes
         winner = candidate

print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

analysis_results += (
     f"---------------------------\n"
     f"Winner: {winner}\n"
     f"---------------------------\n"
)
print(analysis_results)

with open(file_to_output, "w") as txt_file:
    txt_file.write(analysis_results)
          