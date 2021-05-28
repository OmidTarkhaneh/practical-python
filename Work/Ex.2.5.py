# report.py
#
# Exercise 2.5


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
        # dict1=dict(zip(headers,row))---- this method can be used too-- somehow pythonic :)
        dict1[converted_list[0]]=row[0].strip('"')
        dict1[converted_list[1]]=row[1]
        dict1[converted_list[2]]=row[2].strip()
        portfolio.append(dict1)
        dict1={}

    return portfolio    


portfolio = read_portfolio('Data/portfolio.csv')
print('portfolio:', portfolio)
