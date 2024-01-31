# 1. Faça um Programa que peça dois números e imprima o maior deles.
num1 = float(input("Digite um numero"))
num2 = float(input("Digite outro numero"))
if num1 > num2:
    print(f"O primeiro numero {num1} é maior que o segundo numero {num2}")
elif num2 > num1:
    print(f"O segundo numero {num2} é maior que o primeiro numero {num1}")
else:
    print("Os numeros são iguais")

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = float(input("Digite um numero: "))
if numero > 0:
    print("O numero é positivo")
elif numero < 0:
    print("O numero é negativo")
else:
    print("numero zero")

# 3. Faça um Programa que verifique se uma letra digitada é “F” ou “M”. Conforme a letra digitada
# escreva: F - Feminino, M - Masculino, Sexo Inválido (Caso não for F ou M).
sexo = input("Digite F ou M")
if sexo.upper() == "M":
    print("Sexo Masculino")
elif sexo.upper() == "F":
    print("Sexo Feminino")
else:
    print("Sexo invalido")

# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra")
letra_maiuscula = letra.upper()
if letra_maiuscula == ("A" or "B" or "C" or "D" or "E"):
    print("É uma vogal")
else:
    print("É uma consoante")
# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
# calcular a média alcançada por aluno e apresentar:
# • A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
# • A mensagem “Reprovado”, se a média for menor do que sete;
# • A mensagem “Aprovado com Distinção”, se a média for igual a dez.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media == 10:
    print(f"Sua nota foi {media}. Parabéns você foi aprovado com distinção")
elif (media<10 and media>=7):
    print(f"Parabens você foi aprovado com a média {media}")
else:
    print(f"Infelizmente você foi reprovado com a nota {media}. Tente da proxima vez")