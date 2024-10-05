'''Verificar se três  valores podem ser os comprimentos de um lado do triângulo. 
Se podem, então classificar o triângulo em equilátero, isósceles ou escaleno. 
Se eles não formarem um triângulo, escrever uma mensagem informando.'''
while True:
    t = []
    for i in range(1,4):
        t.append(int(input(f'Digite o {i}º lado: ')))
    if t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]:
        print('\033[32mÉ um triângulo ',end='')
        if t[0] == t[1] == t[2]:
            print('equilátero!\033[m')
        elif t[0] != t[1] and t[1] != t[2] and t[0] != t[2]:
            print('escaleno!\033[m')
        else:
            print('isósceles!\033[m')
    else:
        print('\033[31mNão é um triângulo!\033[m')
