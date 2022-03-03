n1=int(input("Digite o primeiro termo de uma PA:"))
r=int(input("Digie sua razão:"))
an=n1+(9*r)
print(n1)
for c in range(n1,an,r):
    n1=n1+r
    print("{}".format(n1))