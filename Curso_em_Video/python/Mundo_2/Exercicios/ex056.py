



idade_h_velho = 0
nome_h_velho = ''

total_mulher = 0
mulher_menos20 = 0

lista_info = []

rep = int( input('Quantas pessoas ira cadastrar: '))
for i in range(1, rep+1):
    print('-=-'*20)
    print(i, '° Pessoa')
    nome = str( input('Seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str( input('Seu sexo M/F: ').strip().upper())

    info = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }
    lista_info.append(info)

    if sexo == 'M':
        if idade > idade_h_velho:
            idade_h_velho = idade
            nome_h_velho = nome

    if sexo == 'F':
        total_mulher += 1
        if idade < 20:
            mulher_menos20 +=  1

media = sum(soma_idades['idade'] for soma_idades in lista_info)/len(lista_info)

print('===='*20)
print('A media das idades é: ',media)

print('O Homem mais velho é: ', nome_h_velho)
print('O total de mulher é {} e desse total {} tem menos de 20 anos'. format(total_mulher, mulher_menos20))


