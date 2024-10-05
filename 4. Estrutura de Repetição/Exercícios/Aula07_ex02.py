'''
O cardápio de uma lanchonete é o seguinte:
100 Cachorro quente 	11,00
101 Misto simples 	    13,00
102 Misto c/ovo 	    15,00
103 Hamburger 	        11,00
104 Cheeseburger 	    13,00
105 Refrigerante 	    10,00

Escreva um algoritmo que leia o código do item pedido, 
a quantidade e calcule o valor a ser pago por aquele lanche. 
O algoritmo só finalize se o código informado for zero.
'''
cardapio = ['Cachorro quente','Misto simples','Misto c/ovo','Hamburger','Cheeseburger','Refrigerante']
valores = [11,13,15,11,13,10]
while True:
    print('-'*28)
    print('BEM-VINDO A LANCHONETE UFPI')
    print('''----------------------------
[100] Cachorro quente 	- R$11,00
[101] Misto simples     - R$13,00
[102] Misto c/ovo 	 - R$15,00
[103] Hamburger 	 - R$11,00
[104] Cheeseburger 	 - R$13,00
[105] Refrigerante 	 - R$10,00
\033[31m[ 0 ] SAIR\033[m''')
    cod = int(input('Digite o código do item: '))
    if cod == 0:
        print('Saindo!')
        break
    else:
        qtd = int(input('Quantos itens? '))
        print('-'*30)
        print(f'Você pediu {qtd}x {cardapio[(cod-100)]} o valor total é de R${valores[(cod-100)]*qtd},00')


    
