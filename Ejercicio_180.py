palabra="Procrastinar"
for i in range(len(palabra)):
    if palabra[i]=='a':             #Busca si letra es "a"
        print("Letra encontrada")
        break                       #Suspende la ejecución del for
    print(palabra[i])               #Imprime hasta que encuentra la "a"