A=[[1,2],[3,4]]
B=[[10,20],[30,40]]
C=[[0,0],[0,0]]
i=0
while i<2:                      #Repite dos veces el ciclo interior
    j=0
    while j<2:                  #Ciclo interno con dos iteraciones
        C[i][j]=A[i][j]+B[i][j];j+=1
    i+=1
print(f"{A = }")
print(f"{B = }")
print(f"{C = }")    