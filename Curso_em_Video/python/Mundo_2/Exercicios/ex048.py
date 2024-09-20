


s = 0
for i in range(1, 500+1):
    # if i % 3 == 0: # ver se o N° é multiplo de 3
    #     if i % 2 != 0:
    #         s += i
    if (i % 3 == 0) and (i % 2 != 0):
        print(i)
        s += i
print('\nA soma dos N° impares, multiplos de 3 no intervalo de 1 até 500 é: {} '.format(s))