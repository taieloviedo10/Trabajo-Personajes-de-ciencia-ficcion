class NodoHabilidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subhabilidades = []

    def agregar_sub(self, nodo):
        self.subhabilidades.append(nodo)


# Recorridos para árbol general
def preorden_hab(nodo):
    if nodo:
        print(nodo.nombre)
        for sub in nodo.subhabilidades:
            preorden_hab(sub)

def postorden_hab(nodo):
    if nodo:
        for sub in nodo.subhabilidades:
            postorden_hab(sub)
        print(nodo.nombre)