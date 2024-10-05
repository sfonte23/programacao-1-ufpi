'''Uma loja abriu uma linha de crédito para os funcionários. 
O valor máximo da prestação não poderá ultrapassar 30% do salário bruto. 
Fazer um programa que permita entrar com o salário bruto e o valor da prestação, 
e informar se o empréstimo pode ou não ser concedido.'''
while True:
    print('=-'*30)
    nome = input('| Qual o nome do funcionário: ').title()
    sb = float(input(f'| Digite o salário bruto de {nome}: R$'))
    divida = int(input('| Qual valor do empréstimo? R$'))
    prest = int(input('| Quantas prestações? '))
    parcela = divida//prest
    print('=-'* 30)
    if parcela > 0.3*sb:
        print(f'\033[31mA prestação será de R${parcela}, desculpe mas não foi aprovado!\033[m')
    else:
        print(f'\033[32mAprovado!\033[m')