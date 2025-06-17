num = int(input("Digite um número inteiro: "))
print('''Escolha uma das opções abaixo: 
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input(""))
b = bin(opcao)
o = oct(opcao)
h = hex(opcao)
if opcao == 1:
    print("Convertendo {} para binário, ficaria {}. ".format(num,b))
elif opcao == 2:
    print("Convertendo {} para octal, ficaria {}. ".format(num,o))
elif opcao == 3:
    print("Convertendo {} para hexa, ficaria {}. ".format(num,h))

