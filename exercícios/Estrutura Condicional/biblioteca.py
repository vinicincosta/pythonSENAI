from datetime import datetime

print("")
print("BIBLIOTECA DATETIME")
print("")
saudacao = 0
numero_mes = 0

now = datetime.now()
nome = input("Nome: ")
print("Olá, meu nome é {}!".format(nome),
      "fiquei congelado por muito tempo e quero saber tudo sobre em qual época estamos, você poderia me ajudar?")
print("Claro", nome, "aqui está")
print("")
print("Estamos no ano", now.year)

print("")

while True:
    try:
        numero_mes = now.month
        if numero_mes < 1 or numero_mes > 12:
            print("Valor inválido, tente novamente.")
        else:
            break
    except ValueError:
        print("Valor inválido, tente novamente.")


if numero_mes == 1:
    print("Estamos em Janeiro")
elif numero_mes == 2:
    print("Estamos em Fevereiro")
elif numero_mes == 3:
    print("Estamos em Março")
elif numero_mes == 4:
    print("Estamos em Abril")
elif numero_mes == 5:
    print("Estamos em Maio")
elif numero_mes == 6:
    print("Estamos em Junho")
elif numero_mes == 7:
    print("Estamos em Julho")
elif numero_mes == 8:
    print("Estamos em Agosto")
elif numero_mes == 9:
    print("Estamos em Setembro")
elif numero_mes == 10:
    print("Estamos em Outubro")
elif numero_mes == 11:
    print("Estamos em Novembro")
elif numero_mes == 12:
    print("Estamos em Dezembro")

print("Mês", now.month)
print("")

numero = now


if numero.strftime("%w") == "0":
    print("Domingo, amanhã tem que trabalhar 😒")
elif numero.strftime("%w") == "1":
    print("Segunda-feira")
elif numero.strftime("%w") == "2":
    print("Terça-feira")
elif numero.strftime("%w") == "3":
    print("Quarta-feira")
elif numero.strftime("%w") == "4":
    print("Quinta-feira")
elif numero.strftime("%w") == "5":
    print("Sexta-feira, ufa vamo curtir 😁")
elif numero.strftime("%w") == "6":
    print("Sábado, ainda tem mais por hoje 😎")

print("Dia", now.day)
print("")


if now.hour <12 and now.hour>0:
    print("Bom dia")
elif now.hour>12 and now.hour<18:
    print("Boa tarde")
elif now.hour>18 and now.hour<24:
    print("Boa noite")
print("São", now.hour, "horas e", now.minute, "minutos, e por fim", now.second, "segundos")

