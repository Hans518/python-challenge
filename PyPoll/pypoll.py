# Modules
import os
import csv

#set variable for csv path
election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')

#Read CSV   
with open(election_data_csv, 'r') as csvfile:
    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #Declare necessary variables. 
    vote_count = 0
    #candidate_list = []
    cadidate_name = str()
    khan_count = 0
    khan_perc = float() 
    correy_count = 0
    correy_perc = float()
    li_count = 0
    li_perc = float() 
    otooley_count = 0
    otooley_perc = float()

    #Parse through data
    for row in csvreader:

        #Count the total votes cast
        vote_count = vote_count + 1

        #Determine the list of candidates since there are 3.5 million votes. 
        #if row[2] not in candidate_list:
         #   candidate_list.append(row[2])        

        #Count votes
        if row[2] == "Khan":
            khan_count = khan_count + 1
        elif row[2] == "Correy":
            correy_count = correy_count + 1
        elif row[2] == "Li":
            li_count = li_count + 1
        elif row[2] == "O'Tooley":
            otooley_count = otooley_count + 1

#Calculate vote percentages.

#Khan
khan_perc = round((khan_count / vote_count), 2) * 100 
#Correy
correy_perc = round((correy_count / vote_count), 2) * 100
#Li
li_perc = round((li_count / vote_count), 1) * 100
#O'Tooley
otooley_perc = round((otooley_count / vote_count), 2) * 100

#Calculate winner
candidate_vote_count = [khan_count, correy_count, li_count, otooley_count]
winner = max(candidate_vote_count)
if max(candidate_vote_count) == correy_count:
        winner_count = correy_count
        winner_name = "Correy"
elif max(candidate_vote_count) == li_count:
        winner_count = li_count
        winnder_name = "Li"
elif max(candidate_vote_count) == otooley_count:
        winner_count = otooley_count
        winner_name = "O'Tooley"
elif max(candidate_vote_count) == khan_count:
        winner_count = khan_count
        winner_name = "Khan"

#Print output data.
#print(header)
print(f"-------------------------------------------")
print(f"There were {vote_count} total votes cast.")  
print(f"-------------------------------------------")
print(f"Khan:      {khan_perc}%       {khan_count}")     
print(f"Correy:    {correy_perc}%       {correy_count}")   
print(f"Li:        {li_perc}%       {li_count}")
print(f"O'Tooley:  {otooley_perc}%        {otooley_count}")        
print(f"-------------------------------------------")
print(f" The winner is {winner_name} in a landslide.")            
print(f"-------------------------------------------")

with open("output.txt", "w") as text_file:
    print(f"-------------------------------------------", file=text_file)
    print(f"There were {vote_count} total votes cast.", file=text_file)  
    print(f"-------------------------------------------", file=text_file)
    print(f"Khan:      {khan_perc}%       {khan_count}", file=text_file)     
    print(f"Correy:    {correy_perc}%       {correy_count}", file=text_file)   
    print(f"Li:        {li_perc}%       {li_count}", file=text_file)
    print(f"O'Tooley:  {otooley_perc}%        {otooley_count}", file=text_file)        
    print(f"-------------------------------------------", file=text_file)
    print(f" The winner is {winner_name} in a landslide.", file=text_file)            
    print(f"-------------------------------------------", file=text_file)