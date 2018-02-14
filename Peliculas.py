from cola import Cola
from pila import Pila


class Pelicula:

    def __init__(self, nombre,genero):
        self.nombre= nombre
        self.genero= genero


def apilarGenero(cola,genero):
    pila = Pila()
    while (cola.es_vacia()!=True):
        pelicula= cola.desencolar()
        if(pelicula.genero==genero):
            pila.apilar(pelicula)
    return pila

peliculas = [Pelicula("Terminator","AC"),Pelicula("Misión Imposible", "AC"), Pelicula("La Ouija","TR")]

cola= Cola()

[cola.encolar(x) for x in peliculas]

genero= "AC"

print([x.nombre for x in cola.items])

pilaGenero= apilarGenero(cola,genero)

while (pilaGenero.es_vacia()!=True):
    x=pilaGenero.desapilar()
    print(x.nombre+" "+x.genero)

#print ([x.nombre+" "+x.genero for x in pilaGenero.items])




