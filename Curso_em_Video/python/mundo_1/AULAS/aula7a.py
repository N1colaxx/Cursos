



# Ordem de procedencia
# 1 -> ()
# 2 -> **
# 3 -> * / // %
# 4 -> + -



n1 = int (input('Um valor: '))
n2 = int (input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
dr = n1 % n2
                                            # aqui nesse couchetes definimos q o resultado teta 3 casa decimais de n° flutuantes.
print ('A soma {}, multiplicação {}, divisao  {:.3f}, expondenciação {}'.format(s, m, d, e, end=' ')) # esse END= ''   é para q o print n quebre a linha
print('divisao inteira {}, potencia {}, o resto da divisao {}'.format(di, e, dr))































