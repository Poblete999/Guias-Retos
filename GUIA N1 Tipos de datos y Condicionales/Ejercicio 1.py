'''
1. Realizar un algoritmo que indique el numero menor y el numero mayor entre tres
enteros leidos por consola. Solo se deben ingresar numeros enteros.

'''

N1 = int(input("Ingrese el primer número "))
N2 = int(input("Ingrese el segundo número "))
N3 = int(input("Ingrese el tercer número "))

if N1 > N2:
    N1 > N3
    print("El número mayor es ", N1)
else: 
    if N2 > N3:
        print("El número mayor es ", N2)
    else:
        print("El número mayor es ", N3)
