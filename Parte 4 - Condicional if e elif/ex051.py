ano=int(input("Digite a o ano de seu nascimento:"))
from datetime import date
ano2=date.today().year
if (ano2-ano)<=9:
    print("Sua categoria é mirim.")
elif (ano2-ano)<=14:
    print("Sua categoria é infantil.")
elif (ano2-ano)<=19:
    print("Sua categoria é junior.")
elif (ano2-ano)<=20:
    print("Sua categoria é senior.")
else:
    print("Sua categoria é master.")