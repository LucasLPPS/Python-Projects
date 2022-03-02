l1=int(input("Digite o primeiro lado:"))
l2=int(input("Digite o segundo lado:"))
l3=int(input("Digite o terceiro lado:"))
if (l1>abs(l2-l3) and l1<l2+l3) and (l2 > abs(l1 - l3) and l2 < l1 + l3) and (l3 > abs(l1 - l2) and l3 < l1 + l2):
    print("Pode ser formado um triângulo.")
else:
    print("Não pode ser formado triângulo.")
if l1==l2 and l2==l3:
    print("O triângulo é equilátero.")
elif l1==l2 or l2==l3 or l3==l1:
    print("O triângulo é isósceles.")
elif l1!=l2 and l1!=l3 and l2!=l3:
    print("O triângulo é escaleno.")
