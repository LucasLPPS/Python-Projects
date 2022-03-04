n=int(input("Digite quantos termos da série fibonacci você quer visualizar:"))
c=0
c2=1
c3=0
cont=0
while n!=cont:
    print("{}".format(c), end=" -> ")
    c3=c+c2
    c=c2
    c2=c3
    cont=cont+1
print("Fim.")

