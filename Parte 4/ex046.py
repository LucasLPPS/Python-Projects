casa=float(input("Digite o valor da casa R$:"))
sal=float(input("Digite o valor do seu salário R$:"))
anos=int(input("Digite em quantos anos pretende pagar:"))
prest=(casa/anos)/12
if prest>(sal*0.3):
    print("Você não pode comprar essa casa infelizmente!"
    print("A prestação da casa vale {} e 30% do seu salário vale {}.".format(prest,sal*0.3))
else:
    print("Parabéns, você vai realizar o sonho da casa prórpia!")