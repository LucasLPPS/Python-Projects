mais18=quantH=quantM20=opção=0
while True:
    print("===CADASTRO DE PESSOA===")
    idade=int(input("Digite a idade:"))
    sexo = str(input("Digite o sexo [M] Masculino ou [F] Feminino:")).strip.().upper().[0]
    if idade>18:
        mais18=mais18+1
    if sexo=="M":
        quantH=quantH+1
    if sexo=="F":
        if idade<20:
            quantM20=quantM20+1
    if sexo!="M" and sexo!="F":
        while sexo!="M" and sexo!="F":
            print("Digite um sexo válido.")
            sexo = str(input("Digite seu sexo [M] Masculino ou [F] Feminino:")).upper()
            if sexo == "M":
                quantH = quantH + 1
            if sexo == "F":
                if idade < 20:
                    quantM20 = quantM20 + 1
    opção=str(input("Deseja continuar? [S/N]:")).strip().upper()[0]
    if opção!="N" and opção!="S":
        while opção!="N" and opção!="S":
            print("Digite uma opção válida:")
    if opção=="N":
        break
print(f"A quantidade de pessoas com mais de 18 é {mais18}.")
print(f"A quantidade de homens cadastrados é {quantH}.")
print(f"A quantidade de mulheres com menos de 20 é {quantM20}.")


