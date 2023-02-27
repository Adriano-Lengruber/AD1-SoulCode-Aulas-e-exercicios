
idade = int(input("Por favor, digite sua idade para verificarmos sua categoria de inscrição: "))

if idade < 5:
    print("Infelizmente é muito jovem para participar...")
elif idade >= 5 and idade <=7:
    print(f'Sua categoria é: Infantil A')
elif idade >= 8 and idade <=10:
    print(f'Sua categoria é: Infantil B')
elif idade >= 11 and idade <=13:
    print(f'Sua categoria é: Juvenil A')
elif idade >= 14 and idade <=17:
    print(f'Sua categoria é: Juvenil B')
else: print("Você está classificado na categoria Sênior!! Boa sorte!")