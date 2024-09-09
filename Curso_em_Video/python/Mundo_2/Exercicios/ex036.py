




# prestaço >= 30% do salrario ou então nega o emprestimo


valor_casa = int (input('Informe o valor da casa: '))
sal_comprador = float (input('Informe seu salario: '))
pres = int (input('Em quantas prestações: '))

pres_mes = (valor_casa / pres)
percentual_sal = sal_comprador * (30/100)
if pres_mes >= percentual_sal:
    print('Desculpe! Seu emprestimo foi \033[4;31m Negado!')
else:
    print('Parabens!! Seu emprestimo foi \033[4;32m Aprovado!!!!')

