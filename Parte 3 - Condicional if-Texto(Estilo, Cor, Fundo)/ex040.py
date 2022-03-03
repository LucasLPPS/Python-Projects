ano=int(input("Digite um ano para saber se é ou não bissexto:"))
if ano%4==0 and ano%100!=0 or ano%400==0:# ano%100!=0 ano que não seja múltiplo de 100
                                         # ano%400==0 ano múltiplo de 400
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
# para pegar o ano do PC
# from datetime import date
# ano = date.today().year