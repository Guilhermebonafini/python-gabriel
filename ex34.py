contador = 0

while true:
    numero = int(input("digite um numero (0 para sair): "))

    if numero == 0:
        break

    contador = contador + 1

print("quantidade:", contador)
