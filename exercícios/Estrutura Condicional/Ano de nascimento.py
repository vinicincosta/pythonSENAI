# SOLICITE O ANO DE NASCIMENTO
print("ANO DE NASCIMENTO")
print('')

nascimento = 0
calcule_idade = 2024 - nascimento


def solicite_nascimento():
    while True:
        try:
            nascimento = int(input('Digite seu ano de nascimento: '))
            if nascimento > 1900 and nascimento < 2025:
                return nascimento
            else:
                print("Valor inválido, tente novamente")

        except ValueError:
            print("Valor inválido, tente novamente")


def exiba_idade(solicite_nascimento):
    calcula_idade = 2024 - nascimento
    print("essa pessoa tem", calcula_idade, "anos")


def conta_nascimento():
    while True:
        if calcule_idade > 18:
            print("Você é maior de idade")
        elif calcule_idade < 18:
            print("Você é menor de idade")
        break


solicite_nascimento()
exiba_idade(solicite_nascimento)
conta_nascimento()
