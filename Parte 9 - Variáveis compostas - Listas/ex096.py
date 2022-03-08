nums=[]
while True:
    num=int(input("Digite um número:"))
    if num not in nums:
        nums.append(num)
    resp=str(input("Deseja cadastrar outro número? [S/N]:")).strip().upper()[0]
    while resp!="S" and resp!="N":
        print("Escolha uma opção válida!")
        resp=str(input("[S/N]:")).strip().upper()[0]
    if resp=="N":
        break
nums.sort()
print(f"A sua lista em ordem crescente é:{nums}.")