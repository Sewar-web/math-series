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

print(lucas(0))        
print(lucas(1))        
print(lucas(2))        
print(lucas(3))        
print(lucas(4))  