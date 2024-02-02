# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

AreaPintada = float(input("Digite a quantidade de pintura em m²: "))

litrosUtilizados = AreaPintada/3

latasUtilizadas = (litrosUtilizados//18)+1

print(f"Para {AreaPintada} m² utiliza-se {litrosUtilizados} litros e se precisa de {latasUtilizadas} galoes de 18L")

