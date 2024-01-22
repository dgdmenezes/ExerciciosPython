nome = "Dom Pedro II"

print(f"Meu nome é {nome}")

print("Meu nome é ",nome)

print("Meu nome é " + nome)

print("Meu nome é {}" .format(nome))

horacio = """Carpie diem,
quam minimum
credula postero"""

print(type(horacio))

print('Eu sei um "pouco" de pogramação - Seu Creysson')

print("concatenar" + "strings")

a = 42
a = str(a)

print(type(a), a)

print("alice"*5)

sentencao = "quantas letras tem nessa sentença"
print(sentencao, len(sentencao))

print(sentencao.replace('e', 'a'))
print(sentencao.capitalize())


palavra = "Dante"

print(palavra[0])
print(palavra.index("D"))

sentencaoSplitada = sentencao.split(" ")

print(sentencaoSplitada, len(sentencaoSplitada))

print("quantos" in sentencao)

msg = "Athur foi fazer um show de Blues"
if "show" in msg:
    print("Teve Show")
else:
    print("Dont have show mothefucker")
    