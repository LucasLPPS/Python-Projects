num=int(input("Digite um número inteiro para saber se é par ou ímpar:"))
if num<=0:
    print("Não pode ser zero nem negativo.")
else:
    if num%2==0:
        print("O número é par!")
    else:
        print("O número é ímpar!")