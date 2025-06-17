import math
a = float(input("Digite o ângulo que deseja: "))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print("O seno de {} vai ser igual a: {}.".format(a,s))
print("O cosseno de {} vai ser igual a: {}.".format(a,c))
print("A tangente de {} vai ser igual a: {}.".format(a,t))