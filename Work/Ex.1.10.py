principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_pay = 1000.0
start_month = 61
end_month = 108

while principal > 0:
    
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month = month + 1
    if month >= start_month and month <= end_month:
        principal = principal - extra_pay
        total_paid = total_paid + extra_pay

    print(month, round(total_paid,2), round(principal, 2))
    
print('Total paid', round(total_paid, 2))
print('Months', month)