import csv
from os import name

def read_portfolio(filename):
    """ This function return portfolio in a dictonary
    """
    portfolio=[]
    dict1={}


    f=open(filename,'rt')
    rows=csv.reader(f)
    headers=next(rows)
         

    for rowno, row in enumerate(rows, start=1):
        try:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)
        except ValueError:
                print(f'Row {rowno}: Bad row: {row}')    

    return portfolio 


portfolio=read_portfolio('Data/portfolio.csv')


# using list comprehension
more100=[ stocks for stocks in portfolio if stocks['shares']>100]
# print(more100, '\n')

msftibm=[ stocks for stocks in portfolio if stocks['name'] in {'MSFT','IBM'}]

# print(msftibm)

cost10k = [ stocks for stocks in portfolio if stocks['shares'] * stocks['price'] > 10000 ]
# print(cost10k)




# ex.2.22
name_shares =[ (s['name'], s['shares']) for s in portfolio ]
#print(name_shares)

names={s['name'] for s in portfolio}
print(names)

holdings={name: 0 for name in names}
print(holdings)