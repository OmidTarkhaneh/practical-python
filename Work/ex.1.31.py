# pcost.py
#
# Exercise 1.31


def Total_PortfolioCost(path):
    """ This function return total cost of purchasing price of shares
    """
    total_cost=0

    f=open(path,'rt')
    headers=next(f)

    for line in f:
        row=line.split(',')
        total_cost+=int(row[1])*float(row[2])

    return total_cost    


path='Data/portfolio.csv'
total_cost=Total_PortfolioCost(path)
print(total_cost)

