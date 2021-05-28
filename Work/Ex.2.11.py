# report.py
import csv

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
        dict1[converted_list[1]]=int(row[1])
        dict1[converted_list[2]]=float(row[2].strip())
        portfolio.append(dict1)
        dict1={}

    return portfolio  

def read_prices(filename):
    '''
    Read a CSV file of price data
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    '''
    
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
        
      

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')



report = make_report(portfolio, prices)

# Output the report
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
