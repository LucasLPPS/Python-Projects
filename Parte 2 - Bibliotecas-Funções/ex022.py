import math
num=float(input("Digite um número qualquer para saber sua porção inteira:"))
inteiro=math.floor(num)
print("A parte inteira de {} é {}".format(num,inteiro))
# outras formas de fazer seria usando as funções int(var) e math.trunc(var)
