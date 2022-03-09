numspar=list()
numsimpar=list()
for c in range(0,7):
    num=int(input(f"Digite o {c+1}º valor:"))
    if num%2==0:
        numspar.append(num)
    else:
        numsimpar.append(num)
numspar.sort()
numsimpar.sort()
print(f"A lista par em ordem crescente: {numspar}")
print(f"A lista ímpar em ordem crescente: {numsimpar}")


