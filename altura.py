altura = int(input("dijite el numero de alturas"))
cont=0
suma=0
while cont < altura:
    altura = float(input("ingrese la altura:"))
    suma=suma + altura 
    cont=cont+1
    promedio=suma/altura
print ("el promedio de la altura es:", promedio) 