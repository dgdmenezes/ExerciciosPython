# 1. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois
# modifique o programa para que ele mostre os números um ao lado do outro.
for numero in range(20):
    print(numero+1, end=" ")
# 2. Qual é a diferença entre range(10), range(0, 10) e range(0, 10, 1) em um loop for?
#R range(10) pega o intervalo de 0 - 9, range(0,10) faz o mesmo.
#Ranger(0,10,1) faz o mesmo que os anteriores, começa em 0, limite em 10 e incremente de 1 em 1
print("")
# 3. Crie um pequeno programa que mostre os números de 1 a 10 usando um loop for. Em
# seguida, crie um programa equivalente que mostre os números de 1 a 10 usando um loop
# while.
print("Com for in")
for i in range(1,11):
    print(i)

print("Com for while")
limite = 1

while limite !=11:
    print(limite)
    limite+=1

# 4. Faça um programa que itera em uma string e toda vez que uma vogal aparecer na sua string
# imprima a palavra ‘vogal’ entre as letras
    
frase = "Oi cara tudo bem? tudo tranqs?"

for letra in frase:
    print(f"letra: {letra}", end=" ")
    if letra.upper() in ("A","E","I","O","U"):
        print("Sapora é vogal ;/")
    else:
        print("Não vogal")

# função round() arredonda o numero, função abs() transforma o numero em absoluto tipo a stefhany
        
        #77