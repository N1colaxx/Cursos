




n1 = int (input('Digite a Primeira nota: '))
n2 = int (input('Digite a Segunda nota: '))
media = (n1 + n2)/2

if media > 7:
    print('\033[0;30;42m Aprovado \033[m')
elif media > 5:
    print('\033[0;30;43m Recuperação \033[m')
else:
    print('\033[0;31;40m Reprovado \033[m')