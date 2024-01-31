# 2. Faça um programa que receba uma string, com um número de ponto flutuante, e imprima a
# parte decimal
# n = '3.14'
# resposta: 14
number = float(input("Digite um numero fracionado (ex.: 3,14)"))
inteiro = number//1
resposta = number - inteiro

lista = str(number).split(".")
print(f"A resposta é {resposta}")
print(f"A resposta 2 é {lista[1]}")
