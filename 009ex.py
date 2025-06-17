import random
n = random.randint(0,5)
nu = int(input("Qual o número? "))
if n == nu:
    print("Acertou, parabéns!")
else:
    print("Você errou!")
    print("O numero era {}!".format(n))


