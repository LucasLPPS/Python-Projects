n1=int(input("Digite um valor:"))
n2=int(input("Digite um segundo valor:"))
s=n1+n2
#print("A soma entre",n1,"e",n2,"vale",s) --> primeira forma de mostrar a soma.
# forma mais organizada
print("A soma entre {} e {} vale {}".format(n1,n2,s))