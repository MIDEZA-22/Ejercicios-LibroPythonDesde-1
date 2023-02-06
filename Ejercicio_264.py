from turtle import color


def colores(colorlocal='azul'):
    global color                    #"color" declarado como global y en la función
    color='rojo'
    print("Color local dentro de función colores:",colorlocal)
    print("Color dentro de función colores:",color)

colores()
print("Color fuera de función colores:",color)