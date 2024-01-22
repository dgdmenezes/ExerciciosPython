#LISTAS
bichos = ["gatos", "rato", "elefante", "cachorro"]

print(type(bichos))
print(len(bichos))

print(bichos)

bichos.pop()

print(bichos)


numeros = [1,3,5,6]

numeros.reverse()

print(numeros)

listaDeCompras = ["Sabao", "sabonete", "arroz", "Feijuca", 123, 4.5, bichos, numeros]

print(listaDeCompras)

print(listaDeCompras[6])
print(listaDeCompras[6][-3])

inteiros = [0,1,2,3,4,5,6,7,8,9]
print(inteiros)
inteiros[3:6]
print(inteiros[3:6])
print(inteiros[2:])
print(inteiros[:2])

print(bichos)
bichos[-1] = "zebra" #substituiu o numero elemento
print(bichos)
del bichos[1] #Remove o elemento na posição 1
print(bichos)

listaNova = bichos + numeros


print(listaNova)

materiais = ['canetas', 'cadernos', 'livros', 'réguas', 'borracha', 'giz']

for i in range(len(materiais)):
    print(f"Item = {i} - {materiais[i]} ")


gato = [20, "Branca", "tom"]
tamanho, cor, nome = gato

print(tamanho)
print(cor)
print(nome)

print(materiais)

materiais.append("hidrocor")
print(materiais, len(materiais))

materiais.insert(0,"estilete")
print(materiais, len(materiais))
