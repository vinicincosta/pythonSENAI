print("positivo / negativo")
print("veremos se o número é POSITIVO ou NEGATIVO")
print("")


while True:
    try:
        numero1 = float(input("Digite um numero: "))
        if numero1 <0:
            print("Número negativo")

        elif numero1 >0:
            print("Número positivo")

        else:
            print("Numero igual =0, portanto neutro")
        break

    except ValueError:
        print("Numero inválido, tente novamente")



