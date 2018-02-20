from pila import Pila
from arbol import Nodo

def insertar(arbol,valor):
    if arbol == None:
        return Nodo(valor)
    if comparar(arbol) and comparar(arbol.der):
        if(arbol.der == None):
            return Nodo(arbol.valor,arbol.izq,insertar(arbol.der, valor))
        else:
            if(not(comparar(arbol.der.izq)))and(not(comparar(arbol.der.der))):
                tempVal = evaluar(arbol.der)
                temp = Nodo(arbol.valor,arbol.izq,Nodo(tempVal))
                return insertar(temp,valor)
            else:
                return Nodo(arbol.valor,arbol.izq,insertar(arbol.der, valor))
    else:
        temp = Nodo(arbol.valor,insertar(arbol.izq, valor),arbol.der)
        if(comparar(Nodo(valor))or(buscar(temp,valor))):
            return temp
        else:
            tempVal = evaluar(temp)
            return Nodo(tempVal)
                    
def comparar(elemento):
    if  elemento == None :
        return True
    if elemento.valor=='+' or elemento.valor=='-' or elemento.valor=='*' or elemento.valor=='/':
        return True
    else:
        return False

def buscar (arbol, valor):
    if arbol.izq== None:
        return True
    elif arbol.izq.valor==valor:
        return False
    else:
        return buscar(arbol.izq,valor)+buscar (arbol.der,valor)

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

def preorden(arbol):
     if arbol==None:
        return ""
     else:
        return str(arbol.valor)+str(preorden(arbol.izq))+str(preorden(arbol.der))

def crearArbol(pilita):
    arbol = Nodo(pilita.desapilar())
    while not(pilita.es_vacia()):
        arbol = insertar(arbol,pilita.desapilar())
        #print preorden(arbol)
    return arbol

def iniciar(entrada):
        print evaluar(crearArbol(crearPila(entrada)))

iniciar("4 5 - 9 7 + 9 7 - + *")
iniciar("8 2 - 9 7 + *")
