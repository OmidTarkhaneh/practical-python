def sumcount(n):
    '''
    This function return the sum of a number from 1..n 
      
    '''
    try:
        n=int(n)
    except ValueError:
        print("Oopps..you got a value error!")
        return   

        total=0
        while n>0:
            total+=n
            n-=1

        return total

             
# n=30

n='N/A'
total=sumcount(n)
print(f'sum of {n} is: {total}')    

print(help(sumcount))