
from math import factorial

while True:
    print('Descubra o fatorial de um N°')
    num = int(input('Digite o numero: '))
    num_fac = factorial(num)

    print('O Fatorial de {} é {}'.format(num, num_fac))
    break

# while True:
#     num = int(input('Digite um N°: '))
#
#     res = 1
#     for num in range(1, num+1):
#         res *= num
#     print(f"O fatorial de {num} é {res}")