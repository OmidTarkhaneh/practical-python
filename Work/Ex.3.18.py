
# exercise 3.18

import csv
import FixedcsvParser

def read_portfolio(filename):
    """ Read portfolio.csv using  FixedcsvParser module
    """
    with open(filename) as lines:
        return FixedcsvParser.parse_csv(lines, select=['name','shares','price'], types=[str,int,float],is_header=True)

def read_prices(filename):
    '''
    Read a CSV file of price data  using  FixedcsvParser module
    '''
    with open(filename) as lines:
       return dict(FixedcsvParser.parse_csv(lines, types=[str,float], is_header=False))
    



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

def main():
    portfolio=read_portfolio('Data/portfolio.csv')
    prices=read_prices('Data/prices.csv')
    report=make_report(portfolio,prices)
    print_report(report)


if __name__=='__main__':
    main()


# Modified pcost.py is as below

# def pcost(filename):
#     total_cost=0

#     with open(filename) as lines:
#         portfolio= FixedcsvParser.parse_csv(lines, select=['name','shares','price'], types=[str,int,float],is_header=True)

#     for stocks in portfolio:
#         total_cost+=stocks['shares']*stocks['price']

#     return total_cost 


# def main():
#     total_cost=pcost('Data/portfolio.csv')
#     print(total_cost)


# if __name__=='__main__':
#     main()
