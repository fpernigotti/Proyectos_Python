

def sumar(numero_1,numero_2):
    
    res = numero_1 + numero_2
    
    print("el resultado es: ", str(res))
    

def restar(numero_1,numero_2):
    
    res = numero_1 - numero_2
    
    print("el resultado es: ", str(res))
    

def multiplicar(numero_1,numero_2):
    
    res = numero_1 * numero_2
    print("el resultado es: ", str(res))


def dividir(numero_1,numero_2):
    
    if(numero_2 != 0):
        
        res = numero_1/numero_2
        print ("el resultado es: ",str(res))
    else:
        print("El divisor es 0")







while True:
    try:
        numero_1 = int(input("Ingrese el primer numero: "))
        numero_2 = int(input("Ingrese el segundo numero: "))
        
        print("Elija una opcion:")
        print("1_suma")
        print("2_resta")
        print("3_producto")
        print("4_division")
        
        opcion = int(input())
        
    except:
        print("Error")
        
#######################################################################        
        
    if( opcion == 1):
        
        sumar(numero_1,numero_2)
        break
    
    elif( opcion == 2 ):
        
        restar(numero_1,numero_2)
        break
    
    elif( opcion == 3):
        
        multiplicar(numero_1,numero_2)
        break
    elif( opcion == 4):
        
        dividir(numero_1,numero_2)
        break
    else:
        print("opcion erronea")
        
            





