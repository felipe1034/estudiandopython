nombres=[]
notas=[]
amejor = []
mb=0
b=0
iN=0

for x in range(1,4):
    nom = input("por favor ingresar el nombre del alumno")
    nombres.append(nom)
    no = int(input(f"por favor ingresar las notas del alumno: {x}"))
    notas.append(no)
    
for y in range(len(nombres)):
    print(nombres[y])
    print(notas[y])


if notas[x]>=8:
    print("alumno muy bueno")
    mb +=1
    amejor.append(nombres[y])
else:
    if notas[x]>=4:
        print("alumno bueno")
        b += 1
    else:
        print("alumno no aprueba la materia")
        iN += 1

        
for z in len(notas):
    if notas[z]>=4 and notas[z]<=7:
        #notas.pop(z)
        #nombres.pop(z)
        eliminar.append

for d in sorted(eliminar,reverse=true):
    notas.pop[d]
    nombres.pop[d]
        
print("cantidad de alumnos muy buenos son:",mb)
print("lo nombres de los mejores alumnos x nota son:",amejor)
print("listado de alumnos ", nombres[z])

