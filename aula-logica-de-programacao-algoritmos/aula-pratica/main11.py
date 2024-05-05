dicio = {}
cont = 0

while True:
    user = []
    name = input('Digite seu nome: ')
    birth = int(input('Digite o ano do seu nascimento: '))
    sex = input('Digite qual é o seu sexo: ')
    user.append(name)
    user.append(birth)
    user.append(sex)
    dicio[f'user{cont}'] = user
    cont += 1
    if not name or not birth or not sex:
        break
print(dicio)