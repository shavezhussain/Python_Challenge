
import pandas as pd


file_path = "election_data.csv"
data = pd.read_csv(file_path)

#The total number of votes cast
total_votes = len(data)

#A complete list of candidates who received votes
unique_candidates = data["Candidate"].unique()

#The total number of votes each candidate won
candidate_votes = data["Candidate"].value_counts()

#The percentage of votes each candidate won
candidate_percentages = candidate_votes / total_votes * 100

#The winner of the election based on popular vote
winner = candidate_votes.idxmax()


print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate in unique_candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Export Results to Text File
output_path = "election_results.txt"
with open(output_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("----------------------------\n")
    for candidate in unique_candidates:
        output_file.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("----------------------------\n")

print(f"Results have been printed to the terminal and saved to '{output_path}'.")