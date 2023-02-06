frase=input("¿Cuál es la frase del día?: ").lower()
vocales=0
for letra in frase:                     #Obtiene letra por letra
    if letra in set("aeiouáéíóúü"):     #Evalúa si letra es vocal
        vocales+=1
print(f'{frase} tiene {vocales} vocales')