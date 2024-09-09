


# Ler um numero e ecolher pra qual quer converte
# Binario, octal ou Hexadecimal[



num = int (input('digite um numero INT qualquer: '))
print(''''
Excolha para qual base sera convertido: 
- 1 para Binario 
- 2 para Octal 
- 3 para Hexadecimal
''')

resp = int (input('Informe sua esposta: '))

if resp == 1:
    resp_1 = 'Binario'
    conv_b = bin(num)[2:]
    print('O numero {} convertido para {} é = {}'. format(num, resp_1, conv_b))
elif resp == 2:
    resp_2 = 'Octal'
    conv_o = oct(num)[2:]
    print('O numero {} convertido para {} é = {}'. format(num, resp_2, conv_o))
elif resp == 3:
    resp_3 = 'Hexadecimal'
    conv_h = hex(num)[2:].upper()
    print('O numero {} convertido para {} é = {}'. format(num, resp_3, conv_h))
else:
    print('Resposta \033[4;31m INVALIDA \033[m')
