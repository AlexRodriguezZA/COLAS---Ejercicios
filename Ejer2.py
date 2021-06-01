from cola import Cola
from pila import Pila

#Utilizando operaciones de cola y pila, invertir el contenido de una cola.

pila = Pila()
cola = Cola()

for i in range(0,5):
    numero = int(input("Ingrese un numero: "))
    cola.arribo(numero)

print("Cola original")
while (not cola.cola_vacia()):
    x = cola.atencion()
    print(x)
    pila.apilar(x)

while (not pila.pila_vacia()):
    z = pila.desapilar()
    cola.arribo(z)

TamañoCola = cola.tamanio_cola()
indice = 0;
print("Cola invertida")
while (indice < TamañoCola):
    dato = cola.mover_final()
    print(dato)
    indice += 1


