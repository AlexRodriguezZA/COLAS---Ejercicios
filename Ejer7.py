from cola import Cola

#Eliminar el i-ésimo elemento después del frente de la cola.

cola = Cola()
colaAux = Cola()

for i in range(0,5):
    numero = int(input("Ingrese un numero: "))
    cola.arribo(numero)

contador = 0;
while not cola.cola_vacia():
    dato = cola.atencion()
    if contador != 1:
        colaAux.arribo(dato)
    else:
        print("Se elimino el elemento --> ",dato)
    contador +=1

while not colaAux.cola_vacia():
    x = colaAux.atencion()
    print(x)







