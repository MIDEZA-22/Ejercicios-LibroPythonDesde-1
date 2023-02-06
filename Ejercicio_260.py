def titulo(texto):                  #Función para imprimir encabezado
    print(25*'*')
    print(f'*{texto:^23}*')
    print(25*'*')

def muestraMenu(texto,*opciones):   #Función para imprimir menu
    titulo(texto)                   #Invoca función "titulo()"
    for i in opciones:
        print(f'[{opciones.index(i)+1:^3d}] => {i:22s}')

muestraMenu('Menu Opciones','Abrir','Guardar','Guardar como','Salir')