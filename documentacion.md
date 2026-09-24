# Proyecto integrador: biblioteca

## Problema

Llevar el control del catalogo de una biblioteca: cuantos ejemplares hay
de cada libro, cuales estan disponibles y quien se los llevo prestados.
Hay libros fisicos, que tienen un numero limitado de copias, y libros
digitales, que no se agotan nunca.

## Como esta armado

`modelos.py` tiene las clases. `Libro` guarda titulo, autor, cantidad de
ejemplares y cuantos estan prestados, con metodos para prestar y
devolver. `LibroDigital` hereda de `Libro` pero sobreescribe esos
metodos porque una copia digital no tiene limite.

Antes de descontar un ejemplar se valida que haya stock; si no hay,
se lanza un error que el programa captura para no cortarse.

Para buscar un libro por titulo hay una funcion aparte de las clases,
y para ordenar el catalogo por autor se usa una funcion lambda dentro
de sorted().

Los prestamos se guardan en una lista de diccionarios (libro y
usuario), pensando en que despues eso pase a ser una tabla de base de
datos.

Hay dos formas de correrlo: `biblioteca.py`, que muestra todo por
consola, y `biblioteca_gui.py`, con una ventana hecha con tkinter,
para la exposicion. Las dos usan las mismas clases de `modelos.py`.

## Falta

Los datos del catalogo estan puestos a mano en el codigo. Lo que sigue
es conectarlo a una base de datos real.
