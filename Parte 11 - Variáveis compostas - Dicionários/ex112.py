jogador = dict()
jogador['Nome'] = str(input("Nome do jogador:"))
partidas = int(input("Quantas partidas jogou:"))
gols = list()
total = 0
for c in range(0, partidas):
    gol = (int(input(f"Quantos gols na {c+1}º partida?")))
    total = total + gol
    gols.append(gol)
jogador['Gols'] = gols
jogador['total'] = total
print("-="*30)
print(jogador)
print("-="*30)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")
print("-="*30)
print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.")
for c in range(0, partidas):
    print(f"Na {c+1}º partida fez {jogador['Gols'][c]}")
print(f"Foi um total de {total} gols.")

