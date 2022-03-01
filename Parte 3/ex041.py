num1=float(input("Digite o primeiro número:"))
num2=float(input("Digite o segundo número:"))
num3=float(input("Digite o terceiro número:"))
if num1>num2 and num2>num3:
    print("O maior número é {} e o menor é {}.".format(num1,num3))
else:
    if num1>num3 and num3>num2:
        print("O maior número é {} e o menor é {}.".format(num1,num2))
    else:
        if num2>num1 and num1>num3:
            print("O maior número é {} e o menor é {}.".format(num2,num3))
        else:
            if num2 > num3 and num3 > num1:
                print("O maior número é {} e o menor é {}.".format(num2, num1))
            else:
                if num3 > num1 and num1 > num2:
                    print("O maior número é {} e o menor é {}.".format(num3, num2))
                else:
                    if num3 > num2 and num2 > num1:
                        print("O maior número é {} e o menor é {}.".format(num3, num1))
                    else:
                        if num1==num2 or num2==num3 or num1==num3:
                            print("Existem números iguais, repita o processo!")
