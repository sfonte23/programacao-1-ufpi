'''Exemplo:
Definindo uma função que solicita dois números 
ao usuário, realiza a soma e exibe o resultado'''

def func_somar(n1,n2):
    resultado = int(n1+n2)
    return resultado;

# Solicita ao usuário que insira 2 números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

#chama a função
solucao = func_somar(n1,n2)    
# Exibe o resultado
print("A soma é:", solucao)