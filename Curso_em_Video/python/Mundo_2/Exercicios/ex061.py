

t = int( input('informe o 1° termo da PA: '))
r = int( input('informe a razão da PA: '))
i = 1
while i <= 10 :
    t += r
    print('{} ➡ '.format(t), end='')
    i += 1
print('FIM')