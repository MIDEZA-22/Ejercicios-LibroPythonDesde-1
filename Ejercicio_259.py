def promedio(*calificaciones):      #Recibe lista de calificaciones
    suma=0
    contador=0
    for n in calificaciones:        #Recorre la lista de parámetros
        suma+=n
        contador+=1
    return suma/contador            #Calcula el promedio

a=promedio(10,8,8,9,9)
b=promedio(9,9,9)
print(a)
print(b)