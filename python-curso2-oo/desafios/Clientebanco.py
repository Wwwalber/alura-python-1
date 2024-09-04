class ClienteBanco:
    quantos_clientes = 0

    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = conta_bancaria(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")

print(cliente1)
# Exemplo de uso do método de classe
conta2 = criar_conta('Elizâ',2000)
print(f'Conta de {conta2.titular} | saldo {conta2.saldo}')