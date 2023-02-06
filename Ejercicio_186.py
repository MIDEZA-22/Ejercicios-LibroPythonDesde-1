palabra="abracadabra"
for i in range(len(palabra)):
    if palabra[i]=='e':                         #Búsqueda del carácter "e"
        break
else:
    print(f"En {palabra} no existe la letra e")  