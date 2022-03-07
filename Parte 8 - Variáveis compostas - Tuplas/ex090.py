from random import randint
num1=randint(1,100)
num2=randint(1,100)
num3=randint(1,100)
num4=randint(1,100)
num5=randint(1,100)
nums=(num1,num2,num3,num4,num5) # poderia ter colocado -> nums=(randint(1,100),randint(1,100),...
print(f"A lista de números aleatórios é: {nums}.")
nums2=sorted(nums)
print(f"O maior valor da lista é {nums2[-1]} e o menor valor é {nums2[0]}.")
# outra forma de fazer, sem usar a função sorted(), seria usando o max(nums) e min(nums), que já retornaria direto o maior e menor valor
