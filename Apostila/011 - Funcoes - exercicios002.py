# 3. Escreva uma função chamada ajustar, que receba uma string chamada s como parâmetro
# e exiba a string com espaços suficientes à frente para que a última letra da string esteja na
# coluna 70 da tela:
# Dica: Use concatenação de strings. Além disso, o Python oferece uma função integrada
# chamada len, que apresenta o comprimento de uma string, então o valor de
# len(‘ciencia’) é 7.
# 4. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem
# e valor_produto, que é o valor do produto antes do imposto.

def ajustar(s):
    posicao = len(s)
    print(" "*(70-posicao), s)

ajustar("Joao")

def somaImposto(taxaImposto, valor_produto):
    produtoAposImposto = (valor_produto*taxaImposto*0.01) + valor_produto
    return produtoAposImposto

print(somaImposto(10, 130))
#86
