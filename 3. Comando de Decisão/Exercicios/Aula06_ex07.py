'''Criar um programa que leia dois números e 
imprimir o quadrado do menor número 
e raiz quadrada do maior número, se for possível.'''
while True:
    for i in range(0,2):
        n = int(input('Digite um número: '))
        if i == 0:
            maior = menor = n
        else:
            if n < menor:
                menor = n
            elif n > maior:
                maior = n

    print(f'O quadrado do menor é {menor**2}')
    if menor >=0:
        print(f'A raiz do maior é {maior*0.5}')
    else:
        print(f'O maior não tem raiz inteira.')