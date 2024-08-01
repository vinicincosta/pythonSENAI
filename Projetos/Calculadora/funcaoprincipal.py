from funcaocalculadora import *

opcao = solicite_escolha()
while True:
    if opcao == 1:
        descubra_resistencia()
    elif opcao == 0:
        sair(opcao)
        break
    elif opcao == 2:
        descubra_tensao()
    elif opcao == 3:
        descubra_resistencia_resistor()
    elif opcao == 4:
        descubra_corrente()
    opcao = solicite_escolha()

