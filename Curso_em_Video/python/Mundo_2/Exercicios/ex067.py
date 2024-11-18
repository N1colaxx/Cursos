try:
    num = int( input('Qual tabuada: '))
except ValueError:
    print('Numero digitado não é INT, digite novamente')
else:
    i = 0
    while i <= 10:
        res = num * i
        print('{} * {} = {}'.format(i, num, res))
        i += 1
