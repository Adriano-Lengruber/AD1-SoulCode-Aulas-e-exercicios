'''
13) Criar um algoritmo em Python que a partir da idade e peso do paciente calcule a
dosagem de determinado medicamento e imprima a receita informando quantas gotas
do medicamento o paciente deve tomar por dose. Considere que o medicamento em
questão possui 500 mg por ml, e que cada ml corresponde a 20 gotas.
- Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual ou
acima de 60 quilos devem tomar 1000 mg; com peso abaixo de 60 quilos
devem tomar 875 mg.

- Para crianças e adolescentes abaixo de 12 anos a dosagem é calculada pelo
peso corpóreo conforme a tabela a seguir:

Peso Dosagem
5 kg a 9 kg 125 mg
9.1 kg a 16 kg 250 mg
16.1 kg a 24 kg 375 mg
24.1 kg a 30 kg 500 mg
Acima de 30 kg 750 mg
'''

idade = int(input("Por favor, digite sua idade: "))
peso = float(input("Por favor, digite quantos kilos você tem: "))
ml = 20
gotas = 0

if idade >= 12 and peso < 60:
    gotas = 875/ml
    print(f'Para sua idade de {idade} anos e para seu peso: {peso}Kg, deverá tomar {gotas} gotas 875mg! ')

elif idade < 12 and peso >= 5 and peso <= 9:
    gotas = 125/ml
    print(f'Para sua idade de {idade} anos e para seu peso: {peso}Kg, deverá tomar {gotas} gotas ! ')

elif idade < 12 and peso >= 9.1 and peso <= 16:
    gotas = 250/ml
    print(f'Para sua idade de {idade} anos e para seu peso: {peso}Kg, deverá tomar {gotas} gotas ! ')

elif idade < 12 and peso >= 16.1 and peso <= 24:
    gotas = 375/ml
    print(f'Para sua idade de {idade} anos e para seu peso: {peso}Kg, deverá tomar {gotas} gotas ! ')

elif idade < 12 and peso >= 24.1 and peso <= 30:
    gotas = 500/ml
    print(f'Para sua idade de {idade} anos e para seu peso: {peso}Kg, deverá tomar {gotas} gotas ! ')

elif idade < 12 and peso >= 30.1 :
    gotas = 750/ml
    print(f'Para sua idade de {idade} anos e para seu peso: {peso}Kg, deverá tomar {gotas} gotas ! ')

else:
    print("Dados Incorretos")