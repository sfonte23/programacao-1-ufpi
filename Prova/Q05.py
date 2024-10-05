'''Faça uma função que dado um dicionário que armazena o nome, 
matrícula e o curso de alunos, retorna todos os dados dos
alunos de um determinado curso.'''

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um ERRO ao abrir o Arquivo!')
    else:
        for linha in a:
            dado = linha.split(',')
            dado[1] = dado[1].replace('\n', '')
            aluno['nome'] = dado[0].strip()
            aluno['matrícula'] = dado[1].strip()
            aluno['curso'] = dado[2].strip()
            listadealunos.append(aluno.copy())
            aluno.clear()
    finally:
        a.close()

def vercursos(lista):
    i=0
    for j in lista:
        if j["curso"] not in cursos:
            cursos.append(j["curso"])
            print(f'{i} - {j["curso"]}')
            i+=1

def alunosPorCurso(lista, curso_desejado):
    alunos_do_curso = []
    for aluno in lista:
        if aluno["curso"] == curso_desejado:
            alunos_do_curso.append(aluno)
    return alunos_do_curso

# Programa Principal
arq = 'dados.txt'
listadealunos = []
aluno = {}
cursos = []

lerArquivo(arq)
print('=-' * 20)
print('Qual curso deseja verificar os alunos?')

vercursos(listadealunos)

print('=-' * 20)

curso_desejado = input("Digite o nome do curso desejado: ").title()
if curso_desejado.isnumeric():
    curso_desejado = int(curso_desejado)
    if curso_desejado >= 0 and curso_desejado < len(cursos):
        curso_desejado = cursos[curso_desejado]
    else:
        print("Número de curso inválido.")

alunos = alunosPorCurso(listadealunos, curso_desejado)

if alunos:
    print(f"\033[32mAlunos do curso '{curso_desejado}':\033[m")
    for aluno in alunos:
        print(f"\033[35mNome: \033[m{aluno['nome']} - \033[36mMatrícula:\033[m {aluno['matrícula']}")
    print('=-' * 20)
else:
    print(f"Não há alunos no curso '{curso_desejado}'.")

