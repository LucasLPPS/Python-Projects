print("-"*30)
print("      NÚMEROS MEGA SENA     ")
print("-"*30)
from random import randint
from time import sleep
quant=int(input("Quantos sorteios você deseja?"))
nums=list()
for c in range(0,quant):
    for i in range(0,6):
        aleatorio=randint(1,60)
        if aleatorio not in nums:
            nums.append(aleatorio)
        else:
            nums.append(randint(1,60))
    nums.sort()
    print(f"Jogo {c+1}:", end="")
    print(f"{nums}")
    sleep(1)
    nums.clear()
print("=========BOA SORTE=========")
