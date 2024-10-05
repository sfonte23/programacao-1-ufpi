'''Elabore um algoritmo que, dada a idade de um atleta. 
Classifique-o em uma das seguintes categorias:
Infantil : 5 a 10 anos;
Juvenil : 11 a 17 anos;
Sênior: 18 anos ou mais.
'''
idade = int(input('Digite a idade do Atleta: '))
print('-'*25)
if idade < 11:
    print('A categoria do atleta é Infantil')
elif idade > 17:
    print('A categoria do atleta é Sênior')
else:
    print('A categoria do atleta é Juvenil')