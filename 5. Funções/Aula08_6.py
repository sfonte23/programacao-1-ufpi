def dist_sem_retorno(p1,p2):
    distancia=((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)
    print(distancia)

def dist_com_retorno(p1,p2):
    distancia=((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)
    return distancia

print('1-exemplo sem usar função:')
print('2-exemplo com função sem retorno:')
print('3-exemplo com  função com retorno:')
opcao=int(input('Informe sua opção:'))
a,b,c=[0,0],[4,0],[2,4]
if opcao ==1:
    distancia = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)
    print(distancia)
    distancia = ((a[0] - c[0])**2 + (a[1] - c[1])**2)**(1/2)
    print(distancia)
    distancia = ((c[0] - b[0])**2 + (c[1] - b[1])**2)**(1/2)
    print(distancia)
elif opcao==2:
    dist_sem_retorno(a,b)
    dist_sem_retorno(a,c)
    dist_sem_retorno(c,b)
elif opcao==3:
    print(dist_com_retorno(a,b))
    print(dist_com_retorno(a,c))
    print(dist_com_retorno(c,b))
else:
    print('Opção inválida')
    
    
