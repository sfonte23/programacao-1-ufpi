import matematica.estatisticas
import matematica.estatisticas as est

def executar():
    valores=[]
    for i in range(1,11):
        valores.append(int(input('Infome o %dº valor: ' %(i))))
    print('A média é %.4f' %(matematica.estatisticas.media(valores)))
    print('A mediana é %.4f' %(est.mediana(valores)))
    print('A variância é %.4f' %(matematica.estatisticas.variancia(valores)))
    print('O desvio padrão é %.4f' %(est.desvio_padrao(valores)))
    print('Todas =',matematica.estatisticas.todas(valores))
    
if __name__ == "__main__":
    print('O nome do módulo é:',__name__)
    executar()


