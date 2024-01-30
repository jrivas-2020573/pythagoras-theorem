from math import sqrt

opcion = int(input("1 = hallar cateto, 2 = hallar hipotenusa: "))

def switch(opcion): 
    if opcion == 1:
        hipotenusa = float(input("Ingrese la hipotenusa: "))
        cateto = float(input("Ingrese el cateto conocido: "))
        res = sqrt(hipotenusa**2 - cateto**2)
        print(f"El valor del cateto es: {res}")
    elif opcion == 2:
        cateto1 = float(input("Ingrese el primer cateto: "))
        cateto2 = float(input("Ingrese el segundo cateto: "))
        res = sqrt(cateto1**2 + cateto2**2)
        print(f"El valor de la hipotenusa es: {res}")
    else:
        print("Opción no válida")

switch(opcion)
