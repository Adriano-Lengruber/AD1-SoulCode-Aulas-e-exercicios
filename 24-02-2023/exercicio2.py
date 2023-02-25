'''
2) Crie um algoritmo que leia 5 números e informe na tela o maior número lido.
'''
print("Por favor, digite 5 números para verificarmos qual o maior dentre eles.")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
  print(f'O número {num1} é o maior dentre os 5')

if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
  print(f'O número {num2} é o maior dentre os 5')

if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
  print(f'O número {num3} é o maior dentre os 5')

if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
  print(f'O número {num4} é o maior dentre os 5')

if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
  print(f'O número {num5} é o maior dentre os 5')