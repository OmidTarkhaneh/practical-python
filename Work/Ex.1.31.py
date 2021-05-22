
total_cost=0


try:
    f=open('Data/portfolio.csv','rt')
    headers=next(f)

    for line in f:
        row=line.split(',')
        total_cost+=int(row[1])*float(row[2])
except:
    print("OOps..  you have an Error.")
      

print(total_cost)

