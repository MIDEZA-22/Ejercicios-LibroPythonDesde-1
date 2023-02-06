print('Menu de opciones')
print('[1] Altas')
print('[2] Bajas')
print('[3] Cambios')
print('[4] Reportes')
print('[5] Salir')

op=int(input('Elije una opción: '))
if op==1:                                   #Opción 1
    print("Bloque para realizar altas")
elif op==2:                                 #Opción 2
    print("Bloque para realizar bajas")
elif op==3:                                 #Opción 3
    print("Bloque para hacer cambios")
elif op==4:                                 #Opción 4
    print("Bloque para generar reportes")
elif op==5  :                               #Opción 5
    print("Gracias por participar")
else:                                       #Opción por defecto
    print("Opción no valida")   