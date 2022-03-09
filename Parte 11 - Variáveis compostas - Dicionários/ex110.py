'''
jogadores = list()
jogador = dict()
from random import randint
from time import sleep
from operator import itemgetter
for c in range(0, 4):
    jogador['nome'] = str(input("Digite o nome do jogador:"))
    jogador['numdado'] = int(randint(1, 6))
    jogadores.append(jogador.copy())
# -------------------------------------- ok
for c in range(0, 4):
    print(f"O jogador {jogadores[c]['nome']} tirou {jogadores[c]['numdado']}")
    sleep(1)
# -------------------------------------- ok
vencedores = jogadores.copy()
print(vencedores) # tentar colocar em ordem da forma que está'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {"jogador1": randint(1, 6),
        "jogador2": randint(1, 6),
        "jogador3": randint(1, 6),
        "jogador4": randint(1, 6)}
print("Valores sorteados:")
for k,v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # pega pelo value para fazer a ordem, e usa-se o reverse para colocar em ordem descrescente
print("-="*20)
for k,v in enumerate(ranking):
    print(f"{k+1} lugar: {v[0]} com {v[1]}")
    sleep(1)

