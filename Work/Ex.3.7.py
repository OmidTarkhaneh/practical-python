# Exercise 3.7

import csv

def parse_csv(filename,select=None,types=None, is_header=False, Mydelimiter=' '):
    '''
    This function parse a csv file into a list of records and filter it based on select and type options
    '''

    with open(filename) as f:
        rows=csv.reader(f,delimiter=Mydelimiter)

        # Read the file header
        headers=next(rows)
        # if not is_header:
        #     headers=[]

        records=[]
        if select:
            idx=[headers.index(cols) for cols in select]
            if is_header:
               headers=select
            else:
                headers=[]   

        for row in rows:
            if not row:
                continue  # skip rows with no data
            # indices = [ headers.index(colname) for colname in select ]
            
                # records.append(record)
            if select:
                row=[row[idxs] for idxs in idx]
                  
            if types:
                row = [func(val) for func, val in zip(types, row)]     
            
            if is_header:
              record = dict(zip(headers, row))
              
            else:
                record=tuple(row)
                  
            records.append(record)
    
    return records

records=parse_csv('Data/portfolio.dat',types=[str,int],select=['name','shares'],is_header=True)           
print(records)