import heapq
class Mision:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad  # menor = más importante

    def __lt__(self, other):
        return self.prioridad < other.prioridad


class ColaPrioridades:
    def __init__(self):
        self.heap = []

    def agregar(self, mision):
        heapq.heappush(self.heap, mision)

    def tomar(self):
        return heapq.heappop(self.heap) if self.heap else None