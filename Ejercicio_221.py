n=3
while n>0:
    print("¡Hola Mundo!")
    msj="Quieres saludar nuevamente [si,no]:"
    if input(msj).lower() not in {'si','s'}:break
    n-=1
else:
    print("¡Hoy realizamos todos nuestros saludos!")