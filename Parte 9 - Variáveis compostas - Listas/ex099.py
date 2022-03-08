nums=[]
while True:
    num=int(input("Digite um número:"))
    nums.append(num)
    resp=str(input("Deseja cadastrar outro número? [S/N]:")).strip().upper()[0]
    while resp!="S" and resp!="N":
        print("Escolha uma opção válida!")
        resp=str(input("[S/N]:")).strip().upper()[0]
    if resp=="N":
        break
numspar=[]
numsimpar=[]
for c in nums:
    if c%2==0:
        numspar.append(c)
    else:
        numsimpar.append(c)
print(f"A sua lista digitada foi: {nums}.")
print(f"Os números pares da sua lista foram: {numspar}.")
print(f"Os números ímpares da sua lista foram: {numsimpar}.")
