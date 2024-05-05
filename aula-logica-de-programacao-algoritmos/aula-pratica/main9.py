strings = (
    "Python",
    "Inteligente",
    "Criatividade",
    "Conhecimento",
    "Aprender",
    "Explorar",
    "Gentileza",
    "Persistência",
    "Imaginação",
    "Tecnologia"
)

def encontrar_vogais(tupla):
    vogais = 'aeiouAEIOU'
    vogais_ordem = []
    # percorre a tupla
    for i in tupla:
        exibir = []
        exibir.append(i)
        # percorre as strings de cada tupla
        for char in i:
            # averigua se na string tem uma vogal
            if char in vogais:
                exibir.append(char)
        vogais_ordem.append(exibir)
        # exibir.clear()
    return vogais_ordem

chamada = encontrar_vogais(strings)
print(chamada)