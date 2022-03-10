def ficha(nome="", gols=0):
    if nome != "" and gols != 0:
        print(f"O jogador {nome} fez {gols} gols no campeonato.")
    elif nome == "":
        print(f"O jogador <desconhecido> fez {gols} gols no campeonato.")
    elif gols == 0:
        print(f"O jogador {nome} fez 0 gols no campeonato.")
    elif nome == "" and gols == 0:
        print("O jogador <desconhecido> fez 0 gols no campeonato.")


ficha("ronaldo", 5)
