from modelos.banco import Banco

class Agencia(Banco): # A herança é indicada pelo uso de parênteses na declaração da classe
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero
