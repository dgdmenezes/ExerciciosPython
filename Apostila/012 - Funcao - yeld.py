def menu():
    yield("Salada")
    yield("Pizza")
    yield("Sobremesa")

print(menu())

itens = menu()

print(next(itens))
print(next(itens))
print(next(itens))
