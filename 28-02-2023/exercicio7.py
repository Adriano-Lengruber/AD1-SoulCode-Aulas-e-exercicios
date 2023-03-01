#7) Crie uma tabuada do 1 ao 10 utilizando o comando while. Ex de saída: 1 x 0 = 0 1 x 1 = 1 1 x 2 = … 1 x 10 = 10

i = 0
j = 0
conta = 0

while i <= 10:
    j = 0
    while j <= 10:
        print(f'{i} X {j} = {(i * j)}')
        j += 1
    i += 1
    print('\n')
