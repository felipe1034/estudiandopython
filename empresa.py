cont = 0
numeros = 0
acum = 0 
acumul = 0
empleados = int(input("cuantos empleados quiere verificar"))
while cont < empleados :
    sueldo = int(input("ingrese su sueldo"))
    numeros = numeros + sueldo
    cont + 1
    print("el empleado numero", cont, "recibe un sueldo de", sueldo)
    if sueldo >= 1300000 and sueldo <= 3000000:
        acum +1
    elif sueldo >= 3000000:
        acuml +=1
    print("la cantidad de empleados que cobran entre $10.000.000 y $ 3000.000 es", acum)
    print("la cantidad de empleados que cobran $3.000.000 o mas", acuml)
    print("el importe que gasta la empresa e peresonal es", numeros)     