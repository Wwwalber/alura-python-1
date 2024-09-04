class ContaBancaria:
    def __init__(self, titular='', saldo=0, ativo=False):
        self.titular= titular
        self.saldo = saldo
        self.ativo = ativo

    def __str__(self):
        return f'Conta pertencente a {self.titular} | conta ativa? {self.ativo} | saldo {self.saldo}'

    def ativa_conta(self):
        self.ativo = True

conta1 = ContaBancaria('Walber Costa',0)
conta1.ativa_conta()
print(conta1)

    