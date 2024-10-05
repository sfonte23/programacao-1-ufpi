def mediana(lista):
    print('O nome do módulo estatiticas.py é:',__name__)
    tam=len(lista)
    lista.sort()
    return lista[tam//2]

def media(lista):
    soma=0.0
    n=len(lista)
    for val in lista:
        soma+=val
    return soma/n

def variancia(lista):
    soma=0.0
    n=len(lista)
    m=media(lista)
    for val in lista:
        soma+=(val-m)**2
    return soma/(n-1)
    
def desvio_padrao(lista):
    return variancia(lista)**0.5
  
def todas(lista):
    v1=media(lista)
    v2=mediana(lista)
    v3=variancia(lista)
    v4=desvio_padrao(lista)
    return [v1,v2,v3,v4]
