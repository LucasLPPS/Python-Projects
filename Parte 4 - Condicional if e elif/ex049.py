ano=int(input("Digite seu ano de nascimento:"))
from datetime import date
ano2=date.today().year
if (ano2-ano)<18:
    print("Você deve se alistar! Ainda faltam {} anos para o alistamento.".format(18-(ano2-ano)))
elif (ano2-ano)>18:
    print("Você já passou do período de alistamento. O período máximo expirou há {} anos.".format((ano2-ano)-18))
elif (ano2-ano)==18:
    print("Você está na data limite para se alistar!")

