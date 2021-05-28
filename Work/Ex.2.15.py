# pcost.py   usig enumerate
#
# Exercise 2.15
total_cost=0

f=open('Data/missing.csv','rt')
headers=next(f)

for rowno, row in enumerate(f):
    try:
        row=row.split(',')
        total_cost+=int(row[1])*float(row[2])
    except ValueError:
        print(f'Row{rowno}: Bad row:{row}')



print(total_cost)

