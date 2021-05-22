import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)

for row in rows:
  print(row)