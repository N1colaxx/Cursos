



nome = str (input('digite seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cladia':
        print('Nelo nome feminino')
else:
    print('Seu nome é bem normal.')
print('tenha um Bom dia, {}"!'.format(nome))