import matplotlib.pyplot as plt
import numpy as np

# Es el número de puntos con el que vamos a graficar la circunferencia, irrelevante.
def PuntosCircunferencia(N_Puntos=10000):   # Le damos un default de 10000 q con eso alcanza.
    Puntos_Circ = [[],[]]
    Alfa = (2*np.pi)/N_Puntos
    for i in range(N_Puntos):   # Calculamos el sen y cos para un angulo dado, y con eso sacamos las coordenadas X e Y.
        Puntos_Circ[0].append(np.cos(Alfa*i))
        Puntos_Circ[1].append(np.sin(Alfa*i))
    return Puntos_Circ


def AreaCirculo_ConPoligonos(N_Lado, Puntos_Circ):
    Puntos_Poligono = [[],[]]
    Alfa = (2*np.pi)/N_Lado

    for i in range(N_Lado+1):
        Puntos_Poligono[0].append(np.cos(Alfa*i))
        Puntos_Poligono[1].append(np.sin(Alfa*i))

    Valor_Area = (N_Lado/2)*np.sin(Alfa)   # Este es el valor del area del polígono.

    plt.figure(figsize=[8,8])
    plt.plot(Puntos_Circ[0], Puntos_Circ[1], ".", ms=2, color="grey")
    plt.plot(Puntos_Poligono[0], Puntos_Poligono[1], color="crimson")
    plt.title("Circunferencia de radio R=1 centrada en (0,0).\nCon n="+str(N_Lado)+" se tiene Area="+str(Valor_Area))
    plt.show()


if __name__ == "__main__":
    # Aproximar el Area del círculo usando polígonos.    
    Puntos_Circ = PuntosCircunferencia()    # Círculo de radio 1.

    # Notar que al aumentar el número de lados del polígono, el valor del
    # area del poligono se acerca cada vez mas a PI, el área de circulo.
    N_Lados = [3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000, 100000, 1000000]    # El número de lados que tendrán nuestro polígonos.
    
    for N_Lado in N_Lados:
        AreaCirculo_ConPoligonos(N_Lado, Puntos_Circ)
