from personaje import Personaje
from habilidad import NodoHabilidad, preorden_hab, postorden_hab
from arbolpersonajes import ArbolPersonajes, NodoPersonaje
from mision import Mision, ColaPrioridades
from grafo import Grafo 
from grafodirigido import GrafoDirigido

# invocaciones
if __name__ == "__main__":
    darius = Personaje("Darius", "Humano", "Noxus", 900)
    darius.agregar_habilidad("Decimate")
    darius.agregar_habilidad("Crippling Strike")

    # Árbol binario
    arbol = ArbolPersonajes()
    arbol.insertar(darius)
    arbol.insertar(Personaje("Garen", "Humano", "Demacia", 850))
    arbol.insertar(Personaje("Aatrox", "Darkin", "Desconocido", 1500))

    print("\nInorden del árbol de personajes:")
    arbol.inorden(arbol.raiz)

    # Árbol de habilidades
    raiz_hab = NodoHabilidad("Decimate")
    sub1 = NodoHabilidad("Decimate Mejorado I")
    sub2 = NodoHabilidad("Decimate Mejorado II")
    raiz_hab.agregar_sub(sub1)
    sub1.agregar_sub(sub2)

    print("\nÁrbol de habilidades (preorden):")
    preorden_hab(raiz_hab)

    # Cola de prioridades
    cola = ColaPrioridades()
    cola.agregar(Mision("Defender Noxus", 1))
    cola.agregar(Mision("Entrenar", 3))
    cola.agregar(Mision("Cazar intrusos", 2))

    print("\nMisión más urgente:", cola.tomar().nombre)

    # Grafo del universo
    universo = Grafo()
    universo.agregar_arista("Noxus", "Demacia", 5)
    universo.agregar_arista("Noxus", "Freljord", 8)
    universo.agregar_arista("Demacia", "Jonía", 10)

    print("\nDFS desde Noxus:")
    universo.dfs("Noxus")

    print("\nCamino óptimo Noxus → Jonía (Dijkstra):")
    print(universo.dijkstra("Noxus", "Jonía"))

    # Orden topológico
    entreno = GrafoDirigido()
    entreno.agregar_dependencia("Golpe Brutal II", "Golpe Brutal I")
    entreno.agregar_dependencia("Golpe Brutal III", "Golpe Brutal II")

    print("\nOrden de entrenamiento:")
    print(entreno.topologico())

    print("\nAnálisis de eficiencia:")
    print("""
Árbol binario → Inserción y búsqueda: O(log n) promedio  
Árbol general → Recorridos: O(n)  
Cola de prioridad → Inserción y extracción: O(log n)  
Grafo → BFS/DFS: O(V + E)  
Dijkstra → O(E log V)  
Orden topológico → O(V + E)
    """)
