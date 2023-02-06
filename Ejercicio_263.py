def funcionInternaNivel1():             #Bloque 1,interno al principal
    def funcionInternaNivel2():         #Bloque 2,interno al bloque 1
        def funcionInternaNivel3():     #Bloque 3,interno al bloque 2
            objLocalNivel3=40
            print(objLocalNivel3)
            print(objLocalNivel2)
            print(objLocalNivel1)
            print(objLocalPrincipal)    #Fin del bloque 3

        objLocalNivel2=30
        funcionInternaNivel3()          #Fin del bloque 2
        
    objLocalNivel1=20
    funcionInternaNivel2()              #Fin del bloque 1

objLocalPrincipal=10
funcionInternaNivel1()                  #Bloque principal
