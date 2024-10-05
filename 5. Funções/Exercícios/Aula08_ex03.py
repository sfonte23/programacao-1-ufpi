'''Utilize a função anterior e crie uma função que calcula o maior entre três números.'''

'''Crie uma função que receba 2 números e retorne o maior valor.'''

def maior(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
    
while True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = int(input('Digite o terceiro número: '))
    print('-='*20)
    print(f'O maior entre eles é {maior(n1,n2,n3)}')