from random import choice
from time import sleep

#variáveis para contabilização
ponto = empate = perda = contador = 0

print('=-'*12)
print(' PEDRA, PAPEL E TESOURA')
print('=-'*12)

while True:
    jokenpo = [1,2,3]
    jogador = int(input(" [0] - Sair ❌\n [1] - Pedra 🤜\n [2] - Papel 🖖\n [3] - Tesoura ✌\nEscolha a sua opção: "))
    computador = choice(jokenpo)
    contador += 1
    if jogador <= 3:
        if jogador == 0:
            break
        
        #pausa dramática
        print('\nJo')
        sleep(0.5)
        print('Ken')
        sleep(0.5)
        print('Po!\n')
        sleep(0.5)

        #Quando o computador escolhe o mesmo que o jogador.
        if computador == jogador:
            empate += 1
            print('\033[034mEmpate!\033[m Tente de novo!')

        #Quando computador joga pedra
        elif computador == 1 and jogador == 2:
                ponto += 1
                print('(PC) 🤜  x 🖖  (Você)')
                print('\033[032mGanhou!\033[m')

        elif computador == 1 and jogador == 3:
                perda += 1
                print('(PC) 🤜  x ✌  (Você)')
                print('\033[031mPerdeu!\033[m')

        #Quando computador joga Papel
        elif computador == 2 and jogador == 1:
                perda += 1
                print('(PC) 🖖  x 🤜  (Você)')
                print('\033[031mPerdeu!\033[m')
            
        elif computador == 2 and jogador == 3:
                ponto += 1
                print('(PC) 🖖  x ✌  (Você)')
                print('\033[032mGanhou!\033[m')

        #Quando computador joga tesoura:       
        elif computador == 3 and jogador == 1:
                ponto += 1
                print('(PC) ✌  x 🤜  (Você)')
                print('\033[032mGanhou!\033[m')

        elif computador == 3 and jogador == 2:
                perda += 1
                print('(PC) ✌  x 🖖  (Você)')
                print('\033[031mPerdeu!\033[m')

    #caso escolha outro número fora
    else:
        print("Opção Inválida!\n")

    print("=-"*15) 
#resultados      
print("\nVolte Sempre 👋")
if contador != 1:
    print(f"\nVocê fez \033[32m{ponto}\033[m ponto(s)")
    print(f"Você empatou: \033[34m{empate}\033[m vez(es)")
    print(f"Você perdeu: \033[31m{perda}\033[m vez(es)")

print('''
   ---------------------------.
 `/""""/""""/|""|'|""||""|   ' \.
 /    /    / |__| |__||__|      |
/----------=====================|
| \  /V\  /    _. \033[33mUFPI – PROG I\033[m |
|()\ \W/ /()   _10  na  Kombi   |
|   \   /     / \ \033[31mGrupo D\033[m  / \  |-( )
=C========C==_| ) |--------| ) _/==] _-{_}_)
 \_\_/__..  \_\_/_ \_\_/ \_\_/__.__.''')