from AlgoritmoDijkstra import Graph

grafo = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
}

funcionesGrafo = Graph(graph=grafo)

sourceNode = input("¿Cual sera el nodo de origen?: ' ").strip()
targetNode = input("¿Cual sera el nodo destino?:  ").strip()

try:
    exploredPath = funcionesGrafo.shortest_path(sourceNode, targetNode)
    print(f"La ruta más corta de {sourceNode} a {targetNode} es: {exploredPath}")

    distances, _ = funcionesGrafo.shortest_distances(sourceNode)
    print(f"La distancia más corta de {sourceNode} a {targetNode} es: {distances[targetNode]}")
except KeyError:
    print("Uno o más de los nodos ingresados no existen en el grafo.")
