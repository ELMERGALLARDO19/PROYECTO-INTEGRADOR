class Libro:
    def __init__(self, titulo, autor, cantidad_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_ejemplares = cantidad_ejemplares
        self.prestados = 0

    def disponibles(self):
        return self.cantidad_ejemplares - self.prestados

    def prestar(self):
        if self.disponibles() <= 0:
            raise ValueError(f"No hay ejemplares disponibles de {self.titulo}")
        self.prestados += 1
        return f"Se presto un ejemplar de {self.titulo}"

    def devolver(self):
        if self.prestados <= 0:
            raise ValueError(f"No hay ejemplares prestados de {self.titulo}")
        self.prestados -= 1
        return f"Se devolvio un ejemplar de {self.titulo}"


class LibroDigital(Libro):
    def __init__(self, titulo, autor):
        super().__init__(titulo, autor, cantidad_ejemplares=0)

    def disponibles(self):
        return "ilimitado"

    def prestar(self):
        return f"Se descargo una copia digital de {self.titulo}"

    def devolver(self):
        return "No es necesario devolver una copia digital"


def buscar_libro(catalogo, titulo):
    for libro in catalogo:
        if libro.titulo == titulo:
            return libro
    return None
