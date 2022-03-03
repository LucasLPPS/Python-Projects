n=int(input("Digite um número para saber se ele é primo:"))
if n==2 or n==3 or n==5 or n==7:
    print("O número é primo.")
elif n==1 or n%2==0 or n%3==0 or n%5==0 or n%7==0:
    print("O número não é primo.")
else:
    print("O número é primo.")