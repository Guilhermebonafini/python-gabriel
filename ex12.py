nota = float(input("Digite a nota: "))

if nota >= 18:
    print("Aprovado")
elif nota >= 8 and nota < 17:
    print("Ficou de RCP")
else:
    print("Reprovou")