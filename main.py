import os

print("///// * MENU * /////\n")
print("1 - Nova Venda")
print("2 - Gerar Relatório")
print("3 - Sobre")
print("4 - Sair")
print("\n")
opcao = (input("Digite a opção desejada: "))
os.system('clear')
print("\n")
if (opcao == "1"):
  print("Nova Venda")
  sal_qtd = int(input("Digite a quantidade de pão de sal "))
  leite_qtd = int(input("Digite a quantidade de pão de leite"))
  milho_qtd = int(input("Digite a quantidade de pão de milho "))
  total = sal_qtd + leite_qtd + milho_qtd
  print("Total de pães " ,str(total))
elif (opcao == "2"):
  print("Gerar Relatório")
elif (opcao == "3"):
  print("Sobre")
elif (opcao == "4"):
  print("Sair")
else:
  print("Opção inválida. Tente Novamente")
