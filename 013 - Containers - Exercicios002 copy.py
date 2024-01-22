
# 2. Faça um programa que dada a entrada de uma lista, ele faça o cálculo acumulativo da mesma:
# Exemplo:
# Entrada: [1, 2, 3, 4]
# Saída: [1, 3, 6, 10]
listaEx2 = [1, 2, 3, 4]

print(len(listaEx2))
listaResultado = []
listaResultado.append(listaEx2[0])
acumulador = 0

for i in range(len(listaEx2)-1):
    acumulador = listaEx2[i]+listaEx2[i+1]
    print(f"ar1: [{listaEx2[i]}] + ar2: [{listaEx2[i+1]}]")
    listaResultado.append(acumulador)

print(listaResultado)