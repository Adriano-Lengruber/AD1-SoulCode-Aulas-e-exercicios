'''
10) Escreva um algoritmo em Python que dada a idade de uma pessoa, determine
sua classificação segundo a seguinte tabela:
- maior de idade;
- menor de idade;
- pessoa idosa (idade superior ou igual a 65 anos).
'''

idade = int(input("Por favor, digite sua idade: "))

if idade >= 65:
    print(f'Sua idade é {idade} e está na classificação: "Pessoa Idosa"')
elif idade < 65 and idade >= 18:
    print(f'Sua idade é {idade} e está na classificação: "Maior de Idade."') 
else: 
    print(f'Sua idade é {idade} e está na classificação: "Menor de Idade".')
