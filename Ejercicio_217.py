s=3,6,9,-5,7
i,c=0,0
while i<len(s):
    if s[i]>0:c+=1
    i+=1
else:                           #Cuando "i" es igual a 5
    print(f"Número de Positivos: {c}")