print("represente os dias da semana com números")
numero = 0

while True:
    while True:
        try:
            numero = int(input("Digite um número de 1 a 7:"))
            if numero <0 or numero >7:
                print("Valor inválido, tente novamente")
            else:
                break
        except ValueError:
            print("Valor inválido, tente novamente")
    print("QUAL SERÁ")
    if numero == 1:
        print("Realizando o cáluclo....")
        print("Domingo, amanhã tem que trabalhar 😒")
    elif numero == 2:
        print("Realizando o cáluclo....")
        print("Segunda-feira")
    elif numero == 3:
        print("Realizando o cáluclo....")
        print("Terça-feira")
    elif numero == 4:
        print("Realizando o cáluclo....")
        print("Quarta-feira")
    elif numero == 5:
        print("Realizando o cáluclo....")
        print("Quinta-feira")
    elif numero == 6:
        print("Realizando o cáluclo....")
        print("Sexta-feira, ufa vamo curtir 😁")
    elif numero == 7:
        print("Realizando o cáluclo....")
        print("Sábado, ainda tem mais por hoje 😎")


