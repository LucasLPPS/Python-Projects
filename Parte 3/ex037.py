vel=float(input("Digite a velocidade do carro (Km/h):"))
if vel>=80:
    multa=(vel-80)*7
    print("Sua velocidade foi {}Km/h, e ultrapassou a velocidade máxima!".format(vel))
    print("O valor da multa será de R${} reais".format(multa))
else:
    print("Velocidade dentro do permitido.")
