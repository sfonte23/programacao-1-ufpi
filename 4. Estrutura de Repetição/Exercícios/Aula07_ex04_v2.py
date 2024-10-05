soma = 0.0
denominador = 1
termo=1

for numerador in range(1, 100, 2):
    print(f'{termo} = {numerador} / {denominador}')
    termo = numerador / denominador
    denominador += 1

print(f'A soma da série é: {soma}')