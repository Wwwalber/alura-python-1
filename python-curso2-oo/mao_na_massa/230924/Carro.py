from Veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar(self):
        return f"O carro {self.marca} {self.modelo} está ligado."