#Jogo adivinhação

import random
continuacao_programa = 0
escolha_programa = 0

print("PARABÉNS usuário, você está dentro do jogo, vamos jogar !!!!")
print("*************************************************************************************************************************")
print("O jogo consiste em que o programa escolhe um número de 1 á 100, e você tentar acertar o número escolhido pelo programa")
print("**************************************************************************************************************************")
print(f"[Entrar] 1, [Sair] 2")
escolha = input("você deseja entrar ou sair: ")
print("")
while escolha != "1" and escolha != "2":
    print("entrada errada, digite novamente")
    escolha = input("você deseja entrar ou sair: ")


numero_aleatorio = random.randint(1, 100)

if escolha == "1":
    print("Começou o jogo")
    print("você deverá escolher um número até 100")
    print("COMPUTADOS vs USUÁRIO")
    print("")



    while True:

        try:

            escolha_usuario = float(input("Digite sua escolha:"))
            if escolha_usuario > 100 or escolha_usuario < 1:
                raise TypeError
            else:
                if numero_aleatorio > escolha_usuario:
                    print("você está chegando perto, tente novamente")
                    print("o número misterioso é maior")

                elif numero_aleatorio < escolha_usuario:
                    print("você está chegando perto, tente novamente")
                    print("o número misterioso é menor")

                elif numero_aleatorio == escolha_usuario:
                    print("parabéns, você acertou o numero")
                    print("[1] Continuar jogando, [2] Sair do jogo")
                    try:
                        continuacao_programa = int(input("Deseja continuar jogando? "))
                        if continuacao_programa == 1:
                            numero_aleatorio = random.randint(1, 100)

                        elif continuacao_programa == 2:
                            print("")
                            print("obrigado por ter jogado usuário, beijos")
                            break

                        elif continuacao_programa != 1 and continuacao_programa != 2:
                            print("Entrada errada, digite novamente")
                    except ValueError:
                        print("Entrada errada, digite novamente")
        except ValueError:
            print('Entrada errada, digite novamente')
        except TypeError:
            print("Entrada errada, digite novamente")
else:
    print("sair do jogo, ficamos pra próxima")


