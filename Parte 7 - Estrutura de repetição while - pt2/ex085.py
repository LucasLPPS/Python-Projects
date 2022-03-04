total=cont=maisbarato=nomemaisbarato=0
while True:
    produto=str(input("Digite o nome do produto:"))
    preço=float(input("Digite o preço do produto (R$):"))
    total=total+preço
    if preço>1000:
        cont=cont+1
    if maisbarato==0:
        maisbarato=preço
        nomemaisbarato=produto
    if preço<maisbarato:
        maisbarato=preço
        nomemaisbarato=produto
    opção = str(input("Deseja cadastrar mais produtos? [S/N]:")).strip().upper()[0]
    if opção != "N" and opção != "S":
        while opção != "N" and opção != "S":
            print("Digite uma opção válida:")
    if opção == "N":
        break
print(f"O total gasto em compras foi de R${total} reais.")
print(f"{cont} produto(s) custam mais de R$1000 reais.")
print(f"{nomemaisbarato} foi o produto mais barato.")
