print("calculadora de ohm")
print("0 - Sair")
print("1 - resistência")
print("2 - tensão")
print("3 - resistência do resistor")
print("4 - corrente")
print("")

opcao = int(input("Digite o numero da escolha desejada: "))

while opcao != 0:

    if opcao == 1:
        print("resistencia")
        print("")
        while True:
            try:
                tensao = float(input("Digite a tensão em volts: "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")

        while True:
            try:
                corrente = float(input("Digite a corrente em amperes: "))
                if corrente > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")
        resistencia = tensao / corrente
        print(f"A resistência é",resistencia)


    elif opcao == 2:
        print("tensão")
        print("")
        while True:
            try:
                corrente = float(input(" descobir o valor da corrente elétrica em amperes"))
                if corrente > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")

        while True:
            try:
                resistencia = float(input("digite o valor da resistencia elétrica em ohms"))
                if resistencia > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")
        tensao = resistencia * corrente
        print(f"A tensão é {tensao} em volts")




    elif opcao == 3:
        print("resistência do resistor")
        print("")
        while True:
            try:
                tensao_da_fonte = float(input("digite o valor da tensão da fonte em volts"))
                if tensao_da_fonte > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")

        while True:
            try:
                corrente_led = float(input("digite o valor da corrente led em amperes"))
                if corrente_led > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")

        while True:
            try:
                tensao_led = float(input("digite o valor da tensão led em volts"))
                if tensao_led > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")
        resistencia_resistor = (tensao_da_fonte - tensao_led) / corrente_led
        print(f"A resistência do resistor é: {resistencia_resistor}")


    elif opcao == 4:
        print("corrente")
        print("")
        while True:
            try:
                tensao = float(input("digite o valor da tensão em volts: "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")
        while True:
            try:
                resistencia = float(input("digite o valor da resistência em ohm:"))
                if resistencia > 0:
                    break
            except ValueError:
                print("Valor invalido, digite um número utilizando o ponto como separador. Ex 1.0 ")
        corrente = tensao / resistencia
        print(f"O valor da corrente é, {corrente} em amperes")

    else:
        print("opçãp inválida")

    print("")
    print("calculadora de ohm")
    print("0 - Sair")
    print("1 - resistência")
    print("2 - tensão")
    print("3 - resistência do resistor")
    print("4 - corrente")
    print("")
    opcao = int(input("Digite o numero da escolha desejada: "))
