def mayor(a,b):
    if a>b:
        return a    #Regresa "a" como el mayor
    elif b>a:
        return b    #Regresa "a" como el mayor
    else:
        return -1   #Regresa -1 si son iguales

print(mayor(10,6))