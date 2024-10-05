'''Faça um programa que lê um arquivo chamado dados.txt, que armazena o nome, 
matrícula e o curso de alunos. Esses dados devem ser carregados em um dicionário.'''

def lerArquivo(nome):
    try:
        a= open(nome,'rt')
    except:
        print('Houve um ERRO ao abrir o Arquivo!')
    else:
        for linha in a:
            dado = linha.split(',')
            dado[1] = dado[1].replace('\n','')
            aluno['nome'] = dado[0].strip()
            aluno['matrícula'] = dado[1].strip()
            aluno['curso'] = dado[2].strip()
            listadealunos.append(aluno.copy())
            aluno.clear()
    finally:
        a.close()

#Programa Principal
arq = 'dados.txt'
listadealunos = []
aluno={}
lerArquivo(arq)
for i,j in enumerate(listadealunos):
    print(f'Aluno {i+1}: {j} ')