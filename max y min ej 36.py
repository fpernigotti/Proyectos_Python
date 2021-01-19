n = int(input("Cuantos valores va a ingresar? "))
primeravez = True


for i in range(n):
    
    valor = int(input("ingrese el valor:"))
    
    if(primeravez == True):
        
        Min = valor
        Max = valor
        primeravez = False
    else:
        
        if(valor > Max):
            Max = valor
    
        if(valor<Min):
            Min = valor



print("Max: ",str(Max))
print("Min: ", str(Min))