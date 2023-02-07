import random as rd
import numpy as np
import matplotlib.pyplot as plt
import sys


def posicion_N(N,r_i):
    """Función encargada de retornar la posición final (r_f)
    de acuerdo al número de pasos (N) que entra como parámetro. Además,
    también entra como parámetro la posición inicial en la que se encuentra
    la partícula (r_i). Finalmente, r_t es la variable que pertenece al paso 
    que da la partícula en una de las iteraciones dentro del ciclo for."""
    r_f = r_i
    for i in range(N):
        #Se genera un número aleatorio entre [0,1]
        r_t = rd.random()
        if r_t>0.5:
            r_f+=1
        else:
            r_f-=1
    return r_f

#Menú presentación consola

def printMenu():
    print("\nBienvenido")
    print("1- Posición r de la partícula luego de N pasos")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        N = int(input("Ingrese el número de pasos N: "))
        r_i = int(input("Ingrese la posición inicial de la partícula (Número entero): "))
        r_f = posicion_N(N,r_i)
        if r_f ==0:
            print(f"\nLa posición final de la particula luego de {N} pasos es: {r_f} ")
        elif r_f <0:
            print(f"\nLa partícula se encuentra {r_f*-1} pasos a la izquierda respecto a su posición inicial.")
        else:
            print(f"\nLa partícula se encuentra {r_f} pasos a la derecha respecto a su posición inicial.")

    else:
        sys.exit(0)



