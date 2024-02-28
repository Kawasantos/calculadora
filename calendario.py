import calendar

ano = int(input('digite o ano '))
mes = int(input('digite o mes '))

cal = calendar.month(ano, mes)
print(f"Aqui está o calendário para {calendar.month_name[mes]} de {ano}:\n")
print(cal)

if calendar.isleap(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
