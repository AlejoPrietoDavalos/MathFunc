import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat

def Grafico_Funcion(a, b, k, ColorFunc="black", Title="Gráfico de la Función", XLabel="Eje X", YLabel="Eje Y"):
    x = np.linspace(a-k,b+k,1000)
    y = f(x)        
    plt.figure(figsize=[8,8])
    plt.plot([a-k,b+k], [0,0], color=ColorFunc)     # Dibujo una recta horizontal en Y=0 para que se vea el eje X.
    plt.plot(x, y, color=ColorFunc)
    plt.title(Title)
    plt.xlabel(XLabel)
    plt.ylabel(YLabel)
    plt.show()


# Hace una partición desde [a,b] con "n" intervalos de ancho "(b-a)/n". Devuelve una lista con los valores de los Xi.
def PartirIntervalo(a,b,n,dx):
    Xi = [a+i*dx for i in range(n)]
    Xi.append(b)
    return Xi


# Acá hace la Suma Inferior y Superior de Riemann y devuelve 2 numeros con el valor de dichas sumas.
# También devuelve una lista con las coordenadas Xi de la partición y otras 2 listas con las alturas de los rectángulos de las particiones.
def Suma_Riemann(a, b, n):
    dx = (b-a)/n
    Xi = PartirIntervalo(a, b, n, dx)
    Alt_Inf_i = []        #Acá voy a almacenar la altura del rectángulo para la posición i, de la suma inferior.
    Alt_Sup_i = []        #Lo mismo pero en la suma superior.
    Suma_Inferior = 0
    Suma_Superior = 0
    
    for i in range(len(Xi)-1):
        Y_i = f(Xi[i])        #Acá calculo cuanto vale la función en Xi
        Y_imas1 = f(Xi[i+1])  #Acá calculo cuanto vale la función en Xi+1
        if Y_imas1 == Y_i:
            Suma_Inferior += Y_i*dx
            Suma_Superior += Y_i*dx
            Alt_Inf_i.append(Y_i)
            Alt_Sup_i.append(Y_i)
        elif Y_imas1 > Y_i:     
            Suma_Inferior += Y_i*dx
            Suma_Superior += Y_imas1*dx
            Alt_Inf_i.append(Y_i)
            Alt_Sup_i.append(Y_imas1)
        else:   
            Suma_Inferior += Y_imas1*dx
            Suma_Superior += Y_i*dx
            Alt_Inf_i.append(Y_imas1)
            Alt_Sup_i.append(Y_i)

    return Suma_Inferior, Suma_Superior, Xi, Alt_Inf_i, Alt_Sup_i    # La suma inferior, superior de Riemann y la partición.


def Grafico_Suma_Riemann(a, b, n, k, hayLineas):
    Suma_Inferior, Suma_Superior, Xi, Alt_Inf_i, Alt_Sup_i = Suma_Riemann(a, b, n)

    x = np.linspace(a-k, b+k, 1000)
    y = f(x)
    dx = (b-a)/n
    fig = plt.figure(figsize=[8,8])
    ax = fig.add_subplot(111)
    
    for i in range(len(Alt_Inf_i)):     #Acá grafica los rectángulos sin el borde de contorno negro.
        Rect_Sup=pat.Rectangle( (Xi[i],0), width=dx, height=Alt_Sup_i[i], color="crimson", alpha=0.9)    #Lo mismo de arriba pero con la suma Superior
        ax.add_patch(Rect_Sup)      #Agrego ese rectangulito al grafico.
        
        Rect_Inf=pat.Rectangle( (Xi[i],0) , width=dx , height=Alt_Inf_i[i] , color="orange" , alpha=0.9)    #Creo un rectangulito de Riemann de la suma Inferior en posicion i.
        ax.add_patch(Rect_Inf)      
        
        if hayLineas==True:        #Acá le pone contorno negro a los rectángulos, es solo estético.
            Rect_Sup2=pat.Rectangle( (Xi[i],0) , width=dx , height=Alt_Sup_i[i] , color="black" , alpha=0.9,fill=False)
            ax.add_patch(Rect_Sup2)
            
            Rect_Inf2=pat.Rectangle( (Xi[i],0) , width=dx , height=Alt_Inf_i[i] , color="black" , alpha=0.9 , fill=False)
            ax.add_patch(Rect_Inf2)
    
    plt.plot([a-k,b+k],[0,0],color="black")
    plt.plot(x,y,color="black")     #Grafico la función.
    plt.title("Suma de Riemann con n="+str(n)+"."+"\nInf="+str(Suma_Inferior)+".    Sup="+str(Suma_Superior)+".")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.show()


# Esto es para ver como se acercan la suma Sup e Inf cuando n-->infinito.
def SumasRiemann_nInfinito(a, b, n_maximo):
    Inf_n = []
    Sup_n = []
    Num_n = []

    for n in range(1, n_maximo+1):
        Suma_Inf, Suma_Sup, _,_,_ = Suma_Riemann(a, b, n)
        Inf_n.append(Suma_Inf)
        Sup_n.append(Suma_Sup)
        Num_n.append(n)

    plt.figure(figsize=[8,8], dpi=100)
    plt.plot(Num_n, Inf_n, ".", ms=5, color="orange")
    plt.plot(Num_n, Sup_n, ".", ms=5, color="crimson")
    plt.title(f"Acá graficamos Suma Inf y Sup en función de n.\n Con n={n_maximo}, SumaInf={round(Inf_n[-1],3)}, SumaSup={round(Sup_n[-1],3)}")
    plt.xlabel("Valor de n")
    plt.ylabel("Valor de la suma Inf y Sup de Riemann")
    plt.show()


def f(x):
    ecuation = np.exp(np.cos(x))*np.log(x)      #En este renglón escribir la ecuación de la función que le queremos calcular el área.
    return ecuation


if __name__ == "__main__":
    #----------Hay que definir el intervalo [a,b] y cuantas "n" particiones queremos----------
    a = 1
    b = 20
    
    # Va a hacer el gráfico por cada número de intervalos que le pasemos.
    # Si solo queremos un intervalo podemos simplemente ponerlo asi [50].
    N_Intervalos = [10, 20, 30, 40, 50, 100]
    
    # True --> Queremos que grafique las Sumas de Riemann. False --> Solo grafica la función.
    hayRiemann = True
    
    # True --> Los intervalos tienen líneas. NOTA: Si el número de n es muy grande, todas las líneas forman una mancha negra.
    # False --> Si no graficamos las líneas, conviene si n es grande. Con n chiquito dejalo en True.
    hayLineas = True

    # IMPORTANTE, SI CAMBIAS EL VALOR DE K
    # Es para que el gráfico se vea bien, k es la distancia excedente que se grafica la función en relación a las Sumas de Riemann.
    # Es decir, las Sumas de Riemann se granfican entre [a,b] y la función [a-k,b+k]
    k = 0.5

    # Grafico tendencia de Suma Superior e Inferior de Riemann cuando n--->infinito.
    hacerGrafTendenciaSumas = True
    # Va a calcular la Suma inf y sup para n={1,2,3,....,n_maximo} y va a graficar
    # ambos para que se vea la tendencia de ambas al valor del área "REAL".
    # No te zarpes con este número, por que sinó va a tardar mucho en procesarlo.
    n_maximo = 500
    

    
    for n in N_Intervalos:
        if hayRiemann:
            Grafico_Suma_Riemann(a, b, n, k, hayLineas)
        else:
            Grafico_Funcion(a, b, k)
    
    SumasRiemann_nInfinito(a, b, n_maximo)
