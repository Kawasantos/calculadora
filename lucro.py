faturamento = int(input('Por favor, digite o faturamento:'))
custo = int(input('por favor, digite o custo:'))
lucro =  (faturamento - custo)
print(f'o lucro foi de {lucro}')
if lucro >=500:
    print('parabens, a meta foi batida')
else:
    print('a meta nao foi batida')    
#codigo simples de simulador de meta  de empresas  