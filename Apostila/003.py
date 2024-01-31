import math

lista = [1,2,5, "palavra"]

palavra = "palavra"

numero = int(input("Digite o numero que vc quer o fatorial: "))

fator = math.factorial(numero)

print(f"O fatorial de {numero} é: {fator}")

print(type(lista), type(numero))

print(type(palavra), len(palavra))
