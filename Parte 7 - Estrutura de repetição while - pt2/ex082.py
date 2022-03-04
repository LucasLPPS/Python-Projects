while True:
    n=int(input("Digite um número para saber sua tabuada:"))
    if n<0:
        break
    print(f"A tabuada de {n} é:")
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
print("Programa finalizado.")
