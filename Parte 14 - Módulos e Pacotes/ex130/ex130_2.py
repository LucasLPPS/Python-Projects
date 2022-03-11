def metade(n=0):
    return n/2


def dobro(n=0):
    return n*2


def aumentar(n=0):
    return n + (0.1*n)


def diminuir(n=0):
    return n - (0.13*n)


def moeda(n=0, moeda="R$"):
    return f"{moeda}{n:>8.2f}".replace(".",",")