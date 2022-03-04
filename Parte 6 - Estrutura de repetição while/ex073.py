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
# outra forma de se fazer esse jogo, como foi feito pelo professor,
# seria pré-selecionando o valor do número aleatório, e depois fazer um
# while para pegar um número do usuário, se o número digitado for maior que o escolhido
# pela máquina,  retornar "Menos...tente mais uma vez", se for menor, retornar "Mais..tente mais uma vez"
# até o número escolhido pelo usuário ser igual ao número pré-selecionado