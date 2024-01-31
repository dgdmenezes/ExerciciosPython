# 2. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome
# do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre-se que ao
# informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

# nome = input("Digite seu nome: \n")
# nome = nome.upper()


# print(nome)

# for x in range(len(nome), 0, -1):
#     print(nome[x-1])


# 3. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima
# a data com o nome do mês por extenso.
# Entrada: 27/11/1975
# Saída: 27 de Novembro de 1975

entrada = "27/11/1975"
print(entrada[:2], end=" ")
opcao = entrada[3:5]

match opcao:
    case "01":
        print("janeiro")
    case "02":
        print("fevereiro")
    case "03":
        print("março")
    case "04":
        print("abril")
    case "05":
        print("maio")
    case "06":
        print("junho")
    case "07":
        print("julho")
    case "08":
        print("agosto")
    case "09":
        print("setembro")
    case "10":
        print("outubro")
    case "11":
        print("novembro")
    case "12":
        print("dezembro")


print(entrada[6:])

