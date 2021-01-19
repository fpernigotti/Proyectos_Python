zona =int(input("Ingrese la zona: "))



while (zona != 0):
    
    
    
    edad = int(input("ingrese la edad: "))
    
    #-si la zona está ente 1 y 3 informar que le corresponde Categoría A y que de acuerdo a su edad le corresponde Tipo 1 hasta 15 años, Tipo 2 hasta 25 y Tipo 3 si supera los 25 años.
    if((zona>=1)and(zona<=3)):
        print("Categoria A")
        
        if(edad<=15):
            print("Tipo 1")
        elif((edad>15)and(edad<=25)):
            print("tipo 2")
        else:
            print("tipo 3")
    #-si la zona está ente 4 y 6 informar que le corresponde Categoría B y que de acuerdo a su edad le corresponde 
    #Tipo 1 hasta 20 años, Tipo 2 hasta 40 y Tipo 3 si supera los 40 años.
    elif((zona>=4)and(zona<=6)):
        print("Categoria B")
        
        if(edad<=20):
            print("Tipo 1")
        elif((edad>20)and(edad<=40)):
            print("tipo 2")
        else:
            print("tipo 3")

    #-si la zona está ente 7 y 8 informar que le corresponde Categoría C y que 
    #de acuerdo a su edad le corresponde Tipo 1 hasta 20 años, Tipo 2 hasta 35 y Tipo 3 si supera los 35 años.
    elif((zona==7)or(zona==8)):
        print("Categoria C")
        
        if(edad<=20):
            print("Tipo 1")
        elif((edad>20)and(edad<=35)):
            print("tipo 2")
        else:
            print("tipo 3")
    
    #-y si la zona está ente 9 y 10 informar que le corresponde Categoría D y que de acuerdo a su edad le corresponde 
    #Tipo 1 hasta 18 años, Tipo 2 hasta 30, Tipo 3 hasta 50 y Tipo 4 si supera los 50 años de edad.
    elif((zona==9)or(zona==10)):
        print("Categoria D")
        
        if(edad<=18):
            print("Tipo 1")
        elif((edad>18)and(edad<=30)):
            print("tipo 2")
        elif((edad>30)and(edad<=50)):
            print("tipo 3")
        else:
            print("tipo 4")        
    
    
    zona =int(input("Ingrese la zona: "))
   





print("muchas gracias")

