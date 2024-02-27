nome = str(input('digite seu nome:'))
print(f'seja-bem vindo {nome}')
velo = float(input('qual é a velocidade atual do carro: ?'))
if velo <=80:
    print('esta dentro do limite de velocidade, tenha um bom dia')
    print('continue dirigindo com segurança')
else:
    print(f'MULTADO! voce excedeu o limite permitido que é de 80km/h ')
    multa = (velo - 80) *7 #isso é soma 
    print(f'voce deve pagar a multa que de {multa:.2f} ')
#calculo de multa
