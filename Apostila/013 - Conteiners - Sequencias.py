myDog = {
    "tamanho":"medio",
    "cor":"tricolor",
    "idade": 2.9
}

# De modo diferente das listas, os itens de um dicionários não estão ordenados. Não há um
# “primeiro” item em um dicionário. Enquanto a ordem dos itens é importante para determinar
# se duas listas são iguais, não importa em que ordem os pares chave-valor são digitados em um
# dicionário.

for valor in myDog.values():
    print(valor)

for chave in myDog.keys():
    print(chave)

for item in myDog.items():
    print(item)

for k,v in myDog.items():
    print(f"chave: {k} - valor: {v}")

dados = [
    {
    "nome":"Evadro Avelar",
    "endereço":["Rua dos bobos", 0, "Aguas Claras", "DF"]
    },
    {
    "nome":"Dante",
    "endereço":["Rua dos mais bobos", 1, "Camamum", "BA"]
    }
]
dadosKeys = dados[1].keys()
print(dadosKeys)
#117