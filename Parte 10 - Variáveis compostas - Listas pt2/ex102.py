dados=list()
pessoas=list()
quant=0
while True:
    dados.append(str(input("Digite o nome:")))
    dados.append(float(input("Digite o peso:")))
    pessoas.append(dados[:])
    dados.clear()
    quant=quant+1
    resp=str(input("Deseja cadastrar outra pessoa? [S/N]:")).strip().upper()[0]
    while resp!="S" and resp!="N":
        print("Escolha uma opção válida!")
        resp=str(input("[S/N]:")).strip().upper()[0]
    if resp=="N":
        break
print(f"A quantidade de pessoas cadastradas foi de {quant}.")
maiorpeso=0
menorpeso=0
maispesado=list()
menospesado=list()
for c in pessoas:
    if maiorpeso==0:
        maiorpeso = c[1]
    if menorpeso==0:
        menorpeso=c[1]
    if c[1]>=maiorpeso:
        maiorpeso=c[1]
        maispesado.append(c[0])
    if c[1]<=menorpeso:
        menorpeso=c[1]
        menospesado.append(c[0])
print(f"O maior peso foi de {maiorpeso}Kg das pessoas: {maispesado}.")
print(f"O menor peso foi de {menorpeso}Kg das pessoas: {menospesado}.")