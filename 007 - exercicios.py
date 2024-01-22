# 1. Por que a expressão a seguir causa um erro? Como você pode corrigi-la?
# 'Eu tenho que comer' + 99 + 'hamburguers' R: Por conta da tipagem forte do python
# 2. Por que eggs é um nome válido de variável enquanto 100 é inválido? O python não permite numero como variável, nem que comece com numero
# 3. Quais três funções podem ser usadas para obter de um valor uma versão inteira, de ponto
# flutuante ou string? int(), float(), str()

a = "Dante"
b = "Menezes"

c = a+b

print(c)

lista = ['a','b', 'c']

print(lista, id(lista))

lista.pop()
print(lista, id(lista))

lista[1] = 'z'
print(lista, id(lista))

palavra = "Caderno"

print(palavra, palavra[2])

print(palavra, palavra[2])