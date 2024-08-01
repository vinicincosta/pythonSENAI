#PESO_ALTURA
def peso():
    while True:
        try:
            peso = float(input("Digite o peso em kg:"))
            return peso
        except ValueError:
            print("Valor inválida, tente novamente.")

def altura():
    while True:
        try:
            altura = float(input("Digite a altura em metros:"))
            return altura
        except ValueError:
            print("Valor inválida, tente novamente.")


def calcula(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def imc_classificacao(imc):
    classificacao = ""

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso Normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc <40:
        classificacao = "Obesidade"
    else:
        classificacao = "Obesidade Morbida"
    return classificacao
peso = peso()
altura = altura()
imc = calcula(peso, altura)
classificacao = imc_classificacao(imc)
print(f'uma pessoa com {altura}m de altura e pesando {peso}Kg é classificado como {classificacao}')


