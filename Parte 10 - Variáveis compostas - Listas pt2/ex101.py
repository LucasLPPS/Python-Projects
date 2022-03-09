# posso colocar uma lista dentro de uma posição em outra lista
# EX:
# dados=["Pedro", 25]
# pessoas.append(dados[:]) -> isso garante que uma cópia de dados está sendo armazenada na proxima posição disponível em pessoas
#----------------------------------------------------
# Ex de uma lista composta:
'''pessoas=[["Pedro", 25],["Maria",19],["João",32]]
print(pessoas[0][0]) # retorna o elemento "Pedro"
print(pessoas[1][1]) # retorna o elemento "19"
print(pessoas[2][0]) # retorna o elemento "João"
print(pessoas[1]) # retorna o elemento ["Maria", 19]'''
#-------------------------------------------------------
'''teste=list()
teste.append("Lucas")
teste.append(29)
galera=list()
galera.append(teste[:])
teste[0]="Catharina"
teste[1]=23
galera.append(teste[:])
print(galera) -> retorna [['Lucas', 29], ['Catharina', 23]] '''
#--------------------------------------------------------------
'''pessoas=[["Pedro", 25],["Maria",19],["João",32]]
for c in pessoas:
    print(f"{c[0]} tem {c[1]} de idade.")'''
#--------------------------------------------------------------
galera=list()
dado=list()
for c in range(0,3):
    dado.append(str(input("Digite um nome:")))
    dado.append(int(input("Digite a idade:")))
    galera.append(dado[:]) # cuidado para não esquecer [:]
    dado.clear() # comando para apagar os últimos dados salvos em "dado"
print(galera)
maiores=0
menores=0
for c in galera:
    if (c[1])>18:
        print(f"{c[0]} é maior de idade.")
        maiores=maiores+1
    else:
        print(f"{c[0]} é menor de idade.")
        menores=menores+1
print(f"O total de maiores é {maiores} e o total de menores é {menores}.")







