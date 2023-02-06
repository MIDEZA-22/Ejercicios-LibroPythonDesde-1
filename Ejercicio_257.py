def colorFavorito(color='rojo'):        #Por defecto asigna rojo
    msg=f'Tu color favorito es {color}'
    return msg

if c:=input("Dime tu color favorito: "):
    print(colorFavorito(c))
else:
    print(colorFavorito())