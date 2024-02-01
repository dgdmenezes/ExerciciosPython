# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo .
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
num3 = float(input("Digite um numero float: "))

calcA = 2*num1 *(num2/2)
calcB = (3*num1) + num3
calcC = num3**3

print(f"o produto do dobro do primeiro com metade do segundo é {calcA} .")
print(f"# b - a soma do triplo do primeiro com o terceiro é {calcB}")
print(f"# c - o terceiro elevado ao cubo é {calcC}")
