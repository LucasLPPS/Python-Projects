#n=0
#soma=0
#while n!=999:
#    n=int(input("Digite um número:"))
#    soma=soma+n
#print("A soma vale {}.".format(soma))
# --> para o código acima, eu precisei criar uma flag 999, porém a soma vai adicionar o 999,
# e para evitar o uso de gambiarra, fazendo no fim soma-999, utiliza-se o while true-> break
n=0
soma=0
cont=0
while True:
    n=int(input("Digite um número:"))
    if n==999:
        break
    soma=soma+n
    cont=cont+1
#print("A soma vale {}.".format(soma)) -> existe uma outra forma de escrever isso
print(f"A quantidade de números foi {cont} e a soma vale {soma}.") # essa é a forma atualizada.
