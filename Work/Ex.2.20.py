import csv

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
total_cost = 0.0
# for stocks in portfolio:
#     total_cost += int(stocks['shares'])*float(stocks['price'])    


# using list comprehension
total_cost=sum([int(stocks['shares'])*float(stocks['price']) for stocks in portfolio])
print(total_cost)

