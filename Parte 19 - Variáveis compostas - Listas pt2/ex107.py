alunos=list()
aluno=list()
while True:
    nome=str(input("Nome:"))
    aluno.append(nome)
    nota1=float(input("Nota 1:"))
    aluno.append(nota1)
    nota2=float(input("Nota 2:"))
    aluno.append(nota2)
    alunos.append(aluno[:])
    resp=str(input("Deseja cadastrar outra pessoa? [S/N]:")).strip().upper()[0]
    while resp!="S" and resp!="N":
        print("Escolha uma opção válida!")
        resp=str(input("[S/N]:")).strip().upper()[0]
    if resp=="N":
        break
    aluno.clear()
media=list()
for c in alunos:
    media.append((c[1]+c[2])/2)
print("No. NOME                MEDIA")
for c in range(0,len(alunos)):
    print(c,end="")
    print(f"   {alunos[c][0]:.<20}", end="") # alinhado a esquerda, dentro de 30 espaços de caracteres, com pontos completando o restante vazio
    print(f"{media[c]:>5.2f}") # alinhado a direita, dentro de 7 espaços de caracteres, e o valor aparecendo com 2 casas decimais
while True:
    escolha=int(input("Mostrar notas de qual aluno? (999 interrompe):"))
    if escolha == 999:
        break
    if (escolha<0) or (escolha>=len(alunos)):
        while (escolha < 0) or (escolha >= len(alunos)):
            print("Escolha uma opção válida!")
            escolha=int(input("Opção:"))
            if escolha == 999:
                break
    for c in alunos:
        if escolha==alunos.index(c):
            print(f"As notas de {alunos[alunos.index(c)][0]} foram {alunos[alunos.index(c)][1]} e {alunos[alunos.index(c)][2]}.")
    if escolha == 999:
        break

