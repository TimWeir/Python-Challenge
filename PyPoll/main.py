#PyPoll
import os
import csv

#Fix file path for source file
source_file = os.path.join("Resources", "election_data.csv")
#Call the file to write results
output_file = os.path.join("Analysis", "PyPoll_results.txt")

#define objects
candidates = []
votes = []
total_votes = 0
margins = []
most_votes = 0

#Open source file as read only
with open(source_file, 'r', newline='') as csv_source:
    csvreader = csv.reader(csv_source, delimiter=",")
    # Trick to ignore the header row as it is not involved in the analysis
    csv_header = next(csv_source)

    #for loop in csv_source:
    for row in csvreader:
        #total votes cast
        total_votes = total_votes + 1

        #name of the candidate to analyze
        name = row[2]
   
        if name in candidates: #if the name is in the candidates list
            name_index = candidates.index(name) #grab the index number
            votes[name_index] = votes[name_index] + 1 #and increment the number of votes (i.e. count) for this name
        else:# if the name is not in the list
            candidates.append(name) # add the new name
            votes.append(1) #and add the first vote for the new name
    
    # do the numbers
    for cand_count in range(len(candidates)): #for each name in the candidates list (by index)
        percent = votes[cand_count]/total_votes*100 #calc the name's percentage of total votes
        margins.append(percent) #add the percentage of total votes to list called margins
        #store the index of name with most votes (this is the winner)
        if votes[cand_count] > most_votes: #if the votes at this index in the votes list is greater than "most_votes"
            most_votes = votes[cand_count] #replace "most_votes"
            windex = cand_count #and the candidate name at this index is the winner or windex (see what I did there?)
    winner = candidates[windex] #name the winner by index in the list of candidates    

    # OUTPUT
    print("") #bumpity bump
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total votes: {total_votes}")
    print(f"----------------------------")
    for cand_count in range(len(candidates)):
        print(f"{candidates[cand_count]}: {margins[cand_count]:.3f}% ({votes[cand_count]})")
    print(f"----------------------------")
    print(f"Winner: {candidates[windex]}")
    print(f"----------------------------")

#file for results
with open(output_file, 'w') as txtwriter:
    #write results
    txtwriter.write(f"Election Results\n")
    txtwriter.write(f"----------------------------\n")
    txtwriter.write(f"Total votes: {total_votes}\n")
    txtwriter.write(f"----------------------------\n")
    for cand_count in range(len(candidates)):
        txtwriter.write(f"{candidates[cand_count]}: {margins[cand_count]:.3f}% ({votes[cand_count]})\n")
    txtwriter.write(f"----------------------------\n")
    txtwriter.write(f"Winner: {candidates[windex]}\n")
    txtwriter.write(f"----------------------------\n")