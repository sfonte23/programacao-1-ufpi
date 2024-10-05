'''Crie uma função que retorna as raízes de uma equação do 2o grau: 
ax² + bx + c=0 (reais ou complexas). 
Crie antes uma função que calcula o delta.'''

import cmath
def calcular_delta(a, b, c):
    return b**2 - 4*a*c
def calcular_raizes_quadraticas(a, b, c):
    delta = calcular_delta(a, b, c)
    if delta > 0:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        return raiz1, raiz2
    elif delta == 0:
        raiz_unica = -b / (2*a)
        return raiz_unica
    else:
        raiz1 = (-b + cmath.sqrt(delta)) / (2*a)
        raiz2 = (-b - cmath.sqrt(delta)) / (2*a)
        return raiz1, raiz2
    
coeficientes =[]
for i in range (0,3):
    coeficientes.append(int(input('Quais são os 3 coeficientes (a,b,c)? ')))

raizes = calcular_raizes_quadraticas(coeficientes[0],coeficientes[1],coeficientes[2])
print('-='*20)
print("As Raízes da equação:", raizes)
