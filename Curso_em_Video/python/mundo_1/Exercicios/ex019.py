



# 4 alunos -> nome
# sorteio
# res-> nome


# from random import choice
#
# n1 = input('primeiro aluno: ')
# n2 = input('segundo aluno: ')
# n3 = input('terceiro aluno: ')
# n4 = input('quarto aluno: ')
# lista = [n1, n2, n3, n4]
# escolha = choice(lista)
# print('O aluno escolhido foi {}'.format(escolha))



import random

lista = []
for loop in range(1,5):
    alunos = str(input(' Digite o nome do aluno N°{}: '.format(loop)))
    lista.append(alunos) # Adiciona cada aluno a lista

escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))