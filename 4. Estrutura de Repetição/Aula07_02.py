from math import inf

op='-1'
menuPrincipal='\n'*10
menuPrincipal+=('_____'+'M E N U'+'_____\n')
menuPrincipal+=('1 - Exercício 1\n')
menuPrincipal+=('2 - Exercício 2\n')
menuPrincipal+=('3 - Exercício 3\n')
menuPrincipal+=('4 - Exercício 4\n')
menuPrincipal+=('S - sair\n')

while (op.upper()!='S'):
    print(menuPrincipal)
    op=input('Informe sua opção:')
    if op=='1':
        faixa=range(1,11)
        soma,maior,menor=0,-inf,inf
        for i in faixa:
            print('\nInforme %dº valor:' %(i), end='')
            valor=int(input())
            soma+=valor
            if valor>maior:maior=valor
            if valor<menor:menor=valor 
            print("valor =",valor)
            print("soma =",soma)
            print("maior =",maior)
            print("menor =",menor)
            
    elif op=='2':
        print('Questão do discente.')

    elif op=='3':
        somaPos=qntNeg=valor=0
        i=1
        while valor!=-999:
            print('Digite -999 para finalizar.\nInforme %dº valor:' %(i), end='')
            valor=int(input())
            if valor!=-999:
                i+=1
                if valor>0:somaPos+=valor
                if valor<0:qntNeg+=1
        print('A soma dos positivos deu', somaPos)
        print('A quantidade de negativos foi', qntNeg)
        
    elif op=='4':
        soma, numerador, denominador = 0,1,range(1,51)
        for d in denominador:
            soma+=numerador/d
            numerador+=2
        print('A soma deu %4.3f' %(soma))
            
        
    elif op.upper()=='S':
        print('Encerrando.')
    else:
        print('Opção inválida!')
