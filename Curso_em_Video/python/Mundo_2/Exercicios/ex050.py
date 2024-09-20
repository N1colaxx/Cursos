



s= 0
list_imp = []

for i in range (1, 6+1):
    num = int( input('Digite um n° int: '))
    if num % 2 == 0:
        s += num
    else:
        imp = num
        list_imp.append(imp)

print(f'A soma dos N° pares foi : {s}')
print('Este numero é Impar e foi desconsiderado: {}'.format(list_imp))