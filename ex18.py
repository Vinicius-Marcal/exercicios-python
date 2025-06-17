cont = 0
soma = 0
for c in range(1,7):
    n = int(input("Escolha o {} número: ".format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print("A soma dos pares é igual a {}".format(soma))



