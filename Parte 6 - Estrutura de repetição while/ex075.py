n=int(input("Digite um número para saber seu fatorial:"))
num=n
fat=1
while num!=0:
    fat=fat*(num)
    num=num-1
print("O valor de {}! é {}.".format(n,fat))
# poderia ser usado a função for c in range (5,1,-1):
# mas nesse caso eu sei quais são os limites, o uso do while garante o uso do programa com qualquer termo
