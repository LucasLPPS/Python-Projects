s=0
tot=0
for c in range(1,501):
    if c%2!=0 and c%3==0:
        tot=tot+1 # outra forma de escrever isso seria tot+=1
        s=s+c     # na mesma linha de raciocínio acima s+=c
print("A soma dos {} números compreendidos entre 1 e 500, ímpares e divísiveis por 3 é {}.".format(tot,s))
