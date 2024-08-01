def solicite_lado1():
    while True:
        try:
            lado1 = int(input("Digite o lado 1: "))

            return lado1
        except ValueError:
            print("Valor invalido, tente novamente")

def solicite_lado2():
    while True:
        try:
            lado2 = int(input("Digite o lado 2: "))

            return lado2
        except ValueError:
            print("Valor invalido, tente novamente")

def solicite_lado3():
    while True:
        try:
            lado3 = int(input("Digite o lado 3: "))
            return lado3
        except ValueError:
            print("Valor invalido, tente novamente")


lado1 = solicite_lado1()
lado2 = solicite_lado2()
lado3 = solicite_lado3()


if lado1 == lado2 == lado3:
    print("Lados iguais, TRIANGULO EQUILATERO")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Triangulo ESCALENO")

else:
    print("TRIANGULO ISÓSCELES")




