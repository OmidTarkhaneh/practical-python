# report.py
#
# Exercise 2.4

# pcost.py
#
# Exercise 1.30


def read_portfolio(filename):
    """ This function return total cost of purchasing price of shares
    """
    portfolio=[]

    f=open(filename,'rt')
    headers=next(f)

    for line in f:
        row=line.split(',')
        holding=(row[0],int(row[1]),float(row[2]))
        portfolio.append(holding)

    return portfolio    


portfolio = read_portfolio('Data/portfolio.csv')
print('portfolio:', portfolio)
