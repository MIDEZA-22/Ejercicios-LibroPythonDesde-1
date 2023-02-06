cad="carambolas"
cuenta=0
for i in range(len(cad)):
    if cad[i]!='a':                         #Si la letra no es una "a"
        continue                            #Ignora las 2 línea siguientes
    cuenta+=1
    print("Encontré una 'a' en cad[",i,"]")
print("Total de letras 'a':",cuenta)
