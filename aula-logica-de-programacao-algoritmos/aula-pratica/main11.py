import datetime

dicio = {}
cont = 0
flag = True

def average_age(dicio):
    """This function calculate the average age of registered users, and return the value.

    Returns:
        media: returns the average age of registered users.
    """
    for value in dicio.values():
        x = value[1]
        age = datetime.datetime.now().year - x
        age += age
    global average
    average = age / (cont + 1)
    return average



while flag:
    user = []
    name = input('\nDigite seu nome: ')
    birth = int(input('Digite o ano do seu nascimento: '))
    sex = input('Digite qual é o seu sexo: [M/F] ')
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
print(f'O total de cadastros efetuados foi de {cont + 1}.')
media = average_age(dicio)
print(media)
