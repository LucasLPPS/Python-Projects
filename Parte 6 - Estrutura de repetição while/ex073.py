print("Jogo do acerto e erro!")
import random
num=0
aleat=1
quant=0
while num!=aleat:
    num=int(input("Escolha um número entre 0 e 10:"))
    aleat=random.randint(1,11)
    quant=quant+1
print("Parabéns, você escolheu o mesmo número que a máquina!")
print("Levou {} tentativas para isso acontecer!".format(quant))