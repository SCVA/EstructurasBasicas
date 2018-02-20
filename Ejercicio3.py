from pila import Pila
from arbol import Nodo

def insertar(arbol,valor):
    if arbol == None:
        return Nodo(valor)
    if comparar(arbol.valor):
        return Nodo(arbol.valor,arbol.izq,insertar(arbol.der, valor))
    else:
        if(arbol.der == None):
            return Nodo(arbol.valor,arbol.izq,insertar(arbol.der, valor))
        else:
            return Nodo(arbol.valor,insertar(arbol.izq, valor),arbol.der)
                    
def comparar(elemento):
    if elemento=='+' or elemento=='-' or elemento=='*' or elemento=='/':
        return True
    else:
        return False

def evaluar(arbol):
    if arbol.valor=='+':
        return evaluar(arbol.izq)+ evaluar(arbol.der)
    elif arbol.valor=='-':
        return evaluar(arbol.izq)- evaluar(arbol.der)
    elif arbol.valor=='*':
        return evaluar(arbol.izq)* evaluar(arbol.der)
    elif arbol.valor=='/':
        return evaluar(arbol.izq)/ evaluar(arbol.der)
    else:
        return int(arbol.valor)

def crearPila(cadena):
    elementos=cadena.split(" ") 
    lista = Pila()
    [lista.apilar(x) for x in elementos]
    return lista


def crearArbol(pilita):
    arbol = Nodo(pilita.desapilar())
    while not(pilita.es_vacia()):
        arbol = insertar(arbol,pilita.desapilar())
        print preorden(arbol)
    return arbol

def iniciar(entrada):
        print evaluar(crearArbol(crearPila(entrada)))

print(iniciar("8 2 - 9 7 + *"))
