print('-----MENU----------')
print('1 - Exemplo 1')
print('2 - Exemplo 2')
print('3 - Exemplo 3')
print('4 - Exemplo 4')
print('5 - Exemplo 5')
print('6 - Exemplo 6')
op=input('Informe sua opção:')
if op=='1':
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    if media>=7:
        print('Média %4.2f' %(media))
        print('Aprovado.')	        
elif op=='2':
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    if(media>=7):print('Aprovado.')
elif op=='3':
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    if media>=7:
        print('Aprovado.')
    else:
        print('Reprovado.')
elif op=='4':
    n1=float(input('Nota 1:'))
    n2=float(input('Nota 2:'))
    media=(n1+n2)/2
    print('Média %4.2f' %(media))
    if media>=7:
        print('Aprovado.')
        print('Só alegria.')
    elif media>=4.0:
        print('Prova final.')
        print('Vou estudar mais.')
    else:
        print('Reprovado.')
        print('Vou estudar MUITO mais.')
elif op=='5':
    temperatura=int(input('Informe a temperatura:\n'))
    if temperatura < 0: print('Muito frio')
    elif temperatura >= 0 and temperatura < 15: print('Frio')
    elif temperatura >= 15 and temperatura < 30: print('Agradável')
    else: print('Quente')
elif op=='6':
    temperatura=int(input('Informe a temperatura:\n'))
    if temperatura < 0: print('Muito frio')
    elif 0 <= temperatura < 15: print('Frio')
    elif 15 <= temperatura < 30: print('Agradável')
    else: print('Quente')    
else: print('Opção inválida!')
