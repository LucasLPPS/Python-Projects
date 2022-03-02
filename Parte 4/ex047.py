num=int(input("Digite um número:"))
print("Qual a base de conversão?")
print("1.Binário")
print("2.Octal")
print("3.Hexadecimal")
esc=int(input("Opção:"))
if esc==1:
    print("O número {} em binário é {}.".format(num,bin(num)))
elif esc==2:
    print("O número {} em octal é {}.".format(num,oct(num)))
elif esc==3:
    print("O número {} em hexadecimal é {}.".format(num,hex(num)))
elif esc!=1 and esc!=2 and esc!=3:
    print("Escolha uma opção válida!")