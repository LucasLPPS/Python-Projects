cont50 = cont20 = cont10 = cont1 = 0
print("====Banco Eletrônico.====")
valor = int(input("Qual o valor que você quer sacar? (Apenas reais):"))
while True:
    if valor >= 50:
        valor = valor-50
        cont50 = cont50+1
    if (valor >= 20) and (valor < 50):
        valor = valor-20
        cont20 = cont20+1
    if (valor >= 10) and (valor < 20):
        valor = valor-10
        cont10 = cont10+1
    if (valor >= 1) and (valor < 10):
        valor = valor-1
        cont1 = cont1+1
    if valor == 0:
        break
print(f"Total de {cont50} cédulas de R$50 reais.")
print(f"Total de {cont20} cédulas de R$20 reais.")
print(f"Total de {cont10} cédulas de R$10 reais.")
print(f"Total de {cont1} cédulas de R$1 reais.")