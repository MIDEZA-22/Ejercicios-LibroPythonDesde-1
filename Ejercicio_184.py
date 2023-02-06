sumaEdades=0
mayores=0
for i in range(10):
    print(f"Edad de la {i+1}ra persona:",end="")
    edad=float(input())
    if(edad<18):                                    #Descarta incluir en los cálculos los menores de 18 años
        continue                                    
    sumaEdades+=edad
    mayores+=1
promedio=sumaEdades/mayores
print("Promedio:",round(promedio))