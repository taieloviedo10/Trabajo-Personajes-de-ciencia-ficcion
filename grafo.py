from collections import deque, defaultdict
import math
import heapq
class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, origen, destino, peso=1):
        self.grafo[origen].append((destino, peso))
        self.grafo[destino].append((origen, peso))

    # BFS
    def bfs(self, inicio):
        visitado = set()
        q = deque([inicio])
        while q:
            nodo = q.popleft()
            if nodo not in visitado:
                print(nodo)
                visitado.add(nodo)
                for vecino, _ in self.grafo[nodo]:
                    if vecino not in visitado:
                        q.append(vecino)

    # DFS
    def dfs(self, inicio, visitado=None):
        if visitado is None:
            visitado = set()
        print(inicio)
        visitado.add(inicio)
        for vecino, _ in self.grafo[inicio]:
            if vecino not in visitado:
                self.dfs(vecino, visitado)

    # Dijkstra (camino más corto)
    def dijkstra(self, origen, destino):
        dist = {n: math.inf for n in self.grafo}
        dist[origen] = 0
        prev = {}
        pq = [(0, origen)]

        while pq:
            d, nodo = heapq.heappop(pq)
            if nodo == destino:
                break
            for vecino, peso in self.grafo[nodo]:
                nueva_d = d + peso
                if nueva_d < dist[vecino]:
                    dist[vecino] = nueva_d
                    prev[vecino] = nodo
                    heapq.heappush(pq, (nueva_d, vecino))

        # Reconstrucción del camino
        camino = []
        actual = destino
        while actual in prev:
            camino.append(actual)
            actual = prev[actual]
        camino.append(origen)
        return list(reversed(camino))
