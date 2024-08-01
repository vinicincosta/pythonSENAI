
Kelvin = 0
fahrenheit = 0
kelvin_resultado = 0



def solicte_temperatura ():
    while True:
        try:
            celsius = float(input('Informe a temperatura em graus Celsius: '))
            return celsius
        except ValueError:
            print('Informe um valor valido')


def calcula_kelvin(celsius):
    conta_kelvin = celsius + 273.15
    return conta_kelvin


def Fahrenheit(celsius):
    conta_fahrenheit = celsius * 1.8 + 32
    fahrenheit_resultado = conta_fahrenheit
    return fahrenheit_resultado




celsius = solicte_temperatura()
print('')
print("A temperatura convertida em Kelvin é", calcula_kelvin(celsius))
print('')
print("A temperatura convertida em fahrenheit é", Fahrenheit(celsius))