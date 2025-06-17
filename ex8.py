import random
p = str(input("Primeiro aluno: "))
s = str(input("Segundo aluno: "))
t = str(input("terceiro aluno: "))
q = str(input("Quarto aluno: "))
lista = [p,s,t,q]
random.shuffle(lista)
print("aluno escolhido foi: {}".format(lista))