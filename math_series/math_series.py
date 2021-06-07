def fibonacci(n):
    if n==0:
        return 0
    elif n==1 :
        return 1
    else:
       return fibonacci(n-1)+fibonacci(n-2)  
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))


def lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)    

       
print(lucas(1))        
print(lucas(2))        
print(lucas(3))        
 


def sum_series (n ,a=0 ,s=1):
    if a==0 and s==1:
        return fibonacci(n)
    elif a==2 and s==1:
        return lucas(n)
    else:
        return sum_series(n-1 ,a,s)+sum_series(n-2 ,a,s)

print(sum_series(1))
print(sum_series(2))
print(sum_series(3))



print(sum_series(0,2,1))
print(sum_series(3,2,1))
