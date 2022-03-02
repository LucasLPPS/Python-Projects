print("Jogo Pedra, Papel e Tesoura.")
print("Escolha sua opção:")
print("1. Pedra.")
print("2. Papel.")
print("3. Tesoura.")
esc=int(input("Opção:"))
from time import sleep
from random import randrange
esc2=randrange(2,4)
print("Pedra...")
sleep(1)
print("Papel...")
sleep(1)
print("Tesoura!")
sleep(1)
if esc==esc2:
    print("Empate!")
elif esc==1 and esc2==2:
    print("Pedra contra papel, você perdeu!")
elif esc==1 and esc2==3:
    print("Pedra contra tesoura, você ganhou!")
elif esc==2 and esc2==1:
    print("Papel contra pedra, você ganhou!")
elif esc==2 and esc2==3:
    print("Papel contra tesoura, você perdeu")
elif esc==3 and esc2==1:
    print("Tesoura contra pedra, você perdeu!")
elif esc==3 and esc2==2:
    print("Tesoura contra papel, você ganhou!")