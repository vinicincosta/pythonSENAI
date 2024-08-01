print("Solicite os meses do ano com os números de 1 - 12")
print("")

numero_mes = 0

while True:
    while True:
        try:
            numero_mes = int(input("Digite um número entre 1 e 12: "))
            if numero_mes < 1 or numero_mes > 12:
                print("Valor inválido, tente novamente.")
            else:
                break
        except ValueError:
            print("Valor inválido, tente novamente.")
    if numero_mes == 1:
        print("Realizando o cáluclo....")
        print("Janeiro")
    elif numero_mes == 2:
        print("Realizando o cáluclo....")
        print("Fevereiro")
    elif numero_mes == 3:
        print("Realizando o cáluclo....")
        print("Março")
    elif numero_mes == 4:
        print("Realizando o cáluclo....")
        print("Abril")
    elif numero_mes == 5:
        print("Realizando o cáluclo....")
        print("Maio")
    elif numero_mes == 6:
        print("Realizando o cáluclo....")
        print("Junho")
    elif numero_mes == 7:
        print("Realizando o cáluclo....")
        print("Julho")
    elif numero_mes == 8:
        print("Realizando o cáluclo....")
        print("Agosto")
    elif numero_mes == 9:
        print("Realizando o cáluclo....")
        print("Setembro")
    elif numero_mes == 10:
        print("Realizando o cáluclo....")
        print("Outubro")
    elif numero_mes == 11:
        print("Realizando o cáluclo....")
        print("Novembro")
    elif numero_mes == 12:
        print("Realizando o cáluclo....")
        print("Dezembro")

