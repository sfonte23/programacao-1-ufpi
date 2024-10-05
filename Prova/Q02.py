'''2)Faça uma função que calcule o desvio padrão de um vetor V contendo n números, 
dada e expressão abaixo. Sabendo-se que m é a média do vetor.'''

#nao lembro desse tipo de conteúdo nas aulas.

import math

def calculaDesvioPadrao(v):
    # média do vetor
    m = sum(v) / len(v)
    
    somaQDif = sum((x - m) ** 2 for x in v)
    dp = math.sqrt(somaQDif / len(v))
    return dp

# Exemplo
v = [1, 2, 3, 4, 5]
dp = calculaDesvioPadrao(v)
print("Desvio Padrão:", dp)

