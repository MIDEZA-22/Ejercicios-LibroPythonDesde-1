def formulaGeneral(a,b,c):              #Obtiene las raíces reales de una ecuación de la forma ax^2+bx+c
    solucion=([])               
    discriminante=b**2-(4*a*c)
    if discriminante==0:                #Caso con 1 solución
        solucion.append(-b/(2*a))
    elif discriminante<0:               #Caso no hay solución
        solucion.append('Sin solución')
    else:                               #Caso con 2 soluciones
        solucion.append((-b+discriminante**0.5)/(2*a))
        solucion.append((-b-discriminante**0.5)/(2*a))
    return solucion

sol=formulaGeneral(2,3,-5)              #Pasa los valores a: "a","b" y "c")
for i in sol:
    print(i)                            #Imprime el listado de soluciones