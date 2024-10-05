'''Criar um programa que leia um número inteiro entre 1 e 12 
e escrever o mês correspondente. 
Caso o usuário digite um número fora desse intervalo, 
deverá aparecer uma mensagem informando que não existe mês com este número.'''

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto',
        'Setembro','Outubro','Novembro','Dezembro']
while True:
    n = int(input(f'Digite um número para ver o mês: '))
    if n > 12 or n < 1:
        print('Número não válido, digite novamente!')
    else:
        break
print(f'O mês correspondente é {meses[n-1]}')