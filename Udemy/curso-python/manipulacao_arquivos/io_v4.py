try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
            print('Nome: {}, Idade: {}'.format(registro.strip().split(',')))

except IndexError:
    pass

finally:
    print('finally')
    arquivo.close

if arquivo.close:   
    print('Arquivo ja foi fechado...')
