



city = input('Digite o nome de uma Cidade: ').strip()
if city.upper().startswith('SANTO'): ## Converte para maiúsculas para garantir a comparação correta
        print('Essa cidade entra no requisito!!')
else:
        print('Essa cidade entra não entra!!')