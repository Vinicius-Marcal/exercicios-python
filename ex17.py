n = float(input("Escolha um número para fazer a tabuada: "))
cont = 1
for c in range(1,11):
    tab = n * c
    print("{} x {} = {}".format(n,cont,tab))
    cont += 1

