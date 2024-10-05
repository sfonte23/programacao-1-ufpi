'''Crie uma função que receba 2 números e retorne o maior valor.'''

def maior(a,b):
    if a > b:
        return a
    else:
        return b

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('-='*20)
print(f'O maior entre eles é o {maior(n1,n2)}')