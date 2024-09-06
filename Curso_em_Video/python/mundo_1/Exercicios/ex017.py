


from math import sqrt

cto = float (input('\n Digiteo valor do Cateto Oposto: '))
cta = float (input('Digite o valor do Cateto Adjacente: '))
hip = sqrt((cto ** 2) + (cta ** 2))
print('O comprimento da hipotenusa é {:.2f}'.format(hip))