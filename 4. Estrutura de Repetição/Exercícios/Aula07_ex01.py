'''Escreva um algoritmo que 
lê, soma e exibe 10 valores, 
encontra o maior e o menor deles.'''

valores = list()
soma = 0
for i in range(1,11):
    n = int(input('Digite um número: '))
    valores.append(n)
    soma += n
    if i==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print('=-'*20)
print(f'Os valores digitados foram {sorted(valores)}')
print(f'O maior valor da lista é {maior}, o menor é {menor} e a soma deles é {soma}')