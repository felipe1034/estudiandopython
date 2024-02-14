grupo1 = 0
grupo2 = 0
grupo3 = 0

for m in range (6):
    mañana = int(input("por favor ingrese las edades de los estudiantes ded la mañana"))
    grupo1 = grupo1 + mañana
    
for t in range (7):
    tarde = int(input("por favor ingrese las edades de los estudiantes de la tarde"))
    grupo2 = grupo2 + tarde
    
for n in range (12):
    noche = int(input("por favor ingresar las edades de los estudiantes de la noche"))
    grupo3 = grupo3 + noche 
    
promedio1 = grupo1/6
promedio2 = grupo2/7
promedio3 = grupo3/12

if promedio1 > promedio2 and promedio3 >promedio3:
    print(f"el promedio de edades del grupo de la mañana es: {grupo1} y el promedio es {promedio1}")
elif promedio1 > promedio2 and promedio3 >promedio3:
    print(f"el promedio de edades del grupo de la mañana es: {grupo2} y el promedio es {promedio2}")
else:
    print(f"el promedio de edades del grupo de la mañana es: {grupo3} y el promedio es {promedio3}")