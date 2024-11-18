


def call_fib(n):
    n1 = 0
    n2 = 1
    if n == 0:
        return n1
    if n == 1:
        return n2

    i = 2
    n = n + 2

    lista = []
    while i < n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        i += 1

        lista.append(n3)
    return lista



num = int( input('Digite um N° int: '))

res = call_fib(num)
print('Sequencia de Fibonacci ate os {} primeiros termos: {}'.format(num, res))