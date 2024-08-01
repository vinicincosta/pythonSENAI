print("Vamos calcular a média")
print("")

nota1 = 0
nota2 = 0
media = 0

while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        if nota1 <0 and nota1 >100:
            print("número inválido,tente novamente")
        break
    except ValueError:
        print("número inválido,tente novamente")



while True:
    try:
       nota2 = float(input("Digite a segunda nota: "))
       if nota2 <0 and nota1 >100:
            print("número inválido,tente novamente")
       break
    except ValueError:
        print("número inválido,tente novamente")

media = nota1 + nota2
print("o valor da média das duas notas é", media)






