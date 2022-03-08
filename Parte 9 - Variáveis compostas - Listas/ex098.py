nums=[]
quant=0
while True:
    num=int(input("Digite um número:"))
    nums.append(num)
    quant=quant+1
    resp=str(input("Deseja cadastrar outro número? [S/N]:")).strip().upper()[0]
    while resp!="S" and resp!="N":
        print("Escolha uma opção válida!")
        resp=str(input("[S/N]:")).strip().upper()[0]
    if resp=="N":
        break
nums.sort(reverse=True)
print(f"A quantidade de números digitados foi: {quant}.") # ou usar simplesmente len(nums)
print(f"A lista em ordem descrescente é: {nums}.")
if 5 in nums:
    print("O valor 5 está na lista. E está nas posições", end="")
    for c, i in enumerate(nums):
        if i==5:
            print(f"...{c}")
else:
    print("O valor 5 não está na lista.")