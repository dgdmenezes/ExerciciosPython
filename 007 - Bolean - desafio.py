# Desafio: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa
# que nos dê:
# • salário bruto.
# • quanto pagou ao INSS.
# • quanto pagou ao sindicato.
# • o salário líquido.
# • calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# 52
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

preco_hora = float(input("Quanto você ganha por hora?"))
horas_trabalhadas = int(input("Quantas horas você trabalha por mês?"))

salario_bruto = preco_hora * horas_trabalhadas

print("Salario Bruto :", salario_bruto)
print("Desconto Imposto de Renda (11%):", salario_bruto*0.11)
print("Desconto INSS (8%):", salario_bruto*0.08)
print("Desconto Sindicato (5%):", salario_bruto*0.05)

print("Salario Liquido :", (salario_bruto - ((salario_bruto*0.11) + (salario_bruto*0.05) + (salario_bruto*0.08))))




