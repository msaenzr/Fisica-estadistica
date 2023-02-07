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
        #Se verifica si el paso es a la derecha
        if r_t>0.5:
            r_f+=1
        else:
            r_f-=1
    return r_f

def datahistograma_r(N,n,r_i):
    """Función encargada de retornar los datos para un histograma, donde entra como 
    parámetro N (Número de pasos), n (Número de iteraciones) y r_i (posición
    inicial de la partícula)."""
    # r = Lista que guarda todo los valores dados dentro de las n iteraciones.
    r = []
    for i in range(n):
        r_n = posicion_N(N,r_i)
        r.append(r_n)
    #bins = Se definen los limites del histograma teniendo en cuenta el número menor y mayor de r.
    bins = range( min(r), max(r)+1)
    return (r,bins)

def histograma_r(N,n,r_i):
    #Se definen los datos del histograma y toda la parte estética de la gráfica.
    t = datahistograma_r(N,n,r_i) 
    plt.hist(t[0],t[1],color="brown")
    plt.title('Histograma marcha aleatoria 1D')
    plt.xlabel('Posición final (m)')
    plt.ylabel('Frecuencia')
    plt.show()

def ley_probabilidad(N,n,r_i):

    t =datahistograma_r(N,n,r_i)
    x = np.linspace(min(t[0]),max(t[0]))
    a = 2/(2*np.pi*N)
    b = -(x**2)/(2*N)
    f = a* np.exp(b)
    plt.plot(x,f,color="brown")
    plt.title('Ley de probabilidad')
    plt.xlabel('Posición final (m)')
    plt.ylabel('Frecuencia')
    plt.show()



#Menú presentación consola

def printMenu():
    print("\nBienvenido a la marcha aleatoria en una dimensión")
    print("1- Posición r de la partícula luego de N pasos")
    print("2- Histograma con N =500 fijo")
    print("3- Comparación ley de probabilidad N = 500 - a = 1")
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
    elif int(inputs[0]) == 2:
        histograma_r(500,40000,0)
    elif int(inputs[0]) == 3:
        ley_probabilidad(500,40000,0)
    else:
        sys.exit(0)



