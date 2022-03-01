print("Jogo do acerto e erro!")
num=int(input("Escolha um número entre 0 e 5:"))
import random
aleat=random.randrange(6)
if aleat==num:
    print("Parabéns, você acertou!")
else:
    print("Infelizmente você errou!")