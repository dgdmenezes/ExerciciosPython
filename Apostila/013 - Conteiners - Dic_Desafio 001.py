# Dada uma lista de entradas de usuário de números inteiros, construa um dicionário com uma
# lista dos valores digitados, uma lista dos valores elevados ao quadrado e uma lista dos valores
# elevados ao cubo.
# Fala um número aí: 1
# Fala um número aí: 2
# Fala um número aí: 3
# Fala um número aí: 4
# Fala um número aí: 5
# Fala um número aí: 6
# Fala um número aí: 7
# Fala um número aí: 8
# Fala um número aí: 9
# Fala um número aí: 10
# {'lista padrão': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'lista quadrada': [1, 4, 9, 16, 25, 36, 49,

listaPadrao = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaQuadrada = []
listaCubica = []

for numero in listaPadrao:
      listaQuadrada.append(numero**2)
      listaCubica.append(numero**3)

# print(listaQuadrada)
# print(listaCubica)

dicionarioListas = {}
dicionarioListas["lista padrão"] = listaPadrao
dicionarioListas["lista quadrada"] = listaQuadrada
dicionarioListas["lista cubica"] = listaQuadrada

for lista in dicionarioListas:
      print(lista)

print(dicionarioListas.keys())

for lista in dicionarioListas:
      print(f"{lista} - {dicionarioListas[lista]}")

print(dicionarioListas.values())

# dicionarioListas.pop("lista padrão")

if "lista padrão" in dicionarioListas:
      print("existe")
else:
      print("Non ecsiste")



for lista in dicionarioListas:
      print(f"{lista} - {dicionarioListas[lista]}")