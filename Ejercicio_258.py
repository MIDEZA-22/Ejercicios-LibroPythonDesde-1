def sumaAcumulada(*sumandos):       #Recibe la lista de valores
    suma=0
    for n in sumandos:              #Recorre la lista y se acumula la suma
        suma+=n
    return suma

a=sumaAcumulada(2,4,3,1)
b=sumaAcumulada(1,2,3,4,5,6,7,8,9)
print(a)
print(b)