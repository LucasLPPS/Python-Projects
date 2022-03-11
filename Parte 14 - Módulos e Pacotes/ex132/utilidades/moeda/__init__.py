def metade(n=0, format=False):
    res = n/2
    return res if format is False else moeda(res)


def dobro(n=0, formato=False):
    res = n*2
    return res if formato is False else moeda(res)


def aumentar(n=0, formato=False):
    res = n + (0.1*n)
    return res if formato is False else moeda(res)


def diminuir(n=0, formato=False):
    res = n - (0.13*n)
    return res if formato is False else moeda(res)


def moeda(n=0, moeda="R$"):
    return f"{moeda}{n:>8.2f}".replace(".", ",")


def resumo(n):
    print("-"*30)
    print("Resumo do Valor".center(30))
    print("-"*30)
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço: \t{dobro(n,True)}")
    print(f"Metade do preço: \t{metade(n, True)}")
    print(f"10% de aumento: \t{aumentar(n, True)}")
    print(f"13% de redução: \t{diminuir(n, True)}")
    print("-"*30)