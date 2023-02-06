def areaCuadrado(lado):                 #Calcula el área de la base
    area=lado*lado
    return area

def volumenCubo(lado):
    volumen=areaCuadrado(lado)*lado     #Reutilización del área x altura
    return volumen

print(volumenCubo(2))