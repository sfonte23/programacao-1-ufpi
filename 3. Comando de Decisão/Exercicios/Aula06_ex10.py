'''Criar um programa que leia o destino do passageiro, 
se a viagem inclui retorno (ida e volta) 
e informar o preço da passagem conforme a tabela a seguir:'''

'''
   CONDIÇÃO        - IDA - VOLTA
REGIAO NORTE       - 500 -  900
REGIAO NORDESTE    - 350 -  650
REGIAO CENTRO-OESTE- 350 -  600
REGIAO SUL         - 300 -  550 
'''
while True:
    dest = int(input('''Qual o seu destino?
[1] Norte
[2] Nordeste
[3] Centro-Oeste
[4] Sul
Destino: '''))
    if 5 > dest > 0:
        break
    else:
        print('Número Inválido, digite novamente.')
print('-'*20)
while True:
    trajeto = int(input('''Qual Trajeto?
[1] Ida
[2] Volta
[3] Ida e Volta
Trajeto: '''))
    if 4 > trajeto > 0:
        break
    else:
        print('Número Inválido, digite novamente.')
if dest == 1:
    if trajeto == 1:
        valor = 500
    elif trajeto == 2:
        valor = 900
    else:
        valor = 500+900

elif dest == 2:
    if trajeto == 1:
        valor = 350
    elif trajeto == 2:
        valor = 650
    else:
        valor = 350+650
elif dest == 3:
    if trajeto == 1:
        valor = 350
    elif trajeto == 2:
        valor = 600
    else:
        valor = 350+600
else:
    if trajeto == 1:
        valor = 300
    elif trajeto == 2:
        valor = 550
    else:
        valor = 300+550
print('=-'*15)
print(f'>>> O valor de sua viagem fica em R${valor}')