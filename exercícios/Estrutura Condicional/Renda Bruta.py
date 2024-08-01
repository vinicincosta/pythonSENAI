print("")
print("RENDA ANUL BRUTA / IMPOSTO DE RENDA")
print("")

renda_bruta = 0
aliquota = 0
desconto = 0
desconto_aplicado = 0
while True:
    while True:
        try:
            renda_bruta = float(input("Digite a renda bruta: "))
            if renda_bruta <0:
                print("RENDA INVALIDA")
            else:
                break
        except ValueError:
            print("RENDA INVALIDA")

    if renda_bruta == 56072:
        print("Você não terá desconto")
        aliquota = 0
    elif renda_bruta >= 56072 and renda_bruta <= 238532:
        print("Seu desconto será de 7.50%")
        aliquota = 7.50
    elif renda_bruta >= 238532 and renda_bruta <= 522400:
        print("Seu desconto será de 15%")
        aliquota = 15
    elif renda_bruta >= 522400 and renda_bruta <=987600:
        print("Seu desconto será de 22.50%")
        aliquota = 22.50
    elif renda_bruta >= 987600:
        print("27.50%")
        aliquota = 27.5


    desconto = aliquota / 100 * renda_bruta
    desconto_aplicado = renda_bruta - desconto

    print("O valor do desconto aplicado é de {:.3f}".format(desconto))
    print("O valor da renda bruta após o desconto é de {:.3f}".format(desconto_aplicado))



