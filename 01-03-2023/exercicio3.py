#3) Faça um programa que leia 10 números inteiros positivos e mostre, no final, a soma dos
# números pares e a soma dos números ímpares.

# inteiro10 = 0
# i = 0
# par = 0
# impar = 0


# for i in range(inteiro10)):
#     inteiro10 = int(input('Por favor, digite 10 números "inteiros" e "positivos : "'))
#     if inteiro10[i] % 2 == 0:
#         par += inteiro10[i]
#     else: 
#         impar += inteiro10[i]

# print(f'A soma dos números pares foi: {par}')
# print(f'A soma dos números ímpares foi: {impar}')
'''
Minha solução acima
abaixo do prof
'''

somaPar = 0
somaImpar = 0

for i in range(10):
    n = int(input(f'Digite o {i+1}º número : '))
    while n < 1:
        n = int(input(f'Digite o {i+1}º número : '))
    
    if n % 2 == 0:
        somaPar += n
    else:
        somaImpar += n

print(f'A soma dos números pares foi: {somaPar}.')
print(f'A soma dos números ímpares foi: {somaImpar}.')
