

# como utilizar os códigos de escape sequence ANSI

#     Stely                   Text             Back
   #  0   none          Branco      30          40
   #  1   Blod          Vervelho    31          41
   #  4   Underline     Verde       32          42
   #  7   Negativo      Amarelo     33          43
   #                    Azul        34          44
   #                    Roxo        35          45
   #                    Azul claro  36          46
   #                    Cinza       37          47


   # Estrutura -> \033[0;33;44m

   #  \033[ -> Inicias as cores
   #  1v; 2v; 3vm
   #    1v ->  Formatação do Texto
   #    2v ->  Cor da Letra
   #    3v = m -> Cor do Fundo


   #    \033[0;30:41m
   #    \033[4;33:44m
   #    \033[1;35:43m
   #    \033[30;42m
   #    \033[m
   #    \33[7:30m


print('\033[4;34;47m Hello Word!! \033[m') # O ultimo \033[m  é para Limite ate on de a cor vai

a = 1
b = 2
print('O valor de A = \033[32m{} e B = \033[31m{} \033[m'.format(a, b))

nome = 'Nicolas'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'PretoBranco':'\033[7;37m'
}

print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))
print('---'*15)
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['PretoBranco'], nome, cores['limpa']))


