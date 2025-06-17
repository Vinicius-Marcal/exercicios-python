from datetime import date

atual = date.today().year
nasc = int(input("nasceu em que ano? "))

idade = atual - nasc

if idade < 18:
    print("Você não está pronto para se alistar, ainda faltam {] anos.".format(18 - idade))
elif idade == 18:
    print("Você está na idade exata para se alistar!")
elif idade > 18:
    print("Você passou da hora de se alistar, ja fazem {} anos.".format(idade - 18))