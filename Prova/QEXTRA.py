'''As cartas de um jogo de baralho possuem naipes e valores.
Os naipes podem ser: ouro, paus, copas e espadas.
Os valores podem ser: A, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K.

Desenvolva um programa que distribui ALEATORIAMENTE as cartas de um baralho para N jogadores.

O programa deve perguntar:
 A) quantidade de jogadores
 B) quantidade de cartas para cada jogador

Exigências:
1) Não pode haver cartas repetidas;
2) Todos os jogadores devem obrigatoriamente receber a mesma quantidade de cartas.
3) Imprimir as cartas que cada jogador recebeu.
4) Imprimir as cartas que não foram distribuídas.'''
            
from random import shuffle
from time import sleep

naipes = ['♦', '♣', '♥', '♠']
valores = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']

print('=-'*25)
print(f'{"DISTRIBUIDOR DE CARTAS":^50}')
print('=-'*25)

#Solicitando a quantidade de jogadores, tratando erro por não ser número inteiro.
while True:
    try:
        num_jogadores = int(input('\033[mQuantos Jogadores irão participar?\033[32m '))
    except ValueError:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    else:
        break

#Solicitando número de cartas para cada jogador, com tratamento também.
while True:
    try:
        num_cartas_por_jogador = int(input('\033[mQuantas cartas para cada jogador?\033[32m '))
    except ValueError:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    else:
        break

#Pausa Dramática    
print('\033[m=-'*25)
print('Sorteando',end='',flush=True)
sleep(1)
print('.',end='',flush=True)
sleep(1)
print('.',end='',flush=True)
sleep(0.5)
print('.',flush=True)
sleep(0.5)
print('=-'*25)

#Criando um baralho completo e embaralhando ele em seguida.
baralho = [(valor,naipe) for naipe in naipes for valor in valores]
shuffle(baralho)

#Tratando caso tenha mais jogadores do que cartas
if num_cartas_por_jogador * num_jogadores > len(baralho):
    print('A distribuição não poderá ocorrer pois o número de cartas é menor do que o necessário para todos os jogadores.')
else:
    #Distribuindo as cartas
    mao_jogadores = [[] for i in range(num_jogadores)]

    for c in range(num_cartas_por_jogador):
        for j in range(num_jogadores):
            carta = baralho.pop()
            mao_jogadores[j].append(carta)

    # Imprimir as cartas que cada jogador recebeu
    for i, mao in enumerate(mao_jogadores):
        print(f'\n\033[35mCartas do Jogador {i + 1}:\033[m {mao}')
    print()
    # Imprimir as cartas que não foram distribuídas
    print('=-'*25)
    print(f'\n\033[31mCartas não distribuídas:\033[m {baralho}')
