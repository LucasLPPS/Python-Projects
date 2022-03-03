n1=int(input("Digite o primeiro termo de uma PA:"))
r=int(input("Digie sua razão:"))
an=n1+(9*r)
for c in range(n1,an,r):
    print("{} ".format(n1), end=" ")
    n1=n1+r
