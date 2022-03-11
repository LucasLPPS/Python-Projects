from ex129_2 import metade
from ex129_2 import dobro
from ex129_2 import aumentar
from ex129_2 import diminuir
# ou simplesmente usar import ex129_2
num = float(input("Digite um preço (R$):"))
print(f"A metade de R${num} vale R${metade(num)}.")
print(f"O dobro de R${num} vale R${dobro(num)}.")
print(f"O aumento em 10% de R${num} vale R${aumentar(num)}.")
print(f"A diminuição em 13% de R${num} vale R${diminuir(num)}.")

