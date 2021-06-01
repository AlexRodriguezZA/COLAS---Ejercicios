from cola import Cola
#Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.

cola = Cola()

print(">>Ingrese los números:")
for i in range(0,5):
    numero = int(input(">"))
    cola.arribo(numero)

numeroBuscado = int(input("-Ingrese el número que desee ver si se repite: "))
contador = 0;
i = 0;

while i < cola.tamanio_cola():
    dato = cola.mover_final()
    if (dato == numeroBuscado):
        contador += 1
    i += 1

print("El número de ocurrencias del n ",numeroBuscado," es de --> ",contador)