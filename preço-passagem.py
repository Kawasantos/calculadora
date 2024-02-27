distancia = float(input('qual é a distancia de sua viagem'))
print(f'voce esta prestes a começar uma viagem de {distancia}km')
if distancia <=200:
    preço = distancia * 0,50
else:
    preço = distancia * 0,45
print(f'o preço de sua passagemsera de {preço:.2f}')