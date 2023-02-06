tuTemperatura=int(input("Deme su temperatura: "))
if tuTemperatura>=38:
    print("Tiene fiebre")           #Bloque alternativa 1
    print("Acuda a un médico")
elif tuTemperatura<=35:
    print("Tiene hipotermina")      #Bloque alternativa 2
    print("Llame a emergencias")
else:
    print("Temperatura normal")     #Bloque alternativa 2
