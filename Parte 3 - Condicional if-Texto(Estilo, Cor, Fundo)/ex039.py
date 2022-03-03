dist=float(input("Digite a distância percorrida de uma viagem (Km):"))
if dist<=200:
    print("O valor da passagem será de R${} reais.".format(0.5*dist))
else:
    print("O valor da passagem será de R${} reais".format(0.45*dist))