import os
import csv
import pandas as pd

#open the file
with open('../PyPoll/Resources/election_data.csv', 'r', encoding='utf-8') as csvfile:
#read the file
    csvreader = csv.reader(csvfile, delimiter=",")
# skip the header
    csv_header = next(csvreader)
# total votes
    tot_votes = len(list(csvreader))
    print(f'--------------------\n Election Results \n--------------------')
    print(f'Total Votes: {tot_votes}\n--------------------')
    csvreader = pd.read_csv('../PyPoll/Resources/election_data.csv')
# each candidate's vote and percent details
    candidates = pd.unique(csvreader.loc[:,'Candidate'])
    vote_count = []
    for candidate in candidates:
        votes = csvreader.loc[csvreader['Candidate'] == candidate]
        cand_votes = votes.shape[0]
        vote_count.append(cand_votes)
        percent_cand_votes = round((cand_votes *100 / tot_votes),2)
        print(f'{candidate}: {percent_cand_votes}% ({cand_votes}) ')
# look for max values and index
    max_votes = max(vote_count)
    max_votes_indx = vote_count.index(max_votes)
# find winner
    winner = candidates[max_votes_indx]
    print(f'--------------------\n Winner: {winner}\n--------------------')
