from collections import deque, defaultdict
class GrafoDirigido:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_dependencia(self, habilidad, prereq):
        self.grafo[prereq].append(habilidad)

    def topologico(self):
        visitado = set()
        pila = []

        def dfs(nodo):
            visitado.add(nodo)
            for vecino in self.grafo[nodo]:
                if vecino not in visitado:
                    dfs(vecino)
            pila.append(nodo)

        for nodo in list(self.grafo):
            if nodo not in visitado:
                dfs(nodo)

        return pila[::-1]