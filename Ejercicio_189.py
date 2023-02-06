prod=('ok','ok','bad','ok','ok')
for i in range(len(prod)):
    if prod[i]=='bad':
        print('Producto erróneo')       #Se encontró producto erróneo
        break                           #Interrumpe la ejecución del for
    print("Parece que todo bien")
else:
    print("Excelente calidad")