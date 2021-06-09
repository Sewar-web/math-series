def fibonacci(n):
    if n==0:
        return 0
    elif n==1 :
        return 1
    else:
       return fibonacci(n-1)+fibonacci(n-2)  
fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(5)


def lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)    

       
lucas(1)      
lucas(2)        
lucas(3)        
 


def sum_series (n ,a=0 ,s=1):
    if a==0 and s==1:
        return fibonacci(n)
    elif a==2 and s==1:
        return lucas(n)
        
    else:
        if n==0:
            return sum_series(a)
        elif n==1:
            return sum_series(s) 
        else:
             return sum_series(n-1,a,s) + sum_series(n-2,a,s)
   


sum_series(1)
sum_series(2)
sum_series(3)



sum_series(0,2,1)
sum_series(1,2,1)
sum_series(3,2,1)
