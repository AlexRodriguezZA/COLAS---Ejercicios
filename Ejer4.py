from cola import Cola
from pila import Pila
from random import randint

#Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.

cola = Cola()
colaAux = Cola()
validacion = None;

def EliminarNumeroPrimo(n):
        if n < 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True        
    
for i in range(0,10):
    cola.arribo(randint(0,100))

i = 0;
print(">> Los elementos cargados son: ")
while (i < cola.tamanio_cola()):
    dato = cola.mover_final()
    print(dato)
    i += 1 

print(">>Elementos que no son primos: ")
while not cola.cola_vacia():
    z = cola.atencion()
    if EliminarNumeroPrimo(z) != True:
        print(z)
        colaAux.arribo(z)







