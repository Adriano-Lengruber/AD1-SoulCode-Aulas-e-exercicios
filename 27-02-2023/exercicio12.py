'''
12) Depois da liberação do governo para as mensalidades dos planos de 
saúde, as pessoas começaram a fazer pesquisas para descobrir um bom plano,
não muito caro. Um vendedor de um plano de saúde apresentou a tabela
a seguir. Criar um algoritmo em Python que entre com a idade de uma
pessoa e imprima o valor que ela deverá
pagar, segundo a seguinte tabela:

Idade Valor

Até 10 anos R$ 30,00
Acima de 10 até 29 anos R$ 60,00
Acima de 29 até 45 anos R$ 120,00
Acima de 45 até 59 anos R$ 150,00
Acima de 59 até 65 anos R$ 250,00
maior que 65 anos R$ 400,00
'''

idade = int(input("Por favor, digite sua idade: "))

if idade <= 10 and idade > 0 :
    print(f'Sua idade é {idade} anos e seu plano fica no valor de R$30,00')
elif idade > 10 and idade <= 29 :
    print(f'Sua idade é {idade} anos e seu plano fica no valor de R$60,00')
elif idade > 29 and idade <= 45 :
    print(f'Sua idade é {idade} anos e seu plano fica no valor de R$120,00')
elif idade > 45 and idade <= 59 :
    print(f'Sua idade é {idade} anos e seu plano fica no valor de R$150,00')
elif idade > 59 and idade <= 65 :
    print(f'Sua idade é {idade} anos e seu plano fica no valor de R$250,00')
elif idade <= 0 and float :
    print(f'Idade informada: {idade} não existe')
else :
    print(f'Sua idade é {idade} anos e seu plano fica no valor de R$400,00')