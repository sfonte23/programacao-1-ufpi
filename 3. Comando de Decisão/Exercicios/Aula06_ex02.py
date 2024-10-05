'''Escreva um programa para determinar se um dado número N 
é POSITIVO, NEGATIVO ou NULO.'''
while True:
    n = int(input(f'Digite um número: '))
    if n > 0:
        print(f'O número {n} é positivo!')
    elif n == 0:
        print(f'O número {n} é nulo!')
    else:
        print(f'O número {n} é negativo!')