# • Listas e tuplas tem posições
# • Conjuntos e Dicionários: seus elementos não tem posições
# • Conjuntos armazena itens não duplicados
# • O acesso do elementos no conjunto é mais rápido que em listas
# • Os itens de um conjunto são não ordenados
# • Conjuntos tem suporte à operações matemáticas (União, Intersecção e diferença).
listas = [1,2,3]
tuplas = (1,2,3)
conjuntos_a = {1,2,3,4}
conjuntos_b = {3,4,5,6}

conjuntos_c = conjuntos_a.union(conjuntos_b)
conjuntos_d = conjuntos_a.intersection(conjuntos_b)
conjuntos_e = conjuntos_a.difference(conjuntos_b)
conjuntos_f = conjuntos_b.difference(conjuntos_a)
conjuntos_g = conjuntos_e.union(conjuntos_f)
conjuntos_ab = {1,2,3,4}
conjuntos_bb = {3,4,5,6}

conjuntos_ab.union(conjuntos_bb)
conjuntos_ab.update(conjuntos_bb)


print(conjuntos_c)
print(conjuntos_d)
print(conjuntos_e)
print(conjuntos_f)
print(conjuntos_g)

print(conjuntos_ab)
conjuntos_ab.discard(6)
print(conjuntos_ab)
conjuntos_ab.pop()
print(conjuntos_ab)

lista = [1, 1, 1, 2, 2, 5, 6, 3, 9, 8, 4, 2]

conjunto = set(lista)
tupla = tuple(lista)

print(lista)
print(conjunto)
print(tupla)