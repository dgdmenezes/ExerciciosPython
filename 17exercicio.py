# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# * comprar apenas latas de 18 litros;
# * comprar apenas galões de 3,6 litros;
# * misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#  Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

AreaPintada = float(input("Digite a quantidade de pintura em m²: "))

litrosUtilizados = (AreaPintada/3)*1.1

latasUtilizadas = (litrosUtilizados//18)+1
galoesUtilizadas = (litrosUtilizados//3.6)+1


print(f"Para {AreaPintada} m² utiliza-se {litrosUtilizados} litros (com margem de segurança de 10% a maos)")
print(f"e se precisa de {latasUtilizadas} latoes de 18L ou {galoesUtilizadas} galões de 3,6L")

if litrosUtilizados<=18:
    
    print(f"Para {AreaPintada} m² utiliza-se {litrosUtilizados} litros (com margem de segurança de 10% a maos)")
    print(f"e se precisa de {galoesUtilizadas} galões de 3,6L")
else:
    galoesRestantes = ((litrosUtilizados%18)//3.6)+1
    print(f"Para {AreaPintada} m² utiliza-se {litrosUtilizados} litros (com margem de segurança de 10% a maos)")
    print(f"precisa de {litrosUtilizados//18} latas de 18L mais {galoesRestantes} galoes de 3,6L")
