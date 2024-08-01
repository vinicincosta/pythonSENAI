def menu_calculadora():
    print("Menu principal")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")

def solicite_numero_A():
    while True:
        try:
            numero = float(input("Digite um numero: "))
            return numero
        except ValueError:
            print("Opção inválida. Tente novamente.")


numero1 = solicite_numero_A()
numero2 = solicite_numero_A()

def soma(numero1, numero2):
    resultado_soma = numero1 + numero2
    return resultado_soma

def subtracao(numero1, numero2):
    resultado_subtracao = numero1 - numero2
    return resultado_subtracao

def multiplicacao(numero1, numero2):
    resultado_multiplicacao = numero1 * numero2
    return resultado_multiplicacao

def divisao(numero1, numero2):
    resultado_divisao = numero1 / numero2
    return resultado_divisao

def escolha_operacao():
    menu_calculadora()
    while True:
        try:
            opcao = int(input("Escolha sua operação:"))
            return opcao
        except ValueError:
            print("Opção Inválida. Tente novamente.")

opcao = escolha_operacao()
soma = soma(numero1, numero2)
subtracao = subtracao(numero1, numero2)
multiplicacao = multiplicacao(numero1, numero2)
divisao = divisao(numero1, numero2)

if opcao == 1:
    print("O resultado é", soma)
elif opcao == 2:
    print("O resultado é",subtracao)
elif opcao == 3:
    print("O resultado é",divisao)
else:
    print("O resultado é",multiplicacao)



