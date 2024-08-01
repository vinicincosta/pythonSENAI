from datetime import datetime

def solicite_nome():
    while True:
        try:
            nome = str(input("Digite seu nome: "))
            if nome.isnumeric():
                print("digite em letras")
            else:
                return nome
        except ValueError:
            print("opação inválida")


def horario(horario_atual):
    if horario_atual > 0 and horario_atual <= 6:
        return  "Bom madrugada"
    elif horario_atual > 6 and horario_atual <= 12:
        return "Boa dia"
    elif horario_atual > 12 and horario_atual <= 18:
        return "Boa tarde"
    else:
        return "Boa noite"


print("MENSAGEM AUTOMÁTICA")
print("")

#Pega hora atual da biblioteca (datetime)
horario_atual = datetime.now().hour

#Salva o nome solicitado na variavel
nome = solicite_nome()

print(horario(horario_atual), nome)
