# mortgage.py
#
# Exercise 1.17

principal=500000.0
rate=0.05
payment=2684.11
total_paid=0.0

flag=True
Ex_month=12
Ex_value=1000

while principal > 0:
    while (Ex_month > 0) and (flag):
        principal=principal-Ex_value
        total_paid+=Ex_value
        Ex_month=Ex_month-1
        
    flag=False
    principal=principal * (1+rate/12)-payment
    total_paid= total_paid+payment


print('Total Paid', total_paid)    



