



fra = input('Escreva uma frase: '.replace('', "")) # replace removi Todos os espaços da String
fra = fra.upper() # Converti todas as letras para Maiusculs
fra_inv = fra[::-1] # inverti a String
print('-='*10, '\n', fra, '\n', '-='*10)

if fra == fra_inv:
    print('Essa prase é Polindromo.')
else:
    print('Essa frase Não é Polindroma.')