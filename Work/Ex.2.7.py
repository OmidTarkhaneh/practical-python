# report.py
import csv

prices = {}

def read_prices(filename):
    """ This function return prices in a dict
    """
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices 


def read_portfolio(filename):
    """ This function return portfolio in a dictonary
    """
    portfolio=[]
    dict1={}


    f=open(filename,'rt')
    headers=next(f).split(',')
    headers=list(headers)
    
    converted_list = []


    for element in headers:

        converted_list.append(element.strip())


    for line in f:
        row=line.split(',')
        dict1[converted_list[0]]=row[0].strip('"')
        dict1[converted_list[1]]=row[1]
        dict1[converted_list[2]]=row[2].strip()
        portfolio.append(dict1)
        dict1={}

    return portfolio    


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')


total_cost = 0.0
for stocks in portfolio:
    total_cost += int(stocks['shares'])*float(stocks['price'])


print('Total cost', total_cost)


totalval = 0.0
for st in portfolio:
    totalval += int(st['shares'])*float(prices[st['name']])
     
   
print('Current value', totalval)
print('Gain', totalval - total_cost)





