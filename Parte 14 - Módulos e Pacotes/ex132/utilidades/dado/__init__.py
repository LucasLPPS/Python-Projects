def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(",",".").strip()
        if entrada.isalpha() or entrada == "":
            print("\033[0;31mPreço inválido.\033[m")
        else:
            válido = True
            return float(entrada)
