from cola import Cola
from pila import Pila

#Utilizando operaciones de cola y pila, invertir el contenido de una pila.

pila = Pila()
cola = Cola()

#Cargamos la pila
for i in range(0,5):
    numero = int(input("Ingrese un número: "))
    pila.apilar(numero)

#Desapilamos y cargamos en la cola y mostramos la pila
print(">> Los elementos de la pila son:")
while not pila.pila_vacia():
    x = pila.desapilar()
    print(x)
    cola.arribo(x)

#Descargamos la cola y apilamos en la pila
while not cola.cola_vacia():
    z = cola.atencion()
    pila.apilar(z)
#Mostramos el contenido invertido de la pila
print(">> Los elementos de la pila invertida son:")
while not pila.pila_vacia():
    dato = pila.desapilar()
    print(dato)