def añobisiesto():
    ano = int(input("dijite el año"))
    bis(ano)
    
def bis(anno):
    if anno %4 == 0 and anno %100!=0:
        print("el {anno} es bisiesto")
    else:
        print("el {anno} no es bisiesto")
        
añobisiesto()