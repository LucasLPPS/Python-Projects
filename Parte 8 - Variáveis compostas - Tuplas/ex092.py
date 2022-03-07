lista = ("Lápis",1.75,"Borracha",2,"Caderno",15.90)
#while True:
#    lista.append(input("Digite o produto:"))
#    lista.append(input("Digite o preço:"))
#    resp=str(input("Deseja cadastrar outro produto? [S/N]:")).strip().upper()[0]
#    while resp!="S" and resp!="N":
#        print("Escolha uma opção válida!")
#        resp=str(input("[S/N]:")).strip().upper()[0]
#    if resp=="N":
#        break

print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}") # estou dizendo que é centralizado entro do espaço de 40 caracteres
print("-"*40)
for c in range(0,len(lista)):
    if c%2==0:
        print(f"{lista[c]:.<30}", end="") # alinhado a esquerda, dentro de 30 espaços de caracteres, com pontos completando o restante vazio
    else:
        print(f"R$ {lista[c]:>7.2f}") # alinhado a direita, dentro de 7 espaços de caracteres, e o valor aparecendo com 2 casas decimais
print("-"*40)