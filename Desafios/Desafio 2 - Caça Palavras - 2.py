import numpy as np
import random
import string

print("-=" * 15)
titulo = "CAÇA PALAVRAS"
print(titulo.center(30))
print("-=" * 15)

quant = 'str'
while True:
    while True:
        quant = input("Quantas palavras deseja? (0 para finalizar):").strip()
        if quant == "0":
            break
        elif quant.isnumeric():
            quant = int(quant)
            break
        elif type(quant) == str:
            print("Opção inválida. Tente novamente.")
    if quant == "0":
        print("Volte sempre!")
        break
    # --------------------------------------------------------------------------
    # armazenando as palavras:
    while True:
        palavras = list()
        for c in range(0, quant):
            temp = input(f"Digite a {c + 1}º palavra:").strip().upper()
            temp2 = temp.replace(" ", "")
            if temp2.isalpha():
                palavras.append(list(temp2))
            else:
                while not temp2.isalpha():
                    print("Palavra inválida.")
                    temp = input(f"Digite a {c + 1}º palavra novamente:").strip().upper()
                    temp2 = temp.replace(" ", "")
                    if temp2.isalpha():
                        palavras.append(list(temp2))
        break

    # --------------------------------------------------------------------------

    # randomizando se vai estar ao contrário
    for c in palavras:
        escolha = random.choice([0, 1])
        if escolha == 0:
            c.reverse()

    # --------------------------------------------------------------------------

    # criando uma matriz de controle e transformando-a em str:
    matriz = np.random.randint(1, 2, (quant+15, quant+40))
    matriz_nova = matriz.astype('str')

    # colocando letras aleatórias na matriz de str:
    for c in range(0, quant+15):
        for i in range(0, quant+40):
            matriz_nova[c][i] = random.choice(string.ascii_letters.upper())

    # --------------------------------------------------------------------------

    # colocando as palavras na matriz:
    respostas = list()
    for c in range(0, len(palavras)):
        pos = random.choice(["horiz", "vert"])
        if pos == "horiz" or len(palavras[c]) > 20:
            lin = random.randint(0, quant+5)
            col = random.randint(0, quant+15)
            resp = (lin, col)
            respostas.append(resp)
            for i in range(0, len(palavras[c])):
                matriz_nova[lin][col] = palavras[c][i]
                col = col + 1
        elif pos == "vert":
            lin = random.randint(0, 5)
            col = random.randint(0, quant+40)
            resp = lin, col
            respostas.append(resp)
            for i in range(0, len(palavras[c])):
                matriz_nova[lin][col] = palavras[c][i]
                lin = lin + 1

    # ---------------------------------------------------------------------------

    # mostrando a matriz com o desafio:
    for c in range(0, quant+15):
        for i in range(0, quant+40):
            print(f'{matriz_nova[c][i]} ', end="")
        print()

    # ---------------------------------------------------------------------------

    # perguntando se gostaria de ver a resposta
    ans = str(input("Deseja ver a resposta? [S/N]:")).strip().upper()[0]
    if ans == "S":
        for r in range(0, len(respostas)):
            print(f"{r+1}º palavra na posição: {respostas[r]}.")
    elif ans != "S" or ans != "N":
        while True:
            print("Escolha [S/N]!")
            ans = str(input("[S/N]:")).strip().upper()[0]
            if ans == "S" or ans == "N":
                break
        if ans == "S":
            for r in range(0, len(respostas)):
                print(f"{r + 1}º palavra na posição: {respostas[r]}.")

    # encontrar se existe uma forma de colorir as posições onde se encontram as palavras

    # ---------------------------------------------------------------------------

    # perguntando se gostaria de jogar novamente
    ans2 = str(input("Deseja jogar novamente? [S/N]:")).strip().upper()[0]
    if ans2 == "N":
        print("Volte sempre!")
        break # referente ao while True inicial
    else:
        while True:
            print("Escolha [S/N]!")
            ans2 = str(input("[S/N]:")).strip().upper()[0]
            if ans2 == "S" or ans2 == "N":
                break
        if ans2 == "N":
            print("Volte sempre!")
            break  # referente ao while True inicial

    # ---------------------------------------------------------------------------

# fazer testes
print("Programa finalizado.")
