def valorFuturo(valorActual,tasaInteres,periodos):
    VF=valorActual*(1+tasaInteres/100)**periodos
    return VF

print(valorFuturo(10000,10,1))  #-tasa del 10% en un año
print(valorFuturo(10000,2,12))  #-tasa del 2% mensual