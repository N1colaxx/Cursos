



# Nome = 'Nicolas Cardozo Felix Borges'
#  aqui tem 29 caracteres

nome = input('\nDigite seu nome completo:')

print('Nome em maiusculo => {}'.format(nome.upper()))
print('Nome em minusculo => {}'.format(nome.lower()))


ls = nome.strip()
ls = nome.replace(' ', '')
print('''\nQuantidade de Letras sem considererar 
os espaços =>''', len(ls))




# ele separa como um lista ex: 'Nicols', 'Cardozo', 'Felix', 'Borges'
#                                  0         1          2       3
lista_nome = nome.split()

# Acessa o Primeiro nome = 0
primeiro_nome = lista_nome[0]

# Ve o comprimento
comprimento = len(primeiro_nome)

print ('''\nQuantidade de letras do Primeiro nome!
P Nome é {} 
Quantidade de letras é {}'''.format(primeiro_nome, comprimento))