import random
continuacao_programa = 0

print("PARABÉNS usuário, você está dentro do jogo, vamos jogar !!!!")
print("*********************************************************************")
print("Esse jogo consiste no par ou ímpar, escolha um número de 0 á 5 e bora pro jogo")
print("*********************************************************************")
print("COMPUTADOR vs USUÁRIO")
print("*********************************************************************")
print("")
print(f"[Entrar] 1, [Sair] 2")
print("")
escolha = input("você deseja entrar ou sair: ")
while escolha != "1" and escolha != "2":
    print("entrada inválida")
    escolha = input("você deseja entrar ou sair: ")


if escolha == "1":
    print("começou o jogo")

    while True:
        print("[1] Par, [2] Impar")
        while True:
                try:
                    par_impar = int(input("Você deseja par ou impar: "))
                    if par_impar != 1 and par_impar != 2:
                        raise TypeError
                    else:
                        break

                except TypeError:
                    print("Entrada inválida, você deseja par ou impar")
                except ValueError:
                    print("Entrada inválida, você deseja par ou impar")



        while True:
            try:
                escolha_numero = float(input("faça sua escolha de 0 á 5:"))
                if escolha_numero < 0 or escolha_numero > 5:
                    raise TypeError
                break
            except TypeError:
                print("Valor invalido, digite um número de 0 a 5")
            except ValueError:
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
        else:
            print("você perdeu")

        while True:
            try:
                print("[1] Continuar jogando, [2] Sair do jogo")
                continuacao_programa = int(input("Deseja continuar jogando? "))
                if continuacao_programa == 1:
                    numero_computador = random.randint(0,5)
                elif continuacao_programa == 2:
                    break
                if continuacao_programa != 1 and continuacao_programa != 2:
                    raise TypeError
                else:
                    break
            except TypeError:
                    print("Opção Inválida, tente novamente")
            except ValueError:
                print("Opção Inválida, tente novamente")
        if continuacao_programa == 2:
            print("")
            print("obrigado por ter jogado usuário, beijos")
            break

else:
    print("sair do jogo, te esperamos na próxima usuário")
