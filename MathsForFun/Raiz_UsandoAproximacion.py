import numpy as np
'''Este script aproxima la raiz cuadrada "np.sqrt(k)" de un número k, con un error que le pasemos por parámetro.
No es trivial esto, si quisieramos calcular raices cuadradas podríamos aproximar la función f(x)=np.sqrt(k)
con un polinomio de taylor de grado muy alto, y sacar el error con la fórmula de taylor. Pero las derivadas de 
f(x) no son lindas, y tendríamos que considerar un polinomio de grado muy alto.

Este es un método para conseguir raices por tanteo, usando como función a f(x)=x**2-k, notar que las raices
de esta función son, np.sqrt(k) y -np.sqrt(k), nos quedamos con la raíz positiva por simplicidad.
Si encontramos las raices de esta f(x) estamos encontrando el valor de np.sqrt(k).

Primero tenemos que encontrar una cota inferior y superior para la raiz, luego evaluamos la función en puntos intermedios
si la función resulta positiva, quiere decir que la raiz se encuentra a la izquierda (por que f(x) es cuadrática creciente
con x>0).
De igual forma, si nos da negativo quiere decir que la raiz esta a la derecha de ese valor.
Y así cambiamos las cotas inferiores y superiores para que la raíz esté siempre en medio, y esto nos va a dar intervalos cada vez
mas chicos, cuan chicos necesitamos que sean? Dependerá del error que estemos dispuestos a tolerar.
El error está determinado por la distancia entre la cota inferior y la superior dividido 2. El radio del intervalo.
El error será como MUCHO esa longitud.

Para encontrar las cotas inferior y superior iniciales, como no sabemos el valor de np.sqrt(k) es complicado,
sobretodo si k es muy grande. Entonces lo que voy a hacer es, que si el valor de k es pequeño elija como cotas el
0 y int(k)+1, de esta forma nos aseguramos que k está en medio.

Si k es grande vamos a dividir el intervalo antes mencionado en, por ejemplo, 10 partes y ver entre medio de cuales partes se encuentra.
Y realizamos este proceso varias veces hasta que el intervalo sea razonablemente chico. Ya vamos a definir bien que significa "razonable".
'''
def f(x,k):
    return x**2-k

# Hace una partición desde [a,b] con "n" intervalos de ancho "(b-a)/n". Devuelve una lista con los valores de los Xi.
def PartirIntervalo(a,b,n):
    dx = (b-a)/n
    Xi = [a+i*dx for i in range(n)]
    Xi.append(b)
    return Xi

def VM(a,b):   #Devuelve el valor medio entre 2 números
    return (a+b)/2

def MaxError(a,b):
    return (max(a,b) - min(a,b))/2

# Esta función es súper eficiente, encuentra las cotas con distancia <1 en
# menos de 0.001 segundos para números de 17 cifras.
def BuscarCotas(k):
    CotaInf, CotaSup = 0, int(k)+1      # Valor por default, la raíz siempre va a estar entre estos valores.
    N_Digitos_k = int(np.log10(k))+1

    # Si dividimos el intervalo en 10, tantas veces como número de dígitos tenga k,
    # al final nos va a quedar |CotaSup-CotaInf|<1, un número razonable para empezar.
    for _ in range(N_Digitos_k):
        Intervalo = PartirIntervalo(CotaInf, CotaSup, 10)

        i=0
        encontreCotas = False
        while i<len(Intervalo)-1 and not(encontreCotas):
            if f(Intervalo[i],k)==0:    # Estas condiciones es si por casualidad llego a encontrar el valor de k exacto.
                CotaInf = CotaSup = Intervalo[i]
                return CotaInf, CotaSup
            elif f(Intervalo[i+1],k)==0:
                CotaInf = CotaSup = Intervalo[i+1]
                return CotaInf, CotaSup
            

            if f(Intervalo[i+1],k)>0:   # Si el valor siguiente es positivo, significa que el anterior es negativo, por que recorre de izquierda a derecha.
                CotaInf, CotaSup = Intervalo[i], Intervalo[i+1]
                encontreCotas = True
            i+=1
    return CotaInf, CotaSup

def AproxRaiz(k, ErrorDeseado):
    CotaInf, CotaSup = BuscarCotas(k)
    Error = MaxError(CotaInf, CotaSup)

    while Error>ErrorDeseado:
        ValorMedio = VM(CotaInf, CotaSup)
        if f(ValorMedio,k) == 0:
            CotaInf = CotaSup = ValorMedio
        elif f(ValorMedio,k) > 0:
            CotaSup = ValorMedio
        else:
            CotaInf = ValorMedio
        Error = MaxError(CotaInf, CotaSup)
    
    raiz = VM(CotaInf,CotaSup)
    return raiz, Error


if __name__ == "__main__":    
    k = 123
    decimales_correctos = 9     # Quiero que los primeros "decimales_correctos" decimales estén bien.
    ErrorDeseado = 10**-decimales_correctos

    if k<0:
        print("No se puede calcular la raíz cuadrada de un número negativo.")
    elif k==0:
        print("raiz=0\nerror=0")
    else:
        raiz, error = AproxRaiz(k, ErrorDeseado)
        print(f"raiz={raiz}\nerror={error}")
    

    




