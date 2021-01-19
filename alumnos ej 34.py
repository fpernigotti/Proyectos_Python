def mostrar_promedio(suma_notas,cantidad_de_alumnos):
    
    promedio = suma_notas/cantidad_de_alumnos
    print("el promedio es ", promedio)
    


alumnos_promocionados = 0
cantidad_de_alumnos  = 0
suma_notas = 0
print("Desea agregar un nuevo alumno?")
print("1-Si")
print("2-no")

opc = int(input())

while(opc == 1):
    
    notafinal = int(input("Ingrese la nota final: "))
    
    if(notafinal>=4):
        suma_notas = suma_notas+notafinal
        cantidad_de_alumnos = cantidad_de_alumnos +1
        
    
    
    if(notafinal>=6):
        alumnos_promocionados = alumnos_promocionados +1
    
    
  
    print("Desea agregar un nuevo alumno?")
    print("1-Si")
    print("2-no")

    opc = int(input())
    
    

mostrar_promedio(suma_notas,cantidad_de_alumnos)

print("Hay ",str(alumnos_promocionados)," alumnos promocionados con mas de 6" )

