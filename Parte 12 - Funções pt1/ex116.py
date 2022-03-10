print("Controle de Terrenos")
print("-"*30)


def area(a, b):
    ar = a*b
    print(f"A área de um terreno {a}x{b} é de {ar}m².")


largura = float(input("Largura (m):"))
comprimento = float(input("Comprimento (m):"))
area(largura, comprimento)
