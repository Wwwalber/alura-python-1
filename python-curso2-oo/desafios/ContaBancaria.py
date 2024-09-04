class ContaBancaria:
    def __init__(self, titular, saldo, ativo=False):
        self._titular= titular
        self._saldo = saldo
        self._ativo = ativo

    def __str__(self):
        return f'Conta pertencente a {self._titular} | conta ativa? {self._ativo} | saldo {self._saldo}'

    def ativa_conta(self):
        self._ativo = True

    @property
    def is_ativo(self):
        return 'Ativa' if self._ativo else 'Inativa'

    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
        
conta1 = ContaBancaria('Walber Costa',0)
conta1.ativa_conta()
print(conta1)
print(f'conta de {conta1.titular} está {conta1.is_ativo}')

    