lista=[2,3,4,9,5,6,7,8,10,1]
cambio, n=True, len(lista)-1
while n>0:
    cambio=False
    for i in range(n):
        if lista[i] > lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            cambio=True
    if not cambio:break
    n-=1
print(lista)