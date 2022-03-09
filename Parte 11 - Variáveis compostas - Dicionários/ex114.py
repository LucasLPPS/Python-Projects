atletas = list()
jogador = dict()
gols = list()
total = 0
while True:
    jogador['Nome'] = str(input("Nome do jogador:"))
    partidas = int(input("Quantas partidas jogou:"))
    for c in range(0, partidas):
        gol = (int(input(f"Quantos gols na {c + 1}º partida?")))
        total = total + gol
        gols.append(gol)
    jogador['Gols'] = gols.copy()
    jogador['total'] = total
    atletas.append(jogador.copy())
    jogador.clear()
    gols.clear()
    total = 0
    resp = str(input("Deseja cadastrar outro jogador? [S/N]:")).strip().upper()[0]
    while resp != "S" and resp != "N":
        print("Escolha uma opção válida!")
        resp = str(input("[S/N]:")).strip().upper()[0]
    print("-" * 50)
    if resp == "N":
        break
# --------------------------------------------- ok
print("-=" * 30)
print("Cod  nome        gols            total")
print("-" * 50)
for c in range(0, len(atletas)):
    print(c, end="")
    print(f"    {atletas[c]['Nome']:<12}", end="")
    print(f"{atletas[c]['Gols']}", end="")
    print(f"{atletas[c]['total']:>7}")
# --------------------------------- ok
while True:
    escolha = int(input("Mostrar dados de qual jogador?"))
    if escolha == 999:
        break
    while (escolha < 0) and (escolha > len(atletas)) and (escolha != 999):
        print("Escolha uma opção válida!")
        escolha = int(input("Opção:"))
    if resp == 999:
        break
    for c in range(0, len(atletas[escolha]['Gols'])):
        if escolha == c:
            for i in range(0, len(atletas[escolha]['Gols'])):
                print(f"No jogo {i}, {atletas[c]['Nome']} fez {atletas[c]['Gols'][i]} gols.")
print("Programa finalizando...")
# --------------------------------------------
