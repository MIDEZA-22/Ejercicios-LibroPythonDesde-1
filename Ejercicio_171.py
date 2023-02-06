contador=0
for z in range(100,501):                #"z" recorre del 100 al 500
    if z%7==0:                          #Evalúa si "z" es múltiplo de 7
        contador+=1                     #Si es múltiplo lo cuenta
print("Total múltiplos de 7:",contador)