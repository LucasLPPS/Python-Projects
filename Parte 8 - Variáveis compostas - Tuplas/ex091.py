num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o primeiro número:"))
num3=int(input("Digite o primeiro número:"))
num4=int(input("Digite o primeiro número:"))
nums=(num1,num2,num3,num4)
print(f"A sua lista foi: {nums}.")
cont9=0
for c in nums:
    if c==9:
        cont9=cont9+1
print(f"O número 9 apareceu {cont9} vez(es)")
#teria sido mais fácil apenas usar nums.count(9)
while True:
    for c in nums:
        if c==3:
            pos=nums.index(3)
    break
# teria sido mais fácil ter usado nums.index(3) direto, que retornaria a primeira posição apenas
if 3 in nums:
    print(f"A primeira vez que o número 3 aparece é na posição {pos}.")
else:
    print("Não há número 3.")
par=0
print("Números pares:")
for c in nums:
    if c%2==0:
        par=c
        print(par, end=" -> ")
print("Fim.")
