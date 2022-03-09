dados = dict()
from datetime import date
ano2 = date.today().year
dados['Nome'] = str(input("Digite o nome:"))
ano = int(input("Digite o ano de nascimento:"))
dados['Idade'] = ano2 - ano
carteira = int(input("Digite a carteira de trabalho (CTPS) (0 caso não tenha): "))
if carteira == 0:
    for k,v in dados.items():
        print(f"{k} é {v}.")
    print("Não possui CTPS.")
else:
    dados['CTPS'] = carteira
    anocontrato = int(input("Ano de contratação:"))
    dados['Contratação'] = anocontrato
    dados['Salário'] = float(input("Salário:"))
    dados['Aposentadoria'] = (ano2 - ano) + (35 - (ano2 - anocontrato))
    for k,v in dados.items():
        print(f"{k} é {v}.")
