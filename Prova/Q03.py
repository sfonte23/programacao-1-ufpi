'''Faça um programa que recebe e armazena o nome, matrícula e o curso de alunos em uma lista. 
Após armazenar, o programa deve gravar todos os dados num arquivo dados.txt.'''
def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

        print(f'Arquivo {nome} criado com sucesso')

def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print(f'Houve um ERRO na criação do Arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def cadastrar(arq,lista):
    try:
        a= open(arq,'at')
    except:
        print('Houve um ERRO na abertura do Arquivo!')
    else:
        try:
            for n in lista:
                a.write(f'{n["nome"]},{n["matrícula"]},{n["curso"]}\n')
        except:
             print('ERRO ao escrever no Arquivo!')
        else:
            print(f'\033[32mNovo registro de pessoas adicionado com sucesso\033[m')
            a.close()

#Programa Principal
arquivo = 'dados.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

pessoa = {}
pessoas = []
while True:
    pessoa['nome'] = input('Nome: ').capitalize().title()
    while True:
        pessoa['matrícula'] = int(input('Número de Matrícula: '))
        if pessoa['matrícula'] != int:
            break
        else:
            print('ERRO! Por favor, o número de matrícula contém apenas números')
    pessoa['curso'] = input('Curso: ').title()
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = input('Quer continuar? [S|N] ').upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
        cadastrar(arquivo,pessoas)
        break
