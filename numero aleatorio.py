from random import randint
from time import  sleep #faz criar um tempo como se reslmente o pc estivesse "pensando"
pc = randint(0, 10) #fazer o computador 'pensar'
print('-=-' *20) #deixa mais dinamico e bonito para o jogador
print('vou pensar em um numero entre 0 e 10 tente adivinha ')
print('-=-' *20)
jagador = int(input('em que numero eu pensei ? ha ha duvido que acerte:')) #jogador tem que adivinha
print('ANALISANDO...')
sleep(3) 
if jagador == pc:
    print('caramba, voce realmente acertou, parabens:)')
else:
    print('avisei, que voce nao conseguiria, ha ha ha ')
print('de qualquer forma, muito obrigado por participar')
#em resumo o jogador tem que adivinha um numero que o pc esta 'pensando'











