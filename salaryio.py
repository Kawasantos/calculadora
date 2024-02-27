salario = float(input('qual é o salario do fucionario ? R$'))
if salario <=1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'quem ganhava {salario:.2f}R$ agora passa a ganha {novo:.2f}R$')





# salarios altos recebem 10% de aumentos
# a media sera de 5000
# salarios mais baixos vao receber 15% de aumento