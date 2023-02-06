num=1246.848
cad=""
x,y=0,0
for i in str(num):                          #Número tratado como cadena
    if i=='.':
        x=int(cad)
        cad=""
    else:
        cad+=i                              #Concatena dígito a dígito
y=int(cad)
print(x,y,sep=";") if x!=0 else print(y)