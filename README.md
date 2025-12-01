# Trabajo-Personajes-de-ciencia-ficcion
Trabajo Práctico – Personajes de Ciencia Ficción
Estructuras de Datos – Python

Este proyecto implementa un conjunto de estructuras de datos aplicadas a un universo ficticio de personajes, planetas y misiones.
El objetivo es demostrar el uso de árboles, grafos, colas de prioridad y algoritmos clásicos para resolver problemas dentro de un entorno simulado.

personaje.py          # Clase principal de personajes
habilidad.py          # Árbol general de habilidades
arbolpersonajes.py    # Árbol binario de personajes
mision.py             # Cola de prioridad para misiones
grafo.py              # Grafo no dirigido (universo)
grafodirigido.py      # Grafo dirigido (entrenamiento)
main.py               # Ejecución y ejemplos

Funcionalidades Principales
 Personaje

Modelo con nombre, planeta, inventario, habilidades y cálculo recursivo del poder total.

 Árbol Binario

Ordena personajes por nivel de poder y permite recorridos (preorden, inorden, postorden).

 Árbol de Habilidades

Representa un árbol general de progresión donde cada habilidad puede tener mejoras.

 Cola de Prioridad

Administra misiones según nivel de amenaza o recompensa.

 Grafos

No dirigido: rutas entre planetas (BFS y DFS).

Dirigido: dependencias de entrenamiento (ordenamiento topológico).

Dijkstra: calcula la ruta más óptima entre dos ubicaciones.

 Ejecucion
Python3

 Autores
Lucas Oviedo
Michael Martinez
Rodrigo Garay
