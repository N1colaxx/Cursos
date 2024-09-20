



from emoji import emojize
from time import sleep

# for emoji_code, emoji_data in emoji.EMOJI_DATA.items():
#         print(f'{emoji_code}: {emoji_data["en"]}')
# emoji_code -> codigo dos emoji /  emoji_data -> a img do emoji
#print(emoji.emojize("Ola Mundi :bow_and_arrow:"))



print('Contagem regressiva para os Fogos')
print('em...')
sleep(2)
for i in range(10, 0, -1):
    print(i,'...')
    sleep(0.5)
print( 'FOGOS!', emojize(':fireworks:'*15))


#  fui colocar um time pra ver quanto tempo levava para fazer esse codigo, 3 mim o codigo e
#  50mim aprendendo sobre as bibliotecas pqp, e so vi o basico kkkkkkkkkk