# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("Digite a temperatura em Fahrenheit"))

convCelsius = 5 * ((fahrenheit-32)/9)

print(f"{fahrenheit} Farenheit equivale a {convCelsius} em graus Celsius")
