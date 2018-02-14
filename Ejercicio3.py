from pila import Pila
from arbol import Nodo

def insertar(arbol,valor):
    if arbol == None:
        return Nodo(valor)
    if comparar(arbol.valor):
        return Nodo(arbol.valor,insertar(arbol.izq, valor),arbol.der)
    else:
        return Nodo(arbol.valor,arbol.izq,insertar(arbol.der, valor)) 
        
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

def crearArbol(arbolito,pilita):
    if pilita.es_vacia():
        return arbolito
    else:
        arbolito = insertar(arbolito, pilita.desapilar())
        return crearArbol(arbolito,pilita)

def iniciar(entrada):
    print evaluar(crearArbol(None,crearPila(entrada)))

print(iniciar("8 2 - 9 7 + *"))
