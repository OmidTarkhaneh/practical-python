# pcost.py
#
# Exercise 1.33

import sys

def portfolio_cost(filename):
    """ This function return total cost of purchasing price of shares
    """
    total_cost=0

    f=open(filename,'rt')
    headers=next(f)

    for line in f:
        row=line.split(',')
        total_cost+=int(row[1])*float(row[2])

    return total_cost    

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)