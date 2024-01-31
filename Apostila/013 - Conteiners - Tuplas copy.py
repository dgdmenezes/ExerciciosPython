#Porém a principal característica que diferencia as tuplas das listas é que as tuplas, assim
#como as strings, são imutáveis. As tuplas não podem ter seus valores modificados,
#adicionados ou removidos.

tupla = ("a", "b", "c")
lista = ["a", "b", "c"]

moedas = "Real", "Dolar", "Euro"

tupla
lista.pop()

print(tupla)
print(lista)
print(type(moedas))

minha_tupla = ("Dante", 38, "Camamu")
nome, idade, cidade = minha_tupla

print(f"{nome}, mora na cidade {cidade} e tem {idade} anos")

resposta = [0,1,2,3,4,5]
universo = resposta
universo[1] = "opa"

print(f"{resposta}, {universo}")

from copy import copy

lista_resposta = [0,1,2,3,4,5]

lista_universo = copy(lista_resposta)

lista_universo[1] = "Ahaha"

print(f"{lista_resposta} {lista_universo}")