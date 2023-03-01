#6) Digitados dois números (base e expoente ), calcule o resultado  da potência utilizando apenas
#operadores básicos da matemática(soma, subtração, multiplicação ou divisão) e o comando FOR;


'''
 base = 2
 expoente = 3 
 2 * 2 * 2
 resultado = 8

 base = 3
 expoente = 2
 3 * 3
 resultado = 9 
'''
base = int(input('Digite o valor da base: '))
exp = int(input('Digite o valor do expoente: '))

resultado = 1

for i in range(exp):
  resultado = resultado * base

print(resultado)