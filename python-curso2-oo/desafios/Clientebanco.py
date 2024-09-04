class ClienteBanco:
    quantos_clientes = 0

    def __init__(self, nome, cpf, contabancaria, saldo, ativo):
        self._nome = nome
        self._cpf = cpf
        self._contabancaria = contabancaria
        self._saldo = saldo
        quantos_clientes += 1

    @classmethod
    def quantidade_de_clientes(cls):
        return quantos_clientes

cliente1 = ClienteBanco('Walber', 574502868244, 'conta bancaria', 0, True)

print(cliente1)