# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valorHoraTrabalhada = float(input("Quanto você ganha por hora trabalhada?  "))
qtdHoraTrabalhada = int(input("Quantas horas você trabalha por mês?  "))

ganhoMensal = valorHoraTrabalhada * qtdHoraTrabalhada

print(f"Voce ganha por mês: {ganhoMensal}")


