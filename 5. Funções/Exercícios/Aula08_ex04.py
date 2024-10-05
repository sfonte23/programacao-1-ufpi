'''Crie uma função chamada dado() que retorna aleatoriamente um número de 1 até 6. 
Chame a função dado() mil vezes e imprima quantas vezes cada valor foi sorteado.'''
from random import randint

def dado():
    return randint(1, 6)
print('=-'*15)
print(f'       SORTEIO DE DADO')
print('=-'*15)
jogadas = int(input('Quantas vezes deseja jogar? '))
print('-='*15)
resultado = [0, 0, 0, 0, 0, 0]
for i in range(jogadas):
    valor = dado()
    resultado[valor - 1] += 1
for i, contagem in enumerate(resultado):
    if i == 5:
        print(f'| \033[32m{i + 1}\033[m foi sorteado {contagem:>4} vezes.  |')
        print('-='*15)
    else:
        print(f'| \033[32m{i + 1}\033[m foi sorteado {contagem:>4} vezes.  |')