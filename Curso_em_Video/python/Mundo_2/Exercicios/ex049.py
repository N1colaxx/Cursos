



num = int( input('\n\nInforme um N°: '))

print('''
    Tabuado do Número {}
==============================='''.format(num))
for i in range (0, 10+1):
    tab = num * i
    print('         {} x {} = {}'.format(num, i,  tab))