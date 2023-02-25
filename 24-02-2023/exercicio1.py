'''
1) Crie um algoritmo que leia um número e diga se ele está no intervalo fechado
entre 25 e 200.
'''

num = int(input("Digite um número inteiro e vamos verificar se ele está entre 25 e 200 : "))

if num < 25 :
  print(f'O número "{num}" está fora do intervalo')

if num >= 25 and num <= 200 :
  print(f'O número "{num}" está dentro do intervalo')