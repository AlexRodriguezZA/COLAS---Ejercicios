from cola import Cola

#Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
#de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
#a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
#b. indicar el plantea natal de Luke Skywalker y Han Solo
#c. insertar un nuevo personaje antes del maestro Yoda
#d. eliminar el personaje ubicado después de Jar Jar Binks
 
cola = Cola()
colaAux = Cola()

personajes = ["Luke Skywalker","Alderaan"]
cola.arribo(personajes)
personajes = ["Yoda","Alderaan"]
cola.arribo(personajes)
personajes = ["Han Solo","Marte"]
cola.arribo(personajes)
personajes = ["C3po","Endor"]
cola.arribo(personajes)
personajes = ["Jar Jar Binks","Tatooine"]
cola.arribo(personajes)
personajes = ["darth vader","Tatooine"]
cola.arribo(personajes)

eliminacion = bool
perosnajeAntesYoda = ["Alexxx","Tierra"]


while not cola.cola_vacia():
    pers = cola.atencion()
    if pers[1] == "Alderaan" or pers[1] == "Endor" or pers[1] == "Tatooine":
        print("El personaje -> ",pers[0]," pertenece a ", pers[1])
    if pers[0] == "Han Solo" or pers[0] == "Luke Skywalker":
        print("Planeta Natal de ",pers[0]," es ", pers[1])
    if pers[0] == "Yoda":
        colaAux.arribo(perosnajeAntesYoda)
    if (pers[0] == "Jar Jar Binks"):
        eliminacion = True #Se acitva cuando aparece Jar Jar Binks para no agregar el proximo  
    if eliminacion != True:
        colaAux.arribo(pers)

while not colaAux.cola_vacia():
    x = colaAux.atencion()
    print(x[0])

