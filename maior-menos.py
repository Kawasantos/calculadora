from time import  sleep
print('nesse programa voce sabera qual o maior e menor valo digitado')
a = int(input('primeiro valor'))
b = int(input('segundo  valor'))
c = int(input('terceiro  valor'))
#verificando que é o menor, melhor metador
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# agora verifica o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('ANALIZANDO... PI PI PI')
sleep(3) 
print(f'HA HA HA BRINCADEIRA, O MAIOR É {maior} E O MENOR É {menor}')