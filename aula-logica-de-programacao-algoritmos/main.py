import time

preco = float(input('Digite o preço do seu produto: R$'))
# cria um delay de meio segundo
time.sleep(0.5)
print('Você receberá 10% de desconto! ')
time.sleep(0.5)

# calcula o desconto
desconto = preco * 0.10
preco_final = preco - desconto
print(f'Você irá pagar R${preco_final:.2f}')