n=int(input("Digite um número para saber seu fatorial:"))
num=n
fat=1
while num!=0:
    fat=fat*(num)
    num=num-1
print("O valor de {}! é {}.".format(n,fat))
