nums=[]
for c in range(0,5):
    num=int(input("Digite um valor:"))
    #nums.insert(0, num)
    if nums == []:
        nums.append(num)
        print("Adicionando no final da lista...")
    elif (num >= nums[0]) and (num <= nums[1]):
        nums.insert(1, num)
        print("Adicionando na posição 1 da lista...")
    elif num <= nums[0]:
        nums.insert(0, num)
        print("Adicionando na posição 0 da lista...")
    elif num > nums[2]:
        nums.append(num)
        print("Adicionando no final da lista...")
    elif num < nums[2]:
        nums.insert(2,num)
        print("Adicionando na posição 2 da lista...")

print(f"Sua lista em ordem crescente é : {nums}.")

