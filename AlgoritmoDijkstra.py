from heapq import heapify, heappop, heappush

class Graph:
   def __init__(self, graph: dict = {}):
       self.graph = graph  # El diccionario del grafo es una lista de adyacencia

   def add_edge(self, node1, node2, nodeWeight):
       if node1 not in self.graph:  # Revisa si el nodo ya existe dentro del grafo
           self.graph[node1] = {}  # Si no existe, crea ese nodo
       self.graph[node1][node2] = nodeWeight  # Si el nodo ya existe, entonces crea la conexion de ese nodo1 con el nodo2

   def shortest_distances(self, sourceNode: str):
       distances = {node: float("inf") for node in self.graph}# El peso inicial de todos los nodos es infinito
       distances[sourceNode] = 0  # El peso del nodo inicial es 0

       # Inicia una cola de prioridad
       priorityQueue = [(0, sourceNode)]
       heapify(priorityQueue)

       # Iniciamos una lista que no acepta elementos repetidos para guardar los nodos visitados
       visitedNodes = set()

       while priorityQueue:  # Mientras que la cola de prioridad no este vacia,
           currentDistance, currentNode = heappop(priorityQueue) # Obten el nodo con el peso minimo

           if currentNode in visitedNodes:
               continue  # Si el nodo de menor peso ya lo visitamos, saltalo
           visitedNodes.add(currentNode)  # Si no lo hemos visitado, se añade a la lista de nodos visitados

           for neighborNode, nodeWeight in self.graph[currentNode].items():
               # Calcula la distancia desde el nodo actual a su vecino
               tentativeDistance = currentDistance + nodeWeight

               if tentativeDistance < distances[neighborNode]: #Si la distancia teorica es menor a la distancia recorrida
                   distances[neighborNode] = tentativeDistance #Se añade la distancia recorrida a ese nodo vecino
                   heappush(priorityQueue, (tentativeDistance, neighborNode)) #Añade a la cola de prioridad ese nodo vecino

       nodePredecessors = {node: None for node in self.graph}

       for node, distance in distances.items():
           for neighborNode, nodeWeight in self.graph[node].items():
               if distances[neighborNode] == distance + nodeWeight:
                   nodePredecessors[neighborNode] = node

       return distances, nodePredecessors

   def shortest_path(self, sourceNode: str, targetNode: str):
       # Genera el diccionario de predecesores
       _, nodePredecessors = self.shortest_distances(sourceNode)

       exploredPath = []
       currentNode = targetNode

       # Se devuelve desde el nodo en el que este hacia el nodo origen
       while currentNode:
           exploredPath.append(currentNode)
           currentNode = nodePredecessors[currentNode]

       # Como estamos iniciando desde el ultimo nodo hasta el inicio, lo reversamos para mostrarlo:
       exploredPath.reverse()

       return exploredPath
