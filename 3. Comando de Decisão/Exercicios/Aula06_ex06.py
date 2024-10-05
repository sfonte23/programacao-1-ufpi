'''Construa um programa, que receba três valores distintos, A, B e C, 
e armazene-os em três variáveis com os seguintes nomes: 
MAIOR, INTER e MENOR (os nomes correspondem aos valores ordenados).'''

for i in  range(0,3):
    n = int(input('Digite um número: '))
    if i == 0:
        maior = inter = menor = n
    else:
        if n > maior:
            inter = maior
            maior = n
        elif n < menor:
            inter = menor
            menor = n
        elif menor < n < maior:
            inter = n
print(f'O maior é {maior}, o intermediário é {inter} e o menor é {menor}')