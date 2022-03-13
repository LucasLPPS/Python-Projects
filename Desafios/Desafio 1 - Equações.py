# -> Usuário pode digitar qualquer expressão matemática
# -> expressões do tipo Z = X ? Y, onde ? = [+,-,*,/]
print("-="*15)
print("    RESOLUÇÃO DE EQUAÇÕES:")
print("-="*15)
print("Digite uma expressão do tipo Z = X ? Y")
print(" - Onde Z, X, Y são as variáveis e ? um operador matemático: +,-,*,/")
print(" - Pelo menos duas das variáveis devem ser conhecidas com valores inteiros.")
print(" - Exemplo: Z = 1 + 2")
exp = str(input("Equação: ")).strip().lower()
eq = exp.replace(" ", "")
print(f"Sua equação é: {eq}")
# transformando o texto em uma lista:
eqList = list(eq)
print(eqList) # excluir
# identificando os números:
eqListF = list()
for c in eqList:
    if c.isnumeric():
        eqListF.append(int(c))
    else:
        eqListF.append(c)
print(eqListF) # excluir
# descobrindo onde estão os números:
indices = list()
for c, i in enumerate(eqListF):
    if type(i) == int:
        print(f"Na posição {c} econtrei o valor {i}!") # excluir
        indices.append(c)
print(indices) # excluir
i = min(indices)

d = 0
for c in range(0, len(indices)-1):
    d = c+1
    if indices[c] + 1 != indices[d]:
        f = indices[c]
print(f"Início - {i} ; Fim - {f}") # excluir
# voltando a lista para str para tentar juntar os números:
# >> obs: procurar forma de juntar int <<
eqListT = list() # lista de transição
for c in eqListF:
    if type(c) == int:
        eqListT.append(str(c))
    else:
        eqListT.append(c)
print(eqListT) # excluir
# juntando o número:
itens_unidos = "".join(eqListT[i:f+1])
eqListT[i:f+1] = [itens_unidos]
print(eqListT) # excluir
# -------------------------------------------------
# repetindo o processo para encontrar o outro número:
eqListF2 = list()
for c in eqListT:
    if c.isnumeric():
        eqListF2.append(int(c))
    else:
        eqListF2.append(c)
print(eqListF2) # excluir
# descobrindo onde estão os números:
indices1 = list()
for c, i in enumerate(eqListF2):
    if type(i) == int:
        print(f"Na posição {c} econtrei o valor {i}!") # excluir
        indices1.append(c)
print(indices1) # excluir
# até aqui está ok!
# encontrar forma de ignorar o primeiro número e juntar o segundo número.
d1 = 0
for c in range(0, len(indices1)-1):
    d1 = c+1
    if indices1[c] + 1 != indices1[d1]:
        i1 = indices1[d1]
f1 = max(indices1)
print(f"Início - {i1} ; Fim - {f1}") # excluir
# ------------------------------------- ok
# voltando a lista para str para juntar os números:

eqListT2 = list() # lista de transição
for c in eqListF2:
    if type(c) == int:
        eqListT2.append(str(c))
    else:
        eqListT2.append(c)
print(eqListT2) # excluir

itens_unidos2 = "".join(eqListT2[i1:f1+1])
eqListT2[i1:f1+1] = [itens_unidos2]
print(eqListT2) # excluir
# transformando novamente em números:
eqListFinal = list()
for c in eqListT2:
    if c.isnumeric():
        eqListFinal.append(int(c))
    else:
        eqListFinal.append(c)
print(eqListFinal) # excluir
# ------------------------------------------- ok
# checar cada valor da equação para identificar se é um número ou letra
# for c in eqListFinal:
# lista = 0,1,2,3,4
# procurar forma de validar como número ou letra um termo isolado de uma lista


