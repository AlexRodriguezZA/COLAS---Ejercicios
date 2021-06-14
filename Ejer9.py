from cola import Cola;
#Dada una cola de valores enteros calcular su rango y contar cuantos elementos negativos hay

colaEnteros = Cola();

for i in range(0,5):
    numeroCargar = int(input("cargue el numero: "))
    colaEnteros.arribo(numeroCargar);


numerosNegativos = 0;
MayorNumero = 0;
MenorNumero = colaEnteros.en_frente(); 
while(not colaEnteros.cola_vacia()):
    dato = colaEnteros.atencion();
    if (dato<0):
        numerosNegativos +=1;
    if (dato>=MayorNumero):
        MayorNumero = dato;
    if (dato<MenorNumero):
        MenorNumero = dato

rango = (MayorNumero - MenorNumero);

print(f"> La cantidad de numeros negativos que hay en la lista es de -> {numerosNegativos}")
print(f"> El rango de la lista de enteros es {rango}")

