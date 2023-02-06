def esNatural(n):
    if n>0 and int(n)==n:
        return True         #Regresa True si "n" es número natural
    else:
        return False        #Regresa False si "n" no es natural

print(esNatural(26.345))