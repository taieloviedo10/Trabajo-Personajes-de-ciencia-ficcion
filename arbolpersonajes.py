class NodoPersonaje:
    def __init__(self, personaje):
        self.personaje = personaje
        self.izq = None
        self.der = None

class ArbolPersonajes:
    def __init__(self):
        self.raiz = None

    def insertar(self, personaje):
        nodo = NodoPersonaje(personaje)
        if not self.raiz:
            self.raiz = nodo
        else:
            self._insertar(self.raiz, nodo)

    def _insertar(self, actual, nodo):
        if nodo.personaje.nivel_poder < actual.personaje.nivel_poder:
            if actual.izq is None:
                actual.izq = nodo
            else:
                self._insertar(actual.izq, nodo)
        else:
            if actual.der is None:
                actual.der = nodo
            else:
                self._insertar(actual.der, nodo)

    # Recorridos
    def preorden(self, nodo):
        if nodo:
            print(nodo.personaje.nombre)
            self.preorden(nodo.izq)
            self.preorden(nodo.der)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.personaje.nombre)
            self.inorden(nodo.der)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.personaje.nombre)