km=float(input("Digite a quantidade de Km percorridos pelo carro alugado:"))
dias=int(input("Digite quantos dias o carro ficou alugado:"))
aluguel=(60*dias)+(0.15*km)
print("O total que deve ser pago de aluguel pelo carro é R${:.2f} reais.".format(aluguel))