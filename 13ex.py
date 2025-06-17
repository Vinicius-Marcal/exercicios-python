from random import randint
itens = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0,2)

print("E aí, qual vai ser a sua jogada?")
print('''Opções:

        [0] Pedra
        [1] Papel
        [2] Tesoura
        ''')
jog = int(input(""))
print("O computador escolheu {}".format(itens[comp]))
if comp == 0:
    if jog == 0:
        print("O jogo empatou!")
    elif jog == 1:
        print("Você ganhou!")
    elif jog == 2:
        print("Você perdeu")
elif comp == 1:
    if jog == 0:
        print("Você perdeu")
    elif jog == 1:
        print("O jogo empatou!")
    elif jog == 2:
        print("Você ganhou")
elif comp == 2:
    if jog == 0:
        print("Você ganhou")
    elif jog == 1:
        print("Você perdeu")
    elif jog == 2:
        print("O jogo empatou")
