# Dica: para pegar o segundo elemento de uma lista devemos chamar lista[1]
# 3. Faça um programa que diga ‘Olá Mundo’, pergunte seu nome, te comprimente usando seu
# nome, diga o tamanho do seu nome, pergunte sua idade e diga quantos anos você vai fazer,
# conforme exemplo abaixo:
# Olá Mundo!
# Qual é o seu nome?
# **Evandro**
# Bom te conhecer Evandro
# O tamanho do seu nome é:
# 7
# Quantos anos você tem?
# **46**
# Você vai fazer 47 anos.
# 37
print("Olá Mundo!")
nome = input("Qual o seu nome?")

print(f"Bom te conhecer {nome}")
print(f"O tamanho do seu nome é: {len(nome)}")

from datetime import date

anoAtual = date.today().year

anoNascimento = int(input("Qual ano você nasceu?"))

print(f"Você tem ou vai fazer {anoAtual-anoNascimento}")