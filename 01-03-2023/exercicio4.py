#4) Crie um programa que leia 10 números e informe na tela o maior e o menor número lido.


for i in range(10):
    n = int(input(f'Digite o {i+1}º número : '))
    
    if i == 0 :
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    
    

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')

