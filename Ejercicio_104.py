a="Hola mundo, Hola ¿cómo estas?"
print(f'{a.find("la")=}')   #Busca "la" desde el inicio
print(f'{a.find("la",8)=}') #Busca "la" a partir de posición 8
print(f'{a.find("XX")=}')   #NO encuentra la "XX"