# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename,select=None,types=None, is_header=False):
    '''
    This function parse a csv file into a list of records and filter it based on select and type options
    '''

    with open(filename) as f:
        rows=csv.reader(f)

        # Read the file header
        headers=next(rows) if is_header else []
  
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
                row = [func(val) for func, val in zip(types, row) ]      
            
            if is_header:
                record = dict(zip(headers, row))
            
            else:
                record=tuple(row)

            records.append(record)    

    return records
