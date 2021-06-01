from cola import Cola
from pila import Pila
#Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo.

pila = Pila()
cola = Cola()
pilaAux = Pila()
contadorValidaciones = 0;

palabra = str(input("Ingrese la palabra: "))

for letra in palabra:
    pila.apilar(letra)
    cola.arribo(letra)

while (not cola.cola_vacia()):
    letraPila = pila.desapilar()
    letraCola = cola.atencion()
    if letraPila == letraCola:
        contadorValidaciones += 1

if contadorValidaciones == len(palabra):
    print("La palabra es paliendromo")
else:
    print("La palabra NO es paliendromo")

