from datetime import date

data_atual = date.today().year

nome = input("Digite o nome do usuário: ")
senha = input("Digite sua senha")

if senha == "secreta":
    ano_nasc = int(input("Digite o ano que você nasceu: "))
    idade = data_atual - ano_nasc
    print(f"Você tem ou vai fazer {idade} anos")
else:
    print("Sua senha está errada")