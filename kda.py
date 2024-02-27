kill = float(input('digite quantas kill voce fez:'))

death = float(input("digite quantas vezes morreu:"))

help = float(input("digite quantas vezes ajudou os aliados:"))

performance =  (kill + death + help) /3

if  performance <=6:
    print(f'sua performace foi pessima foi {performance}, ajude mais a equipe nas proximas partidas')

if performance >=7 or performance <=8:
     print(f" voce foi muito bem, ajudou bastante em seu time,foi {performance} recebera prata em seu desempenho")

else:
     print(f'parabens, voce colaborou demias para seu time, recebera ouro em seu desempenho {performance}')


