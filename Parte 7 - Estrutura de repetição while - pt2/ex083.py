print("Jogo par ou ímpar!")
import random
escolha=escolha2=m_escolha=cont=0
while True:
    escolha = int(input("Escolha um número:"))
    m_escolha = random.randrange(0, 11)
    escolha2=int(input("Escolha [1] Par ou [2] Ímpar."))
    if escolha2==1:
        if (escolha+(m_escolha))%2==0:
            print("Parabéns, você ganhou!")
            cont=cont+1
        else:
            print("Você perdeu!")
            break
    elif escolha2==2:
        if (escolha+(m_escolha))%2!=0:
            print("Parabéns, você ganhou!")
            cont=cont+1
        else:
            print("Você perdeu!")
            break
    elif escolha2<1 or escolha2>2:
        print("Digite uma opção válida.")
print(f"Fim de jogo! Você ganhou {cont} vezes.")

# tipo=" "
# while tipo not in "PI":
#     tipo=str(input("Par ou ímpar?[P/I]:")).strip().upper()[0] --> remove os espaços no início e fim, coloca tudo maísculo e pega apenas a primeira posição
#--> esse código significa que enquanto o tipo não for "PI", ele irá se repetir, uma forma mais simples de resolver certas condições