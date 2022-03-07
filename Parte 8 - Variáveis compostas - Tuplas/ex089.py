brasileirão = ("Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "RB Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos", "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense")
print("Os cinco primeiros colocados do Brasileirão 2021 foram:")
c=0
for c in range(0,5):
    print(f"{c+1}º - {brasileirão[c]}", end=" -> ")
print("Fim.")
print("Os últimos quatro colocados do Brasileirão 2021 foram:")
for c in range(-1,-5,-1):
    print(f"{c+21}º - {brasileirão[c]}", end=" -> ")
print("Fim")
print("Os times em ordem alfabética ficam:")
print(sorted(brasileirão))
print(f"A {brasileirão[19]} ficou em {brasileirão.index('Chapecoense')+1}º lugar nessa edição.")