aluno = dict()
aluno["nome"] = str(input("Digite o nome do aluno:"))
aluno["media"] = float(input("Digite sua média:"))
if aluno['media'] < 7:
    aluno['situação'] = "Reprovado"
else:
    aluno['situação'] = "Aprovado"
print(f"O aluno é {aluno['nome']}.")
print(f"A sua média é {aluno['media']}.")
print(f"A sua situação é {aluno['situação']}.")

