#The data we need to retrieve.
# Assign a variable for the file to load and the path.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load=os.path.join('election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file.

#1. Intialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []

#declare an empty dictionary
candidate_votes={}

#winning candidate and winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentages = 0

with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #read and the header row
    headers=next(file_reader)

    #Print each row in the csv file.
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #If the candidate doesn't match any existing candidates...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            #2. Begin tracking that candidate's voting count.
            candidate_votes[candidate_name]=0

        #add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

    #save the results to the txt file
    with open(file_to_save,"w") as txt_file:
    #print the final vote count to the terminal.
        election_results=(
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total Votes {total_votes:,}\n"
            f"------------------------\n")
        print(election_results, end="")
        #Save the final vote count to the text file.
        txt_file.write(election_results)

        #Determine the percentage of votes for each candidate by looping through the counts.
        #1.Iterate through the candidate list.
        for candidate in candidate_votes:
            #2. retrieve vote count of the candidate
            votes=candidate_votes[candidate]
            #3. Calculate the percentage of votes.
            vote_percentage=float(votes)/float(total_votes)*100
            
            # To Do: Print out each candidates name, vote count and percentage of votes to the terminal
            #print(f"{candidate}:{vote_percentage:.2f}% ({votes:,})\n")
            candidate_results=(
                f"{candidate}:{vote_percentage:.1f}% ({votes:,})\n")
            #print each candidate's voter count and percentage to the terminal.
            print(candidate_results)
            # Save the candidates results to our txt file
            txt_file.write(candidate_results)
 
            #Determine winning vote count and candidate
            #1. Determine if votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentages):
                #2. if true then set winning_count = votes and winning percentage = vote_percentage
                winning_count=votes
                winning_percentages=vote_percentage
                #3. Set the winning_candidate equal to the candidates name.
                winning_candidate=candidate
        #To Do: Print outeach candudates name, vote count and percentage of votes to the terminal
        # Print winning candidate's result to the terminal

        winning_candidate_summary=(
            f"------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentages:.2f}%\n"
            f"------------------------------\n")
        print(winning_candidate_summary)
        #Save winning candidate summary to the terminal
        txt_file.write(winning_candidate_summary)
        
