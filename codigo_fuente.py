import random as rd
import numpy as np
import matplotlib.pyplot as plt
import sys
import statistics as stats


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

def prom_r(N,n,r_i):
    """Función encargada de retornar una tupla con la siguiente información
    (N,<r>,<r^2>). Para esto se utilizan dos listas, r_s donde se almacenan
    todos los r encontrados y l_final, donde se almacenan todas las tuplas para
    cada N."""
    l_final = []
    for i in N:
        r_s = []
        r_s2 = 0
        for j in range(n):
            r = posicion_N(i,r_i)
            r_2 = r**2
            r_s2+=r_2
            r_s.append(r)
        prom = stats.mean(r_s)
        prom2 = r_s2/n
        t = (i,prom,prom2)
        l_final.append(t)
    return l_final


#Menú presentación consola

def printMenu():
    print("\nBienvenido a la marcha aleatoria en una dimensión")
    print("1- Posición r de la partícula luego de N pasos")
    print("2- Histograma con N =500 fijo")
    print("3- Comparación ley de probabilidad N = 500 - a = 1")
    print("4- <r> y <r^2> para distintos N")
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
    elif int(inputs[0]) == 4:
        N = [100,200,400,50,500]
        re = prom_r(N,200,0)
        for i in re:
            print(f"\nPara N = {i[0]}")
            print(f"\n <r> = {i[1]}")
            print(f"\n <r^2> = {i[2]}")
    else:
        sys.exit(0)



