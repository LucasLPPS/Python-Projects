from ex131_2 import metade
from ex131_2 import dobro
from ex131_2 import aumentar
from ex131_2 import diminuir
from ex131_2 import moeda
num = float(input("Digite um preço (R$):"))
print(f"A metade de {moeda(num)} vale {metade(num, True)}.")
print(f"O dobro de {moeda(num)} vale {dobro(num, True)}.")
print(f"O aumento em 10% de {moeda(num)} vale {aumentar(num, True)}.")
print(f"A diminuição em 13% de {moeda(num)} vale {diminuir(num, True)}.")