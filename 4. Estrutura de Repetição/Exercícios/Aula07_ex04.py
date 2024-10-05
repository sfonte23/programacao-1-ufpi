'''Faça um programa que calcula e escreve a seguinte soma:
	soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
'''
numerador = denominador = 1
soma = 0
while numerador != 101:
    if numerador == 99:
        soma += numerador/denominador
        print(f'{numerador}/{denominador} = {soma}',end='')
        break
    else:
        print(f'{numerador}/{denominador} + ',end='')
        numerador += 2
        denominador += 1
        soma += numerador/denominador