"""Definición de Recta Tangente: (Rtg)
La recta tangente al gráfico de una función f(x) en X0, es un recta que pasa por "1 punto" rozando a la función.
Mas precisamente, es la mejor aproximación lineal al gráfico de una función en el punto X0.
Para encontrar esta recta se tiene que encontrar primero su pendiente (mtg), pero para poder sacar la pendiente necesitamos
conocer 2 puntos por donde pasa la función. El problema es que solo conocemos 1 punto por donde pasa esta recta, el punto (X0, f(X0)).

Nos vamos a inventar un segundo punto por donde pasa esta recta, el punto (X0+h, f(X0+h)) siendo h un número arbitrario.
De esta forma tenemos 2 puntos, y la recta que pasa por dichos puntos es SECANTE a la función. NO es la recta que nos interesa.

La pendiente de la recta secante es:        # Acá estamos usando la definición de pendiente de una recta que pasa por 2 puntos m=(Y2-Y1)/(X2-X1)
m_sec = (f(X0+h) - f(X0)) / (X0+h - X0)     # Los X0 se tachan.
m_sec = (f(X0+h) - f(X0)) / h

Luego, notar que si h-->0, es decir, se hace cada vez mas chiquito, entonces el 2do punto (X0+h, f(X0+h)) se acerca
al primero (X0, f(X0)). En el límite estos puntos estan tan cerca que son prácticamente el mismo punto.
En ese caso límite, esa sería mi recta tangente.
Entonces:

mtg = lim    m_sec
      h-->0

mtg = lim   (f(X0+h) - f(X0)) / h
      h-->0


Prop:
    La función y la recta tangente en el punto P=(X0, f(X0)) toman el mismo valor.
    Esto podemos usarlo para sacar la ordenada al origen de la Rtg. 


IDEA DEL PROGRAMA:
    Vamos a hacer un programa que calcule la mtg de manera numérica. Es decir, va a evaluar un "h" muy
    pequeño para simular este h-->0. Y se grafican ambas funciones."""
import numpy as np
import matplotlib.pyplot as plt
import datetime

def Graficar(X0:float, Intervalo:list, GuardarImg:bool=False, h:float=10**-9, Cant_Decimales:int=3):
    """Realiza un gráfico de la función f(x) junto con la Rtg en el punto (X0, f(X0)).
    
    Arg:
        X0 (float): Valor en X0 donde se calcula la mtg.
        Intervalo (list): Intervalo de X donde se realiza el grafico.
        GuardarImg (bool): Si es True guarda la imagen en el mismo directorio que este fichero.
        h (float): Constante arbitraria, la precision de mtg es mayor si cuanto mas pequeña sea h.
        Cant_Decimales (int): Número de decimales con el cual será devuelta la mtg."""
    mtg = mtg_X0(X0, h, Cant_Decimales)
    Ordenada = Ordenada_Rtg_X0(X0, mtg)
    x = np.linspace(Intervalo[0], Intervalo[1], 1000)
    y = f(x)
    y_lineal = Rtg(x, mtg, Ordenada)

    plt.figure(dpi=200)
    plt.plot(x, y, color="crimson")
    plt.plot(x, y_lineal, color="lightblue")
    plt.title(f"Gráfico de f(x) junto a su recta tangente.\nY={mtg}*x+{Ordenada}")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")

    if GuardarImg:      # Se guarda la imagen
        NombreImg = str(datetime.datetime.now())
        plt.savefig(NombreImg+".png")
    else:               # Sino simplemente se muestra.
        plt.show()

def Ordenada_Rtg_X0(X0:float, mtg:float):
    """Recibe el valor de X0, y retorna el valor de la ordenada al origen.
    Notar que: La ordenada al origen se consigue reemplazando en (X0, f(X0)) y despejando.
    
    Arg:
        X0 (float): Valor en X0 donde se calcula la mtg.
        mtg (float): Valor de la mtg al gráfico de f(x) en X0.
    
    Return:
        La ordenada de la recta tangente."""
    return f(X0)-mtg*X0

def mtg_X0(X0:float, h:float, Cant_Decimales:int):
    """Recibe como parámetro el valor X0 donde se quiere calcular la mtg, y retorna este valor.
    
    Arg:
        X0 (float): Valor en X0 donde se calcula la mtg.
        h (float): Constante arbitraria, la precision de mtg es mayor si cuanto mas pequeña sea h.
        Cant_Decimales (int): Número de decimales con el cual será devuelta la mtg.
    
    Return:
        La pendiente de la recta tangente."""
    return round((f(X0+h) - f(X0)) /h,Cant_Decimales)         # Derivada numérica

def Rtg(x, mtg, Ordenada):
    """Ecuación de la recta tangente."""
    return mtg*x+Ordenada

def f(x):
    """Función a la cual le vamos a calcular la mtg."""
    return x**2


if __name__ == "__main__":
    X0 = 3
    Intervalo = [-1,7]      # Intervalo en el que se grafica.
    h = 10**-9              # Valores por defecto.
    Cant_Decimales = 3      # Cantidad de decimales de mtg. Valores por defecto.
    
    Graficar(X0, Intervalo, False, h, Cant_Decimales)



    



