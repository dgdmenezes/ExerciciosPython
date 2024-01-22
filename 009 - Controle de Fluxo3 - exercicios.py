# 1. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")
if (usuario == senha):
    while senha == usuario:
        print("Senha não pode ser igual a usuário")
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")
        if(usuario != senha):
            break
else:
    print("Cadastrado")   

print("Cadastrado")   
    
    

# 2. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.

import random

x = random.randint(0,10)
print(x)

nota = int(input("Digite um numero de 0 a 10"))

while(nota != x):
    nota = int(input("Digite a um numero diferente"))

print("Acertou Miserave")

#66