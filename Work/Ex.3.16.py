# report.py
# exercise 3.16

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


def main(args):
    if len(args) != 3:
        raise SystemExit('Errror in number of arguments' % args[0])
    report=make_report(args[1], args[2])
    print_report(report)

# Output the report
if __name__ == '__main__':
    import sys
    main(sys.argv)



# we can do the same thing on pcost.py



# def pcost(filename):
#     total_cost=0
#     portfolio=FileParser.parse_csv(filename, select=['name','shares','price'], types=[str,int,float],is_header=True)
#     for stocks in portfolio:
#         total_cost+=stocks['shares']*stocks['price']

#     return total_cost  


# def main(args):
#         if len(args) != 2:
#            raise SystemExit('Errror in number of arguments' % args[0])
#         total_cost=pcost(args[1])
#         print(total_cost)

