ancho = int(input("ingrese el ancho del rectangulo"))
altura = int(input("ingrese la altura del rectangulo"))
caract = input("ingrese el caracter a utilizar")

def dibujar(an,al,letra):
    for i in range(an):
        for j in range(al):
            print(letra,end="")
        print()
            
dibujar(ancho,altura,caract)