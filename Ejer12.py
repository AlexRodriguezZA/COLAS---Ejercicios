from cola import Cola
#Dada dos colas con valores ordenados, realizar un algoritmo que permita combinarlas en una
#nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
#ni métodos de ordenamiento.

cola1 = Cola();
cola2 = Cola();
colaBoss = Cola();

setNumeros1 = [1,3,5,6,9];
setNumeros2 = [0,1,1,2,2];

#Cargamos los elementos

for n in setNumeros1:
    cola1.arribo(n);

for n2 in setNumeros2:
    cola2.arribo(n2);

#cargamos la primera cola en la colaBoss
while(not cola1.cola_vacia()):
    x1 = cola1.atencion();
    colaBoss.arribo(x1);


for i in range(0,cola2.tamanio_cola()):
    movimientos = 1;
    while(cola2.en_frente()>colaBoss.en_frente()):

        colaBoss.mover_final();
        movimientos += 1;
    
    x2 = cola2.atencion()
    colaBoss.arribo(x2)
    for i in range(0,colaBoss.tamanio_cola()-movimientos):
        colaBoss.mover_final()

while not (colaBoss.cola_vacia()):
    z = colaBoss.atencion()
    print(z)







    