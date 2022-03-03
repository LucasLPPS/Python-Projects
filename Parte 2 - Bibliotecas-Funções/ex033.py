frase=str(input("Digite uma frase:")).strip().upper()
a=frase.count("A")
print("A letra 'a' aparece {} vezes.".format(a))
print("A letra 'a' aparece na posição {} inicialmente".format(frase.find("A")+1))# add +1 para a posição ser condizente para o usuário
print("A última posição da letra 'a' é {}.".format(frase.rfind("A")+1))