def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] = conta["saldo"] + valor


def saca(conta, valor):
    conta["saldo"] = conta["saldo"] - valor


def extrato(conta):
    print(f"Número: {conta['numero']}")
    print(f"Saldo: {conta['saldo']}")


conta1 = cria_conta("123-4", "João", 120, 1000)
deposita(conta1, 15)
extrato(conta1)
saca(conta1, 35)
extrato(conta1)


