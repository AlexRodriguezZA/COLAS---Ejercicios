from cola import Cola
#Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando
# solo una cola como estructura auxiliar.

colaNumeros = Cola()
colaAux = Cola()
setNumeros = [3,2,5,0,5,2,8,7,9]
setNumeros2 = [2,3,4,6,7,9,10]
ultimoElementoIngresado = 0;
for numero in setNumeros:
    if (colaNumeros.cola_vacia() == True):
        colaNumeros.arribo(numero)
        ultimoElementoIngresado = numero;
    else:
        if (numero >= ultimoElementoIngresado):
            colaNumeros.arribo(numero)
            ultimoElementoIngresado = numero;

        else:
            while not colaNumeros.cola_vacia() and numero<ultimoElementoIngresado:
                dato = colaNumeros.atencion()
                colaAux.arribo(dato)
            colaNumeros.arribo(numero)
            while not colaAux.cola_vacia():
                dato = colaAux.atencion()
                colaNumeros.arribo(dato)
                ultimoElementoIngresado = dato;


        


while not colaNumeros.cola_vacia():
    dato = colaNumeros.atencion()
    print(dato)

