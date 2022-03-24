# User pode digitar qualquer expressão matemática
# expressões do tipo Z = X ? Y, onde ? = [+,-,*,/]
print("-="*15)
print("    RESOLUÇÃO DE EQUAÇÕES ")
print("-="*15)
print("Digite uma expressão do tipo Z = X ? Y")
print(" - Onde Z, X, Y são as variáveis e ? um operador matemático: +,-,*,/")
print(" - Pelo menos duas das variáveis devem ser conhecidas com valores inteiros.")
print(" - Exemplo: Z = 1 + 2")
while True:
    while True:
        while True:
            while True:
                exp = str(input("Equação: ")).strip().lower()
                eq = exp.replace(" ", "")
                print(f"Sua equação é: {eq}")
                # transformando o texto em lista:
                eqList = list(eq)
                totalpha = 0
                for c in eqList:
                    if c.isalpha():
                        totalpha = totalpha + 1
                if totalpha == 0:
                    print("Apenas números digitados.")
                else:
                    break
            # identificando os números:
            eqListF = list()
            for c in eqList:
                if c.isnumeric():
                    eqListF.append(int(c))
                else:
                    eqListF.append(c)
            # descobrindo onde estão os números:
            indices = list()
            for c, i in enumerate(eqListF):
                if type(i) == int:
                    indices.append(c)
            if len(indices) == 0:
                print("Equação sem números.")
            else:
                break
        i = min(indices)
        d = 0
        for c in range(0, len(indices) - 1):
            d = c + 1
            if indices[c] + 1 != indices[d]:
                f = indices[c]
        # voltando a lista para str para tentar juntar os números:
        # lista de transição
        eqListT = list()
        for c in eqListF:
            if type(c) == int:
                eqListT.append(str(c))
            else:
                eqListT.append(c)

        # juntando o número:
        itens_unidos = "".join(eqListT[i:f + 1])
        eqListT[i:f + 1] = [itens_unidos]
        # -------------------------------------------------
        # repetindo o processo para encontrar o outro número:
        eqListF2 = list()
        for c in eqListT:
            if c.isnumeric():
                eqListF2.append(int(c))
            else:
                eqListF2.append(c)
        # descobrindo onde estão os números:
        indices1 = list()
        for c, i in enumerate(eqListF2):
            if type(i) == int:
                indices1.append(c)
        # ------------------------------------- ok
        d1 = 0
        for c in range(0, len(indices1) - 1):
            d1 = c + 1
            if indices1[c] + 1 != indices1[d1]:
                i1 = indices1[d1]
        f1 = max(indices1)
        # ------------------------------------- ok
        # voltando a lista para str para juntar os números:
        # lista de transição
        eqListT2 = list()
        for c in eqListF2:
            if type(c) == int:
                eqListT2.append(str(c))
            else:
                eqListT2.append(c)
        itens_unidos2 = "".join(eqListT2[i1:f1 + 1])
        eqListT2[i1:f1 + 1] = [itens_unidos2]
        # transformando novamente em números:
        eqListFinal = list()
        for c in eqListT2:
            if c.isnumeric():
                eqListFinal.append(int(c))
            else:
                eqListFinal.append(c)
        if len(eqListFinal) > 5:
            print("Equação inválida. Por favor, digite uma equação válida do tipo 'Z = X ? Y'")
        quant_var = 0
        quant_op = 0
        quant_igual = 0
        if len(eqListFinal) == 5:
            for c in eqListFinal:
                if type(c) == str and c != "+" and c != "-" and c != "/" and c != "*" and c != "=":
                    quant_var = quant_var + 1
                if c == "+" or c == "-" or c == "/" or c == "*":
                    quant_op = quant_op + 1
                if c == "=":
                    quant_igual = quant_igual +1
            if quant_igual > 1:
                print("Equação com mais de uma igualdade.")
            if quant_igual < 1:
                print("Equação sem igualdade.")
            if quant_op > 1:
                print("Mais de um operador encontrado.")
            if quant_op < 1:
                print("Nenhum operador encontrado.")
            if quant_var > 1:
                print("Mais de uma variável digitada.")
            if quant_var < 1:
                print("Nenhuma variável digitada.")
            if quant_var == 1 and quant_op == 1 and quant_igual == 1:
                break

    # ------------------------------------------- ok
    if eqListFinal.index("=") == 1:
        if type(eqListFinal[0]) == str:
            if "+" in eqListFinal:
                print(f"O valor de {eqListFinal[0]} é {eqListFinal[2] + eqListFinal[4]}.")
            elif "-" in eqListFinal:
                print(f"O valor de {eqListFinal[0]} é {eqListFinal[2] - eqListFinal[4]}.")
            elif "*" in eqListFinal:
                print(f"O valor de {eqListFinal[0]} é {eqListFinal[2] * eqListFinal[4]}.")
            elif "/" in eqListFinal:
                print(f"O valor de {eqListFinal[0]} é {eqListFinal[2] / eqListFinal[4]}.")
        elif type(eqListFinal[2]) == str:
            if "+" in eqListFinal:
                print(f"O valor de {eqListFinal[2]} é {eqListFinal[0] - eqListFinal[4]}.")
            elif "-" in eqListFinal:
                print(f"O valor de {eqListFinal[2]} é {eqListFinal[0] + eqListFinal[4]}.")
            elif "*" in eqListFinal:
                print(f"O valor de {eqListFinal[2]} é {eqListFinal[0] / eqListFinal[4]}.")
            elif "/" in eqListFinal:
                print(f"O valor de {eqListFinal[2]} é {eqListFinal[0] * eqListFinal[4]}.")
        elif type(eqListFinal[4]) == str:
            if "+" in eqListFinal:
                print(f"O valor de {eqListFinal[4]} é {eqListFinal[0] - eqListFinal[2]}.")
            elif "-" in eqListFinal:
                print(f"O valor de {eqListFinal[4]} é {eqListFinal[2] - eqListFinal[0]}.")
            elif "*" in eqListFinal:
                print(f"O valor de {eqListFinal[4]} é {eqListFinal[0] / eqListFinal[2]}.")
            elif "/" in eqListFinal:
                print(f"O valor de {eqListFinal[4]} é {eqListFinal[2] / eqListFinal[0]}.")
    if eqListFinal.index("=") == 3:
        if type(eqListFinal[0]) == str:
            if "+" in eqListFinal:
                print(f"O valor de {eqListFinal[0]} é {eqListFinal[4] - eqListFinal[2]}.")
            elif "-" in eqListFinal:
                print(f"O valor de {eqListFinal[0]} é {eqListFinal[4] + eqListFinal[2]}.")
            elif "*" in eqListFinal:
                print(f"O valor de {eqListFinal[0]} é {eqListFinal[4] / eqListFinal[2]}.")
            elif "/" in eqListFinal:
                print(f"O valor de {eqListFinal[0]} é {eqListFinal[4] * eqListFinal[2]}.")
        elif type(eqListFinal[2]) == str:
            if "+" in eqListFinal:
                print(f"O valor de {eqListFinal[2]} é {eqListFinal[4] - eqListFinal[0]}.")
            elif "-" in eqListFinal:
                print(f"O valor de {eqListFinal[2]} é {eqListFinal[0] - eqListFinal[4]}.")
            elif "*" in eqListFinal:
                print(f"O valor de {eqListFinal[2]} é {eqListFinal[4] / eqListFinal[0]}.")
            elif "/" in eqListFinal:
                print(f"O valor de {eqListFinal[2]} é {eqListFinal[0] / eqListFinal[4]}.")
        elif type(eqListFinal[4]) == str:
            if "+" in eqListFinal:
                print(f"O valor de {eqListFinal[4]} é {eqListFinal[0] + eqListFinal[2]}.")
            elif "-" in eqListFinal:
                print(f"O valor de {eqListFinal[4]} é {eqListFinal[0] - eqListFinal[2]}.")
            elif "*" in eqListFinal:
                print(f"O valor de {eqListFinal[4]} é {eqListFinal[0] * eqListFinal[2]}.")
            elif "/" in eqListFinal:
                print(f"O valor de {eqListFinal[4]} é {eqListFinal[0] / eqListFinal[2]}.")
    resp = str(input("Deseja resolver outra equação? [S/N]:")).strip().upper()[0]
    while resp != "S" and resp != "N":
        print("Escolha uma opção válida!")
        resp = str(input("[S/N]:")).strip().upper()[0]
    if resp == "N":
        break
print("Programa finalizado.")

