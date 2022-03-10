from random import randint
números = list()
from time import sleep


def sorteio():
    for c in range(0, 5):
        num = (randint(0, 11))
        print(f"{num}", end=" ")
        números.append(num)
        sleep(0.5)
    print("Pronto!")


print("Sorteando 5 valores:", end=" ")
sorteio()


def soma(*lista):
    s = 0
    for i in lista[0]:
        if i % 2 == 0:
            s = s + i
    print(s)


print(f"Somando os valores pares de {números}, temos", end=" ")
soma(números)





