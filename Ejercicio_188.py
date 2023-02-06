palabra="crush"
for i in range(len(palabra)):
    if palabra[i]=='u':                 #Busca el carácter "u"
        break                           #Interrumpe ejecución del for
else:
    print("No se encontró letras u")