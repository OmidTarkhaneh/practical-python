# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename):
    '''
    This function parse a csv file into a list of records
    '''

    with open(filename) as f:
        rows=csv.reader(f)

        # Read the file header
        headers=next(rows)
        records=[]
        for row in rows:
            if not row:
                continue  # skip rows with no data
            record=dict(zip(headers,row))
            records.append(record)

    return records

# records=parse_csv('Data/portfolio.csv')           
# print(records)

