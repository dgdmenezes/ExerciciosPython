def multiplicacao(x,y,z):
    resultado = x * y * z
    return resultado

print(multiplicacao(2,5,6))

def soma(x, y):
    resultado = x + y
    return resultado

print(soma(1025,2365))

def ola_mundo():
    return "olá mundo"

print(ola_mundo())

def calcular_pagamento(qtd_horas, valor_hora):
    horas=float(qtd_horas)
    taxa = float(valor_hora)
    if horas <=0:
        salario = horas * taxa
    else:
        h_excd = horas -40
        salario = 40*taxa + (h_excd*(1.6*taxa))
    return salario

print(calcular_pagamento(50, 100))

def media(lista):
    soma = sum(lista)
    qtd = len(lista)
    media = soma / qtd
    return media

A = [1,3,6,8]
print(sum(A))
print(len(A))

print(media(A))

print("o", "na","na","o","na","na","e","a", sep="-")

import random

numero_secreto = random.randint(1,61)

for i in range(1,11):
    palpite = int(input("Tente acertar: "))
    if palpite > numero_secreto:
        print("Seu palpite foi muito alto!")
    elif palpite < numero_secreto:
        print("Seu palpite foi baixo")
    else:
        break

if palpite == numero_secreto:
    print (f"Parabens voce venceu apos {i} tentativas")
else:
    print(f"Você perdeu! o número que pensei foi {numero_secreto}")