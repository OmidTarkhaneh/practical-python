import sys
import csv



def portfolio_cost(filename):
    """ This function return total cost of purchasing price of shares
    """
    total_cost=0

    f=open(filename,'rt')
    rows=csv.reader(f)
    headers=next(rows)
    
    for rowno, row in enumerate(rows, start=1):
        record=dict(zip(headers,row))
       
        try:
            nshares=int(record['shares'])
            price=float(record['price'])
            total_cost+=nshares*price
        except ValueError:
            print(f'Row{rowno}: Bad row: {row}')    

    return total_cost    

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)


#********************************************************************************
# try zip on report.py


prices = {}
headers=[]
shares=[]
prices=[]
change=[]
name=[]

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
    rows=csv.reader(f)
    headers=next(rows)
  
    
    converted_list = []
    for element in headers:
        converted_list.append(element.strip())
        

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

    return portfolio, converted_list    




def make_report():
    '''  This function retuns data in a format of a list
    '''
    portfolio, headers = read_portfolio('Data/portfolio.csv')
    Myprices = read_prices('Data/prices.csv')
    headers.append('change')
    for item in portfolio:
        name.append(item['name'])
        shares.append(int(item['shares']))
        prices.append(float(item['price']))
        change.append(float(Myprices[item['name']])- float(item['price']))
    
    
    return name,shares,prices,change,headers    
    




def main():
    ''' This function shows data in a formated styles
    '''
    name,shares,prices,change,headers=make_report()
    # zippedlst=list(zip(name,shares,prices,change)) # this way googd too
    headers='      '.join(headers)
    print(f'{headers}')
    print('-'*7,' ','-'*7,' ','-'*7,'  ','-'*7)


    for i,k in enumerate(name):
        print(f'{name[i]:<10s} {shares[i]:<10d} ${prices[i]:<10.2f}  {change[i]:<10.2f}')



if __name__=='__main__':
    main()

