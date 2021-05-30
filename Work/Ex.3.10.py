
import csv

def parse_csv(filename,select=None,types=None, is_header=False , silence_errors=True):
    '''
    This function parse a csv file into a list of records and filter it based on select and type options
    '''

    with open(filename) as f:
        rows=csv.reader(f)

        # Read the file header
        headers=next(rows) if is_header else []
        # if not is_header:
        #     headers=[]

        records=[]
        try:
            if select:
                idx=[headers.index(cols) for cols in select]
                headers=select
                
        except:
            if not silence_errors:
               print("select argument requires column headers")        
  
        try:
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
        except Exception as e:
                if not silence_errors:
                   print('Failed : Reason--->', e)
                  
        
    
    return records

records=parse_csv('Data/missing.csv',types=[str,int],is_header=True,silence_errors=True)           
print(records)
