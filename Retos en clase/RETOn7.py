'''
Escibir una funcion que reciba 
una frase por teclado y devuelva 
un diccionario con las palabras 
que contiene y su longitud"
'''


def palabras():
    print("Ingrese su frase:")
    ingresada = str(input())
    separada = ingresada.split()
    diccionario = {}

    for i in separada:
       diccionario[i] = len(i)

    print(diccionario)

palabras()


