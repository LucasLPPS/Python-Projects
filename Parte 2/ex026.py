import random
print("Sorteador de apresentação de trabalhos.")
nom1=str(input("Digite o nome do primeiro aluno:"))
nom2=str(input("Digite o nome do segundo aluno:"))
nom3=str(input("Digite o nome do terceiro aluno:"))
nom4=str(input("Digite o nome do quarto aluno:"))
print("Alunos --> {}, {}, {}, {}".format(nom1,nom2,nom3,nom4))
print("Ordem de apresentação:")
print(random.sample([nom1,nom2,nom3,nom4],k=4))
#outra opção seria utilizando a função random.shuflle([lista]) --> para esse exemplo seria mais simples, sem necessidade de usar o k.



