import os
import time

## VARIÁVEIS GLOBAIS (Disponível para acesso em todo o código)##
# Valor por unidade dos Pães
PAO_SAL = 0.25
PAO_MILHO = 0.15
PAO_LEITE = 0.35

quantidade_vendas = 0
# valor total de cada tipo vendido
sal_qtd = 0
milho_qtd = 0
leite_qtd = 0
## --------------------------------------- ##

## MINHAS FUNÇÕES ##

def novaVenda():#minha função
  os.system('clear') #limpa a tela
  print(" +++++++ Nova venda ++++++ \n")
    # variáveis locais
  sal = int(input("Digite a quantidade Pães de Sal: "))
  leite = int(input("Digite a quantidade Pães de Leite: "))
  milho = int(input("Digite a quantidade Pães de Milho: "))

    # Quantidade total
  total_unidade = sal + leite + milho

    #Valor total
  valor_total = sal*PAO_SAL + leite*PAO_LEITE + milho*PAO_MILHO

  print("\nTotal de pães: %.0f" % total_unidade)
  print("Valor total R$ %.2f" % valor_total)

    # A cada venda o valor dessa variável é incrementada em 1
  global quantidade_vendas, sal_qtd, milho_qtd, leite_qtd
  quantidade_vendas = quantidade_vendas + 1
  sal_qtd = sal_qtd + sal
  milho_qtd = milho_qtd + milho
  leite_qtd = leite_qtd + leite

  input("\n\nPressione ENTER para continuar: ")
  os.system('clear') #limpa a tela

def relatorio():
  os.system('clear') #limpa a tela
  print(" *** Relatório do Dia *** ")
  print("\n")
  print("Quantidade de vendas do dia: ", quantidade_vendas)
  print("\nQuantidade por tipo de pão:")
  print("\t+ Sal: %.0f unidades = R$ %.2f" % (sal_qtd,sal_qtd*PAO_SAL))
  print("\t+ Leite: %.0f unidades = R$ %.2f" % (leite_qtd, leite_qtd*PAO_LEITE))
  print("\t+ Milho: %.0f unidades = R$ %.2f" % (milho_qtd,milho_qtd*PAO_MILHO))

  #print("\nMais vendidos: ")

  v_total = sal_qtd*PAO_SAL + leite_qtd*PAO_LEITE + milho_qtd*PAO_MILHO

  print("\nValor total do dia: R$ %.2f" % v_total)

  q_total = sal_qtd + leite_qtd + milho_qtd
  print("Quantidade total de pães: %.0f unidades" % q_total)

  input("\n\nPressione ENTER para continuar: ")
  os.system('clear') #limpa a tela

def sobre():
  os.system('clear')
  print("\t\t Sobre o Programa ")
  print("\n\t **** Versão 0.1 - 2021 **** \n")
  print("Colaborador: Adaias dos Reis")
  print("GitHub: github.com/adaiasreis")
  print("Contato: adaias046064@aluno.ba.senac.br")
  print("\n\t\t --> DONATE <--")
  time.sleep(12)
  os.system('clear')

def sair():
  os.system('clear')
  print("\nPrograma finalizado, obrigado pela preferência!")
  time.sleep(5)
######## MENU #########
while(True): # loop infinito  
  # Imprime na tela o menu
  print(" ///// *** PANIFICADORA PÃO DURO *** ///// \n")
  print("Quantidade de vendas realizadas hoje: ",quantidade_vendas)

  print("\n1 - Nova Venda")
  print("2 - Gerar relatório")
  print("3 - Sobre")
  print("4 - Sair")
  # Pegar a opção do usuário
  opcao = input("\nDigite a opção desejada: ")

  # Verificar qual opção o usuário escolheu
  if (opcao == "1"): # NOVA VENDA 
    novaVenda() # Chamar uma função
  elif(opcao == "2"): #senao se
    relatorio()
  elif(opcao == "3"):
    print("Sobre")
    sobre()
  elif(opcao == "4"):
    sair()
    break #interrompe a executação do laço
  else:
    print("Opção inválida, tente novamente!")
    os.system('clear')  
print("Sistema Desligado")