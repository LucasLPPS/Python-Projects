from time import sleep


def maior(*num):
    if not num: # chamada para checar se a lista está vazia
        print("Foram digitados 0 valores ao todo.")
    else:
        for c in range(0, len(num)):
            print(f"{num[c]}", end=" ")
            sleep(0.5)
        print(f"Foram informados {len(num)} valores ao todo.")
        print(f"O maior valor foi {max(num)}.")
        print("-="*20)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


