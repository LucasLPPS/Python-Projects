num1=float(input("Digite o primeiro valor:"))
num2=float(input("Digite o segundo valor:"))
if num1>num2:
    print("O número {} é maior do que o número {}.".format(num1,num2))
elif num2>num1:
    print("O número {} é maior do que o número {}.".format(num2, num1))
elif num1==num2:
    print("Os dois números são iguais.")