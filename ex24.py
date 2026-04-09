produto = input("digite o nome do produto: ")
preco = float(input("digite o preço do produto: R$ "))
quantidade = int(input("digite a quantidade: "))

total = preco * quantidade

print(f"produto: {produto}")
print(f"quantidade: {quantidade}")
print(f"total: R$ {total}")