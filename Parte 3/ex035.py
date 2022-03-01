anos=int(input("Quantos anos tem seu carro?"))
if anos>=5:
    print("Seu carro já está velho.")
else:
    print("Seu carro ainda está novo.")
print("Tenha um bom dia!") # este comando sempre vai aparecer, já que está fora
                           # fora da condicional, por isso a importnância da
                           # identação
#outra forma de escrever essa condicional seria ->
# print("Seu carro está velho!" if anos>=5 else "Seu carro está novo!")
# é chamada de condicional simples