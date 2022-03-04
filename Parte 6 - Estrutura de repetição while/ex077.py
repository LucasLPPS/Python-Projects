n1=int(input("Digite o primeiro termo de uma PA:"))
r=int(input("Digie sua razão:"))
an=n1+(9*r)
c=0
while n1!=an+1:
    print("{} ".format(n1), end=" ")
    n1=n1+r
n2=n1
termos=1
while termos!=0:
    termos=int(input("\nQuantos termos a mais vc gostaria de saber?"))
    an2 = n2 + ((termos-1) * r)
    while n2!=an2+1:
        print("{} ".format(n2), end=" ")
        n2 = n2 + r

