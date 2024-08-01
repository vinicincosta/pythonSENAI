from datetime import datetime

def menu_calculadora():
    print("calculdora")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisao")


#Exibe o menu da calculadora
menu_calculadora()

print("")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


#Exemplos:

def ola_nome(nome):
    print(f"Ola {nome}")


#Exibe o print com "Olá lucas"
ola_nome("lucas")
print('*****************************************************************')
print("")

#Exercicios (calcular idade)
def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade




def solicite_ano_nascimento():
    while True:
        try:
            nascimento = int(input(" Digite seu ano de nascimento: "))
            if nascimento > datetime.now().year:
                print("opção inválida, digite novamente")
            else:
                return nascimento
        except ValueError:
            print("Digite um valor valido, EX: 2008")



ano_nascimento = solicite_ano_nascimento()
print("sua idade é", calcular_idade(ano_nascimento))
