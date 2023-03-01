#8) Escreva um programa em Python que leia um número inteiro positivo
# e diga se o número informado é primo

divisores = 0

numero = int(input("Digite um número inteiro positivo: "))
    
for i in range(1, numero+1):
  if numero % i == 0:
    divisores += 1
    
if divisores == 2:
  print(f'{numero} é um número primo')
else:
  print(f'Não é número primo')

