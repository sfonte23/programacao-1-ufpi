'''Crie uma função que recebe dois inteiros e retorna o seu MDC.'''

def mdc(a,b):
    #Algoritmo de Euclides:
    while b:
        a, b = b, a % b
    return a

print('=-'*15)
print('         CALCULO MDC')
print('=-'*15)
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
print('Calculando...')
print(f'O MDC entre {n1} e {n2} = {mdc(n1,n2)}')