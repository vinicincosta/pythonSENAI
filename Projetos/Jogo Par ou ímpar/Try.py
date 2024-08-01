# O while repete tudo que está dentro dele
while True:
    # O try vai tentar executar esse bloco de código
    try:
        idade = int(input('Digite sua idade: '))
        #if verifica se a idade é valida, if = se
        if idade >0 and idade <100:
            print(f"idade {idade}")
            #break sai do while
            break
        else:
            print("idade invalida")
    except ValueError:
        # Caso der erro executa aqui

        print("digite sua idade em numeros. exemplos: 16")
