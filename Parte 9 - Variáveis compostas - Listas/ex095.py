nums=[]
for c in range(0,5):
    nums.append(int(input(f"Digite o {c+1} número:")))
maior=max(nums)
menor=min(nums)
print(f"A sua lista foi {nums}.")
print(f"O maior valor foi {maior} nas posições ", end="")
for c,i in enumerate(nums):
    if i==maior:
        print(f"{c}", end="...")
print(f"\nO menor valor foi {menor} nas posições ", end="")
for d,j in enumerate(nums):
    if j==menor:
        print(f"{d}", end="...")
