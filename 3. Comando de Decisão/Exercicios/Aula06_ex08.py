'''Crie um programa que leia a idade de uma pessoa e 
informe a sua classe eleitoral:
Não eleitor (abaixo de 16 anos);
Eleitor obrigatório (entre a faixa de 18 e menor de 65 anos);
Eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive). 
'''

idade = int(input(f'Digite a idade: '))
if idade < 16:
    print('Não Eleitor')
elif 66 > idade > 17:
    print('Eleitor Obrigatório')
else:
    print('Eleitor Facultativo')