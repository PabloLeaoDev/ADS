import time

print('Tipo de instalação:')
print('-----------------')
print('R - residencial')
print('C - comercial')
print('I - industrial')
print('-----------------')
time.sleep(1)
type = input('Qual é o seu tipo de instalação? ')
hwh = int(input('Quanto foi o consumo de energia, em kWh? '))

if (type.upper() not in ['R', 'C', 'I']):
    # se o tipo de instalação não for R, C ou I
    print('Tipo de instalação inválido!')
else:
    valor = 0
    if (type.upper() == 'R'):
        if (hwh <= 500):
            valor = hwh * 0.40
        else:
            valor = hwh * 0.65
    elif (type.upper() == 'C'):
        if (hwh <= 1000):
            valor = hwh * 0.55
        else:
            valor = hwh * 0.60
    elif (type.upper() == 'I'):
        if (hwh <= 5000):
            valor = hwh * 0.55
        else:
            valor = hwh * 0.60
    print(f'O valor a ser pago é de R${valor:.2f}')