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

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")

print(vars(cliente1))
print(vars(cliente2))

# Exemplo de uso do método de classe
conta2 = ClienteBanco.criar_conta('Elizâ',2000)
print(f'Conta de {conta2.titular} | saldo {conta2.saldo}')    