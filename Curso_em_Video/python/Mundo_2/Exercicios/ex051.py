
lista = []

n1 = int( input('informe o 1° termo da PA: '))
r = int( input('informe a razão da PA: '))

for i in range (10):
    pa =  n1 + (i * r)
    lista.append(pa)
print('Os 10 primeiros termos da PO são: \n {}'.format(lista))


