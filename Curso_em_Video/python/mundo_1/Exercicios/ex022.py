



# Nome = 'Nicolas Cardozo Felix Borges'
#  aqui tem 29 caracteres

nome = str(input('\nDigite seu nome completo:'))

print('Nome em maiusculo => {}'.format(nome.upper()))
print('Nome em minusculo => {}'.format(nome.lower()))


ls = nome.strip()
lss = nome.replace(' ', '') # remove os espaços do nome TODOS
print('''\nQuantidade de Letras sem considererar os espaços =>''', len(lss))




# ele separa como um lista ex: 'Nicols', 'Cardozo', 'Felix', 'Borges'
#                                  0         1          2       3
lista_nomes = nome.split()

# Acessa o Primeiro nome = 0
primeiro_nome = lista_nomes[0]

# Ve o comprimento
comprimento = len(primeiro_nome)

print ('''\nQuantidade de letras do Primeiro nome!
P Nome é {} 
Quantidade de letras é {}'''.format(primeiro_nome, comprimento))