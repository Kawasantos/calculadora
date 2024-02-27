print('ola, seja bem-vindo')
nome = str(input('por favor, digite seu nome:'))
print(f'ola, {nome}')
n1 = float(input('digite sua primeira nota:'))
n2 = float(input('digite sua segunda nota:'))
n3 = float(input('digite sua terceira nota:'))
n4 = float(input('digite sua quarta nota:'))
media = (n1+n2+n3+n4)/4
if media >=6.0:
    print(f'sua media foi {media:.1f} parabens :)')
else:
    print(f'sua media foi {media:.1f} estude mais na recuperação')
print('----fim de programa----')






