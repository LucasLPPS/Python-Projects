preço=float(input("Digite o preço do produto (R$):"))
print("Escolha a forma de pagamento:")
print("1. À vista no dinheiro.")
print("2. À vista no cartão.")
print("3. Em até 2x no cartão.")
print("4. 3x ou mais no cartão.")
pag=int(input("Opção:"))
if pag==1:
    print("O valor do produto final será R${} reais.".format(preço-(preço*0.1)))
elif pag==2:
    print("O valor do produto final será R${} reais.".format(preço-(preço*0.05)))
elif pag==3:
    print("O valor do produto final será R${} reais.".format(preço))
elif pag==4:
    print("O valor do produto final será R${} reais.".format(preço+(preço*0.2)))
else:
    print("Digite uma opção válida.")