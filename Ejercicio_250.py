def factorial(n):
    if n==0:
        return 1        #El factorial de 0 es 1
    else:
        res=1
        while n>0:      #El factorial de "n" es n x n-1 x n-2, ... ,1
            res*=n
            n-=1
        return res

print(factorial(5))