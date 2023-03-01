#5) Em uma turma há 10 alunos. Cada aluno tem 2 notas.
# Um professor precisa calcular a média das duas notas de cada aluno.
#Crie um programa que resolva este problema.

# aluno1 = float(input("Aluno 1, digite suas 2 notas: "))
# aluno2 = float(input("Aluno 2, digite suas 2 notas: "))







'''
Minha solução acima
abaixo do prof
'''


for i in range(10):
    soma_notas = 0
    for j in range(2):
        nota = float(input(f'Digite a {j + 1}º nota do aluno {i + 1} '))

        while nota < 0 or nota > 10:
            nota = float(input(f'Digite a {j + 1}º nota do aluno {i + 1} '))
        soma_notas = soma_notas + nota
    media_notas = soma_notas / 2
    print(f'A média do aluno {i+1} foi {media_notas}')
