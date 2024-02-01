# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
# (72.7*altura) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura em metros: "))

sexo = "d"

while sexo not in ("M", "H"):
    sexo = input("Qual o seu sexo? Responda M - mulher ou H - homem: ")
    print(f"Sexo = {sexo}")
    
if sexo == "H":
       pesoIdeal = (72.7*altura) - 58
else:
       pesoIdeal = (62.1*altura) - 44.7

print(f"Você é {sexo} e Seu peso ideal é {pesoIdeal}")
