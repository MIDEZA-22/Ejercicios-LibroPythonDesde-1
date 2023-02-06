def diaSemana(d):        #Recibe parámetro 1 en "d"
    semana=('Lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo')
    return semana[d-1]  #Regresa día de semana

dia=diaSemana(1)        #Invoca función con parámetro 1
print(dia)              #Imprime día de la semana