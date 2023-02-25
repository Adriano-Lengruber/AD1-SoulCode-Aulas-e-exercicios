'''
5) Crie um algotimo que leia um número e diga se ele é par ou ímpar.
'''
print("Por favor, digite um número inteiro para vermos se é par ou ímpar : ")

num = int(input("Digite o número: "))

if num % 2 == 0 :
  print(f'O número {num} é par!')
else :
  print(f'O número {num} é ímpar!')
