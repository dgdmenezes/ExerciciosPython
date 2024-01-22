# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene
# os resultados em uma lista. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use
# um iterável que gere números de (1-6) e uma função para gerar numeros aleatórios, simulando os
# lançamentos dos dados.
import random
from collections import Counter

def lanca_dado():
        numero = random.randint(1,6)
        return numero


lista = []

for i in range(100):
        lista.append(lanca_dado())

print(lista)

counter = Counter(lista)

print(counter)