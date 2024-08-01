print("Solicite 3 números e veja qual é o maior entre eles")

while True:
    try:
        numero1 = int(input("Digite seu primeiro número:"))
        if numero1 <0:
            print("valor invalido, tente novamente")
        break
    except ValueError:
        print("valor invalido, tente novamente")

while True:
    try:
        numero2 = int(input("Digite seu segundo número:"))
        if numero2 <0:
            print("valor invalido, tente novamente")
        break
    except ValueError:
        print("valor invalido, tente novamente")

while True:
    try:
        numero3 = int(input("Digite seu terceiro número:"))
        if numero3 <0:
            print("valor invalido, tente novamente")
        break
    except ValueError:
        print("valor invalido, tente novamente")

if numero1 == numero2 == numero3:
  print("os numero são iguais")
elif numero1 > numero2 and numero1 > numero3:
  print(numero1,"é o maior")
elif numero2 > numero1 and numero2 > numero3:
  print(numero2, "é maior")
else:
  print(numero3, "é o maior",)
