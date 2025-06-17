soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        soma = soma + c
print("O resultado da soma de todos os números divisíveis por três é igual a: {}".format(soma))