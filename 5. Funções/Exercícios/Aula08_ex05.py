'''Crie uma função que retorna todos os números primos até 1000.'''
#Criei um que verifica qualquer numero.

def verifica_numero(i):
    if i <= 1:
        return False

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def verifica_primos(n):
    primos = list()
    for i in range(2, n+1):
        if verifica_numero(i):
            primos.append(i)
    return primos

n = int(input('Escreva até que número deseja ver os primos: '))

print(verifica_primos(n))
