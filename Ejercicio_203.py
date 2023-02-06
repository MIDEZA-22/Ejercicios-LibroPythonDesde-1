M={'EUR':'Euro','INR':'Rupia','GTQ':'Quetzal'}
for clave in M: 
    if clave=='EUR':                                #Obtiene clave del diccionario
        print("Moneda:",M[clave])                  #Recupera valor con la clave
print("Fin de la búsqueda")