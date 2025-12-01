class Personaje:
    def __init__(self, nombre, especie, planeta, nivel_poder):
        self.nombre = nombre
        self.especie = especie
        self.planeta = planeta
        self.nivel_poder = nivel_poder
        self.habilidades = []
        self.inventario = []
        self.transformaciones = []  # Para poder recursivo

    # Métodos para interfaz de habilidades/inventario
    def agregar_habilidad(self, hab):
        self.habilidades.append(hab)

    def eliminar_habilidad(self, hab):
        if hab in self.habilidades:
            self.habilidades.remove(hab)

    def agregar_objeto(self, obj):
        self.inventario.append(obj)

    def eliminar_objeto(self, obj):
        if obj in self.inventario:
            self.inventario.remove(obj)

    # Poder total recursivo
    def poder_total(self):
        total = self.nivel_poder
        for t in self.transformaciones:
            total += t.poder_total()
        return total