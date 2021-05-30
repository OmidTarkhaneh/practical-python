
import FileParser
'''
This module will utilize FileParser module and modify pcost.py
'''
total_cost=0

portfolio=FileParser.parse_csv('Data/portfolio.csv', select=['name','shares','price'], types=[str,int,float],is_header=True)
for stocks in portfolio:
    total_cost+=stocks['shares']*stocks['price']

print(total_cost)    