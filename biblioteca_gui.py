import tkinter as tk
from tkinter import messagebox
from modelos import Libro, LibroDigital, buscar_libro

catalogo = [
    Libro("Cien anios de soledad", "Gabriel Garcia Marquez", 2),
    Libro("El principito", "Antoine de Saint-Exupery", 1),
    LibroDigital("Python para todos", "Charles Severance"),
]

# cada elemento de aqui seria despues una fila de una tabla en la bd
prestamos = []


def refrescar_lista():
    lista_catalogo.delete(0, tk.END)
    catalogo_ordenado = sorted(catalogo, key=lambda libro: libro.autor)
    for libro in catalogo_ordenado:
        texto = f"{libro.titulo}  ({libro.autor})  -  disponibles: {libro.disponibles()}"
        lista_catalogo.insert(tk.END, texto)


def obtener_libro_seleccionado():
    seleccion = lista_catalogo.curselection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un libro de la lista")
        return None
    catalogo_ordenado = sorted(catalogo, key=lambda libro: libro.autor)
    return catalogo_ordenado[seleccion[0]]


def prestar_libro():
    libro = obtener_libro_seleccionado()
    if libro is None:
        return
    usuario = entrada_usuario.get().strip()
    if usuario == "":
        messagebox.showwarning("Aviso", "Escribe el nombre del usuario")
        return
    try:
        mensaje = libro.prestar()
        prestamos.append({"libro": libro.titulo, "usuario": usuario})
        actualizar_registro()
        messagebox.showinfo("Prestamo", mensaje)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    refrescar_lista()


def devolver_libro():
    libro = obtener_libro_seleccionado()
    if libro is None:
        return
    try:
        mensaje = libro.devolver()
        messagebox.showinfo("Devolucion", mensaje)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    refrescar_lista()


def buscar_titulo():
    titulo = entrada_busqueda.get().strip()
    encontrado = buscar_libro(catalogo, titulo)
    if encontrado is not None:
        messagebox.showinfo("Busqueda", f"Encontrado: {encontrado.titulo} - {encontrado.autor}")
    else:
        messagebox.showinfo("Busqueda", f"No se encontro el libro '{titulo}'")


def actualizar_registro():
    lista_prestamos.delete(0, tk.END)
    for prestamo in prestamos:
        lista_prestamos.insert(tk.END, f"{prestamo['usuario']} presto {prestamo['libro']}")


ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.geometry("500x500")

tk.Label(ventana, text="Catalogo", font=("Arial", 12, "bold")).pack(pady=(10, 0))
lista_catalogo = tk.Listbox(ventana, width=60, height=6)
lista_catalogo.pack(pady=5)

marco_usuario = tk.Frame(ventana)
marco_usuario.pack(pady=5)
tk.Label(marco_usuario, text="Usuario:").pack(side=tk.LEFT)
entrada_usuario = tk.Entry(marco_usuario, width=20)
entrada_usuario.pack(side=tk.LEFT, padx=5)

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=5)
tk.Button(marco_botones, text="Prestar", command=prestar_libro).pack(side=tk.LEFT, padx=5)
tk.Button(marco_botones, text="Devolver", command=devolver_libro).pack(side=tk.LEFT, padx=5)

marco_busqueda = tk.Frame(ventana)
marco_busqueda.pack(pady=15)
tk.Label(marco_busqueda, text="Buscar por titulo:").pack(side=tk.LEFT)
entrada_busqueda = tk.Entry(marco_busqueda, width=25)
entrada_busqueda.pack(side=tk.LEFT, padx=5)
tk.Button(marco_busqueda, text="Buscar", command=buscar_titulo).pack(side=tk.LEFT)

tk.Label(ventana, text="Prestamos registrados", font=("Arial", 12, "bold")).pack(pady=(15, 0))
lista_prestamos = tk.Listbox(ventana, width=60, height=6)
lista_prestamos.pack(pady=5)

refrescar_lista()

if __name__ == "__main__":
    ventana.mainloop()
