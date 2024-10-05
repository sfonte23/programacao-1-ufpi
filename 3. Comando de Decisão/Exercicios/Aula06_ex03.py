'''Escreva um programa que leia um número e informe se ele é par.'''
while True:
    print('=-'*10)  
    n = int(input('Digite um número [0 = SAIR]:  '))
    print('=-'*10)
    if n == 0:
        print('Saindo!')
        break
    if n %2 == 0:
        print(f'{n} é par!')
    else:
        print(f'{n} é ímpar!')