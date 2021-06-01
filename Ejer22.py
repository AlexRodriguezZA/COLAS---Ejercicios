from cola import Cola

#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce 
# el nombre del personaje, el nombre del superhéroe y su género (Masculino M y FemeninoF) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, 
# etc., desarrollar un algoritmo que resuelva las siguientes actividades:

#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

cola = Cola()

Marvel = ["Tony Stark", "Iron Man", "M"]
cola.arribo(Marvel)
Marvel = ["Natasha Romanoff","Black Widow", "F"]
cola.arribo(Marvel)
Marvel = ["Steve Rogers","Capitán América", "M"]
cola.arribo(Marvel)
Marvel = ["Scott Lang", "Ant-man", "M"]
cola.arribo(Marvel)
Marvel = ["Bruce Banner", "Hulk", "M"]
cola.arribo(Marvel)
Marvel = ["Carol Danvers", "Capitana Marvel", "F"]
cola.arribo(Marvel)

PersonajesConS = []
i = 0
while(i < cola.tamanio_cola()):
    per = cola.mover_final()
    if (per[1] == "Capitana Marvel"):
        print("El nombre de la capitana marvel es --> ", per[0]) # punto A
    if per[2] == "F": #punto B
        print("Personaje femenino --> ", per[1])
    else: #punto C
        print("Peronajes masculino --> ", per[1])
    if per[1] == "Scott Lang":
        print("Scott Lang es --> ", per[1]) #Punto D
    if per[0][0] == "S":
        PersonajesConS.append(per)
    if per[0] == "Carol Danvers":
        print("Carol Danvers está en la lista y su peronaje es --> ", per[1]) #Punto F
    
    i += 1
print()
print("Personajes con inicial S") #Punto E
for p in PersonajesConS:
    print("Nombre: ", p[0])
    print("Super heroe: ", p[1])
    print("Género: ", p[2])