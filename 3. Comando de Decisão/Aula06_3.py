print('-----MENU----------')
print('1 - Exemplo 1')
print('2 - Exemplo 2')
print('3 - Exemplo 3')
print('4 - Exemplo 4')
op=input('Informe sua opção:')
if op=='1':
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    if media>=7:
        print('Média %4.2f' %(media))
        print('Aprovado.')	        
if op=='2':
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    if(media>=7):print('Aprovado.')
if op=='3':
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    if media>=7:
        print('Aprovado.')
    else:
        print('Reprovado.')
if op=='4':
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    print('Média %4.2f' %(media))
    if media>=7:
        print('Aprovado.')
        print('Só alegria.')
    else:
        if media>=4.0:
            print('Prova final.')
            print('Vou estudar mais.')
        else:
            print('Reprovado.')
            print('Vou estudar MUITO mais.')
