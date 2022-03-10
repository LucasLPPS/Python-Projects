from time import sleep


def linhas():
    print("-="*20)


linhas()
print("Contagem de 1 até 10 de 1 em 1:")
for c in range(1, 11):
    print(f"{c}", end=" ")
    sleep(0.5)
print("Fim.")
linhas()
print("Contagem de 10 até 0 de 2 em 2:")
for c in range(10, -1, -2):
    print(f"{c}", end=" ")
    sleep(0.5)
print("Fim.")
linhas()
print("Agora é a sua vez de personalizar a contagem.")


def contador(a, b, i):
    if i == 0:
        if a > b:
            for k in range(a, b-1, -1):
                print(f"{k}", end=" ")
                sleep(0.5)
            print("Fim.")
        if a < b:
            for k in range(a, b+1, 1):
                print(f"{k}", end=" ")
                sleep(0.5)
            print("Fim.")
    if a < b:
        if i > 0:
            for k in range(a, b, i):
                print(f"{k}", end=" ")
                sleep(0.5)
            print("Fim")
        elif i < 0:
            for k in range(a, b, -i):
                print(f"{k}", end=" ")
                sleep(0.5)
            print("Fim")
    elif a > b:
        if i > 0:
            for k in range(a, b, i):
                print(f"{k}", end=" ")
                sleep(0.5)
            print("Fim")
        elif i < 0:
            for k in range(a, b, -i):
                print(f"{k}", end=" ")
                sleep(0.5)
            print("Fim")


a = int(input("Início:"))
b = int(input("Fim:"))
i = int(input("Passo:"))
contador(a, b, i)



