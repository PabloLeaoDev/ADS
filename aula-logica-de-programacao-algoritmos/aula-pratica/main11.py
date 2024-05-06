dicio = {}
cont = 0
flag = True

while flag:
    user = []
    name = input('\nDigite seu nome: ')
    birth = int(input('Digite o ano do seu nascimento: '))
    sex = input('Digite qual é o seu sexo: ')
    user.append(name)
    user.append(birth)
    user.append(sex)
    dicio[f'user{cont}'] = user
    cont += 1
    again = input('\nDeseja cadastrar mais alguém? [S/N] ')
    
    while True:
        if again.upper() == 'S':
            break
        elif again.upper() == 'N':
            flag = False
            break
        else:
            print('\nDigite um valor válido!')
            again = input('Deseja cadastrar mais alguém? [S/N] ')
print(dicio)