cont=0
par=0
impar=0
n=1
while n!=0:
    n=int(input("Digite um número:"))
    if n!=0:
        cont=cont+1
    if n%2==0 and n!=0:
        par=par+1
    elif n%2!=0 and n!=0:
        impar=impar+1
print("Acabou a contagem.")
print("Você digitou {} números.".format(cont))
print("A quantidade de números pares é {} e ímpares é de {}.".format(par,impar))