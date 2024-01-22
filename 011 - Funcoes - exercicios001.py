# 1. Faça um programa, com uma função, que calcule a média de uma lista. Funções nativas que
# pode ajudar:
# • len(lista) -> calcula o tamanho da lista
# • sum(lista) -> faz o somatória dos valores
# Exemplo de entrada: [1, 3, 4, 6, 11]
# Exemplo de saída: Média: 5.0
# 2. Faça um programa, com uma função, que calcula a mediana de uma lista. Funções embutidas
# que podem te ajudar:
# • sorted(lista) -> ordena a lista
# lista2 = [7, 4, 4, 5, 1, 7, 7, 6]
# Mediana: 5.5
# lista3 = [9, 2, 8, 9, 3, 2, 7]
# Mediana: 7

lista = [7, 4, 4, 5, 1, 7, 7, 6]

def media(x):
    soma_total = sum(x)
    total_elementos = len(x)
    media = soma_total/total_elementos
    return media

print(f"A média da lista é: {media(lista)}")

print(len(lista)%2)

def mediana(x):
    sorted_x = sorted(x)
    
    if sum(sorted_x)%2 !=0:
        sorted_x = sorted(x)
        mediana1 = (len(sorted_x)/2)-1
        int_mediana1 = int(mediana1)
        int_mediana2 = int(mediana1+1)
        mediana = (sorted_x[int_mediana1] + sorted_x[int_mediana2])/2
    else:
        mediana1 = (len(sorted_x)/2) - 0.5
        int_mediana = int(mediana1)
        mediana = sorted_x[int_mediana]

    return mediana


lista2 = [7, 4, 4, 5, 1, 7, 7, 6]

lista3 = [9, 2, 8, 9, 3, 2, 7]

print("Lista 2 ordenada: ", sorted(lista2))
print("Mediana lista 2: ", mediana(lista2))

print("Lista 2 ordenada: ", sorted(lista3))
print("Mediana lista 3: ", mediana(lista3))