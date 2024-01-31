# 1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
#   R: Python retorna erro de sintaxe

# 2. Se estiver tentando imprimir um texto, o que acontece se omitir uma das aspas ou ambas?
#   R: Python retorna erro de sintaxe

# 3. A função print sempre pula uma linha ao final da impressão. Descubra na internet como
# usar o print de forma que ele nao mude de linha no final
print("esse print", end=" ")
print("não pula linha", end=" ")

# 4. Faça um Programa que mostre a mensagem “Alo mundo!!!” na tela.
print("Alo mundo!!!")

# 5. Escreva um programa que lê o nome e idade e escreve na tela a frase abaixo(pesquisar na
# internet):
# Bem vindo <nome> fico feliz em saber que tem <idade> anos.

nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))

print(f"Bem vindo {nome} fico feliz em saber que tem {idade} anos.")
