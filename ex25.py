produto = input("digite o nome do produto: ")
preco = float(input("digite o preço do produto: R$ "))
quantidade = int(input("digite a  quantidade: "))
total = preco * quantidade

if total > 50:
    desconto = total * 0.10
    total_final = total - desconto
    print("desconto aplicado: 10%")
else:
    total_final = total
    print("sem desconto")

print(f"produto: R$ {total_final:.2f}")
print(f"total a pagar: R$ {total_final:.2f}")
