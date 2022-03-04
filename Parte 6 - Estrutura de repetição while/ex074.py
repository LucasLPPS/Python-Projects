c=0
while c!=5:
    n1 = int(input("Digite o primeiro valor:"))
    n2 = int(input("Digite o segundo valor:"))
    print("Operação:")
    print("[1] Somar.")
    print("[2] Multiplicar.")
    print("[3] Determinar o maior.")
    print("[4] Novos números.")
    print("[5] Sair do programa.")
    c=int(input("Opção:"))
    if c==1:
        soma=n1+n2
        print("A soma entre {} e {} é {}.".format(n1,n2,soma))
    if c==2:
        mult=n1*n2
        print("A multiplicação entre {} e {} é {}.".format(n1,n2,mult))
    if c==3:
        if n1>n2:
            maior=n1
            print("O maior é {}".format(maior))
        elif n2>n1:
            maior=n2
            print("O maior é {}".format(maior))
        elif n2==n1:
            print("Os números são iguais.")
    if c!=1 or c!=2 or c!=4 or c!=5:
        print("Digite uma opção válida.")
print("Programa finalizado.")
# se eu retirar de dentro do while !=5 as seguintes linhas:
# n1 = int(input("Digite o primeiro valor:"))
# n2 = int(input("Digite o segundo valor:"))
# e adicionar uma condição de if c==4 pedindo pra digitar os novos números com
# esses mesmo comandos, o programa nunca vai parar até eu digitar 5
# no estado atual do meu código, o programa finaliza quando escolho as opções de 1 a 3