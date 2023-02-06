calificacion=0
suma=0
for _ in range(3):                          #Genera tres iteraciones
    print("Teclee calificación: ",end="")   #Inicio del bloque for
    calificacion=float(input())
    suma+=calificacion                      #Fin del bloque for
print("Promedio: ",suma/3)