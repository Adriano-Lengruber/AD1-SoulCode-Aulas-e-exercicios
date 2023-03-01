#9) Escrever um algoritmo que leia uma quantidade desconhecida
# de números e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deve terminar quando for lido um número negativo.


intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while True:
    n = int(input("Digite um número qualquer. :"))
    if n < 0:
        print ("Obrigado por utilizar nosso sistema, Volte Sempre!")
        break

    if 0 <= n <= 25:
        intervalo1 += 1
    elif 26 <= n <= 50:
        intervalo2 += 1
    elif 51 <= n <= 75:
        intervalo3 += 1
    elif 76 <= n <= 100:
        intervalo4 += 1

REVER E TERMINARRRRRRRR