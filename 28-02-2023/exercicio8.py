#8) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva 
# a média aritmética dos valores lidos, a quantidade de valores positivos, 
# a quantidade de valores negativos e o percentual de valores negativos e positivos.

somaNumeros = 0
qtdPositivos = 0
qtdNegativos = 0
nLidos = 0

while True:
    n = float(input("Digite um número qualquer"))
    nLidos += 1
    somaNumeros += nLidos
    if n > 0:
        qtdPositivos += 1
    if n < 0:
        qtdNegativos +=1

    cond = input("Quer continuar digitando numeros? [s/n] ")
    if cond.lower() == 'n':
        break

media = somaNumeros / nLidos

CONTINUAR E TERMINARRRRRRRRRR