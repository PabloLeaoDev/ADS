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

if (type == 'R' or type == 'r'):
    if (hwh <= 500):
        valor = hwh * 0.40
        print(f'O valor a ser pago é de R${valor:.2f}')
    else:
        valor = hwh * 0.65
        print(f'O valor a ser pago é de R${valor:.2f}')
elif (type == 'C' or type == 'c'):
    if (hwh <= 1000):
        valor = hwh * 0.55
        print(f'O valor a ser pago é de R${valor:.2f}')
    else:
        valor = hwh * 0.60
        print(f'O valor a ser pago é de R${valor:.2f}')
elif (type == 'I' or type == 'i'):
    if (hwh <= 5000):
        valor = hwh * 0.55
        print(f'O valor a ser pago é de R${valor:.2f}')
    else:
        valor = hwh * 0.60
        print(f'O valor a ser pago é de R${valor:.2f}')
else:
    print('Tipo de instalação inválido!')