# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=['name','shares','price']):
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
            
            if select:
                indices = [ headers.index(colname) for colname in select ]
                record = { colname: row[index] for colname, index in zip(select, indices) } 
            else:
                record=dict(zip(headers,row))
                record = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
                }    
            records.append(record)

    
    return records

records=parse_csv('Data/portfolio.csv')           
print(records)