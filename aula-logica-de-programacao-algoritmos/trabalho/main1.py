def menu():
    print('Bem-vindo a Loja de Gelados do Pablo Leão')
    text = 'CARDÁPIO'
    print(f'{text:-^46}')
    print('---| Tamanho | Cupuaçu (CP) |  Açaí (AC)  |---')
    print('---|    P    |   R$  9.00   |  R$ 11.00   |---')
    print('---|    M    |   R$ 14.00   |  R$ 16.00   |---')
    print('---|    G    |   R$ 18.00   |  R$ 20.00   |---')
    print(f'-' * 46)
    x = escolher()
    return x
def escolher():
    flag = True
    # "pedidos" irá receber uma lista para cada pedido que o usuário fizer
    pedidos = []
    while flag:
        pedido = []
        sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
        tipo = ('CP', 'AC')
        # Se "sabor" não estiver em "tipo"
        if sabor not in tipo:
            print('Sabor inválido. Tente novamente.')
            continue
        else: 
            pedido.append(sabor)
        while True:
            tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
            # Pequeno, Médio e Grande
            size = ('P', 'M', 'G')
            # Se "tamanho" não estiver em "size"
            if tamanho not in size:
                print('Tamanho inválido. Tente novamente.')
                continue
            else:
                pedido.append(tamanho)
                pedidos.append(pedido)
                novo_pedido = input('\nDeseja mais alguma coisa (S/N)? ').upper()
                if novo_pedido == 'S':
                    break
                else:
                    # Essa condição irá parar as duas iterações, por meio da "flag"
                    flag = False
                    break
    return pedidos
def calcular_valor(pedidos):
    custo_ac = 0
    custo_cp = 0
    # "listas" irá armazenar cada lista contida em "pedidos"
    for listas in pedidos:
        if listas[0] == 'AC':
            if listas[1] == 'P':
                custo_ac += 11
            elif listas[1] == 'M':
                custo_ac += 16
            # Essa condição representa a opção Grande
            else:
                custo_ac += 20
        # Essa condição representa a opção Cupuaçu
        else:
            if listas[1] == 'P':
                custo_cp += 9
            elif listas[1] == 'M':
                custo_cp += 14
            else:
                # Essa condição representa a opção Grande
                custo_cp += 18
    valor_final = custo_ac + custo_cp
    return valor_final

def main():
    pedidos = menu()
    pagar = calcular_valor(pedidos)
    print(f'\nO valor total a ser pago é de R${pagar}')
main()