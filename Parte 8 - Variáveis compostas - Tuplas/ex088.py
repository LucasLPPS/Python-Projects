extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quartoze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
num=0
while num>=0 or num<=20:
    num=int(input("Digite um número entre 0 e 20:"))
    for c in range(0, len(extenso)):
        if num==c:
            print(f"Você digitou {extenso[c]}.")

