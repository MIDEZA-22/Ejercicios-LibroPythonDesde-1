def sonMultiplos(a,b):          #"a" se le asigna 100 y "b" 1000
    if a%b==0:
        return True
    elif b%a==0:
        return True
    else:
        return False

print(sonMultiplos(100,1000))   #Envía dos argumentos