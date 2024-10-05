'''Construa um Algoritmo que, para um grupo de valores inteiros, 
determine:
	A soma dos números positivos;
	A quantidade de valores negativos;
	só finalize se o código informado por -999.
'''
n = neg = positivos = 0
while True:
    n = int(input('Digite um número [-999 para sair]: '))
    if n == -999:
        break
    elif n > 0:
        positivos += n
    elif n < 0:
        neg+=1
print(f'Os valores negativos foram {neg}')
print(f'A soma dos valores positivos {positivos}')