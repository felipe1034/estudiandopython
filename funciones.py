def inicio():
    
    print("MENU PRINCIPAL")
    print("seleccione la opcion correccta:")
    print("1. para operacion sumar")
    print("2. para operacion restar")
    print("3. para operacion multiplicar")
    print("4. para operacion dividir")
    print("5 salir")
    
def main():
    while True:
        inicio()
        opcion = int(input("seleccione la opcion"))
        if opcion == 1:
            print("ha seleccionado la suma")    
            num1 = int(input("ingresar el 1 numero"))
            num2 = int(input("ingresar el 2 numero"))
            sumar = num1+num2
            print("el resultado de la suma es:",sumar)
        elif opcion == 2:
            print("ha selecionado operacion resta")
            num1 = int(input("ingresar el 1 numero"))
            num2 = int(input("ingresar el 2 numero"))
            restar = num1-num2
            print("el resultado de la resta es:", restar)
        elif opcion ==3:
            print("ha selecionado operacion multiplicar")
            num1 = int(input("ingresar el 1 numero"))
            num2 = int(input("ingresar el 2 numero"))
            multi = num1*num2
            print("el resultado de la multiplicacion es:", multi)
        elif opcion == 4:
            print("ha selecionado operacion dividir")
            num1 = int(input("ingresar el 1 numero"))
            num2 = int(input("ingresar el 2 numero"))
            div = num1/num2
            print("el resultado de la division es:", div)
        elif opcion == 5:
            print("HASTA LUEGO")
            break    
        else:
            print("opcion no valida, selecione una opcion valida")                    
main()        