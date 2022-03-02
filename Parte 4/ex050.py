n1=float(input("Digite a primeira nota do aluno:"))
n2=float(input("Digite a segunda nota do aluno:"))
if ((n1+n2)/2)<5:
    print("O aluno está reprovado.")
elif ((n1+n2)/2)>=5 and ((n1+n2)/2)<7:
    print("O aluno está de recuperação.")
elif ((n1+n2)/2)>=7:
    print("O aluno está aprovado.")