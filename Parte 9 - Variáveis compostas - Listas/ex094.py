# as tuplas são imutáveis
# se eu quiser mudar elementos, devo usar uma lista
# lembrando -> () - tuplas; [] - lista
# se eu usar a estrutura [], estarei usando uma lista, e nesse caso posso mudar os termos internos
# para adicionar um elemento uso o comando lista.append(novovalor), que adicionará o novovalor dentro da lista
# se eu quiser adicionar em um local específico, uso lista.insert(0,novovalor), que adicionará o novovalor na posição 0,
# mas não substitui o valor 0 anterior, mas passa ele para a posição 1, e assim sucessivamente
# para deletar um item da lista, uso del lanche[3], que irá deletar o item da posição 3 da lista
# outro comando para apagar um item é lanche.pop(3), caso use apenas lanche.pop(), irá deletar o último termo da lista
# outra forma é usando o lanche.remove(item), que nesse caso vai apagar o item específico da lista, sem ncessidade de saber sua posição
# nos três casos acima, ao deletar o 3º termo da lista, o 4º termo passa se o 3º, e assim sucessivamente
# se eu tentar remover um item que não existe na lista, retornará com erro
# mas para contornar isso, posso usar:
# if item in lista:
#    lista.remove(item)
# posso criar uma lista da seguinte forma:
# lista=list(range(4,11)) -> irá criar uma lista de 4 a 10
# logo, lista=[4,5,6,7,8,9,10]
# se eu tiver lista=[8,2,5,4,9,3,0], para colocar em ordem uso o comando lista.sort()
# para inverter a ordem uso lista.sort(reverse=True)
# para saber o tamanho da lista uso len(lista)
num=[2,5,9,1]
num[2]=3
print(num)
num.append(8)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f"Essa lista tem {len(num)} elementos.")
num.insert(0,10)
print(num)
num.pop()
print(num)
num.pop(4)
print(num)
num.append(3)
print(num)
num.remove(3)# vai escluir apenas o primeiro 3, mas poderia remover o outro com laço
print(num)
if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 4.")
valores=[]
valores.append(5)
valores.append(9)
valores.append(4)
for c in valores:
    print(f"{c}", end="...")
print("\n")
for c,i in enumerate(valores):
    print(f"Na posição {c} econtrei o valor {i}!")
# adicionando valores novos com laço
for c in range(0,5):
    valores.append(int(input("Digite um novo valor:")))
for c,i in enumerate(valores):
    print(f"Na posição {c} econtrei o valor {i}!")
# atenção para o seguinte
a = [2,3,4,5]
b=a # nesse caso não estou criando uma cópia, estou fazendo uma ligação entre as duas listas
a[0]=1 # portanto, se eu atribuir um novo valor a lista "a", estarei modificando "b" também
print(a)
print(b)
# para fazer uma cópia:
b=a[:] # nesse caso não existe uma ligação, pois é apenas uma cópia, se eu mudar um valor de "a", não interfere em "b"