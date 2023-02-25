'''
6) A prefeitura de Contagem abriu uma linha de crédito para os funcionários estatutários. 
O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. 
Fazer um algoritmo que permita entrar com o salário bruto e o valor da prestação, 
e informar se o empréstimo pode ou não ser concedido.
'''

# Msg pra iniciar o programa para o cliente
print("Por favor, digite seu salário e o valor de crédito desejado \npara verificarmos a disponibilidade: \n")

salario = float(input("Digite seu salário: "))
#print(salario)
print(" ")

emprestimo = float(input("Digite o crédito desejado: \n"))
#print(emprestimo)
print(" ")

if emprestimo <= salario*0.3:
  print(f'O valor de R${emprestimo} foi aprovado para você, Parabéns! \n')
  print("Qualquer dúvida estaremos sempre à disposição! \n")

if emprestimo > salario*0.3:
  print(f'O Valor de R${emprestimo} não está disponível no momento para você. \n')

  outraVerificacao = input("Deseja verificar se há outro valor disponível? : SIM ou NAO? \n")
  print(" ")
  
  if outraVerificacao.lower() == "sim" :
    print("Por favor, digite o valor de crédito desejado \npara verificarmos a disponibilidade? \n")
    print(" ")

    emprestimo = float(input("Digite o crédito desejado: \n"))
    #print(emprestimo)
    print(" ")

    if emprestimo <= salario*0.3:
      print(f'O valor de R${emprestimo} foi aprovado para você, Parabéns! \n')
      print("Qualquer dúvida estaremos sempre à disposição! \n")

    if emprestimo > salario*0.3:
      print(f'O Valor de R${emprestimo} não está disponível no momento para você. \n')
      print('Aguarde uma semana e verifique novamente...rsrs \n')
      print('         FIM...        ')
  
  if outraVerificacao.lower() == "nao" : 
    print('Aguarde uma semana e verifique novamente...rsrs \n')
    print('         FIM...        ')
  
  if outraVerificacao.lower() != "sim" and outraVerificacao.lower() != "nao":
    print("Resposta errada!")
    print("FIM...")