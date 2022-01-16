import os
import csv
import pandas as pd

#open the file for reading
with open('../PyBank/Resources/budget_data.csv', 'r', encoding='utf-8') as csvfile:
#read the file
    csvreader = csv.reader(csvfile, delimiter=",")
# skip the header
    csv_header = next(csvreader)
#total months included in data
    tot_months = len(list(csvreader))
    print(f'Total Months: {tot_months}')
#locate the profit/loss column and sum
    csvreader = pd.read_csv('../PyBank/Resources/budget_data.csv')
    tot=sum(csvreader.loc[:,'Profit/Losses'])
    print(f'Net Total: ${tot}')
#calculate monthly changes by iterating over entire column and append to a list
    changes = []
    for x in range(0 , csvreader.shape[0]-1):
        change=csvreader.iloc[x+1, 1]-csvreader.iloc[x, 1]
        changes.append(change)
#average changes oven entire period
    ave_change=round(sum(changes)/(tot_months-1),2)
    print(f'Average Change: ${ave_change}')
#search for max_profit in changes [list] and corresponding date (index in csvreader)
    max_profit = max(changes)
    max_date_indx = changes.index(max_profit)
    max_date = csvreader.iloc[max_date_indx+1,0]
    print(f'Greatest Increase in Profits: {max_date} $({max_profit})')
#search for min_profit in changes [list] and corresponding date (index in csvreader)
    min_profit = min(changes)
    min_date_indx = changes.index(min_profit)
    min_date = csvreader.iloc[min_date_indx+1,0]
    print(f'Greatest decrease in Profits: {min_date} $({min_profit})')
#open external text file writing the results
    s1 = ['Total Months:  ', str(tot_months), '\n', 
        'Net Total:  ', '$', str(tot), '\n',
        'Average Change:  ', '$(',str(ave_change),')','\n',
        'Greatest Increase in Profits:  ', str(max_date),'  $(', str(max_profit),')','\n',
        'Greatest decrease in Profits:  ', str(min_date),'  $(', str(min_profit),')']
with open('../PyBank/pybank_results.txt', 'w', encoding='utf-8') as txtfile:
    for x in s1:
        txtfile.write(x)

    

        



   