# report.py
import csv

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

    headers='       '.join(headers)
    print(f'{headers}')
    # print('-'*10,' ','-'*10,' ','-'*10,'  ','-'*10)
    print('\n')

    for i,k in enumerate(name):
        print(f'{name[i]:<10s} {shares[i]:<10d} {prices[i]:<10.2f} {change[i]:>10.2f}')



if __name__=='__main__':
    main()





