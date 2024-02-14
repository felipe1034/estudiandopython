texto = "buenos dias definiendo un parametro como funcion"
def mensaje():
    n1= int(input("ingresar el primer numero"))
    n2= int(input("ingresar el segundo numero"))
    calcularmayor(n1,n2)
    positivo (n1,n2)
    
def calcularmayor(num1,num2):
    if num1>num2:
        print("el primer numero es el mayor")
    elif num1==num2:
        print("son numeros iguale")
    else:
        print("el segundo numero es el mayor")

def positivo(p1,p2):
    if p1>0 or p2>0:
        print("numero positivo")
    elif p1<0 and p2<0:
        print("son negativos")
    else:
        print("al menos uno de los numeros no es positivo")
        
mensaje()