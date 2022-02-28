import random
print("Sorteador de nomes.")
nom1=str(input("Digite o nome do primeiro aluno:"))
nom2=str(input("Digite o nome do segundo aluno:"))
nom3=str(input("Digite o nome do terceiro aluno:"))
nom4=str(input("Digite o nome do quarto aluno:"))
sorteio=random.choice([nom1,nom2,nom3,nom4]) # retorna um dos valores da sequência -> usar .choice([valores])
print("O aluno sorteado é {}.".format(sorteio))