from ex130_2 import metade
from ex130_2 import dobro
from ex130_2 import aumentar
from ex130_2 import diminuir
from ex130_2 import moeda
num = float(input("Digite um preço (R$):"))
print(f"A metade de {moeda(num)} vale {moeda(metade(num))}.")
print(f"O dobro de {moeda(num)} vale {moeda(dobro(num))}.")
print(f"O aumento em 10% de {moeda(num)} vale {moeda(aumentar(num))}.")
print(f"A diminuição em 13% de {moeda(num)} vale {moeda(diminuir(num))}.")
# atenção que nesse caso estou chamando uma função dentro de outra:
# Ex: moeda(metade(num)) -> estou fazendo a função metade(), e colocando ela formatada
#                           de acordo com a função moeda()
