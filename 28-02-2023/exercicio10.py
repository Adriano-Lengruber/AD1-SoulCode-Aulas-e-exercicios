#10) Escreva um algoritmo que leia um valor inicial A e
# imprima a seqüência de valores do cálculo de A! e o seu resultado. 
# Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120


a = int(input("Digite o numero: "))

cont = 1
fatorial = 1

while cont < a:
    fatorial = (a * cont)
    print(f'{a} X {cont} = {fatorial}')
    cont += 1
    
TERMINARRRRRRR