


from math import sqrt

cto = float (input('\nDigiteo valor do Cateto Oposto: '))
cta = float (input('Digite o valor do Cateto Adjacente: '))
# hip = (cto ** 2) + (cta ** 2) ** (1/2)
hip = sqrt((cto ** 2) + (cta ** 2))
print('O comprimento da hipotenusa é {:.2f}'.format(hip))