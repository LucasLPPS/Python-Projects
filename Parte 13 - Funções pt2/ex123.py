numeros = list()


def fatorial(num, show=False):
    if show is False:
        for c in range(1, num+1):
            numeros.append(c)
        produto = 1
        for c in numeros:
            produto = produto*c
        print(produto)
    if show is True:
        for c in range(1, num+1):
            numeros.append(c)
        produto = 1
        for c in numeros:
            produto = produto*c
        numeros.sort(reverse=True)
        for c in numeros:
            if c > 1:
                print(f"{c}", end=" x ")
            if c == 1:
                print(f"1 = {produto}")


print("-"*30)
fatorial(6, show=True)
