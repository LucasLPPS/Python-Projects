maior=0
menor=1000
for c in range(1,6):
    peso=float(input("Digite o peso da {}º pessoa (Kg):".format(c)))
    if peso>maior:
        maior=peso
    if peso<menor:
        menor=peso
print("O maior peso foi de {}Kg, e o menor peso foi de {}Kg.".format(maior, menor))