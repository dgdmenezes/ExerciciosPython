# 1. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou
# diferentes no conteúdo.
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
String1= "Brasil Hexa 2006"
String2= "Brasil! Hexa 2006!"
# String2= "Brasil! Hexa 2006!"

print(len(String1))
print(len(String2))

if (len(String1) == len(String2)):
    print("As strings são de mesmo tamanho")
else:
    print("as Strings são de tamanhos diferentes")

if (String1 == String2):
    print("As strings são de mesmo conteude")
else:
    print("as Strings são de conteudo diferentes")