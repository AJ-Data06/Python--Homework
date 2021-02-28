# Import Libraries
import os
import csv

# Set File Path for Input and Output
csvpath = os.path.join("Resources_election_data.csv")
file_to_output = "election_results.txt"

# Declaring the Variables 
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""




# Open the File
with open('Resources_election_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #loop through to find the total votes
    for row in csvreader:

        # Find the total vote count
        total_votes += 1

        candidate = row["Candidate"]
        # if statement to run on first occurence of candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1
#by the time this loop is done we should have a list of unique candidates
# as well as a dictionary with candidate names and corresponding votes


#another with statement to create output
#we are also finding winning candidate
with open(file_to_output, 'w') as txt_file:
    #create header
    election_header = (
        f"Election Results\n"
        f"---------------\n")
    txt_file.write(election_header)

    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
        
    winning_summary = (
        f"Winner: {winner}"
    )
    print(winning_summary)
    txt_file.write(winning_summary)