# função que cria uma borda personalizada para a string informada
def border(string):
    phrase = len(string)
    print('+' + '-' * phrase + '+')
    print('|' + string + '|')
    print('+' + '-' * phrase + '+')
    
border(input('Escreva uma frase: '))