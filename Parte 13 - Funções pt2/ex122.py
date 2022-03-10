from datetime import date
# >16 - optativo; 18 - obrigatório; <16 - não pode; >65 - opcinal


def voto(ano):
    ano2 = date.today().year
    idade = ano2 - ano
    if idade < 16:
        print("Voto Negado.") # outra forma de escrever -> return "Voto negado"
    elif (idade >= 16) and (idade < 18):
        print("Voto Opcional.")
    elif (idade >= 18) and (idade < 65):
        print("Voto Obrigatório.")
    elif idade >= 65:
        print("Voto Opcional.")


voto(int(input("Digite o ano de seu nascimento:")))


