import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"Data de abertura: {self.data_abertura}")
        print(f"Transações:")
        for c in self.transacoes:
            print("-", c)


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo = self.saldo + valor
        self.historico.transacoes.append(f"Depósito de {valor}.")

    def saca(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            self.saldo = self.saldo - valor
            self.historico.transacoes.append(f"Saque de {valor}.")

    def extrato(self):
        print(self.saldo)
        self.historico.transacoes.append(f"Extrato da conta retirado, saldo de {self.saldo}.")

    def transfere_para(self, conta_destino, valor):
        if self.saldo < valor:
            print("Saldo insuficiente.")
        else:
            self.saldo = self.saldo - valor
            conta_destino.saldo = conta_destino.saldo + valor
            self.historico.transacoes.append(f"Transferência de {valor} para a conta {conta_destino.numero}.")


cliente1 = Cliente("João", "Oliveira", "000.000.000-1")
cliente2 = Cliente("José", "Azevedo", "000.000.000-2")
conta1 = Conta("123 - 4", cliente1, 120, 1000)
conta2 = Conta("123 - 4", cliente2, 200, 1000)
conta1.deposita(100)
conta1.saca(50)
conta1.transfere_para(conta2, 200)
conta1.extrato()
conta1.historico.imprime()
