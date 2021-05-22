# pcost.py
#
# Exercise 1.30


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



cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
