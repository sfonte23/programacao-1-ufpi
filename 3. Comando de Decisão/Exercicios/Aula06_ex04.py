'''Escreva um programa que leia um número e informe se ele é ou não divisível por 5.'''
while True:
    print('=-'*10)  
    n = int(input('Digite um número [0 = SAIR]:  '))
    print('=-'*10)
    if n == 0:
        print('Saindo!')
        break
    if n %5 == 0:
        print(f'\033[32m{n} é divisível por 5!\033[m')
    else:
        print(f'\033[31m{n} não é divisível por 5!\033[m')