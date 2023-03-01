#7) Dado um número n inteiro e positivo, dizemos que n é perfeito se n for igual à soma de
#seus divisores positivos diferentes de n. Construa um programa em python que verifica se um
#dado número é perfeito. Ex: 6 é perfeito, pois 1+2+3 = 6.

n = int(input("Digite um número positivo: "))
while n < 1:
    n = int(input("Digite um número positivo: "))

somaDivisor= 0

for i in range(1, n):
    if n % i == 0:
        somaDivisor += i


print('É perfeito.') if somaDivisor == n else print ('Não é perfeito.')

