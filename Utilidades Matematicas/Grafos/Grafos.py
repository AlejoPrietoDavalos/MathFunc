'''----------NOTA IMPORTANTE----------
Este script lo diseñé pensando de forma totalmente matemática y no usé
ningún libro de teoría. Puede ser que haya algoritmos mas eficientes,
o mejor manera de hacerlo.
----------NOTA IMPORTANTE----------

Enunciado: Tenemos un conjunto de vértices y aristas formando un grafo.
Tenemos que ir desde el vértice v1 al vértice v2, con el menor número
de pasos posible.

Podemos usar la matriz de adyacencia "M_Ady", es una matriz de KxK, siendo K
el número de vértices que contiene el grafo. M_Ady[i][j] es igual a 1 si el
vértice "vi" y el "vj" están conectados por una arista, y 0 en caso contrario.

Esta matriz te dice con un coste de O(1) si los vértices estan conectados o no.
Y tiene un teorema asociado que es el siguiente:

--> TEOREMA:
Sea A la matriz de adyacencia de N∈KxK, siendo K el número de vértices del grafo.
Y sean 2 vértices cualesquiera "vi" y "vj" con i!=j. Considerando la siguiente matriz
B = A**n con n∈N.
B[i][j] es igual al número de pasos que se toma ir desde "vi" a "vj".

¿Como nos sirve este teorema?
Si nosotros calculamos la matriz A, A**2, A**3,...,A**n. Podemos saber exactamente cuantos
pasos se toma ir desde un vértice a otro. Y si nos quedamos con el menor de esos pasos sería
la trayectoria mas "eficiente".'''

import numpy as np

class Grafo():
    def __init__(self, CantVertices:int):
        self.CantVertices = CantVertices
        self.Vertices = []                                                      # Lista con todos los objetos de tipo Vertice.

        self.M_Ady = np.zeros((self.CantVertices,self.CantVertices),int)        # Matriz de adyacencia.

    def CrearVertices(self, ListadoVerticesAdyacentes:list):
        """Recibe como parámetro el listado con los listados de vértices a los cuales es adyacente cada uno
        de los vértices del grafo, de forma ordenada, es decir, el primer listado corresponde al grafo con ID=0, etc.. 
        Crea los objetos de tipo vértice que pertenecen al grafo.
        
        Args:
            ListadoVerticesAdyacentes (list): Listado que contiene las listas con los vértices a los cuales es adyacente cada uno de los vértices."""
        for V_Ady in ListadoVerticesAdyacentes:
            Vertice(self, V_Ady)

    def AgregarVerticeGrafo(self, Vertice_Obj:object, V_Ady:list):
        """Agrega el vértice previamente creado al grafo. Ésto modifica la matriz de adyacencia
        y lo agrega a la lista de vértices en el grafo. Cada vértice tiene un identificador único
        que coincide con la posición del vértice en el array.

        Args:
            Vertice_Obj (Vertice Object): El objeto de tipo Vertice.
            VerticesAdyacentes (list): Listado con el identificador de cada vértice al cual éste es adyacente."""
        self.Vertices.append(Vertice_Obj)                                       # Agregamos este objeto a la lista de Nodos del grafo.
        indice_NuevoVertice = len(self.Vertices)-1

        for V_Ady in V_Ady:
            self.M_Ady[V_Ady][indice_NuevoVertice] = self.M_Ady[indice_NuevoVertice][V_Ady] = 1

    def N_PasosMin(self, v1:int, v2:int):
        """Recibe como parámetro el ID de cada vértice y devuelve el número de pasos que le toma ir del vértice v1 a v2.
        
        Args:
            v1 (int): Número de ID del primer vértice.
            v2 (int): Número de ID del segundo vértice.
        Return:
            Devuelve el número de pasos que le toma ir de v1 a v2."""
        encontrePasosMin = False
        matriz = self.M_Ady
        PotMatriz = 1           # Esta es la potencia de la matriz, es lo que necesito saber.

        while not(encontrePasosMin):
            if matriz[v1][v2]!=0:
                encontrePasosMin = True
            else:
                matriz = np.dot(matriz, self.M_Ady)
                PotMatriz += 1
        
        return PotMatriz

    def CaminoMinimo(self, v1, v2):
        CaminoMinimo = [v1]                                                     # Arranco siempre desde v1.
        pos = v1
        dist_pos_v2 = self.N_PasosMin(pos, v2)

        while pos!=v2:
            print(dist_pos_v2)
            if dist_pos_v2==1:
                pos = v2
                CaminoMinimo.append(pos)
            else:
                for i in range(len(self.M_Ady)):
                    if self.M_Ady[pos][i]==1 and self.N_PasosMin(i,v2)==dist_pos_v2-1 and pos!=i:
                        CaminoMinimo.append(i)
                        pos = i
            dist_pos_v2 -= 1
        
        return CaminoMinimo



class Vertice():
    def __init__(self, grafo, V_Ady):

        self.grafo = grafo  ########## Creo q no hace falta tener aca guardado el grafo, podemos simplemente usar la función que nos interesa.
        self.ID_Vertice = len(self.grafo.Vertices)   # El primer vertice es el número 0, el segundo será 1, etc..
        self.grafo.AgregarVerticeGrafo(self, V_Ady)
        

class GrafoHexagonal():                 ######### Ver si hereda de grafo.
    def __init__(self, T_H:int):
        self.T_H = T_H                                      # Tamaño del hexágono.
        self.n_filas = 2*T_H-1                              # Número de filas.
        
        """ Listado con el número de elementos que tiene cada una de las filas del hexágono.
            Por ejemplo: Un hexágono con T_H=5 devuelve [5,6,7,8,9,8,7,6,5]"""
        self.n_elem_fila = [self.T_H+i for i in range(self.T_H-1)] + [self.T_H+i for i in range(self.T_H-1, -1, -1)]

        
        """ Estos indices van a ser usados para distinguir en que posición se encuentra cada indice.
            - Indice Superior: Toda celda con indice <= ind_sup corresponde a la parte superior del hexágono.
            - Indice Inferior: Toda celda con indice >= ind_inf corresponde a la parte inferior del hexágono.
            - Indices del Medio: Si ind_sup < indice < ind_inf entonces, la celda corresponde a la parte central."""
        self.ind_sup = sum(self.n_elem_fila[0:T_H-1]) - 1
        self.ind_inf = self.ind_sup + 2*T_H


        self.grafo = Grafo(sum(self.n_elem_fila))
        self.GenerarRedHexagonal()
    

    def GenerarRedHexagonal(self):
        """Esta función se encarga generar los vértices del grafo viendo quienes son los vértices adyacentes.
        """
        for fila in range(self.n_filas):                                # Recorremos cada una de las filas.
            for i in range(sum(self.n_elem_fila[0:fila]), sum(self.n_elem_fila[0:fila]) + self.n_elem_fila[fila]):      # "i" es el ID del vértice. Generamos los "i" que corresponden a esa fila.
                V_Ady = self.ComprobarVerticesAdyacentes(fila, i)       # Comprobamos cuales son los vértices adyacentes a este vértice.
                Vertice(self.grafo, V_Ady)                              # Generamos todos los vértices que el grafo tiene.
                print(f"i:{i} --> {V_Ady}")


    def ComprobarVerticesAdyacentes(self, fila:int, i:int):
        """Comprueba cuales son los vértices adyacentes a un vértice dado. Devuelve una lista con dichos vértices."""
        """Método de búsqueda:
            Observación:
                Lado Superior:  Si hacemos i-self.n_elem_fila[fila], i-self.n_elem_fila[fila]+1, i+self.n_elem_fila[fila],  y i+self.n_elem_fila[fila]+1.
                                Asi conseguimos los 4 hexágonos adyacentes. De arriba y abajo. El de la derecha e izquierda es sumar y restar 1.
                Lado Inferior:  Si hacemos i-self.n_elem_fila[fila], i-self.n_elem_fila[fila]-1, i+self.n_elem_fila[fila],  y i+self.n_elem_fila[fila]-1.
                                Asi conseguimos los 4 hexágonos adyacentes. De arriba y abajo. El de la derecha e izquierda es sumar y restar 1.
                Fila Central:   Es un híbrido entre la superior y la inferior. Para ver los de arriba se comporta como Lado Superior, y para los de abajo como el lado Inferior.
        
        Vamos a revisar, para el vértice dado, la posición de los 6 hexágonos adyacentes.
        No todos los hexágonos tienen 6 adyacentes, por lo tanto, vamos a hacer las cuentas igual. Y comprobar que ese candidato a celda adyacente
        este en la fila que realmente debería estar.
        Ver dibujo explicativo."""
        V_Ady = []
        
        V_Ady += [i-1] if self.FilaPerteneceIndice(i-1)==fila else []                                       # Izquierda
        V_Ady += [i+1] if self.FilaPerteneceIndice(i+1)==fila else []                                       # Derecha

        if i<=self.ind_sup:     #--------------------LADO SUPERIOR--------------------
            if not(fila==0):                        # Para la fila 0 no hay que comprobar arriba.
                ind_UpLeft = i-self.n_elem_fila[fila]
                V_Ady += [ind_UpLeft] if self.FilaPerteneceIndice(ind_UpLeft)==fila-1 else []               # Arriba Izquierda
                V_Ady += [ind_UpLeft+1] if self.FilaPerteneceIndice(ind_UpLeft+1)==fila-1 else []           # Arriba Derecha
            
            ind_DownLeft = i+self.n_elem_fila[fila]
            V_Ady += [ind_DownLeft] if self.FilaPerteneceIndice(ind_DownLeft)==fila+1 else []               # Abajo Izquierda
            V_Ady += [ind_DownLeft+1] if self.FilaPerteneceIndice(ind_DownLeft+1)==fila+1 else []           # Abajo Derecha
        
        elif i>=self.ind_inf:   #--------------------LADO INFERIOR--------------------
            ind_UpRight = i-self.n_elem_fila[fila]
            V_Ady += [ind_UpRight] if self.FilaPerteneceIndice(ind_UpRight)==fila-1 else []                 # Arriba Izquierda
            V_Ady += [ind_UpRight-1] if self.FilaPerteneceIndice(ind_UpRight-1)==fila-1 else []             # Arriba Derecha
            
            if not(fila==self.n_filas-1):           # Para la ultima fila no hay que comprobar abajo.
                ind_DownRight = i+self.n_elem_fila[fila]
                V_Ady += [ind_DownRight] if self.FilaPerteneceIndice(ind_DownRight)==fila+1 else []         # Abajo Izquierda
                V_Ady += [ind_DownRight-1] if self.FilaPerteneceIndice(ind_DownRight-1)==fila+1 else []     # Abajo Derecha
        
        else:                   #--------------------FILA CENTRAL--------------------
            ind_UpLeft = i-self.n_elem_fila[fila]
            V_Ady += [ind_UpLeft] if self.FilaPerteneceIndice(ind_UpLeft)==fila-1 else []                   # Arriba Izquierda
            V_Ady += [ind_UpLeft+1] if self.FilaPerteneceIndice(ind_UpLeft+1)==fila-1 else []               # Arriba Derecha

            ind_DownRight = i+self.n_elem_fila[fila]
            V_Ady += [ind_DownRight] if self.FilaPerteneceIndice(ind_DownRight)==fila+1 else []             # Abajo Izquierda
            V_Ady += [ind_DownRight-1] if self.FilaPerteneceIndice(ind_DownRight-1)==fila+1 else []         # Abajo Derecha

        return V_Ady
    
    
    def FilaPerteneceIndice(self, i:int):
        """ Recibe un indice, y devuelve el número de fila al que pertenece dicho indice.
        
        Arg:
            i (int): Indice del cual queremos saber a que fila pertenece.
        
        Return:
            Devuelve el número de fila en el cual está este indice.
            Si el indice ingresado es erróneo devuelve -1."""
        if 0 <= i < self.grafo.CantVertices:      # Éste es el intervalo de valores permitidos.
            for fila in range(len(self.n_elem_fila)):
                if i < sum(self.n_elem_fila[0:fila+1]):
                    return fila
        else:
            return -1       # Devuelve -1 si el índice es erróneo.
        

grafito = GrafoHexagonal(5)








'''
grafo = Grafo(5)
ListadoVerticesAdyacentes = [[1,2], [0,3], [0,3], [1,2], [1,2]]
grafo.CrearVertices(ListadoVerticesAdyacentes)


for v in grafo.Vertices:
    print(v.ID_Vertice)
'''