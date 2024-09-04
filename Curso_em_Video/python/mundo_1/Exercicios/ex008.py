



m = int (input('Digite a distancia em Metros: '))
cm  = m * 100
mm  = m * 1000
km = m / 1000  # conversão para km
hm = m / 100  # conversão para hm
dm = m * 10  # conversão para dm
print(' Converção de {}m para: \n Em Centimetros fica {}cm \n  Milimetros é {}mm \n  Quilometro {}km \n  Hectometros {}hm \n  Decimetros {}dm \n '.format(m, cm, mm, km, hm, dm))
