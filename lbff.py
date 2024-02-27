from time import  sleep 
print('esse programa soma colocaçaõ de cada time da lbff')
print('-=-'*20)
print('digita os pontos,  colocação e as kills de forma certa')
print('-=-'*20)
print('para não ter  engono, mostraremos a tabela da lbff mais atiualizada')
print('-=-'*20)
#tabela de de porntos da lbff
print('booyah = 12') 
print('segundo lugar = 9')
print('terceiro lugar = 8')
print('quarto lugar = 7')
print('quinto lugar = 6')
print('sexto lugar = 5')
print('setimo lugar = 4')
print('oitavo lugar = 3')
print('nono lugar = 2')
print('decimo lugar = 1')
print('decimo primeiro lugar = 0')
print('decimo segundo lugar = 0')
print('-=-'*20)
      
nome = str(input('qual é o nome do time em questão:'))
pontos = int(input('quantos pontos tem o time atual: '))
colocaçao = int(input('qual foi acolocação do time:'))
kill = int(input('quantas kill o time fez:'))
print('ANALIZANDO...')
sleep(3)


soma = pontos + colocaçao + kill
#colocação do time
print(f' o time {nome} que tinha {pontos} agora esta com {soma}')
