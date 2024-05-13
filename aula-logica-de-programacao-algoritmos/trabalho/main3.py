print('\n\nBem-vindo a Livraria do Pablo Leão')
def cadastrar_livro(id):
    print(f'Id do livro: {id}')
    nome = input('Por favor, entre com o nome do livro: ')
    autor = input('Por favor, entre com o nome do autor do livro: ')
    editora = input('Por favor, entre com o nome da editora do livro: ')
    dicio = {'ID': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(dicio)
def consultar_livro():
    while True:
        print('1. Consultar Todos')
        print('2. Consultar por ID')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu')
        escolha = int(input('>>'))
        match(escolha):
            case 1:
                print(lista_livro)
                break
            case 2:
                id_escolhido = int(input('Qual o ID que você deseja consultar? '))
                ids_lista = []
                for i in lista_livro:
                    for chaves, valores in i.items():
                        value_id = i['ID']
                        ids_lista.append(value_id)
                        if chaves == 'ID' and valores == id_escolhido:
                            print(i)
                if id_escolhido not in ids_lista:
                    print('Esse ID não foi cadastrado. Realize o cadastro ou consulte outro ID!')
                    continue
                break
            case 3:
                autor_escolhido = input('Qual o autor que você deseja consultar? ')
                autor_lista = []
                for i in lista_livro:
                    for chaves, valores in i.items():
                        value_autor = i['autor']
                        autor_lista.append(value_autor)
                        if chaves == 'autor' and valores == autor_escolhido:
                            print(i)
                if autor_escolhido not in autor_lista:
                    print('Esse autor não foi cadastrado. Realize o cadastro ou consulte outro autor!')
                    continue
                break
            case 4:
                break
            case _:
                print('Opção inválida!')
                continue
def remover_livro():
    while True:
        id_escolhido = int(input('Qual o ID do livro que você deseja remover? '))
        ids_lista = []
        for i in lista_livro:
            for chaves, valores in i.items():
                value_id = i['ID']
                ids_lista.append(value_id)
                if chaves == 'ID' and valores == id_escolhido:
                    lista_livro.remove(i)
        if id_escolhido not in ids_lista:
            print('Id inválido. Tente novamente')
            continue
        break

lista_livro = []
id_global = 0
while True:
    print('-' * 40)
    print('MENU PRINCIPAL'.center(40, '-'))
    print('Escolha a opção desejada:')
    print('1. Cadastrar Livro')
    print('2. Consultar Livro(s)')
    print('3. Remover Livro')
    print('4. Sair')
    escolha = int(input('>>'))
    print('-' * 40)
    match(escolha):
        case 1:
            identificador = int(input('Qual o ID do livro que você deseja cadastrar? '))
            id_global = identificador
            cadastrar_livro(id_global)
        case 2:
            consultar_livro()
        case 3:
            remover_livro()
        case 4:
            break
        case _:
                print('Opção inválida!')
                continue