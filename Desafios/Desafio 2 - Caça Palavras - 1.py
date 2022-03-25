import string
import random
print("-=" * 15)
titulo = "CAÇA PALAVRAS"
print(titulo.center(30))
print("-=" * 15)
palavras = list()
while True:
    quant = int(input("Quantas palavras deseja? Escolha de 1-5 (0 para finalizar):"))
    while quant not in range(0, 6):
        print("Escolha uma quantidade válida!")
        quant = int(input("1-5 (0 para finalizar):"))
    if quant == 0:
        break
    for c in range(0, quant):
        temp = str(input(f"Digite a {c + 1}º palavra:")).upper()
        palavras.append(temp)
    print(palavras) # excluir
    matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for l in range(0, 10):
        for c in range(0, 40):
            matriz[l][c] = random.choice(string.ascii_letters.upper()) # pega um elemento do alfabeto (A-Z) por vez
    print("-=" * 15)
    # ---------------------------------------------- ok
    if quant == 1:
        escolha = random.choice([0, 1]) # randomizando se vai estar ao contrário
        if escolha == 0:
            palavralista = list(palavras[0])
        elif escolha == 1:
            palavralista = list(palavras[0])
            palavralista.reverse()
        posição = random.choice(["horiz", "vert"])
        if posição == "horiz" or len(palavralista[0]) > 10:
            l2 = random.randint(0, 10)
            c2 = random.randint(0, 20)
            for c in range(0, len(palavralista)):
                matriz[l2][c2+c] = palavralista[c]
        if posição == "vert":
            l2 = 0
            c2 = random.randint(0, 40)
            for c in range(0, len(palavralista)):
                matriz[l2+c][c2] = palavralista[c]
    # ---------------------------------------------- ok
    if quant == 2:
        # para a 1º palavra:
        escolha = random.choice([0, 1])
        if escolha == 0:
            palavralista = list(palavras[0])
        elif escolha == 1:
            palavralista = list(palavras[0])
            palavralista.reverse()
        # para a 2º palavra:
        escolha1 = random.choice([0, 1])
        if escolha1 == 0:
            palavralista1 = list(palavras[1])
        elif escolha1 == 1:
            palavralista1 = list(palavras[1])
            palavralista1.reverse()
        # para a 1º palavra:
        posição = random.choice(["horiz", "vert"])
        if posição == "horiz" or len(palavralista) > 10:
            l2 = random.randint(0, 10)
            c2 = random.randint(0, 20)
            for c in range(0, len(palavralista)):
                matriz[l2][c2+c] = palavralista[c]
        if posição == "vert":
            l2 = 0
            c2 = random.randint(0, 40)
            for c in range(0, len(palavralista)):
                matriz[l2+c][c2] = palavralista[c]
        # para a 2º palavra:
        posição1 = random.choice(["horiz", "vert"])
        if posição1 == "horiz" or len(palavralista1) > 10:
            l2_1 = random.randint(0, 10)
            c2_1 = random.randint(0, 20)
            for c in range(0, len(palavralista1)):
                matriz[l2_1][c2_1 + c] = palavralista1[c]
        if posição1 == "vert":
            l2_1 = 0
            c2_1 = random.randint(0, 40)
            for c in range(0, len(palavralista1)):
                matriz[l2_1 + c][c2_1] = palavralista1[c]
    # ---------------------------------------------------- ok
    if quant == 3:
        # para a 1º palavra:
        escolha = random.choice([0, 1])
        if escolha == 0:
            palavralista = list(palavras[0])
        elif escolha == 1:
            palavralista = list(palavras[0])
            palavralista.reverse()
        # para a 2º palavra:
        escolha1 = random.choice([0, 1])
        if escolha1 == 0:
            palavralista1 = list(palavras[1])
        elif escolha1 == 1:
            palavralista1 = list(palavras[1])
            palavralista1.reverse()
        # para a 3º palavra:
        escolha2 = random.choice([0, 1])
        if escolha2 == 0:
            palavralista2 = list(palavras[2])
        elif escolha2 == 1:
            palavralista2 = list(palavras[2])
            palavralista2.reverse()
        # para a 1º palavra:
        posição = random.choice(["horiz", "vert"])
        if posição == "horiz" or len(palavralista) > 10:
            l2 = random.randint(0, 10)
            c2 = random.randint(0, 20)
            for c in range(0, len(palavralista)):
                matriz[l2][c2+c] = palavralista[c]
        if posição == "vert":
            l2 = 0
            c2 = random.randint(0, 40)
            for c in range(0, len(palavralista)):
                matriz[l2+c][c2] = palavralista[c]
        # para a 2º palavra:
        posição1 = random.choice(["horiz", "vert"])
        if posição1 == "horiz" or len(palavralista1) > 10:
            l2_1 = random.randint(0, 10)
            c2_1 = random.randint(0, 20)
            for c in range(0, len(palavralista1)):
                matriz[l2_1][c2_1 + c] = palavralista1[c]
        if posição1 == "vert":
            l2_1 = 0
            c2_1 = random.randint(0, 40)
            for c in range(0, len(palavralista1)):
                matriz[l2_1 + c][c2_1] = palavralista1[c]
        # para a 3º palavra:
        posição2 = random.choice(["horiz", "vert"])
        if posição2 == "horiz" or len(palavralista2) > 10:
            l2_2 = random.randint(0, 10)
            c2_2 = random.randint(0, 20)
            for c in range(0, len(palavralista2)):
                matriz[l2_2][c2_2 + c] = palavralista2[c]
        if posição2 == "vert":
            l2_2 = 0
            c2_2 = random.randint(0, 40)
            for c in range(0, len(palavralista2)):
                matriz[l2_2 + c][c2_2] = palavralista2[c]
    # --------------------------------------------------- ok
    if quant == 4:
        # para a 1º palavra:
        escolha = random.choice([0, 1])
        if escolha == 0:
            palavralista = list(palavras[0])
        elif escolha == 1:
            palavralista = list(palavras[0])
            palavralista.reverse()
        # para a 2º palavra:
        escolha1 = random.choice([0, 1])
        if escolha1 == 0:
            palavralista1 = list(palavras[1])
        elif escolha1 == 1:
            palavralista1 = list(palavras[1])
            palavralista1.reverse()
        # para a 3º palavra:
        escolha2 = random.choice([0, 1])
        if escolha2 == 0:
            palavralista2 = list(palavras[2])
        elif escolha2 == 1:
            palavralista2 = list(palavras[2])
            palavralista2.reverse()
        # para a 4º palavra:
        escolha3 = random.choice([0, 1])
        if escolha3 == 0:
            palavralista3 = list(palavras[3])
        elif escolha3 == 1:
            palavralista3 = list(palavras[3])
            palavralista3.reverse()
        # para a 1º palavra:
        posição = random.choice(["horiz", "vert"])
        if posição == "horiz" or len(palavralista) > 10:
            l2 = random.randint(0, 10)
            c2 = random.randint(0, 20)
            for c in range(0, len(palavralista)):
                matriz[l2][c2+c] = palavralista[c]
        if posição == "vert":
            l2 = 0
            c2 = random.randint(0, 40)
            for c in range(0, len(palavralista)):
                matriz[l2+c][c2] = palavralista[c]
        # para a 2º palavra:
        posição1 = random.choice(["horiz", "vert"])
        if posição1 == "horiz" or len(palavralista1) > 10:
            l2_1 = random.randint(0, 10)
            c2_1 = random.randint(0, 20)
            for c in range(0, len(palavralista1)):
                matriz[l2_1][c2_1 + c] = palavralista1[c]
        if posição1 == "vert":
            l2_1 = 0
            c2_1 = random.randint(0, 40)
            for c in range(0, len(palavralista1)):
                matriz[l2_1 + c][c2_1] = palavralista1[c]
        # para a 3º palavra:
        posição2 = random.choice(["horiz", "vert"])
        if posição2 == "horiz" or len(palavralista2) > 10:
            l2_2 = random.randint(0, 10)
            c2_2 = random.randint(0, 20)
            for c in range(0, len(palavralista2)):
                matriz[l2_2][c2_2 + c] = palavralista2[c]
        if posição2 == "vert":
            l2_2 = 0
            c2_2 = random.randint(0, 40)
            for c in range(0, len(palavralista2)):
                matriz[l2_2 + c][c2_2] = palavralista2[c]
        # para a 4º palavra:
        posição3 = random.choice(["horiz", "vert"])
        if posição3 == "horiz" or len(palavralista3) > 10:
            l2_3 = random.randint(0, 10)
            c2_3 = random.randint(0, 20)
            for c in range(0, len(palavralista3)):
                matriz[l2_3][c2_3 + c] = palavralista3[c]
        if posição3 == "vert":
            l2_3 = 0
            c2_3 = random.randint(0, 40)
            for c in range(0, len(palavralista3)):
                matriz[l2_3 + c][c2_3] = palavralista3[c]
    # --------------------------------------------------- ok
    if quant == 5:
        # para a 1º palavra:
        escolha = random.choice([0, 1])
        if escolha == 0:
            palavralista = list(palavras[0])
        elif escolha == 1:
            palavralista = list(palavras[0])
            palavralista.reverse()
        # para a 2º palavra:
        escolha1 = random.choice([0, 1])
        if escolha1 == 0:
            palavralista1 = list(palavras[1])
        elif escolha1 == 1:
            palavralista1 = list(palavras[1])
            palavralista1.reverse()
        # para a 3º palavra:
        escolha2 = random.choice([0, 1])
        if escolha2 == 0:
            palavralista2 = list(palavras[2])
        elif escolha2 == 1:
            palavralista2 = list(palavras[2])
            palavralista2.reverse()
        # para a 4º palavra:
        escolha3 = random.choice([0, 1])
        if escolha3 == 0:
            palavralista3 = list(palavras[3])
        elif escolha3 == 1:
            palavralista3 = list(palavras[3])
            palavralista3.reverse()
        # para a 5º palavra:
        escolha4 = random.choice([0, 1])
        if escolha4 == 0:
            palavralista4 = list(palavras[4])
        elif escolha4 == 1:
            palavralista4 = list(palavras[4])
            palavralista4.reverse()
        # para a 1º palavra:
        posição = random.choice(["horiz", "vert"])
        if posição == "horiz" or len(palavralista) > 10:
            l2 = random.randint(0, 10)
            c2 = random.randint(0, 20)
            for c in range(0, len(palavralista)):
                matriz[l2][c2+c] = palavralista[c]
        if posição == "vert":
            l2 = 0
            c2 = random.randint(0, 40)
            for c in range(0, len(palavralista)):
                matriz[l2+c][c2] = palavralista[c]
        # para a 2º palavra:
        posição1 = random.choice(["horiz", "vert"])
        if posição1 == "horiz" or len(palavralista1) > 10:
            l2_1 = random.randint(0, 10)
            c2_1 = random.randint(0, 20)
            for c in range(0, len(palavralista1)):
                matriz[l2_1][c2_1 + c] = palavralista1[c]
        if posição1 == "vert":
            l2_1 = 0
            c2_1 = random.randint(0, 40)
            for c in range(0, len(palavralista1)):
                matriz[l2_1 + c][c2_1] = palavralista1[c]
        # para a 3º palavra:
        posição2 = random.choice(["horiz", "vert"])
        if posição2 == "horiz" or len(palavralista2) > 10:
            l2_2 = random.randint(0, 10)
            c2_2 = random.randint(0, 20)
            for c in range(0, len(palavralista2)):
                matriz[l2_2][c2_2 + c] = palavralista2[c]
        if posição2 == "vert":
            l2_2 = 0
            c2_2 = random.randint(0, 40)
            for c in range(0, len(palavralista2)):
                matriz[l2_2 + c][c2_2] = palavralista2[c]
        # para a 4º palavra:
        posição3 = random.choice(["horiz", "vert"])
        if posição3 == "horiz" or len(palavralista3) > 10:
            l2_3 = random.randint(0, 10)
            c2_3 = random.randint(0, 20)
            for c in range(0, len(palavralista3)):
                matriz[l2_3][c2_3 + c] = palavralista3[c]
        if posição3 == "vert":
            l2_3 = 0
            c2_3 = random.randint(0, 40)
            for c in range(0, len(palavralista3)):
                matriz[l2_3 + c][c2_3] = palavralista3[c]
        # para a 5º palavra:
        posição4 = random.choice(["horiz", "vert"])
        if posição4 == "horiz" or len(palavralista4) > 10:
            l2_4 = random.randint(0, 10)
            c2_4 = random.randint(0, 20)
            for c in range(0, len(palavralista4)):
                matriz[l2_4][c2_4 + c] = palavralista4[c]
        if posição4 == "vert":
            l2_4 = 0
            c2_4 = random.randint(0, 40)
            for c in range(0, len(palavralista4)):
                matriz[l2_4 + c][c2_4] = palavralista4[c]
    # procurar forma de proteger as posições onde já existem palavras
    for l in range(0, 10):
        for c in range(0, 40):
            print(f"{matriz[l][c]}", end="")
        print()  # para quebrar a linha
    print()
    palavras.clear()
    # -------------------------------------------
    resp = str(input("Deseja cadastrar outro caça palavras? [S/N]:")).strip().upper()[0]
    while resp != "S" and resp != "N":
        print("Escolha uma opção válida!")
        resp = str(input("[S/N]:")).strip().upper()[0]
    if resp == "N":
        break
print("Programa finalizado.")
