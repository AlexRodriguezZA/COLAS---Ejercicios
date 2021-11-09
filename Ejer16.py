from heap import HeapMax
# Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

ColaPrioridad = HeapMax()
ColaAux = HeapMax()
empleados = ["Marcos", "Alex","Mati"]
StaffTI = ["Maria","Euge"]
Gerente = "Santiago"

#PUNTO A
for e in empleados:
    ColaPrioridad.arribo(e,1)

#PUNTO c
for s in StaffTI:
    ColaPrioridad.arribo(s,2)
#PUNTO d
ColaPrioridad.arribo(Gerente,3)
#PUNTO B
for i in range(1):
    print(ColaPrioridad.atencion())


#PUNTO F
NuevoGerente = "Marta"
ColaPrioridad.arribo(NuevoGerente,3)
NuevosEmpleados = ["Tito", "Marisa"]
for e2 in NuevosEmpleados:
    ColaPrioridad.arribo(e2,1)


#PUNTO G
print("cola completaa")
while(not ColaPrioridad.vacio()):
    print(ColaPrioridad.atencion())

#PUNTO E
for i in range(2):
    print(ColaPrioridad.atencion())
