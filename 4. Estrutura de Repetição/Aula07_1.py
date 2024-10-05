op='-1'
while (op.upper()!='S'):
    print('_____'+'M E N U'+'_____')
    print('1 - Exemplo 1')
    print('2 - Exemplo 2')
    print('2b - Exemplo 2 - versão 2')
    print('3 - Exemplo 3')
    print('4 - Exemplo 4')
    print('5 - Exemplo 5')
    print('6 - Exemplo 6')
    print('7 - Exemplo 7')
    print('8 - Exemplo 8')
    print('9 - Exemplo 9')
    print('10 - Exemplo 10')
    print('S - sair')
    op=input('Informe sua opção:')
    if op=='1':
        s,i=0,1
        while i<6:
            s+=i
            i+=1
        print('Soma = %d' %(s))
        
    elif op=='2':
        import math
        angulo=0
        while angulo<=360:
            print('Ângulo: %03d\tseno: %6.3f' %(angulo, math.sin(angulo*3.1415/180.0)))
            angulo+=10
            
    elif op=='2b':
        import math
        angulo=0
        texto=''
        while angulo<=360:
            texto+='Ângulo: {:03d}\tseno: {:6.3f}\n'.format(angulo, math.sin(angulo*3.1415/180.0))
            angulo+=10
        print(texto)
        
    elif op=='3':
        from random import randint
        print('Escolhendo um valor aleatório.')
        segredo=randint(1,10)
        escolha=''
        while segredo!=escolha:
            print('\nEscolha um valor entre 1 e 10. Digite 0 para desistir.')
            escolha = int(input())
            if segredo==escolha:
                print('Parabéns! Você acertou.')
            elif escolha ==0:
                print('Perdeu. Você desistiu')
                break
            else:
                print('Errou tente novamente')
                
    elif op=='4':
        item = 0
        while item <20:
            item+=1
            if item %5==0:
                continue
            print(item)
            
    elif op=='5':
        item = 0
        while item <20:
            item+=1
            if item %5==0:
                continue
            print(item)
        else:
            print('Não gosto de múltiplos de 5.')
            
    elif op=='6':
        soma = 0
        for x in range(1,100):
            soma+=x
            print('%02d) soma = %4d'%(x,soma))

    elif op=='7':
        for j in range(0,51,5):
            print('%02d'%(j))
        print('\n')
        for j in range(1,51,5):
            print('%02d'%(j))    

    elif op=='8':        
        dias = ['domingo','segunda','terça','quarta','quinta','sexta','sábado']
        for x in dias:
            if x=='segunda':
                print('Odeio segunda.')
                continue
            print('Amo %s' %(x))
    elif op=='9':
        i=j=0
        while (i<11):
            j=0
            while(j<11):
                print('%02dX%02d=%2d   '%(j,i,i*j),end='')
                j+=1
            i+=1
            print('')
            
    elif op=='10':
        for i in range(0,11):
            for j in range(0,11):
                print('%02dX%02d=%2d   '%(j,i,i*j),end='')
            print('')            
            
    elif op.upper()=='S':
        print('Encerrando.')
        
    else:
        print('Opção inválida!')
