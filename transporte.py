nombres = []
kilo = []
total_kms = []
conductor = []
acum_km = 0
n= int(input("dijite la cantidad de coductores"))
for c in range(n):
    nom = input("por favor dijite el nombre del conductor")
    nombres.append(nom)


for semana in range(n):
    acum_km=0
    for dias_semana in range (1,8):
        km = int(input("dijite los kilomentros de la semana"))
        acum_km = acum_km + km
    total_kms.append(acum_km)
    
print(total_kms, nombres)