# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

salarioBruto = float(input("Digite o seu salário Bruto: "))

descontoIRPF = salarioBruto*0.11
descontoINSS = salarioBruto*0.08
descontoSindicato = salarioBruto*0.05

salarioLiquido = salarioBruto -descontoIRPF -descontoINSS -descontoSindicato

print(f"{salarioBruto} desconto IRPF {descontoIRPF} + desconto INSS {descontoINSS} + desconto do Sindicato {descontoSindicato} gera um salario líquido de {salarioLiquido}")

