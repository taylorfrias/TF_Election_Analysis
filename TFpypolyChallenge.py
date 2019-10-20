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

#create a list of counties
voting_counties = []

# Declare an empty dictionary for counties
county_votes={}

#open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row
    headers=next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        #add the total vote count
        total_votes += 1

        # Print County name for each vote
        county_name=row[1]

        if county_name not in voting_counties:
            #add it to the list of counties.
            voting_counties.append(county_name)

            # Track votes cast per county
            county_votes[county_name]=0
        #add a vote to that county's count
        county_votes[county_name]+=1
    

print(county_votes)

