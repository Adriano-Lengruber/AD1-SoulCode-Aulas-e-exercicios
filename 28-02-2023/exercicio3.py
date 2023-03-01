# 3) Faça um algoritmo que leia um número positivo e imprima na tela todos os divisores desse número

n = int(input("Digite um numero positivo: "))
i = 1

while n < 1:
    n = int(input("Número inválido, digite um numero positivo! : "))

while i <= n:
    if n % i == 0:
        print(i)
    i += 1