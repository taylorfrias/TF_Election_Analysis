#The data we need to retrieve.
# Assign a variable for the file to load and the path.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load=os.path.join('election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    
    #read and print the header row
    headers=next(file_reader)
    print(headers)
    


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote