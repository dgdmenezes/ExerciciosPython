frase = "Hello world!"
print(len(frase))

print(frase[0:5])
print(frase[:5])
print(frase[6:])

resultado = "Federal" in "Caixa Economica Federal"

print(resultado)

resultadoB = "Federal" not in "Caixa Economica Federal"

print(resultadoB)

vogais = "aeiou"
numeros = "0123456789"
consoantes = "bcdfghjklmnpqrstvwxyz"

palavra = input("Digite uma palavra: ")
palavra = palavra.lower()

for caracter in palavra:
    if caracter in vogais:
        print(f"{caracter} é uma vogal")
    elif caracter in consoantes:
        print(f"{caracter} é uma consoante")
    elif caracter in numeros:
        print(f"{caracter} é um numero")
    else:
        print(f'{caracter} é um espaço ou caracter especial')
