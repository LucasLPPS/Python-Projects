soma=0
idoso = 0
novinha = 0
homem_velho = 0
for c in range(1,5):
    nome=str(input("Digite o {}º nome:".format(c)))
    idade=int(input("Digte a idade de {}.".format(nome)))
    soma=soma+idade
    print("Digite seu sexo:[1] Masculino [2] Feminino")
    opção=int(input())
    if opção ==1:
        if idade > idoso:
            idoso=idade
            homem_velho = nome
    elif opção ==2:
        if idade<20:
            novinha=novinha+1
media=soma/4
print("A média de idades é {}.".format(media))
print("{} é o homem mais velho".format(homem_velho))
print("A quantidade de mulheres com menos de 20 anos é {}.".format(novinha))