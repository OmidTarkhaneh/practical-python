# pcost.py
#
# Exercise 1.27
total_cost=0

f=open('Data/portfolio.csv','rt')
headers=next(f)

for line in f:
    row=line.split(',')
    total_cost+=int(row[1])*float(row[2])

print(total_cost)

