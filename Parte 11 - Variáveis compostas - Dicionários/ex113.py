grupo = list()
pessoa = dict()
mulheres = list()
while True:
    nome = str(input("Nome:"))
    pessoa['Nome'] = nome
    sexo = str(input("Sexo [M/F]:")).strip().upper()[0]
    while sexo != "M" and sexo != "F":
        print("Escolha uma opção válida!")
        sexo = str(input("[M/F]:")).strip().upper()[0]
    if sexo == "F":
        mulheres.append(nome)
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input("Idade:"))
    grupo.append(pessoa.copy())
    pessoa.clear()
    resp = str(input("Deseja cadastrar outra pessoa? [S/N]:")).strip().upper()[0]
    while resp != "S" and resp != "N":
        print("Escolha uma opção válida!")
        resp = str(input("[S/N]:")).strip().upper()[0]
    if resp == "N":
        break
# ----------------------------------------------
print("-="*30)
print(f"{len(grupo)} pessoas foram cadastradas.")
# ----------------------------------------------
print("-="*30)
totalidade = 0
for c in range(0, len(grupo)):
    totalidade = totalidade + grupo[c]['Idade']
media = totalidade/len(grupo)
print(f"A média de idade do grupo é {media}")
# ----------------------------------------------
print("-="*30)
print(f"As mulheres cadastradas são:", end=" ")
for c in range(0, len(mulheres)):
    print(f"{mulheres[c]} -> ", end="")
print("Fim.")
# ----------------------------------------------
print("-="*30)
print("Grupo de pessoas acima da média de idade:")
for c in range(0, len(grupo)):
    if grupo[c]['Idade'] > media:
        print(f"{grupo[c]['Nome']} está com {grupo[c]['Idade']} anos, acima da média de {media} anos.")


