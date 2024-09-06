



# 4 alunos -> nome
# sorteio
# res-> nome


from random import randint

cont = int (0)
for loop in range (1,6):
        cont = cont + 1
        aluno = input(' Digite o nome do aluno n°{}: '.format(cont))
num = randint (1, 5)
if (num == cont):
print(aluno)