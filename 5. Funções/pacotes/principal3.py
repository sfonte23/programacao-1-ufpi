from matematica.estatisticas import media, mediana, variancia, desvio_padrao, todas
#from matematica.estatisticas import *

def executar():
    valores=[]
    for i in range(1,11):
        valores.append(int(input('Infome o %dº valor: ' %(i))))
    print('A média é %.4f' %(media(valores)))
    print('A mediana é %.4f' %(mediana(valores)))
    print('A variância é %.4f' %(variancia(valores)))
    print('O desvio padrão é %.4f' %(desvio_padrao(valores)))
    print('Todas =',todas(valores))
    
if __name__ == "__main__":
    print('O nome do módulo é:',__name__)
    executar()


