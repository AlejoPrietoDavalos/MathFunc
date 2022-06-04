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

        self.grafo = grafo
        self.ID_Vertice = len(self.grafo.Vertices)   # El primer vertice es el número 0, el segundo será 1, etc..
        self.grafo.AgregarVerticeGrafo(self, V_Ady)
        

        
        
        



grafo = Grafo(5)
ListadoVerticesAdyacentes = [[1,2], [0,3], [0,3], [1,2], [1,2]]
grafo.CrearVertices(ListadoVerticesAdyacentes)


for v in grafo.Vertices:
    print(v.ID_Vertice)
