'''64
11) Crie um algoritmo em Python que leia a idade de uma pessoa e informe a
 sua classe eleitoral:
- não eleitor (abaixo de 16 anos);
- eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
- eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive).
'''

idade = int(input("Por favor, digite sua idade: "))

if idade < 16 and idade > 0:
    print(f'Sua idade é {idade} e está na classificação: "Não Eleitor"')
elif idade >= 16 and idade <= 17:
    print(f'Sua idade é {idade} e está na classificação: "Eleitor Facultativo."') 
elif idade >= 18 and idade <= 64:
    print(f'Sua idade é {idade} e está na classificação: "Eleitor Obrigatório".')
elif idade >= 65: 
    print(f'Sua idade é {idade} e está na classificação: "Eleitor Facultativo".')
else: 
    print("Idade Inválida")