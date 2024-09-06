



import math

angulo = float (input('\n Digite o angulo: '))

# PY usa RADIANOS nas consta aqui estou convertendo de Graus para -> Radianos
radiano = math.radians(angulo)

# comvertido faço as contas
seno = math.sin(radiano)
cosceno = math.cos(radiano)
tangente = math.tan(radiano)

print(' Dado o angulo {}° graus temos: \n Seno = {:.3f} \n Cosceno = {:.3f} \n Tangente = {}'.format(angulo, seno, cosceno, tangente))