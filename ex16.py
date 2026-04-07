idade = int(input("idade"))
carteira = input("tem carteira? (sim/não): ")

if idade >= 18 and carteira == "sim":
    print("pode dirigir")
    else:
        print("não pode dirigir")