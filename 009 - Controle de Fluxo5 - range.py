numeros = list(range(30))

for numero in numeros:
    print(numero)

print(numeros)

numeros_teste = list(range(2,5))
print(numeros_teste)

print(list(range(0,101,10)))

palavras = 'DEFIN SUAFI GEXPTO'

for letra in palavras:
    print(letra, end="*")

print("")
nomes = "Dante Gomes Dantas de Menezes".split()

for nome in nomes:
    print(nome)

palavrax = 'varias palavras numa mesma frAse grande'
vogais = 'AEIOUaeiou'

for letra in palavrax:
    if letra in vogais:
        print(f"{letra} é uma vogal")
    elif letra == " ":
        print("Apenas um espaço")
    else:
        print(f"{letra} é uma consoante")

