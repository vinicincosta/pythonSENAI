import random

print("PARABÉNS usuário, você está dentro do jogo, vamos jogar !!!!")
print("Esse jogo consite no par ou ímpar, escolha um número de 0 á 5 e bora pro jogo")
print("COMPUTADOR vs USUÁRIO")
print(f"[Entrar] 1, [Sair] 2")
escolha = input("você deseja entrar ou sair: ")
while escolha != "1" and escolha != "2":
    print("entrada inválida")
    escolha = input("você deseja entrar ou sair: ")


if escolha == "1":
    print("começou o jogo")

    while True:
        print("[1] Par, [2] Impar")
        par_impar = int(input("Você deseja par ou impar: "))
        while par_impar != 1 and par_impar != 2:
            print("entrada inválida")
            par_impar = int(input("Você deseja par ou impar: "))


        while True:
            try:
                escolha_numero = float(input("faça sua escolha de 0 á 5:"))
                if escolha_numero < 0 or escolha_numero > 5:
                    raise TypeError
                break
            except TypeError:
                print("Valor invalido, digite um número de 0 a 5")



        numero_computador = random.randint(0,5)
        print("O número que o computador escolheu foi",numero_computador)
        soma_numero = (escolha_numero + numero_computador)
        print("O resultado dos dois números é",soma_numero)

        if soma_numero % 2 == 0:
            resultado_jogo = 1


        elif soma_numero % 2 != 0:
            resultado_jogo = 2


        if par_impar == resultado_jogo:
            print("você ganhou")
            continuacao_programa = input("Deseja continuar jogando [Sim/Não]? ")
            if continuacao_programa != "Sim":
                break
        else:
            print("você perdeu")
            continuacao_programa = input("Deseja continuar jogando [Sim/Não]? ")
            if continuacao_programa != "Sim":
                break
else:
    print("sair do jogo")

