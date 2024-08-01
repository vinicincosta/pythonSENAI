print("Qual número é maior")

while True:
    try:
        numero1 = float(input("digite seu primeiro numero:"))
        if numero1 <0:
            print("valor invalido, tente novamente")
        break
    except ValueError:
        print("valor invalido, tente novamente")

while True:
    try:
        numero2 =float(input("digite seu segundo numero:"))
        if numero2:
            print("valor invalido, tente novamente")
        break
    except ValueError:
        print("valor invalido, tente novamente")


if numero1 > numero2:
    print(numero1, "é maior que o", numero2)
else:
    print(numero1, "é menor que o", numero2)