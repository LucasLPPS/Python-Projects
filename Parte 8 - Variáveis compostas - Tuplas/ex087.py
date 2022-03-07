# uma tupla é uma variável que guarda vários valores
# os elementos são identificados por índices -> 0,1,2,3..
# o str é uma variável composta, por isso consigo manipular os elementos do texto, como a própria posição das letras
#
# posso usar o comando for para variáveis compostas
# for c in variavelcomposta:
#   print(c)
# para esse comando, o for vai da primeira posição [0] até a última posição da variável composta, imprimindo os seus valores respectivos armazenados
#
# As tuplas são imutáveis, não consigo tirar ou mudar o elemento enquanto o programa está rodando
# () - tupla ; [] - lista ; {} - dicionário
lanche=("Hambúrguer","Suco","Pizza","Pudim")
print(lanche)
print(lanche[0])
print(lanche[2])
print(lanche[-1])
print(lanche[1:3])
print(lanche[0:5:2])
print(lanche[-2])
# lambrando que tuplas são imutáveis:
# lanche[1]="Refrigerante" -> se eu colocar esse comando, voltará com erro, pois já declarei os elementos da tupla anteriormente
# print(lanche[1])
for c in lanche:
    print(f"Eu vou comer {c}.")
print(f"Foi muita comida. Pois comi {len(lanche)} tipos de comida diferentes.")
# outra forma de fazer:
for cont in range(0,len(lanche)):
    print(f"Eu vou comer {lanche[cont]}.")
# outra forma de fazer:
for pos,comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}.")

print(sorted(lanche)) # o sorted coloca em ordem alfabética

a=(2,5,4)
b=(5,8,1,2)
c2=a+b # ele não vai somar os elementos entre si, e sim juntar os dois conjuntos
print(c2)
# a ordem da soma influencia no resultado final, a+b(2, 5, 4, 5, 8, 1, 2) não é igual a b+a(5, 8, 1, 2, 2, 5, 4)
print(len(c2))
print(c2.count(5)) # mostra quem está na posição 5
print(c2.index(8)) # mostra a posição em que está o elemento 8
print(c2.index(5,1)) # mostra a primeira posição do elemento 5, visto que ele aparece duas vezes

pessoa=("Lucas", 29, "Masculino", 71) # posso misturar os tipos dentro da tupla, não necessitando ser do mesmo grupo
print(pessoa)
# comando para deletar da memória é del(pessoa)
# porém não posso apagar elementos individuais da tupla, como del(pessoa(1))
