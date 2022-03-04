resp=0
tot=0
maior=0
menor=0
quant=0
while resp!="N":
    num=int(input("Digite um número:"))
    tot=tot+num
    quant=quant+1
    if menor==0:
        menor=num
    if num>maior:
        maior=num
    if num<menor:
        menor=num
    resp=str(input("Quer continuar?[S/N]")).upper()
print("A média entre os números digitados vale {}, o maior número foi {} e o menor foi {}.".format((tot/quant),maior,menor))