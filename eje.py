Edad = int(input("por favor ingresar su edad"))

if Edad < 4:
    ingreso = 0
elif Edad <=18:
    ingreso = 5000
else:
    ingreso = 10000
    
print ("el csoto de la boleta es", ingreso)