



from math import radians, sin, cos, tan

angulo = float (input('\n Digite o angulo: '))

# PY usa RADIANOS nas contas, aqui estou convertendo de Graus para -> Radianos
radiano = radians(angulo)

# comvertido faço as contas
seno = sin(radiano)
cosceno = cos(radiano)
tangente = tan(radiano)

print(' Dado o angulo {}° graus temos: \n Seno = {:.2f} \n Cosceno = {:.2f} \n Tangente = {:.2f}'.format(angulo, seno, cosceno, tangente))