# fileparse.py
#
# Exercise 3.5

import csv

def parse_csv(filename,select=['name','shares','price'],types=[str,int,float]):
    '''
    This function parse a csv file into a list of records and filter it based on select and type options
    '''

    with open(filename) as f:
        rows=csv.reader(f)

        # Read the file header
        headers=next(rows)
        records=[]
        if select:
            idx=[headers.index(cols) for cols in select]
            headers=select

        for row in rows:
            if not row:
                continue  # skip rows with no data
            # indices = [ headers.index(colname) for colname in select ]
            
                # records.append(record)
            if select:
                row=[row[idxs] for idxs in idx]
                  
            if types:
                row = { func(val) for func, val in zip(types, row) }      
                 
            # if select:
            #     indices = [ headers.index(colname) for colname in select ]
            #     row = { colname: row[index] for colname, index in zip(select, indices) } 
            #     print(row) 
               
            record = dict(zip(headers, row))

            # record=dict(zip(headers,row))
                # record = {
                #  'name'   : record['name'],
                #  'shares' : int(record['shares']),
                #  'price'   : float(record['price'])
                # }    
            records.append(record)

    
    return records

records=parse_csv('Data/portfolio.csv',types=[str,int],select=['name','shares'])           
print(records)