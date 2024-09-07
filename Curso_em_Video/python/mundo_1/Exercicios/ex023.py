

#  Le um N° de 0 a 9999 e mostre os digitos separada mente
# ex: 1834
# unidade = 4
# desena = 3
# centena = 8
# milhar = 10




N = int (input('\nDigite um Numero: '))

# Unidade: Último dígito
unidade = N % 10

# Dezena: Penúltimo dígito
dezena = (N // 10) % 10

# Centena: Terceiro dígito a partir da direita
centena = (N // 100) % 10

# Milhar: Quarto dígito a partir da direita
milhar = (N // 1000) % 10

print('Unidade: {unidade}')
print('Dezena: {dezena}')
print('Centena: {centena}')
print('Milhar: {milhar}')