from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#----------IMPORTANTE: Para trabajar con estas funciones tenes que usar Arrays, no listas.


# Realiza un ajuste lineal de los datos.
def AjusteLineal(Datos_X, Datos_Y, ErrY=None):
    def Lineal(x,m,b):
        return m*x+b
    
    # Devuelve un listado con los residuos del ajuste lineal.
    def ResiduoLineal(Datos_X, Datos_Y, m, b):    
        Residuos = Datos_Y-Lineal(Datos_X, m, b)
        return Residuos
    
    # La primer variable es un vector con 2 coordenadas pendiente y ordenada,
    # y el segundo es la matriz covarianza que tiene en su diagonal a sigma al cuadrado.
    m_y_b, Cov = curve_fit(Lineal, Datos_X, Datos_Y, sigma=ErrY)        # Cov es la matriz de covarianza.
    m,b = m_y_b
    dm,db = np.sqrt(np.diag(Cov))                                   # Error de m y b.

    Res_Ajuste = np.array([m, dm, b, db])
    Residuos = ResiduoLineal(Datos_X, Datos_Y, m, b)
    return Res_Ajuste, Residuos


# Realiza un ajuste cuadrático en forma polinómica de los datos.
def AjusteCuadratico_Polinomica(Datos_X, Datos_Y, ErrY=None):
    def Cuad_Pol(x, A, B, C):
        return A*x**2 + B*x + C
    
    def ResiduoCuad_Pol(Datos_X, Datos_Y, A, B, C):
        Residuos = Datos_Y-Cuad_Pol(Datos_X, A, B, C)
        return Residuos
    
    A_B_C, Cov = curve_fit(Cuad_Pol, Datos_X, Datos_Y, sigma=ErrY)
    A,B,C = A_B_C
    dA,dB,dC = np.sqrt(np.diag(Cov))

    Res_Ajuste = np.array([A, dA, B, dB, C, dC])
    Residuos = ResiduoCuad_Pol(Datos_X, Datos_Y, A, B, C)
    return Res_Ajuste, Residuos


# Realiza un ajuste cuadrático en forma factorizada de los datos.
def AjusteCuadratico_Factorizada(Datos_X, Datos_Y, ErrY=None):
    def Cuad_Fact(x, A, x1, x2):
        return A*(x-x1)*(x-x2)

    def ResiduoCuad_Fact(Datos_X, Datos_Y, A, x1, x2):
        Residuos = Datos_Y-Cuad_Fact(Datos_X, A, x1, x2)
        return Residuos
    
    A_x1_x2, Cov = curve_fit(Cuad_Fact, Datos_X, Datos_Y, sigma=ErrY)
    A,x1,x2 = A_x1_x2
    dA,dx1,dx2 = np.sqrt(np.diag(Cov))

    Res_Ajuste = np.array([A, dA, x1, dx1, x2, dx2])
    Residuos = ResiduoCuad_Fact(Datos_X, Datos_Y, A, x1, x2)
    return Res_Ajuste, Residuos


# Realiza un ajuste cuadrático en forma factorizada de los datos.
def AjusteCuadratico_Canonica(Datos_X, Datos_Y, ErrY=None):
    def Cuad_Canonica(x, A, xv, yv):
        return A*(x-xv)**2 + yv
    
    def ResiduoCuad_Fact(X_Med, Y_Med, A, xv, yv):
        Residuos = Y_Med-Cuad_Canonica(X_Med, A, xv, yv)
        return Residuos
    
    A_xv_yv, Cov = curve_fit(Cuad_Canonica, Datos_X, Datos_Y, sigma=ErrY)
    A,xv,yv = A_xv_yv
    dA,dxv,dyv = np.sqrt(np.diag(Cov))

    Res_Ajuste = np.array([A, dA, xv, dxv, yv, dyv])
    Residuos = ResiduoCuad_Fact(Datos_X, Datos_Y, A, xv, yv)
    return Res_Ajuste, Residuos


# Gráfico de Residuos
def GraficoResiduos(Datos_X, Residuos, XLabel, YLabel="Residuos", Title="Gráfico de Residuos", ms=8, ColorPuntos="crimson", ColorEjeX="black"):
    plt.figure(figsize=[8,8], dpi=100)
    plt.plot(Datos_X, Residuos, ".", ms=ms, color=ColorPuntos)
    plt.plot([min(Datos_X), max(Datos_X)], [0,0], "--", color=ColorEjeX)    # Dibujo el eje X, para q se vea bien la gráfica.
    plt.title(Title)
    plt.xlabel(XLabel)
    plt.ylabel(YLabel)
    plt.show()



