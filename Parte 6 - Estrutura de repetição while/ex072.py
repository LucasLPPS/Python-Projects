sexo=0
while sexo!="M" and sexo!="F":
    sexo=str(input("Digite seu sexo [M/F]:")).upper()
    if sexo=="M":
        print("Você é do sexo masculino.")
    elif sexo=="F":
        print("Você é do sexo feminino.")
    if sexo!="M" and sexo!="F":
        print("Digite uma opção válida.")
