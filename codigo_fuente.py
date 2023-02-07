import random as rd
import numpy as np
import matplotlib.pyplot as plt


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

print(posicion_N(100,0))