



nome_completo = input('Digite o seu nome completo: '.strip()) # Remove os espaços extras no inicio e final

# Dividiu os nomes em um lista
nomes = nome_completo.split()

if len(nomes) >= 2:
    primeiro_nome = nomes [0]
    segundo_nome = nomes [-1]
    print('''
    Primeiro nome = {}
    Segundo nome = {}
    '''.format(primeiro_nome, segundo_nome))
else:
    print('O nome completo deve ter pelo menos dois nomes.')


