kill = float(input('Digite quantas kills você fez: '))
death = float(input('Digite quantas vezes morreu: '))
help = float(input('Digite quantas vezes ajudou os aliados: '))

performance = (kill + death + help) / 3

if performance < 6:
    print(f'Sua performance foi péssima: {performance}. Ajude mais a equipe nas próximas partidas.')
elif 7 <= performance <= 8:
    print(f'Você foi muito bem, ajudou bastante em seu time. Sua performance foi {performance}. Você receberá prata em seu desempenho.')
else:
    print(f'Parabéns! Você colaborou demais para seu time. Sua performance foi {performance}. Você receberá ouro em seu desempenho.')


