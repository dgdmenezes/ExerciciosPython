# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# (32 °F − 32) × 5/9 = 0 °C

F = float(input("Digite a temperatura em Farenheit"))

C = (F-32)* 5/9

print(f"{F} Farenheit equivale a {C} Celsius")
