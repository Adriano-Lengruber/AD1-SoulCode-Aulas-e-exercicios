'''
8) Criar um algoritmo em Python que leia um número inteiro entre 1 e 7 e
escreva o dia da semana correspondente. Caso o usuário digite
um número fora desse intervalo, deverá aparecer uma mensagem
informando que não existe dia da semana
com esse número.

1 - Domingo
2 - Segunda
.
.
.
7 - Sábado
'''

numero = int(input("Por favor dogote um número inteiro de 1 a 7 para vermos o dia da semana correspondente: "))

if numero < 1 and numero > 7:
    print("Número Inválido!!!\n")
elif numero == 1:
    print(f'Você digitou: {numero} , que corresnpode à Domingo !')
elif numero == 2:
    print(f'Você digitou: {numero} , que corresnpode à Segunda-feira !')
elif numero == 3:
    print(f'Você digitou: {numero} , que corresnpode à Terça-feira !')
elif numero == 4:
    print(f'Você digitou: {numero} , que corresnpode à Quarta-feira !')
elif numero == 5:
    print(f'Você digitou: {numero} , que corresnpode à Quinta-feira !')
elif numero == 6:
    print(f'Você digitou: {numero} , que corresnpode à Sexta-feiraaaa!!!')
else: 
    print(f'Você digitou: {numero} , que corresnpode à Sabadão !!!')

print("...FIM...")