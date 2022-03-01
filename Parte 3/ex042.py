sal=float(input("Digite seu salário para saber o novo salário com aumento (R$):"))
if sal>1250:
    print("O novo salário será de R${} reais.".format(sal+(sal*0.1)))
else:
    print("O novo salário será de R${} reais.".format(sal+(sal*0.15)))