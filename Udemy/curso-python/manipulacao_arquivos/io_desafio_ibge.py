# import pandas as pd

# # LER o arquivo CSV, ignorando as três primeiras linhas e sem cabeçalho
# arquivo = pd.read_csv('desafio-ibge.csv', skiprows=3, header=None, encoding='latin1')

# # Pegando as colunas específicas (4ª e 9ª colunas, que são 3 e 8 no índice)
# dados = arquivo[[8, 3]]

# # Exibe os dados selecionados
# for row in dados.values:
#      print(': '.join(str(x) for x in row)) # aqui fiz uma compreensão de lista, e para cada x (item) na linha row, a função str(x) converte esse item para uma string.


import csv 
from urllib import request

def read(url):

    with request.urlopen(url) as entrada:
        print('Baixando os arquivos....')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]} : {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')