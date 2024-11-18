

while True:
    sexo = input('Digite seu sexo, F/M? ').strip().upper()

    # if (sexo == 'F') or (sexo == 'M'):
    if sexo in ['F', 'M']:
        print('Ola seja bem vindo! \n')

    else:
        print('"ERO" Digite novamente!! \n')

