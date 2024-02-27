casa = float(input('valor do imovel: R$'))
salario = float(input('salario do comprador: R$'))
anos = int(input('quantos anos de finaciamento?'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de R$ {casa:.2f} em {anos}', end='')
print(f'a prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('emprestimo pode ser concedido')
else:
    print('emprestimo negado')
