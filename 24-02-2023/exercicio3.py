'''
3) Crie um algoritmo que leia um número e informe na tela se o mesmo é positivo.
Caso seja, mostre o número na tela.
'''

print("Por favor, digite um número inteiro para vermos se é positivo : ")

num = int(input("Digite o número: "))

if num > 0 :
  print(f'O número {num} é positivo')
else :
  print(f'O número {num} não é positivo')