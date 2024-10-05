from estatisticas import media, mediana
from estatisticas import variancia, desvio_padrao
from estatisticas import todas
from random import randint

def executar(valores):
    print(valores)
    #valores.clear()
    #print(valores)
    print('id valores=',id(valores))

    print('A média é %.4f' %(media(valores)))
    print('A mediana é %.4f' %(mediana(valores)))
    print('A variância é %.4f' %(variancia(valores)))
    print('O desvio padrão é %.4f' %(desvio_padrao(valores)))
    print('Todas =',todas(valores))

if __name__ == "__main__": #principal ponto de partida.
    print('O nome do módulo é:',__name__) #é o que define o nome do módulo
    l=[]
    for i in range(1,11):
        x=randint(-10,10)
        print('O %dº valor foi %d.' %(i,x))
        l.append(x)
    print('id l=',id(l))
    executar(l[:])
    print(l)
