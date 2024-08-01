#Programa
resistencia = ""
tensao = ""
resistencia_do_resistor = ""
corrente_eletrica = ""

while True:
    print("Calcule rapidamente e com precisão a resistência, a tensão ou a corrente elétrica.")

    print("MENU DOS FATORES")
    print(f"[1] Resistencia\n [2] Tensão\n [3] Resistencia do Resistor\n [4] Correnete elétrica\n")
    menu = int(input("escolha seu cálculo:"))

    if menu == 1:
        print("descobrir o valor da resistencia")
        loop = True
        while loop:
            tensao = float(input("digite o valor da tensão elétrica em volts:"))
            corrente_eletrica = float(input("digite o valor da corrente elétrica em amperes:"))
            loop = tensao <= 0 or corrente_eletrica <= 0
            if loop:
                print("opção inválida, nem a tensão e a correnete elétrica podem ser negativas ou 0")
            else:
                resistencia = tensao / corrente_eletrica
                print(f"resistencia = {resistencia}.")
                loop = False

    if menu == 2:
        print("descobrir o valor da tensão")
        loop = True
        while loop:
            corrente_eletrica = float(input(" descobir o valor da corrente elétrica em amperes"))
            resistencia = float(input("digite o valor da resistencia elétrica em ohms"))
            loop = corrente_eletrica <= 0 or resistencia <= 0
            if loop:
                print("opção inválida, nem a corrente elétrica e a resistencia podem ser negativas ou 0")
            else:
                tensao = resistencia * corrente_eletrica
                print(f"tensão = {tensao}.")
                loop = False


    if menu == 3:
        print("descobrir o valor da resistencia do resistor")
        loop = True
        while loop:
            tensao_da_fonte = float(input("digite o valor da tensão da fonte"))
            corrente_led = float(input("digite o valor da corrente led"))
            tensao_led = float(input("digite o valor da tensão led"))
            loop = tensao_da_fonte <= 0 or corrente_led <= 0 or tensao_da_fonte <=0
            if loop:
                print("opção inválida, nem a corrente led, tensão led e tensão da fonte podem ser negativas ou 0")
            else:
                resistencia = (tensao_da_fonte - tensao_led) / corrente_led
                print(f"resistencia do resistor = {resistencia}.")
                loop = False

    if menu == 4:
         print("descobrir o valor da corrente elétrica em amperes")
         loop = True
         while loop:
            tensao = float(input("digite o valor da tensão elétrica em volts:"))
            resistencia = float(input("digite o valor da resistencia em ohms:"))
            loop = tensao <= 0 or resistencia <= 0
            if loop:
                print("opção inválida, nem a resistencia e a tensão podem ser negativas ou 0")
            else:
                corrente_eletrica = tensao / resistencia
                print(f"corrente eletrica = {corrente_eletrica}.")
                loop = False
