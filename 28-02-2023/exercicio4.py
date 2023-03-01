# 4) Faça um programa que leia N notas e mostre na tela a média das notas lidas.

qtdNotas = int(input("Digite a qtd de notas que você deseja saber a média: "))
while qtdNotas < 1:
    qtdNotas = int(input("Digite a qtd de notas que você deseja saber a média: "))

soma = 0
cont = 1


while cont <= qtdNotas:
    nota = float(input("Digite uma nota de 0 a 10 : "))
    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida!  Digite uma note de 0 a 10!!: "))
    soma = soma + nota
    cont += 1

media = soma / qtdNotas

print(f'A media das notas lidas foi de {media:.2f}')
