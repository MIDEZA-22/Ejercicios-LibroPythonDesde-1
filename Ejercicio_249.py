def fibonacci(n):       #Fibonacci es la suma de los dos números anteriores de la serie iniciando con 0 y 1
    A=([])          
    a,b=0,1
    while b<n:
        A.append(b)
        a,b=b,a+b
    return A

print(fibonacci(1000))