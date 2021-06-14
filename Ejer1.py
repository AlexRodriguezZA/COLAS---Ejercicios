from cola import Cola
#Eliminar de una cola de caracteres todas las vocales que aparecen.

cola = Cola()

vocales = ["a","e","i","o","u"]

palabra = str(input("Ingrese una palabra: "))

for letra in palabra:
    cola.arribo(letra.lower())

indice = 0;
cantidadDeElementos = cola.tamanio_cola();

while(indice < cantidadDeElementos):
    x = cola.atencion()
    if x not in vocales:
        cola.arribo(x)
    indice += 1

i = 0
while(i < cola.tamanio_cola()):
    dato = cola.mover_final()
    print(dato)
    i += 1





