'''
21) Construa um algoritmo em Python para determinar se o indivíduo está
com um peso favorável. Essa situação é determinada através do IMC
(Índice de Massa Corpórea), que é definida como sendo a relação entre
o peso (PESO) e o quadrado da Altura (ALTURA) do indivíduo. Ou seja,

IMC é igual ao peso dividido pelo quadrado da altura

e, a situação do peso é determinada pela tabela abaixo: Condição Situação

IMC abaixo de 20 Abaixo do peso

IMC de 20 até 25 Peso Normal

IMC de 25 até 30 Sobre Peso

IMC de 30 até 40 Obeso

IMC de 40 e acima Obeso Mórbido
'''


peso = float(input("Como está? Vamos calcular seu IMC hoje? Digite seu peso por favor: "))

altura = float(input("Digite sua altura por favor: "))
    
imc = peso / (altura*2)

if imc < 20: 
    print(f'Seu IMC deu: {imc:.2f}, está categorizado como "Abaixo do Peso".')
elif imc >= 20 and imc < 25:
    print(f'Seu IMC deu: {imc:.2f}, está categorizado como "Peso Normal".')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC deu: {imc:.2f}, está categorizado como "Sobre Peso".')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC deu: {imc:.2f}, está categorizado como "Obeso".')
else:
    print(f'Seu IMC deu: {imc:.2f}, está categorizado como "Obeso Mórbido".')

print("   FIM   ")