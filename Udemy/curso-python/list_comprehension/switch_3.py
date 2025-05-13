def get_tipo_dia(dia):
    dias = {
        (1,7): 'Fim de Semana',
        tuple(range(2,7)): 'Dia de semana',
    }
    # numeros = recebe o N° da tupla
    # tipo = recebe a str
    dia_escolhido = (tipo for numeros, tipo in dias.items()  if dia in numeros)
    # esse 1 TIPO é o que sera retornado a var DIA_ESCOLHIDO, no caso retor no tipo do dia.
    return next(dia_escolhido, '** dia inválido ** ')

if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia} : {get_tipo_dia(dia)}')
        