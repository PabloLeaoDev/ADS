def menu():
    print('Bem-vindo a Copiadora do Pablo Leão')
    print('\nEntre com o tipo de servuço desejado')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')
    op = ['DIG', 'ICO', 'IPB', 'FOT']
    while True:
        escolha = input('>> ').upper()
        if escolha in op:
            break
        else:
            print('Escolha inválida. Entre com o tipo do serviço novamente.')
