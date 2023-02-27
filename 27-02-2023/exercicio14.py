'''
14) Construa um algoritmo em Python para determinar a situação
(APROVADO/EXAME/REPROVADO) de um aluno, dado a sua freqüência (FREQ)
(porcentagem de 0 a 100%) e sua nota (NOTA) (nota de 0.0 a 10.0), sendo que:

Condição Situação

Frequência até 75% Reprovado
Frequência entre 75% e 100% e Nota até 3.0 Reprovado
Frequência entre 75% e 100% e Nota de 3.0 até 7.0 Exame
Frequência entre 75% e 100% e Nota entre 7.0 e 10.0 Aprovado
'''

freq = float(input("Digite sua frequência: de 0 a 100% :  "))
nota = float(input("Digite sua nota: de 0.0 até 10.0 . : "))

if freq <= 75.0 and nota <= 2.9:
    print(f'Sua frequência foi de "{freq}%" e infelizmente está reprovado ')
elif freq >= 75.0 and nota <= 3.0 :
    print(f'Sua frequência foi de "{freq}%" e sua nota foi : {nota}, infelizmente está reprovado.')
elif freq >= 75.0 and nota <= 6.9 :
    print(f'Sua frequência foi de "{freq}%" e sua nota foi : {nota}, terá que fazer outro exame!.')
elif freq >= 75.0 and nota >= 7.0 and nota <= 10.0 :
    print(f'Sua frequência foi de "{freq}%" e sua nota foi : {nota}, parabéns, está aprovado.')
else :
    print("Dados Inválidos")