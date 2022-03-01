print("Jogo do acerto e erro!")
num=int(input("Escolha um número entre 0 e 5:"))
import random
aleat=random.randrange(6) # poderia ter usado o comando random.randint(0,5)
                          # o random.randrange(X) escolhe um número aleatório da posição 0 à posição X
# existe um comando chamado sleep(X), que faz o programa aguardar por X segundos antes de continuar
if aleat==num:
    print("Parabéns, você acertou!")
else:
    print("Infelizmente você errou!")