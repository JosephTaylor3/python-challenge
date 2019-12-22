# Import Dependencies
import os
import csv

# Assign file path
# I copied and pasted the resources folder into my homework folder 
budget_csv = os.path.join(".","Resources","election_data.csv")

# Read in the CSV file
with open(budget_csv, newline='') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Account for header row
    header = next(csvreader)
    
    # create total votes list and count
    voteslist = []
    
    for row in csvreader:
        voteslist.append(row[2])

    # Return total number of votes
    print(f'The total number of votes is {len(voteslist)}')
    
     # create list of candidates who received votes 
    candidateslist = []
    
    # loop through list to get unique values
    for name in voteslist:
        if name not in candidateslist:
            candidateslist.append(name)
    
    # print unique candidates 
    print(f'The candidates who recevied votes are: {candidateslist}')
    
    # loop through candidate list to calculate votes and percentage of votes 
    for candidate in candidateslist:
        print(f'Candidate {str(candidate)} received {voteslist.count(str(candidate))} votes, which is {(voteslist.count(str(candidate))/(len(voteslist))*100)}% of the votes')       
            
    # Create a dictionary of candidates and their vote count
    candidateVotes = {}
    for candidate in candidateslist: 
        candidateVotes = {candidate : voteslist.count(candidate)}
        
        # print dictionary to ensure loop is creating full dictionary 
        print(candidateVotes)

    # create function that draws from the candidateVotes dictionary to find the candidate with max votes 
    def maxvotes(candidateVotes): 
        votesCount=list(candidateVotes.values())
        candidateName=list(candidateVotes.keys())
        print (f'The winner is {candidateName[votesCount.index(max(votesCount))]}!')
    
    maxvotes(candidateVotes)
    
    # I have no idea why the winner comes out as O'Tooley. I tried multiple methods for returning max through a function but got O'Tooley each time. 
    # One guess I had was that my code was counting max number of characters in the last name, in which case O'Tooley wins, but wasn't sure. 
    