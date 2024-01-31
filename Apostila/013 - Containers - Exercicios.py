# 1. Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número inteiro,
# imprima a tabuada desse número.
listaTabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiplicador = int(input("Digite um numero inteiro para tabuada"))

for numero in listaTabuada:
    resultado = multiplicador * numero
    print(f"{numero} x {multiplicador} = {resultado}")