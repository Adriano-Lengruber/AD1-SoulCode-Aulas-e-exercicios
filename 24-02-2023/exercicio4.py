'''
4) Crie um algoritmo que leia um número e informe se ele é divisível por 7.
'''
print("Por favor, digite um número inteiro para vermos se é divisíel por 7 : ")

num = int(input("Digite o número: "))

if num % 7 == 0 :
  print(f'O número {num} é divisível por 7!')
else :
  print(f'O número {num} não é divisível por 7!')