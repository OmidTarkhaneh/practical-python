# exercise 3.12

import csv
import FileParser

def read_portfolio(filename):
    """ Read portfolio.csv using  FileParser module
    """
    return FileParser.parse_csv(filename, select=['name','shares','price'], types=[str,int,float],is_header=True)  

def read_prices(filename):
    '''
    Read a CSV file of price data  using  FileParser module
    '''
    return dict(FileParser.parse_csv(filename,types=[str,float], is_header=False))



def make_report(portfolio, prices):
    '''
      Create a report 
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
        
      
def  print_report(report):

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)


# Output the report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report)





