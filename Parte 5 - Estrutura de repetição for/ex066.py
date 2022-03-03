from datetime import date
ano2 = date.today().year
s=0
s1=0
for c in range(1,8):
    ano=int(input("Diga o ano de nascimento da {}º pessoa:".format(c)))
    if (ano2-ano)<18:
        s=s+1
    elif (ano2-ano)>=18:
        s1=s1+1
print("No total, {} não atingiram a maioridade, e {} já são maiores de idade.".format(s,s1))
