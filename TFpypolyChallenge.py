#The data we need to retrieve.
# Assign a variable for the file to load and the path.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load=os.path.join('election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file.

# Intialize a total vote counter
total_votes=0
c_total_votes=0
# Candidate options
candidate_options=[]
# Candidate Dictionary
candidate_votes={}
#create a list of counties
voting_counties = []
# Declare an empty dictionary for counties
county_votes={}

#winning candidate and winning count tracker.
lrg_county=""
winning_turnout=0
c_winning_percent=0
winning_candidate=""
winning_count=0
winning_percentage=0

#open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row
    headers=next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        #add the total county vote count
        c_total_votes += 1
        # Add the total candidate vote count
        total_votes += 1

        # Print County name for each vote
        county_name=row[1]
        #print the candidate name from each row
        candidate_name=row[2]

        if county_name not in voting_counties:
            #add it to the list of counties.
            voting_counties.append(county_name)

            # Track votes cast per county
            county_votes[county_name]=0
        #add a vote to that county's count
        county_votes[county_name]+=1

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
    #save the results to the txt file
    with open(file_to_save,"w") as txt_file:
        #print the final vot count to the terminal.
        election_results=(
            f"\nElection Results\n"
            f"----------------------\n"
            f"Total Votes {total_votes:,}\n"
            f"-----------------------\n"
            f"County Results\n")
        print(election_results, end="")
        txt_file.write(election_results)


        # Determine percentage of votes per county
        for county in county_votes:
            # Retrieve vote vount of the county
            c_votes=county_votes[county]
            # Calculate the percentage of the votes.
            c_vote_percentage=float(c_votes)/float(c_total_votes)*100

            #print county results
            county_results=( 
                f"{county}:{c_vote_percentage:.1f}% ({c_votes:,})\n")

            print(county_results)
            #save the county results to the txt file
            txt_file.write(county_results)

            if (c_votes>c_total_votes) and (c_vote_percentage>c_winning_percent):
                winning_turnout=c_votes
                c_winning_percent=c_vote_percentage
                lrg_county = county

        lrg_county_turnout=(
            f"--------------------------\n"
            f"Largest County Turnout: {lrg_county}\n"
            f"--------------------------\n")
        print(lrg_county_turnout)
        txt_file.write(lrg_county_turnout)

            
        
        for candidate in candidate_votes:
            votes=candidate_votes[candidate]
            vote_percentage=float(votes)/float(total_votes)*100

            Candidate_results=(
                f"{candidate}:{vote_percentage:.1f}% ({votes:,})\n")
            
            print(Candidate_results)
            txt_file.write(Candidate_results)

            if (votes>winning_count) and (vote_percentage>winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate=candidate

        winning_candidate_summary=(
            f'-------------------------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.2f}%\n'
            f'-------------------------------\n')
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
 

