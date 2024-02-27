from datetime import date
print('caso queira analizar o ano atual, coloque 0')
ano = int(input('qua ano quer analizar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ANO {ano} E BISSEXTO')
else:
    print(f'O ANO {ano} NÁO É BISSEXTO')
