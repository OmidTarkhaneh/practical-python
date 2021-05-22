# bounce.py
#
# Exercise 1.5

Height =100
back_up=3/5
items=10

while items > 0:
    Height= back_up*Height
    items-=1
    print(Height)

