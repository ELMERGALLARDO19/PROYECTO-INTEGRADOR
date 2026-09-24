from modelos import Libro, LibroDigital, buscar_libro

catalogo = [
    Libro("Cien anios de soledad", "Gabriel Garcia Marquez", 2),
    Libro("El principito", "Antoine de Saint-Exupery", 1),
    LibroDigital("Python para todos", "Charles Severance"),
]

# cada elemento de aqui seria despues una fila de una tabla en la bd
prestamos = []

print("catalogo:")
catalogo_ordenado = sorted(catalogo, key=lambda libro: libro.autor)
for libro in catalogo_ordenado:
    print(libro.autor, "-", libro.titulo, "-", "disponibles:", libro.disponibles())

print()
titulo_buscado = "El principito"
encontrado = buscar_libro(catalogo, titulo_buscado)
if encontrado is not None:
    print("encontrado:", encontrado.titulo)
else:
    print("no se encontro el libro", titulo_buscado)

print()
usuarios = ["Ana", "Luis", "Marco"]
i = 0
while i < len(usuarios) and encontrado.disponibles() > 0:
    usuario = usuarios[i]
    print(encontrado.prestar())
    prestamos.append({"libro": encontrado.titulo, "usuario": usuario})
    i += 1

try:
    print(encontrado.prestar())
except ValueError as e:
    print("error:", e)

print()
digital = buscar_libro(catalogo, "Python para todos")
print(digital.prestar())
prestamos.append({"libro": digital.titulo, "usuario": "Ana"})

print()
print("prestamos registrados:")
for prestamo in prestamos:
    print(prestamo["usuario"], "presto", prestamo["libro"])
