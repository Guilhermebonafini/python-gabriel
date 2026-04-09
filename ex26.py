print("1 - hamburguer - R$ 15.00")
print("2 - pizza - R$ 20.00")
print("3- refrigerante - R$ 8.00")

opcao = int(input("escolha uma opção"))

if opcao == 1:
    print("você escolheu hamburguer")
    print("valor: R$ 15.00")
elif opcao == 2:
    print("você escolheu pizza")
    print("valor: R$ 20.00")
elif opcao == 3:
    print("vocẽ escolheu refrigerante")
    print("valor: R$ 8.00")
else:
    print("opção invalída")